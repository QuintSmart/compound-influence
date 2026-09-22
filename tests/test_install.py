from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from install import (  # noqa: E402
    copy_install,
    default_claude_dest,
    default_dest,
    install_claude_skill_mirrors,
)


def test_copy_install_creates_required_trees(tmp_path: Path):
    dest = tmp_path / "compound-influence"
    copy_install(ROOT, dest)
    for name in (
        ".cursor-plugin",
        "skills",
        "commands",
        "references",
        "scripts",
        "README.md",
        "CLAUDE.md",
    ):
        assert (dest / name).exists()
    for leaked in ("docs", "tests", "fixtures", "samples", ".git"):
        assert not (dest / leaked).exists()


def test_claude_skill_mirrors(tmp_path: Path):
    skills_root = tmp_path / "skills"
    installed = install_claude_skill_mirrors(ROOT, skills_root=skills_root)
    assert len(installed) >= 9
    assert (skills_root / "ci-pcg" / "SKILL.md").exists()
    assert (skills_root / "ci-pcg" / "PACK_ROOT.md").exists()


def test_default_claude_dest_name():
    assert default_claude_dest().name == "compound-influence"


def test_copy_install_replaces_existing(tmp_path: Path):
    dest = tmp_path / "compound-influence"
    copy_install(ROOT, dest)
    marker = dest / "skills" / "stale.txt"
    marker.write_text("stale", encoding="utf-8")
    copy_install(ROOT, dest)
    assert not marker.exists()
    assert (dest / "skills" / "ci-diagnose" / "SKILL.md").exists()


def test_symlink_dest_refused(tmp_path: Path):
    real = tmp_path / "real"
    real.mkdir()
    linked = tmp_path / "linked"
    linked.symlink_to(real)
    with pytest.raises(RuntimeError, match="symlink"):
        copy_install(ROOT, linked)


def test_default_dest_name():
    assert default_dest().name == "compound-influence"
