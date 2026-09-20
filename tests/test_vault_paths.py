from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from vault_paths import (  # noqa: E402
    briefing_dir,
    find_influence_akten,
    influence_akte_path,
    resolve_akte_path,
)


def test_briefing_path_shape(tmp_path: Path):
    path = influence_akte_path("Acme Corp", vault=tmp_path)
    assert path == (
        tmp_path
        / "S03 QuintSmart"
        / "300-399 Projects"
        / "Acme Corp"
        / "Briefing"
        / "influence-akte.md"
    )
    assert briefing_dir("Acme Corp", vault=tmp_path) == path.parent


def test_resolve_named_and_slug(tmp_path: Path):
    named = tmp_path / "custom" / "influence-akte.md"
    named.parent.mkdir(parents=True)
    named.write_text("# x\n", encoding="utf-8")
    assert resolve_akte_path(named=named) == named.resolve()
    assert resolve_akte_path(client_or_project="X", vault=tmp_path).name == "influence-akte.md"


def test_find_akten(tmp_path: Path):
    a = (
        tmp_path
        / "S03 QuintSmart"
        / "300-399 Projects"
        / "A"
        / "Briefing"
        / "influence-akte.md"
    )
    a.parent.mkdir(parents=True)
    a.write_text("# A\n", encoding="utf-8")
    found = find_influence_akten(vault=tmp_path)
    assert found == [a]
