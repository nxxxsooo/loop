#!/usr/bin/env python3
"""Validate the multi-skill package and pinned bundled sources."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {"grill-loop", "grilling", "deep-grill"}


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

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    print("multi-skill bundle is complete and pinned sources match")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
