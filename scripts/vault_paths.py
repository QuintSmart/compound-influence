#!/usr/bin/env python3
"""Resolve MyPKMS S03 Briefing paths for influence-akte.md."""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

AKTE_FILENAME = "influence-akte.md"
S03_PROJECTS = Path("S03 QuintSmart") / "300-399 Projects"
BRIEFING_DIRNAME = "Briefing"


def default_vault_root() -> Path:
    env = os.environ.get("COMPOUND_INFLUENCE_VAULT")
    if env:
        return Path(env).expanduser().resolve()
    return (Path.home() / "Documents" / "GitHub" / "MyPKMS").resolve()


def plugin_checkout_roots() -> list[Path]:
    """Known plugin checkouts that must never hold a live Akte."""
    roots = [
        Path(__file__).resolve().parents[1],
        Path.home() / ".cursor" / "plugins" / "local" / "compound-influence",
    ]
    return [p.resolve() for p in roots]


def is_under_plugin_checkout(path: Path) -> bool:
    resolved = path.expanduser().resolve()
    for root in plugin_checkout_roots():
        try:
            resolved.relative_to(root)
            return True
        except ValueError:
            continue
    return False


def assert_writable_akte_path(path: Path) -> Path:
    resolved = path.expanduser().resolve()
    if is_under_plugin_checkout(resolved):
        raise ValueError(
            f"refusing to write Akte inside plugin checkout: {resolved}"
        )
    return resolved


def briefing_dir(client_or_project: str, vault: Path | None = None) -> Path:
    slug = client_or_project.strip().strip("/")
    if not slug:
        raise ValueError("client_or_project slug is required")
    root = (vault or default_vault_root()).resolve()
    return root / S03_PROJECTS / slug / BRIEFING_DIRNAME


def influence_akte_path(client_or_project: str, vault: Path | None = None) -> Path:
    return briefing_dir(client_or_project, vault=vault) / AKTE_FILENAME


def resolve_akte_path(
    *,
    named: Path | str | None = None,
    client_or_project: str | None = None,
    vault: Path | None = None,
) -> Path | None:
    """Resolve an Akte path without creating it.

    Priority: explicit named path → default path for slug → None.
    Does not create directories or files.
    """
    if named is not None:
        return assert_writable_akte_path(Path(named).expanduser())
    if client_or_project:
        return influence_akte_path(client_or_project, vault=vault)
    return None


def find_influence_akten(vault: Path | None = None) -> list[Path]:
    root = (vault or default_vault_root()) / S03_PROJECTS
    if not root.is_dir():
        return []
    return sorted(root.rglob(AKTE_FILENAME))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slug", help="client/project folder under S03 Projects")
    parser.add_argument("--vault", type=Path, default=None)
    parser.add_argument("--list", action="store_true", help="list known influence-akte.md")
    args = parser.parse_args(argv)
    vault = args.vault.expanduser().resolve() if args.vault else None
    if args.list:
        for path in find_influence_akten(vault):
            print(path)
        return 0
    if not args.slug:
        parser.error("--slug is required unless --list")
    print(influence_akte_path(args.slug, vault=vault))
    return 0


if __name__ == "__main__":
    sys.exit(main())
