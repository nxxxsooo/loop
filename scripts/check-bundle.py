#!/usr/bin/env python3
"""Validate the multi-skill package and pinned bundled sources."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {"grill-loop", "grilling", "deep-grill", "what"}
EXPECTED_RAYCAST_SNIPPETS = {
    "grilling": {"keyword": ";gr", "skill": "grilling"},
    "deep grill": {"keyword": ";dg", "skill": "deep-grill"},
    "grill-loop": {"keyword": ";lp", "skill": "grill-loop"},
    "what": {"keyword": ";wt", "skill": "what"},
}


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def frontmatter_name(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path}: missing frontmatter")
    try:
        closing = lines.index("---", 1)
    except ValueError as error:
        raise ValueError(f"{path}: missing closing frontmatter delimiter") from error
    for line in lines[1:closing]:
        if line.startswith("name:"):
            return line.split(":", 1)[1].strip()
    raise ValueError(f"{path}: missing name")


def skill_body(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path}: missing opening frontmatter delimiter")
    try:
        closing = lines.index("---", 1)
    except ValueError as error:
        raise ValueError(f"{path}: missing closing frontmatter delimiter") from error
    return "\n".join(lines[closing + 1 :]).strip()


def main() -> int:
    failures: list[str] = []
    actual = {path.name for path in SKILLS.iterdir() if path.is_dir()}
    if actual != EXPECTED:
        failures.append(f"skill directories differ: expected {sorted(EXPECTED)}, got {sorted(actual)}")

    for name in sorted(EXPECTED):
        folder = SKILLS / name
        skill = folder / "SKILL.md"
        metadata = folder / "agents" / "openai.yaml"
        if not skill.is_file():
            failures.append(f"{skill}: missing")
            continue
        try:
            declared = frontmatter_name(skill)
        except ValueError as error:
            failures.append(str(error))
        else:
            if declared != name:
                failures.append(f"{skill}: name {declared!r} does not match directory {name!r}")
        if not metadata.is_file():
            failures.append(f"{metadata}: missing")
        if not (folder / "LICENSE").is_file():
            failures.append(f"{folder / 'LICENSE'}: missing")

    sources = json.loads((ROOT / "bundle-sources.json").read_text(encoding="utf-8"))
    for name, source in sources.items():
        for relative, expected_hash in source["files"].items():
            path = SKILLS / name / relative
            if not path.is_file():
                failures.append(f"{path}: missing pinned source file")
            elif digest(path) != expected_hash:
                failures.append(f"{path}: differs from pinned source {source['commit']}")

    grilling_notice = SKILLS / "grilling" / "NOTICE"
    if not grilling_notice.is_file():
        failures.append(f"{grilling_notice}: missing")

    grill_loop_license = SKILLS / "grill-loop" / "LICENSE"
    if grill_loop_license.is_file() and digest(grill_loop_license) != digest(ROOT / "LICENSE"):
        failures.append(f"{grill_loop_license}: differs from repository LICENSE")

    raycast_path = SKILLS / "grill-loop" / "assets" / "raycast-snippets.json"
    if not raycast_path.is_file():
        failures.append(f"{raycast_path}: missing")
    else:
        try:
            snippets = json.loads(raycast_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as error:
            failures.append(f"{raycast_path}: invalid JSON: {error}")
        else:
            if not isinstance(snippets, list):
                failures.append(f"{raycast_path}: expected a JSON array")
            else:
                names = [item.get("name") for item in snippets if isinstance(item, dict)]
                if len(snippets) != len(EXPECTED_RAYCAST_SNIPPETS) or set(names) != set(
                    EXPECTED_RAYCAST_SNIPPETS
                ):
                    failures.append(
                        f"{raycast_path}: expected exactly {sorted(EXPECTED_RAYCAST_SNIPPETS)}, "
                        f"got {names}"
                    )

                for item in snippets:
                    if not isinstance(item, dict):
                        failures.append(f"{raycast_path}: every snippet must be an object")
                        continue
                    name = item.get("name")
                    expected = EXPECTED_RAYCAST_SNIPPETS.get(name)
                    if expected is None:
                        continue
                    if item.get("keyword") != expected["keyword"]:
                        failures.append(
                            f"{raycast_path}: {name!r} keyword must be {expected['keyword']!r}"
                        )
                    try:
                        expected_text = skill_body(SKILLS / expected["skill"] / "SKILL.md")
                    except (OSError, ValueError) as error:
                        failures.append(str(error))
                    else:
                        if not item.get("text"):
                            failures.append(f"{raycast_path}: {name!r} text is empty")
                        elif item["text"] != expected_text:
                            failures.append(
                                f"{raycast_path}: {name!r} text differs from "
                                f"skills/{expected['skill']}/SKILL.md body"
                            )

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    print("multi-skill bundle is complete and pinned sources match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
