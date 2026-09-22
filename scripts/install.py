#!/usr/bin/env python3
"""Copy-install Compound Influence for Cursor and/or Claude Code."""

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
    "CLAUDE.md",
)

SKIP_NAMES = {".git", "docs", "tests", "samples", "fixtures"}


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_cursor_dest() -> Path:
    return Path.home() / ".cursor" / "plugins" / "local" / "compound-influence"


def default_claude_dest() -> Path:
    return Path.home() / ".claude" / "compound-influence"


# Back-compat alias used by tests
def default_dest() -> Path:
    return default_cursor_dest()


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
            # CLAUDE.md is required for claude-friendly installs; allow missing
            # only if we somehow run on an ancient tree — fail closed otherwise.
            raise FileNotFoundError(f"missing required install item: {item}")
        target = dest / name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)
    leftover = {p.name for p in dest.iterdir()} & SKIP_NAMES
    if leftover:
        raise RuntimeError(f"install leaked skipped names: {sorted(leftover)}")


def install_claude_skill_mirrors(src: Path, skills_root: Path | None = None) -> list[Path]:
    """Also mirror each ci-* skill into ~/.claude/skills for discovery.

    Claude Code discovers top-level skill folders with SKILL.md. Cards still
    resolve best when the agent works inside the git checkout; mirrors are a
    discovery aid, not a full substitute for the pack.
    """
    root = skills_root or (Path.home() / ".claude" / "skills")
    root.mkdir(parents=True, exist_ok=True)
    installed: list[Path] = []
    skills_dir = src / "skills"
    for skill_dir in sorted(skills_dir.iterdir()):
        if not skill_dir.is_dir():
            continue
        if not (skill_dir / "SKILL.md").exists():
            continue
        dest = root / skill_dir.name
        if dest.is_symlink():
            raise RuntimeError(f"refusing to install over symlink: {dest}")
        if dest.exists():
            shutil.rmtree(dest)
        shutil.copytree(skill_dir, dest)
        # Pointer so agents know where cards live
        pointer = dest / "PACK_ROOT.md"
        pointer.write_text(
            "# Pack root\n\n"
            "Framework cards and the context contract live in the Compound Influence "
            "checkout or in `~/.claude/compound-influence/references/`.\n"
            "Prefer opening the git checkout in Claude Code so relative paths in "
            "SKILL.md resolve.\n",
            encoding="utf-8",
        )
        installed.append(dest)
    return installed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--target",
        choices=("cursor", "claude", "both"),
        default="cursor",
        help="install destination family (default: cursor)",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=None,
        help="override install destination (single target only)",
    )
    parser.add_argument(
        "--no-skill-mirrors",
        action="store_true",
        help="with --target claude|both, skip ~/.claude/skills/ci-* mirrors",
    )
    args = parser.parse_args(argv)
    src = repo_root()

    if args.dest is not None and args.target == "both":
        raise SystemExit("--dest cannot be combined with --target both")

    targets: list[tuple[str, Path]] = []
    if args.target in ("cursor", "both"):
        targets.append(("cursor", (args.dest or default_cursor_dest()).expanduser().resolve()))
    if args.target in ("claude", "both"):
        targets.append(("claude", (args.dest or default_claude_dest()).expanduser().resolve()))

    for label, dest in targets:
        copy_install(src, dest)
        print(f"installed ({label}) {src} -> {dest}")

    if args.target in ("claude", "both") and not args.no_skill_mirrors:
        mirrors = install_claude_skill_mirrors(src)
        print(f"mirrored {len(mirrors)} skills under ~/.claude/skills/")

    if args.target in ("cursor", "both"):
        print("reload Cursor plugins after copy-install")
    if args.target in ("claude", "both"):
        print("open this git checkout in Claude Code; see docs/for-claire.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
