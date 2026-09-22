# Compound Influence (Claude Code)

This checkout is an early **Compound Influence** skill pack: influence / pricing / buy-in coaching doors from Claire Wang’s frameworks, runnable as agent skills.

## When the user asks for a door

If they mention `ci-*`, `/ci-help`, Pain/Cost/Gain, Headline–Insights–CTA, buyer map, mirror, default, diagnose, frame, or live reply:

1. Read `commands/ci-help.md`.
2. Read the matching `skills/<skill-id>/SKILL.md`.
3. Read every `references/…` file that skill names (cards + `context-contract.md`).
4. Follow the skill exactly. Prefer **ohne Akte** for guests unless they set `COMPOUND_INFLUENCE_VAULT` or name a Briefing path.
5. Do not invent vault paths under this repo for live Akten.

## Guest defaults

- Demo input: `samples/demo-offer-brief.md`
- Skip write-back phrases: `skip`, `ohne Akte`, `ablehnen`, `kein Write-back`
- Product name: Compound Influence. Chrome ids stay `ci-*`.

## Install reminder

```bash
python3 scripts/install.py --target claude
```

That copies this pack to `~/.claude/compound-influence` for a durable local copy. Prefer working **inside this git checkout** so relative `references/` paths resolve.
