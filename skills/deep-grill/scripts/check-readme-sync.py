#!/usr/bin/env python3
"""Verify the public deep-grill contract and embedded README excerpts."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- deep-grill-skill-body:start -->"
END = "<!-- deep-grill-skill-body:end -->"


def skill_body(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        raise ValueError(f"{path}: missing opening frontmatter delimiter")

    try:
        closing = lines.index("---", 1)
    except ValueError as error:
        raise ValueError(f"{path}: missing closing frontmatter delimiter") from error

    return "\n".join(lines[closing + 1 :]).strip()


def readme_excerpt(path: Path) -> str:
    lines = path.read_text(encoding="utf-8").splitlines()
    if lines.count(START) != 1 or lines.count(END) != 1:
        raise ValueError(f"{path}: expected exactly one skill-body marker pair")

    start = lines.index(START) + 1
    end = lines.index(END, start)
    quoted = []
    for line in lines[start:end]:
        if line == ">":
            quoted.append("")
        elif line.startswith("> "):
            quoted.append(line[2:])
        else:
            raise ValueError(f"{path}: non-blockquote line inside skill-body markers")

    return "\n".join(quoted).strip()


def main() -> int:
    skill_path = ROOT / "SKILL.md"
    skill_text = skill_path.read_text(encoding="utf-8")
    expected = skill_body(skill_path)
    failures = []

    required = (
        "discovery mode",
        "audit mode",
        "unavailable in the current mode",
        "same concise localized prose question immediately",
        "pending frontier and the recommended option",
        "continue from the ordinary reply",
        "confirmed Product Brief",
        "continue in discovery mode within deep-grill",
        "both modes are self-contained within deep-grill",
    )
    rejected = (
        "recommend `grilling`",
        "hands that interview back to `grilling`",
        "If a user-owned decision tree emerges, recommend",
        "supported but gated behind another mode",
        "do not present the decision in prose",
        "ask the user to switch and continue",
        "wait with the pending frontier intact",
        "grilling-upstream.md",
        "name: grilling",
    )
    for fragment in required:
        if fragment not in skill_text:
            failures.append(f"{skill_path}: missing required contract fragment {fragment!r}")
    for fragment in rejected:
        if fragment in skill_text:
            failures.append(f"{skill_path}: contains retired contract fragment {fragment!r}")

    if (ROOT / "references" / "grilling-upstream.md").exists():
        failures.append("retired grilling source must not be bundled")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    for fragment in ("Copyright (c) 2026 Mingjian Shao", "Permission is hereby granted", "THE SOFTWARE IS PROVIDED"):
        if fragment not in license_text:
            failures.append(f"required DG MIT license text missing: {fragment}")

    for name in ("README.md", "README.zh-CN.md"):
        path = ROOT / name
        try:
            actual = readme_excerpt(path)
        except ValueError as error:
            failures.append(str(error))
            continue

        if actual != expected:
            failures.append(f"{path}: embedded skill body differs from SKILL.md")
        text = path.read_text(encoding="utf-8")
        for link in ("https://github.com/nxxxsooo/loop", "https://github.com/nxxxsooo/loop/tree/main/skills/deep-grill"):
            if link not in text:
                failures.append(f"{path}: missing loop/source entry point {link}")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    print("deep-grill standalone contract, license, links, and README excerpts are valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
