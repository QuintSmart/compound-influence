#!/usr/bin/env python3
"""Copy-install Compound Influence into ~/.cursor/plugins/local/compound-influence."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

COPY_NAMES = (
    ".cursor-plugin",
    "skills",
    "commands",
    "references",
    "scripts",
    "README.md",
)

SKIP_NAMES = {".git", "docs", "tests", "samples", "fixtures"}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_dest() -> Path:
    return Path.home() / ".cursor" / "plugins" / "local" / "compound-influence"


def copy_install(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.is_symlink():
        raise RuntimeError(f"refusing to install over symlink: {dest}")
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    for name in COPY_NAMES:
        item = src / name
        if not item.exists():
            raise FileNotFoundError(f"missing required install item: {item}")
        target = dest / name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)
    leftover = {p.name for p in dest.iterdir()} & SKIP_NAMES
    if leftover:
        raise RuntimeError(f"install leaked skipped names: {sorted(leftover)}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--dest",
        type=Path,
        default=default_dest(),
        help="install destination (default: ~/.cursor/plugins/local/compound-influence)",
    )
    args = parser.parse_args(argv)
    src = repo_root()
    dest = args.dest.expanduser().resolve()
    copy_install(src, dest)
    print(f"installed {src} -> {dest}")
    print("reload Cursor plugins after copy-install")
    return 0


if __name__ == "__main__":
    sys.exit(main())
