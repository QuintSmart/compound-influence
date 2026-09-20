#!/usr/bin/env python3
"""Parse, validate, and append to a Compound Influence Akte."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from vault_paths import (  # noqa: E402
    assert_writable_akte_path,
    find_influence_akten,
    is_under_plugin_checkout,
)

REQUIRED_SECTIONS = (
    "Request / Context",
    "Buyer Map",
    "Felt Problem (Pain / Cost / Gain)",
    "Wants / Fears / Constraints",
    "Open Ask",
    "Diagnose Log",
    "Framing Log",
    "Live Log",
    "Default Status Notes",
)

LOG_SECTIONS = ("Diagnose Log", "Framing Log", "Live Log")
HEADING_RE = re.compile(r"^(##)\s+(.+?)\s*$", re.M)


class AmbiguousAkte(Exception):
    def __init__(self, matches: list[Path]):
        self.matches = matches
        super().__init__(
            f"multiple Akten, name one: {', '.join(str(p) for p in matches)}"
        )


@dataclass
class AkteReport:
    path: Path
    sections: dict[str, str] = field(default_factory=dict)
    errors: list[str] = field(default_factory=list)

    @property
    def ok(self) -> bool:
        return not self.errors


def _heading_bodies(text: str) -> dict[str, str]:
    matches = list(HEADING_RE.finditer(text))
    bodies: dict[str, str] = {}
    for i, match in enumerate(matches):
        title = match.group(2).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        bodies[title] = text[start:end].strip()
    return bodies


def empty_akte_template(
    *,
    request: str = "",
    client: str = "",
) -> str:
    ctx = request.strip() or "_TBD_"
    client_line = f"- Client / project: {client}\n" if client else "- Client / project: _TBD_\n"
    parts = [
        "# Influence Akte\n",
        "\n## Request / Context\n\n",
        client_line,
        f"- Request: {ctx}\n",
    ]
    for name in REQUIRED_SECTIONS:
        if name == "Request / Context":
            continue
        parts.append(f"\n## {name}\n\n_TBD_\n")
    return "".join(parts)


def parse_akte(path: Path) -> AkteReport:
    report = AkteReport(path=path)
    text = path.read_text(encoding="utf-8")
    report.sections = _heading_bodies(text)
    for name in REQUIRED_SECTIONS:
        if name not in report.sections:
            report.errors.append(f"missing required section: {name}")
    return report


def load_akte(path: Path) -> AkteReport:
    if not path.exists():
        raise FileNotFoundError(path)
    return parse_akte(path)


def locate_akte(
    *,
    named: Path | None = None,
    vault_matches: list[Path] | None = None,
) -> Path | None:
    """Locate an Akte. Never silently pick when multiple vault matches exist."""
    if named is not None:
        return named.expanduser().resolve()
    matches = list(vault_matches) if vault_matches is not None else find_influence_akten()
    if len(matches) == 1:
        return matches[0].resolve()
    if len(matches) > 1:
        raise AmbiguousAkte(matches)
    return None


def create_akte(
    path: Path,
    *,
    request: str = "",
    client: str = "",
    overwrite: bool = False,
) -> Path:
    target = assert_writable_akte_path(path)
    if is_under_plugin_checkout(target):
        raise ValueError(f"refusing to write Akte inside plugin checkout: {target}")
    if target.exists() and not overwrite:
        raise FileExistsError(target)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(
        empty_akte_template(request=request, client=client),
        encoding="utf-8",
    )
    return target


def append_log_entry(
    path: Path,
    section: str,
    entry: str,
    *,
    stamp: datetime | None = None,
) -> AkteReport:
    if section not in LOG_SECTIONS:
        raise ValueError(f"section must be one of {LOG_SECTIONS}, got {section!r}")
    target = assert_writable_akte_path(path)
    report = load_akte(target)
    if not report.ok:
        raise ValueError(f"akte invalid before append: {report.errors}")
    text = target.read_text(encoding="utf-8")
    heading = f"## {section}"
    idx = text.find(heading)
    if idx < 0:
        raise ValueError(f"missing section heading: {section}")
    # Find end of this section (next ## or EOF)
    after = idx + len(heading)
    next_h = re.search(r"\n## ", text[after:])
    end = after + next_h.start() if next_h else len(text)
    when = (stamp or datetime.now(timezone.utc)).strftime("%Y-%m-%d %H:%M UTC")
    block = entry.strip()
    addition = f"\n\n### {when}\n\n{block}\n"
    # If body is only _TBD_, replace it
    body = text[after:end].strip()
    if body in {"", "_TBD_"}:
        new_text = text[:after] + addition + text[end:]
    else:
        new_text = text[:end].rstrip() + addition + text[end:]
    target.write_text(new_text, encoding="utf-8")
    return load_akte(target)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("akte", type=Path, nargs="?", help="path to influence-akte.md")
    parser.add_argument("--check", action="store_true", help="validate and exit")
    args = parser.parse_args(argv)
    if not args.akte:
        parser.error("akte path required")
    report = load_akte(args.akte)
    if report.ok:
        print(f"akte ok: {args.akte}")
        return 0
    for error in report.errors:
        print(f"error: {error}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
