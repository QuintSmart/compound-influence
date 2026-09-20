# Compound Influence

English Cursor plugin chrome for QuintSmart offer, pricing, and stakeholder buy-in.

A soft `influence-akte.md` under PKMS **S03 QuintSmart/…/Briefing/** is the long-term memory. Framework cards ship in this repo. The product name is Compound Influence.

## Install

Copy this checkout. Do not symlink it.

```bash
python3 scripts/install.py
```

That writes a real directory to `~/.cursor/plugins/local/compound-influence`.

Then enable the local plugin in Cursor and **Reload Window**.

**Never store a live Akte in this checkout.** Akten live in the MyPKMS S03 Briefing path.

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
