from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ("ci-akte", "ci-diagnose", "ci-frame", "ci-live")


def test_skills_and_help():
    help_text = (ROOT / "commands" / "ci-help.md").read_text(encoding="utf-8")
    assert "Compound Influence" in help_text
    for skill in SKILLS:
        assert skill in help_text
        body = (ROOT / "skills" / skill / "SKILL.md").read_text(encoding="utf-8")
        assert "references/context-contract.md" in body
        name = re.search(r"^name:\s*(\S+)\s*$", body, re.M)
        assert name and name.group(1) == skill


def test_frame_documents_ohne_akte():
    body = (ROOT / "skills" / "ci-frame" / "SKILL.md").read_text(encoding="utf-8")
    assert "ohne Akte" in body or "ohne-Akte" in body


def test_live_documents_ablehnen():
    body = (ROOT / "skills" / "ci-live" / "SKILL.md").read_text(encoding="utf-8")
    assert "ablehnen" in body.lower()
