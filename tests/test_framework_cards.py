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

DEEP = {
    "pain-cost-gain-card.md": ("## Three axes", "## Vitamin vs painkiller", "## Mirror when they do not feel it"),
    "headline-insights-cta-card.md": ("## Three parts", "## CTA needs the most discipline", "## Pyramid Principle vs H–I–CTA"),
    "buyer-map-card.md": ("## Know your buyer", "## Map more than the wallet"),
    "authority-engagement-card.md": ("## Authority trap", "## Silence vs pushback"),
    "become-default-card.md": ("## Economics of trust", "## Operator moves"),
}


def test_wang_card_anchors():
    text = (ROOT / "references" / "wang-influence-cards.md").read_text(encoding="utf-8")
    for anchor in WANG_ANCHORS:
        assert anchor in text
    assert "Pain / Cost / Gain" in text


def test_negotiation_card_anchors():
    text = (ROOT / "references" / "negotiation-basics-card.md").read_text(encoding="utf-8")
    for anchor in NEGO_ANCHORS:
        assert anchor in text


def test_deep_card_anchors():
    for filename, anchors in DEEP.items():
        text = (ROOT / "references" / filename).read_text(encoding="utf-8")
        for anchor in anchors:
            assert anchor in text, f"{filename} missing {anchor}"
