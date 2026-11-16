"""Artifact generation stays repository-local and preserves reorientation text."""

import json
from pathlib import Path
import runpy
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
