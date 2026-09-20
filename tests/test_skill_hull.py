from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    "ci-akte",
    "ci-diagnose",
    "ci-frame",
    "ci-live",
    "ci-pcg",
    "ci-hic",
    "ci-buyer",
    "ci-mirror",
    "ci-default",
)


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


def test_pcg_loads_deep_card():
    body = (ROOT / "skills" / "ci-pcg" / "SKILL.md").read_text(encoding="utf-8")
    assert "references/pain-cost-gain-card.md" in body
    assert "one beat" in body.lower() or "One beat" in body


def test_hic_cta_first():
    body = (ROOT / "skills" / "ci-hic" / "SKILL.md").read_text(encoding="utf-8")
    assert "references/headline-insights-cta-card.md" in body
    assert "CTA first" in body or "CTA zuerst" in body.lower() or "CTA first" in body
