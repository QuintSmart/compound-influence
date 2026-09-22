# Compound Influence

Agent skill pack for offer, pricing, and stakeholder buy-in (Wang frameworks + QuintSmart arena).

Runs as a **Cursor** local plugin and, for guests, as a **Claude Code** project pack. Framework cards ship in this repo. Soft `influence-akte.md` under PKMS **S03 QuintSmart/…/Briefing/** is optional long-term memory (or `COMPOUND_INFLUENCE_VAULT` sandbox). Guests can always say **ohne Akte**.

Early guest notes: [`docs/for-claire.md`](docs/for-claire.md).

## Install

Copy this checkout. Do not symlink it.

```bash
python3 scripts/install.py --target cursor   # ~/.cursor/plugins/local/compound-influence
python3 scripts/install.py --target claude   # ~/.claude/compound-influence (+ skill mirrors)
python3 scripts/install.py --target both
```

**Cursor:** enable the local plugin **Compound Influence**, then **Reload Window**.

**Claude Code:** open this git checkout (so `references/` resolve). See `CLAUDE.md`.

**Never store a live Akte in this checkout.**

## Skills

### Fast doors

| Skill | Job |
| --- | --- |
| `ci-akte` | Create / open / show the Briefing Akte |
| `ci-diagnose` | Quick pre-pitch Buyer + Felt Problem + Pain/Cost/Gain |
| `ci-frame` | One-shot Headline–Insights–CTA rewrite (works ohne Akte) |
| `ci-live` | 2–3 live reply options; ablehnen skips write-back |

### Deep coaching

| Skill | Job |
| --- | --- |
| `ci-pcg` | Pain/Cost/Gain one beat at a time |
| `ci-hic` | Headline–Insights–CTA drill (CTA first) |
| `ci-buyer` | Buyer Map / Wants–Fears–Constraints |
| `ci-mirror` | Mirror questions only when Felt Problem is invisible |
| `ci-default` | Reliability deposit + next small Open Ask |

Open `/ci-help` for the same doors.

## Operator smoke (after Reload)

1. Install and reload.
2. Open `/ci-help`.
3. Run `/ci-pcg` or `/ci-diagnose` against [`samples/demo-offer-brief.md`](samples/demo-offer-brief.md) and a sandbox Briefing path.
4. Confirm Write-back once, then skip / ohne Akte once.

## Verify without Cursor UI

```bash
python3 -m pytest tests -q
python3 scripts/verify.py
```
