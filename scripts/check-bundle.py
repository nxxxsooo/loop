#!/usr/bin/env python3
"""Validate the loop package, contracts, generated snippets, and provenance."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXPECTED = {"loop", "deep-grill", "deep-design", "deep-build"}
EXPECTED_RAYCAST_SNIPPETS = {
    "loop": {"keyword": ";lp", "skill": "loop"},
    "deep grill": {"keyword": ";dg", "skill": "deep-grill"},
    "deep design": {"keyword": ";dd", "skill": "deep-design"},
    "deep build": {"keyword": ";db", "skill": "deep-build"},
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


def require_fragments(path: Path, fragments: tuple[str, ...], failures: list[str]) -> None:
    if not path.is_file():
        failures.append(f"{path}: missing contract file")
        return
    text = path.read_text(encoding="utf-8")
    for fragment in fragments:
        if fragment not in text:
            failures.append(f"{path}: missing contract fragment {fragment!r}")


def reject_fragments(path: Path, fragments: tuple[str, ...], failures: list[str]) -> None:
    if not path.is_file():
        failures.append(f"{path}: missing contract file")
        return
    text = path.read_text(encoding="utf-8")
    for fragment in fragments:
        if fragment in text:
            failures.append(f"{path}: contains retired contract fragment {fragment!r}")


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
    if set(sources) != {"deep-grill"}:
        failures.append(f"bundle-sources.json: expected only deep-grill, got {sorted(sources)}")
    for name, source in sources.items():
        if source.get("commit") != "d9d1fc6634080e6e7333f6e57afb0e75a057822a":
            failures.append(f"bundle-sources.json: {name} is not pinned to released v3 commit")
        for relative, expected_hash in source["files"].items():
            path = SKILLS / name / relative
            if not path.is_file():
                failures.append(f"{path}: missing pinned source file")
            elif digest(path) != expected_hash:
                failures.append(f"{path}: differs from pinned source {source['commit']}")

    contracts = {
        "loop": (
            "When the user's entire trimmed message is exactly `?`",
            "without asking the user to nominate a skill or choose a route",
            "Route By Artifact Readiness",
            "OpenSpec is an internal adapter owned by `deep-design` and `deep-build`",
            "Wayfinder is not part of this workflow",
        ),
        "deep-grill": (
            "discovery mode",
            "audit mode",
            "supported but gated behind another mode",
            "confirmed Product Brief",
        ),
        "deep-design": (
            "confirmed Product Brief",
            "confirmed Build Contract",
            "Use OpenSpec As An Adapter",
            "Do not implement",
        ),
        "deep-build": (
            "confirmed Build Contract",
            "Build In Verified Slices",
            "Changes:",
            "Remaining risks:",
        ),
    }
    for name, fragments in contracts.items():
        require_fragments(SKILLS / name / "SKILL.md", fragments, failures)
        require_fragments(
            SKILLS / name / "agents" / "openai.yaml",
            ("allow_implicit_invocation: true",),
            failures,
        )

    reject_fragments(
        SKILLS / "loop" / "SKILL.md",
        ("`grill-loop`", "Use `grilling`", "`what`", "Offer `wayfinder`"),
        failures,
    )
    reject_fragments(
        SKILLS / "deep-grill" / "SKILL.md",
        ("recommend `grilling`", "hands that interview back to `grilling`"),
        failures,
    )

    for name in ("loop", "deep-design", "deep-build"):
        license_path = SKILLS / name / "LICENSE"
        if license_path.is_file() and digest(license_path) != digest(ROOT / "LICENSE"):
            failures.append(f"{license_path}: differs from repository LICENSE")

    raycast_path = SKILLS / "loop" / "assets" / "raycast-snippets.json"
    if not raycast_path.is_file():
        failures.append(f"{raycast_path}: missing")
    else:
        try:
            snippets = json.loads(raycast_path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError) as error:
            failures.append(f"{raycast_path}: invalid JSON: {error}")
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
                    if item.get("text") != expected_text:
                        failures.append(
                            f"{raycast_path}: {name!r} text differs from "
                            f"skills/{expected['skill']}/SKILL.md body"
                        )

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    print("loop bundle contracts, snippets, licenses, and pinned sources are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
