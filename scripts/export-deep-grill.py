#!/usr/bin/env python3
"""Export canonical DG without committing, pushing, or touching other skills."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
MARKER = "loop-source.json"
OWNER = "https://github.com/nxxxsooo/loop"
PRIVATE = {".git", ".local", ".worktrees", "__pycache__", ".DS_Store"}


def relative_path(value: str) -> str:
    path = PurePosixPath(value)
    if not path.parts or path.is_absolute() or str(path) != value or "\\" in value:
        raise ValueError(f"invalid package path: {value!r}")
    if any(part in PRIVATE or part in {"..", "."} for part in path.parts):
        raise ValueError(f"private or escaping package path: {value!r}")
    if value == MARKER:
        raise ValueError(f"{MARKER} is generated, not a source file")
    return value


def reject_symlinks(path: Path) -> None:
    for part in (path, *path.parents):
        if part.is_symlink():
            raise ValueError(f"refusing symlink path: {part}")


def inventory(path: Path) -> set[str]:
    found = set()
    for base, dirs, files in os.walk(path, followlinks=False):
        dirs[:] = [name for name in dirs if name not in PRIVATE]
        for name in dirs + files:
            item = Path(base) / name
            if item.is_symlink():
                raise ValueError(f"refusing package symlink: {item}")
        found.update((Path(base) / name).relative_to(path).as_posix() for name in files if name not in PRIVATE)
    return found


def description(payload: dict[str, tuple[bytes, int]]) -> dict:
    return {
        name: {"sha256": hashlib.sha256(data).hexdigest(), "mode": mode}
        for name, (data, mode) in sorted(payload.items())
    }


def package(root: Path) -> tuple[dict, dict[str, tuple[bytes, int]]]:
    config = json.loads((root / "distributions/deep-grill.json").read_text(encoding="utf-8"))
    source = root / relative_path(config["source"])
    reject_symlinks(source)
    names = [relative_path(name) for name in config["files"]]
    if len(set(names)) != len(names) or set(names) & set(config["retired_files"]):
        raise ValueError("duplicate or retired files in distribution manifest")
    for name in config["retired_files"]:
        relative_path(name)
    actual = inventory(source)
    if actual != set(names):
        raise ValueError(f"canonical inventory differs from manifest: {sorted(actual ^ set(names))}")
    payload = {name: ((source / name).read_bytes(), (source / name).stat().st_mode & 0o777) for name in names}
    marker = {"repository": OWNER, "source": config["source"], "files": description(payload)}
    payload[MARKER] = ((json.dumps(marker, indent=2, sort_keys=True) + "\n").encode(), 0o644)
    return config, payload


def git(output: Path, *args: str) -> str:
    return subprocess.check_output(["git", "-C", str(output), *args], text=True, stderr=subprocess.PIPE).strip()


def verify_previous(output: Path, config: dict) -> set[str]:
    """Only update our unchanged export or the exact pristine migration baseline."""
    if (output / ".git").exists():
        if Path(git(output, "rev-parse", "--show-toplevel")).resolve() != output:
            raise ValueError("output must be a standalone repository root")
        if git(output, "status", "--porcelain=v1", "--untracked-files=all"):
            raise ValueError("distribution checkout has local changes; inspect/commit them first")
        remote = git(output, "remote", "get-url", "origin").removesuffix(".git")
        if remote not in {config["repository"], "git@github.com:nxxxsooo/deep-grill"}:
            raise ValueError("distribution checkout has an unexpected origin")

    marker = output / MARKER
    if marker.is_file():
        previous = json.loads(marker.read_text(encoding="utf-8"))
        if previous.get("repository") != OWNER or previous.get("source") != config["source"]:
            raise ValueError("output belongs to another source")
        names = {relative_path(name) for name in previous["files"]}
        if inventory(output) != names | {MARKER}:
            raise ValueError("output contains missing or unexpected files")
        actual = {name: ((output / name).read_bytes(), (output / name).stat().st_mode & 0o777) for name in names}
        if description(actual) != previous["files"]:
            raise ValueError("export has local edits; refusing to overwrite")
        return names

    baseline = set(config["files"]) | set(config["retired_files"])
    if not (output / ".git").exists() or git(output, "rev-parse", "HEAD") != config["baseline_commit"]:
        raise ValueError("existing output is not a known export or the pristine DG migration baseline")
    if inventory(output) != baseline or set(git(output, "ls-files").splitlines()) != baseline:
        raise ValueError("migration baseline contains unexpected files")
    return baseline


def export(root: Path, output: Path, *, check: bool = False, update: bool = False) -> None:
    config, payload = package(root)
    output = Path(os.path.abspath(output))
    reject_symlinks(output)
    source = (root / config["source"]).resolve()
    if output == root.resolve() or output in source.parents or source == output or source in output.parents:
        raise ValueError("output must not overlap canonical source")
    if output.is_relative_to(root.resolve()) and not output.is_relative_to(root.resolve() / ".local"):
        raise ValueError("in-repository exports must stay under .local, outside maintained source")
    if output.exists() and not output.is_dir():
        raise ValueError("output is not a directory")
    actual = inventory(output) if output.exists() else set()
    if check:
        if not output.is_dir() or actual != set(payload):
            raise ValueError(f"export inventory differs: {sorted(actual ^ set(payload))}")
        for name, (data, mode) in payload.items():
            path = output / name
            if path.read_bytes() != data or path.stat().st_mode & 0o777 != mode:
                raise ValueError(f"export differs from canonical source: {name}")
        return
    previous = set()
    if output.exists() and any(output.iterdir()):
        if not update:
            raise ValueError("output is not empty; use --check, or --update for a known clean export")
        previous = verify_previous(output, config)
    for name in payload:
        path = output / name
        if path.exists() and not path.is_file():
            raise ValueError(f"output path is not a file: {path}")
        for parent in path.parents:
            if parent == output.parent:
                break
            if parent.exists() and not parent.is_dir():
                raise ValueError(f"output parent is not a directory: {parent}")
    output.mkdir(parents=True, exist_ok=True)
    for name, (data, mode) in payload.items():
        path = output / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        path.chmod(mode)
    # Only files in the verified previous distribution are ever retired.
    for name in sorted(previous - set(payload)):
        (output / name).unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=ROOT / ".local/exports/deep-grill")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="verify an export without writing")
    mode.add_argument("--update", action="store_true", help="refresh a known unchanged export or clean DG checkout")
    args = parser.parse_args()
    try:
        export(ROOT, args.output, check=args.check, update=args.update)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as error:
        print(f"deep-grill export: {error}", file=sys.stderr)
        return 1
    print(f"deep-grill {'verified' if args.check else 'exported'}: {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
