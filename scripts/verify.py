#!/usr/bin/env python3
"""Local Definition of Done for Compound Influence."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
sys.path.insert(0, str(SCRIPTS))

from akte_contract import (  # noqa: E402
    append_log_entry,
    create_akte,
    load_akte,
)
from install import copy_install  # noqa: E402
from vault_paths import (  # noqa: E402
    assert_writable_akte_path,
    influence_akte_path,
    is_under_plugin_checkout,
)

SKILLS = ("ci-akte", "ci-diagnose", "ci-frame", "ci-live")

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


def check_hull(root: Path = ROOT) -> None:
    plugin = root / ".cursor-plugin" / "plugin.json"
    data = json.loads(plugin.read_text(encoding="utf-8"))
    if data.get("name") != "compound-influence":
        raise SystemExit("plugin name must be compound-influence")
    if data.get("displayName") != "Compound Influence":
        raise SystemExit("displayName must be Compound Influence")
    if data.get("skills") != "./skills/":
        raise SystemExit("plugin.json must point skills at ./skills/")
    help_text = (root / "commands" / "ci-help.md").read_text(encoding="utf-8")
    if "Compound Influence" not in help_text:
        raise SystemExit("ci-help must name Compound Influence")
    for skill in SKILLS:
        if skill not in help_text:
            raise SystemExit(f"ci-help must name {skill}")
        path = root / "skills" / skill / "SKILL.md"
        if not path.exists():
            raise SystemExit(f"missing skill: {path}")
        body = path.read_text(encoding="utf-8")
        if "references/context-contract.md" not in body:
            raise SystemExit(f"{skill} must reference context-contract.md")
        name_match = re.search(r"^name:\s*(\S+)\s*$", body, re.M)
        if not name_match or name_match.group(1) != skill:
            raise SystemExit(f"{skill} frontmatter name must be {skill}")


def check_method(root: Path = ROOT) -> None:
    wang = root / "references" / "wang-influence-cards.md"
    nego = root / "references" / "negotiation-basics-card.md"
    examples = root / "references" / "quintsmart-examples.md"
    contract = root / "references" / "context-contract.md"
    for path in (wang, nego, examples, contract):
        if not path.exists():
            raise SystemExit(f"missing {path.relative_to(root)}")
    wang_text = wang.read_text(encoding="utf-8")
    for anchor in WANG_ANCHORS:
        if anchor not in wang_text:
            raise SystemExit(f"wang card missing anchor: {anchor}")
    if "Pain / Cost / Gain" not in wang_text and "Pain/Cost/Gain" not in wang_text:
        raise SystemExit("wang card must include Pain/Cost/Gain")
    nego_text = nego.read_text(encoding="utf-8")
    for anchor in NEGO_ANCHORS:
        if anchor not in nego_text:
            raise SystemExit(f"negotiation card missing anchor: {anchor}")
    diagnose = (root / "skills" / "ci-diagnose" / "SKILL.md").read_text(encoding="utf-8")
    frame = (root / "skills" / "ci-frame" / "SKILL.md").read_text(encoding="utf-8")
    live = (root / "skills" / "ci-live" / "SKILL.md").read_text(encoding="utf-8")
    if "ohne Akte" not in frame and "ohne-Akte" not in frame:
        raise SystemExit("ci-frame must document ohne-Akte path")
    if "ablehnen" not in live.lower():
        raise SystemExit("ci-live must document ablehnen leaves Akte unchanged")
    if "write-back" not in diagnose.lower() and "Write-back" not in diagnose:
        raise SystemExit("ci-diagnose must document write-back default")


def check_brand(root: Path = ROOT) -> None:
    readme = (root / "README.md").read_text(encoding="utf-8")
    help_text = (root / "commands" / "ci-help.md").read_text(encoding="utf-8")
    for text, name in ((readme, "README"), (help_text, "ci-help")):
        if "Compound Influence" not in text:
            raise SystemExit(f"{name} must present Compound Influence")
    if "S03" not in readme or "Briefing" not in readme:
        raise SystemExit("README must state Akte lives in PKMS S03 Briefing")
    if "Never store a live" not in readme and "never store a live" not in readme.lower():
        raise SystemExit("README must forbid live Akte in this checkout")


def check_fixtures(root: Path = ROOT) -> None:
    fresh = root / "fixtures" / "fresh-akte" / "influence-akte.expected.md"
    report = load_akte(fresh)
    if not report.ok:
        raise SystemExit(f"fresh-akte fixture failed: {report.errors}")
    history = root / "fixtures" / "with-history" / "influence-akte.expected.md"
    hist = load_akte(history)
    if not hist.ok:
        raise SystemExit(f"with-history fixture failed: {hist.errors}")
    open_ask = hist.sections.get("Open Ask", "")
    if not open_ask.strip() or open_ask.strip() == "_TBD_":
        raise SystemExit("with-history fixture must expose Open Ask")
    diagnose_log = hist.sections.get("Diagnose Log", "")
    if "Buyer" not in diagnose_log and "buyer" not in diagnose_log.lower():
        raise SystemExit("with-history Diagnose Log must keep prior Buyer notes")
    after = root / "fixtures" / "diagnose-writeback" / "influence-akte.after.md"
    after_report = load_akte(after)
    if not after_report.ok:
        raise SystemExit(f"diagnose-writeback after fixture failed: {after_report.errors}")
    after_log = after_report.sections.get("Diagnose Log", "")
    if "Felt Problem" not in after_log and "felt problem" not in after_log.lower():
        raise SystemExit("AE1: after-fixture Diagnose Log needs Felt Problem marker")
    if "Buyer" not in after_log and "buyer" not in after_log.lower():
        raise SystemExit("AE1: after-fixture Diagnose Log needs Buyer marker")
    frame_note = root / "fixtures" / "frame-ohne-akte" / "expectation.md"
    if not frame_note.exists():
        raise SystemExit("missing frame-ohne-akte expectation")
    if "no vault write" not in frame_note.read_text(encoding="utf-8").lower():
        raise SystemExit("frame-ohne-akte fixture must mark no vault write")
    # Plugin checkout write must be rejected
    try:
        assert_writable_akte_path(root / "influence-akte.md")
    except ValueError:
        pass
    else:
        raise SystemExit("plugin checkout write path must be rejected")
    # Append preserves Framing Log
    with tempfile.TemporaryDirectory() as tmp:
        akte = Path(tmp) / "influence-akte.md"
        akte.write_text(history.read_text(encoding="utf-8"), encoding="utf-8")
        framing_before = load_akte(akte).sections.get("Framing Log", "")
        append_log_entry(
            akte,
            "Diagnose Log",
            "- Buyer: append-test\n- Felt Problem: append-test",
        )
        after_append = load_akte(akte)
        if after_append.sections.get("Framing Log", "") != framing_before:
            raise SystemExit("append Diagnose Log must preserve Framing Log")
        if "append-test" not in after_append.sections.get("Diagnose Log", ""):
            raise SystemExit("append Diagnose Log must retain new entry")


def check_install_copy(root: Path = ROOT) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        dest = Path(tmp) / "compound-influence"
        copy_install(root, dest)
        if not (dest / ".cursor-plugin" / "plugin.json").exists():
            raise SystemExit("copy-install did not write plugin hull")
        if dest.is_symlink():
            raise SystemExit("copy-install produced a symlink")
        for leaked in ("docs", ".git", "fixtures", "tests", "samples"):
            if (dest / leaked).exists():
                raise SystemExit(f"copy-install leaked skipped name: {leaked}")
        for required in (".cursor-plugin", "skills", "commands", "references", "scripts", "README.md"):
            if not (dest / required).exists():
                raise SystemExit(f"copy-install missing {required}")
        linked = Path(tmp) / "linked"
        linked.symlink_to(dest)
        try:
            copy_install(root, linked)
        except RuntimeError as exc:
            if "symlink" not in str(exc):
                raise SystemExit(f"symlink install raised unexpected error: {exc}")
        else:
            raise SystemExit("install over symlink must fail")


def check_vault_helpers(root: Path = ROOT) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        vault = Path(tmp) / "MyPKMS"
        path = influence_akte_path("Demo Client", vault=vault)
        expected = (
            vault
            / "S03 QuintSmart"
            / "300-399 Projects"
            / "Demo Client"
            / "Briefing"
            / "influence-akte.md"
        )
        if path.resolve() != expected.resolve():
            raise SystemExit(f"unexpected akte path: {path}")
        create_akte(path, request="Demo offer", client="Demo Client")
        report = load_akte(path)
        if not report.ok:
            raise SystemExit(f"created akte invalid: {report.errors}")
        if is_under_plugin_checkout(path):
            raise SystemExit("temp vault path incorrectly flagged as plugin checkout")


def verify(run_pytest: bool = True, root: Path = ROOT) -> None:
    check_hull(root)
    check_method(root)
    check_brand(root)
    check_fixtures(root)
    check_vault_helpers(root)
    check_install_copy(root)
    if run_pytest:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests", "-q"],
            cwd=root,
            check=False,
        )
        if result.returncode != 0:
            raise SystemExit("pytest failed")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skip-pytest", action="store_true")
    args = parser.parse_args(argv)
    verify(run_pytest=not args.skip_pytest)
    print("verify ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
