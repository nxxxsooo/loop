#!/usr/bin/env python3
"""Check or regenerate README excerpts and Raycast text from canonical skills."""

import argparse
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]
SNIPPETS = {"loop": "loop", "deep grill": "deep-grill", "deep design": "deep-design", "deep build": "deep-build", "what": "what"}


def body(name: str) -> str:
    text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0]:
        raise ValueError(f"{name}: invalid frontmatter")
    return parts[2].strip()


def outputs() -> dict[Path, str]:
    result = {}
    for name, pages in {
        "loop": ("README.md", "README.en.md"),
        "deep-grill": ("skills/deep-grill/README.md", "skills/deep-grill/README.zh-CN.md"),
    }.items():
        start, end = (f"<!-- {name}-skill-body:{suffix} -->" for suffix in ("start", "end"))
        excerpt = "\n".join("> " + line if line else ">" for line in body(name).splitlines())
        for page in pages:
            path = ROOT / page
            text = path.read_text(encoding="utf-8")
            if text.count(start) != 1 or text.count(end) != 1:
                raise ValueError(f"{page}: expected one excerpt marker pair")
            pattern = re.escape(start) + r"\n.*?\n" + re.escape(end)
            rendered, count = re.subn(pattern, lambda _: f"{start}\n{excerpt}\n{end}", text, flags=re.DOTALL)
            if count != 1:
                raise ValueError(f"{page}: invalid excerpt markers")
            result[path] = rendered
    path = ROOT / "skills/loop/assets/raycast-snippets.json"
    snippets = json.loads(path.read_text(encoding="utf-8"))
    if [item["name"] for item in snippets] != list(SNIPPETS):
        raise ValueError("unexpected Raycast snippet names or order")
    for item in snippets:
        item["text"] = body(SNIPPETS[item["name"]])
    result[path] = json.dumps(snippets, ensure_ascii=False, indent=2) + "\n"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="update generated text; otherwise check only")
    args = parser.parse_args()
    try:
        rendered = outputs()
    except (ValueError, OSError, KeyError) as error:
        print(error, file=sys.stderr)
        return 1
    changed = [path for path, text in rendered.items() if path.read_text(encoding="utf-8") != text]
    if args.write:
        for path in changed:
            path.write_text(rendered[path], encoding="utf-8")
    for path in changed:
        print(f"{'updated' if args.write else 'stale'}: {path.relative_to(ROOT)}")
    return 0 if args.write or not changed else 1


if __name__ == "__main__":
    raise SystemExit(main())
