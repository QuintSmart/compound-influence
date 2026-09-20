from __future__ import annotations

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from akte_contract import (  # noqa: E402
    AmbiguousAkte,
    append_log_entry,
    create_akte,
    load_akte,
    locate_akte,
)
from vault_paths import assert_writable_akte_path  # noqa: E402


def test_fresh_akte_validates():
    report = load_akte(ROOT / "fixtures" / "fresh-akte" / "influence-akte.expected.md")
    assert report.ok
    assert "Buyer Map" in report.sections


def test_missing_heading_fails(tmp_path: Path):
    path = tmp_path / "influence-akte.md"
    path.write_text("# Influence Akte\n\n## Buyer Map\n\nx\n", encoding="utf-8")
    report = load_akte(path)
    assert not report.ok
    assert any("missing required section: Request / Context" in e for e in report.errors)


def test_append_diagnose_preserves_framing_log():
    history = ROOT / "fixtures" / "with-history" / "influence-akte.expected.md"
    # work on a copy — fixtures are read-only contract
    import tempfile

    with tempfile.TemporaryDirectory() as tmp:
        akte = Path(tmp) / "influence-akte.md"
        akte.write_text(history.read_text(encoding="utf-8"), encoding="utf-8")
        before = load_akte(akte).sections["Framing Log"]
        append_log_entry(akte, "Diagnose Log", "- Buyer: test\n- Felt Problem: test")
        after = load_akte(akte)
        assert after.sections["Framing Log"] == before
        assert "Felt Problem: test" in after.sections["Diagnose Log"]


def test_plugin_checkout_write_rejected():
    with pytest.raises(ValueError, match="plugin checkout"):
        assert_writable_akte_path(ROOT / "influence-akte.md")


def test_history_keeps_open_ask():
    report = load_akte(ROOT / "fixtures" / "with-history" / "influence-akte.expected.md")
    assert report.ok
    assert "Pilot" in report.sections["Open Ask"]
    assert "Buyer" in report.sections["Diagnose Log"]


def test_ambiguous_akten_raise():
    matches = [
        Path("/tmp/a/influence-akte.md"),
        Path("/tmp/b/influence-akte.md"),
    ]
    with pytest.raises(AmbiguousAkte):
        locate_akte(vault_matches=matches)


def test_create_akte_outside_plugin(tmp_path: Path):
    path = tmp_path / "Briefing" / "influence-akte.md"
    create_akte(path, request="Demo", client="Demo")
    report = load_akte(path)
    assert report.ok
    assert "Demo" in report.sections["Request / Context"]
