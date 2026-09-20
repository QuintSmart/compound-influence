from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

WANG_ANCHORS = (
    "## Four stages",
    "## Authority trap",
    "## Pain / Cost / Gain",
    "## Headline–Insights–CTA",
    "## Become the default",
)

NEGO_ANCHORS = (
    "## Listening as concession",
    "## Labels",
    "## Compliance vs commitment",
    "## Silence vs pushback",
)


def test_wang_card_anchors():
    text = (ROOT / "references" / "wang-influence-cards.md").read_text(encoding="utf-8")
    for anchor in WANG_ANCHORS:
        assert anchor in text
    assert "Pain / Cost / Gain" in text


def test_negotiation_card_anchors():
    text = (ROOT / "references" / "negotiation-basics-card.md").read_text(encoding="utf-8")
    for anchor in NEGO_ANCHORS:
        assert anchor in text
