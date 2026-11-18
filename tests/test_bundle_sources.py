"""Relocated GSAP documents and notices remain pinned after the fold-in."""

import json
from pathlib import Path
import runpy
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
CHECK = runpy.run_path(str(ROOT / "scripts/check-bundle.py"))


class BundleSourceTests(unittest.TestCase):
    def test_bundle_has_only_five_discoverable_skills(self):
        skills = ROOT / "skills"
        self.assertEqual(
            {path.relative_to(skills).as_posix() for path in skills.rglob("SKILL.md")},
            {
                "loop/SKILL.md", "deep-build/SKILL.md", "deep-design/SKILL.md",
                "deep-grill/SKILL.md", "vendor/impeccable/SKILL.md",
            },
        )

    def test_gsap_pin_checks_content_and_requires_the_license(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            manifest = root / "bundle-sources.json"
            shutil.copyfile(ROOT / manifest.name, manifest)
            sources = json.loads(manifest.read_text(encoding="utf-8"))
            for record in sources.values():
                for filename in record["files"]:
                    relative = Path(record["local"]) / filename
                    (root / relative).parent.mkdir(parents=True, exist_ok=True)
                    shutil.copyfile(ROOT / relative, root / relative)

            failures = []
            CHECK["check_pinned_sources"](root, failures)
            self.assertEqual(failures, [])

            (root / "skills/deep-design/references/gsap-core.md").write_text("changed")
            del sources["gsap-core"]["files"]["assets/gsap-core.LICENSE"]
            manifest.write_text(json.dumps(sources), encoding="utf-8")

            CHECK["check_pinned_sources"](root, failures)
            self.assertTrue(any("gsap-core.md: differs from pinned source" in item for item in failures), failures)
            self.assertTrue(any("gsap-core must pin its relocated reference and license" in item for item in failures), failures)
