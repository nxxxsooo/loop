"""Artifact generation stays repository-local and preserves reorientation text."""

import json
from pathlib import Path
import runpy
import subprocess
import sys
import unittest


ROOT = Path(__file__).resolve().parents[1]
SYNC = runpy.run_path(str(ROOT / "scripts/sync-skill-artifacts.py"))


class SkillArtifactTests(unittest.TestCase):
    def test_generated_outputs_are_current(self):
        for path, text in SYNC["outputs"]().items():
            with self.subTest(path=path):
                self.assertEqual(path.read_text(encoding="utf-8"), text)

    def test_snippets_use_repo_children_and_fixed_reorientation(self):
        snippets = json.loads(SYNC["outputs"]()[ROOT / "skills/loop/assets/raycast-snippets.json"])
        self.assertEqual([item["name"] for item in snippets], list(SYNC["SNIPPETS"]))
        self.assertEqual(snippets[-1]["keyword"], ";wt")
        self.assertEqual(snippets[-1]["text"], (ROOT / "scripts/loop-reorient.txt").read_text().strip())
        for item in snippets[:-1]:
            skill = SYNC["SNIPPETS"][item["name"]]
            self.assertEqual(item["text"], SYNC["body"](skill))

    def test_design_and_build_snippets_route_to_bundled_references(self):
        snippets = json.loads(SYNC["outputs"]()[ROOT / "skills/loop/assets/raycast-snippets.json"])
        by_name = {item["name"]: item["text"] for item in snippets}
        for target in ("references/gsap-utils.md", "references/react-bits.md", "references/shadcn.md"):
            self.assertIn(f"]({target})", by_name["deep design"])
        self.assertIn("Default to `worker-sol`", by_name["deep build"])
        self.assertIn("](../deep-design/SKILL.md#on-demand-component-and-motion-guidance)", by_name["deep build"])
        self.assertIn("](../deep-design/references/shadcn.md)", by_name["deep build"])

    def test_explicit_check_mode(self):
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts/sync-skill-artifacts.py"), "--check"],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_loop_contract_includes_reorientation_and_native_goal(self):
        body = SYNC["body"]("loop")
        for fragment in (
            "## Select The Mode",
            "references/reorientation.md",
            "## Set The Native Goal",
            '"name":"goal"',
            "Check status first",
            "Pause the goal before a reorientation explanation",
            "resume it only when the user chooses Continue",
            "Clear the goal when the user stops, changes tasks, or changes the endpoint",
        ):
            with self.subTest(fragment=fragment):
                self.assertIn(fragment, body)


if __name__ == "__main__":
    unittest.main()
