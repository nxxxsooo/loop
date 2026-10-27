"""Real export checks and isolated safety regressions; no network access."""

import json
import os
from pathlib import Path
import runpy
import subprocess
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
EXPORTER = runpy.run_path(str(ROOT / "scripts/export-deep-grill.py"))
export = EXPORTER["export"]
package = EXPORTER["package"]
MARKER = EXPORTER["MARKER"]


class ExportTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name).resolve()
        self.root = self.base / "loop"
        self.source = self.root / "skills/deep-grill"
        self.source.mkdir(parents=True)
        (self.root / "distributions").mkdir()
        (self.source / "SKILL.md").write_text("canonical skill\n")
        self.config = {
            "source": "skills/deep-grill",
            "repository": "https://github.com/nxxxsooo/deep-grill",
            "baseline_commit": "not-a-commit",
            "retired_files": ["retired.md"],
            "files": ["SKILL.md"],
        }
        self.save_config()
        self.output = self.base / "distribution"

    def save_config(self):
        (self.root / "distributions/deep-grill.json").write_text(json.dumps(self.config))

    def git(self, *args):
        return subprocess.check_output(["git", "-C", str(self.output), *args], stderr=subprocess.PIPE, text=True).strip()

    def init_git(self):
        self.git("init", "-q")
        self.git("config", "user.name", "Export Test")
        self.git("config", "user.email", "export@example.invalid")
        self.git("config", "commit.gpgsign", "false")
        self.git("config", "core.hooksPath", str(self.output / ".git/no-hooks"))
        self.git("remote", "add", "origin", self.config["repository"] + ".git")

    def commit(self):
        self.git("add", ".")
        self.git("commit", "-qm", "test snapshot")

    def test_export_check_and_determinism(self):
        export(self.root, self.output)
        before = (self.output / MARKER).read_bytes()
        export(self.root, self.output, check=True)
        export(self.root, self.output, update=True)
        self.assertEqual(before, (self.output / MARKER).read_bytes())
        self.assertEqual((self.output / "SKILL.md").read_bytes(), (self.source / "SKILL.md").read_bytes())

    def test_check_never_creates_output(self):
        with self.assertRaises(ValueError):
            export(self.root, self.output, check=True)
        self.assertFalse(self.output.exists())

    def test_refuses_existing_without_update(self):
        export(self.root, self.output)
        with self.assertRaisesRegex(ValueError, "not empty"):
            export(self.root, self.output)

    def test_update_to_new_source(self):
        export(self.root, self.output)
        (self.source / "SKILL.md").write_text("updated\n")
        with self.assertRaises(ValueError):
            export(self.root, self.output, check=True)
        export(self.root, self.output, update=True)
        export(self.root, self.output, check=True)

    def test_local_edits_are_preserved(self):
        export(self.root, self.output)
        (self.output / "SKILL.md").write_text("user edit")
        with self.assertRaisesRegex(ValueError, "local edits"):
            export(self.root, self.output, update=True)
        self.assertEqual((self.output / "SKILL.md").read_text(), "user edit")

    def test_unknown_files_are_preserved(self):
        export(self.root, self.output)
        (self.output / "user.txt").write_text("keep")
        with self.assertRaisesRegex(ValueError, "unexpected"):
            export(self.root, self.output, update=True)
        self.assertEqual((self.output / "user.txt").read_text(), "keep")

    def test_unknown_directory_is_not_overwritten(self):
        self.output.mkdir()
        (self.output / "user.txt").write_text("keep")
        with self.assertRaises(ValueError):
            export(self.root, self.output, update=True)

    def test_manifest_rejects_unsafe_and_duplicate_paths(self):
        for names in (["."], ["../secret"], ["/secret"], [".git/config"], [".local/secret"], ["SKILL.md", "SKILL.md"]):
            with self.subTest(names=names):
                self.config["files"] = names
                self.save_config()
                with self.assertRaises(ValueError):
                    export(self.root, self.output)
                self.assertFalse(self.output.exists())

    def test_unlisted_source_is_rejected(self):
        (self.source / "forgotten.md").write_text("do not silently omit")
        with self.assertRaisesRegex(ValueError, "inventory"):
            export(self.root, self.output)

    def test_symlinks_are_rejected(self):
        (self.source / "SKILL.md").unlink()
        (self.source / "SKILL.md").symlink_to(self.base / "secret")
        with self.assertRaisesRegex(ValueError, "symlink"):
            export(self.root, self.output)

    def test_output_symlink_is_rejected(self):
        self.output.symlink_to(self.base / "elsewhere", target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            export(self.root, self.output)

    def test_output_cannot_overlap_source(self):
        for output in (self.root, self.source, self.source / "export", self.root / "skills", self.root / "skills/deep-design"):
            with self.subTest(output=output), self.assertRaises(ValueError):
                export(self.root, output)

    def test_type_collision_is_rejected_before_any_write(self):
        export(self.root, self.output)
        (self.source / "SKILL.md").write_text("updated")
        (self.source / "new.md").write_text("new file")
        self.config["files"].append("new.md")
        self.save_config()
        (self.output / "new.md").mkdir()
        with self.assertRaisesRegex(ValueError, "not a file"):
            export(self.root, self.output, update=True)
        self.assertEqual((self.output / "SKILL.md").read_text(), "canonical skill\n")

    def test_executable_modes_are_preserved_and_checked(self):
        (self.source / "SKILL.md").chmod(0o755)
        export(self.root, self.output)
        self.assertEqual((self.output / "SKILL.md").stat().st_mode & 0o777, 0o755)
        (self.output / "SKILL.md").chmod(0o644)
        with self.assertRaises(ValueError):
            export(self.root, self.output, check=True)

    def test_baseline_migration_preserves_history_and_retires_only_known_file(self):
        self.output.mkdir()
        (self.output / "SKILL.md").write_text("old skill")
        (self.output / "retired.md").write_text("old prompt")
        self.init_git()
        self.commit()
        head = self.git("rev-parse", "HEAD")
        self.config["baseline_commit"] = head
        self.save_config()
        export(self.root, self.output, update=True)
        export(self.root, self.output, check=True)
        self.assertEqual(self.git("rev-parse", "HEAD"), head)
        self.assertFalse((self.output / "retired.md").exists())
        self.assertIn("SKILL.md", self.git("status", "--short"))

    def test_committed_export_can_update_but_dirty_checkout_cannot(self):
        export(self.root, self.output)
        self.init_git()
        self.commit()
        (self.output / "SKILL.md").write_text("uncommitted user edit")
        with self.assertRaisesRegex(ValueError, "local changes"):
            export(self.root, self.output, update=True)
        self.commit()
        with self.assertRaisesRegex(ValueError, "local edits"):
            export(self.root, self.output, update=True)

    def test_clean_generated_checkout_updates_without_commits(self):
        export(self.root, self.output)
        self.init_git()
        self.commit()
        head = self.git("rev-parse", "HEAD")
        (self.source / "SKILL.md").write_text("new canonical source")
        export(self.root, self.output, update=True)
        self.assertEqual(self.git("rev-parse", "HEAD"), head)

    def test_wrong_remote_is_rejected(self):
        export(self.root, self.output)
        self.init_git()
        self.commit()
        self.git("remote", "set-url", "origin", "https://example.invalid/other")
        with self.assertRaisesRegex(ValueError, "origin"):
            export(self.root, self.output, update=True)


class RealPackageTests(unittest.TestCase):
    def test_real_package_exports_and_runs_its_own_checker(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary).resolve() / "deep-grill"
            export(ROOT, output)
            export(ROOT, output, check=True)
            subprocess.run([os.sys.executable, str(output / "scripts/check-readme-sync.py")], check=True, capture_output=True)
            self.assertEqual(list(output.rglob("SKILL.md")), [output / "SKILL.md"])
            self.assertFalse((output / "references/grilling-upstream.md").exists())


if __name__ == "__main__":
    unittest.main()
