from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from verify import (  # noqa: E402
    check_brand,
    check_fixtures,
    check_hull,
    check_install_copy,
    check_method,
    check_vault_helpers,
)


def test_verify_checks_pass():
    check_hull(ROOT)
    check_method(ROOT)
    check_brand(ROOT)
    check_fixtures(ROOT)
    check_vault_helpers(ROOT)
    check_install_copy(ROOT)


def test_diagnose_after_fixture_ae1():
    from akte_contract import load_akte

    after = load_akte(ROOT / "fixtures" / "diagnose-writeback" / "influence-akte.after.md")
    assert after.ok
    log = after.sections["Diagnose Log"]
    assert "Buyer" in log
    assert "Felt Problem" in log
