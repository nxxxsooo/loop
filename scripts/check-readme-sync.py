#!/usr/bin/env python3
"""Verify that both README excerpts exactly match the SKILL.md body."""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
START = "<!-- grill-loop-skill-body:start -->"
END = "<!-- grill-loop-skill-body:end -->"


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
    expected = skill_body(ROOT / "SKILL.md")
    failures = []
    for name in ("README.md", "README.zh-CN.md"):
        path = ROOT / name
        try:
            actual = readme_excerpt(path)
        except ValueError as error:
            failures.append(str(error))
            continue

        if actual != expected:
            failures.append(f"{path}: embedded skill body differs from SKILL.md")

    if failures:
        print("\n".join(failures), file=sys.stderr)
        return 1

    print("README skill excerpts match SKILL.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
