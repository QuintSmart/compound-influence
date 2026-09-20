---
name: ci-akte
description: Create, open, or show a QuintSmart Influence Briefing Akte under PKMS S03.
---

# ci-akte

Equal door for the soft Briefing Akte. German prompts OK. Chrome name stays `ci-akte`.

## Do first

1. Read `references/context-contract.md`.
2. Locate the Akte per the contract (named path → slug under `S03 QuintSmart/300-399 Projects/<slug>/Briefing/influence-akte.md` → single match → ask if many → offer create / ohne Akte).
3. Never write a live Akte into this plugin checkout.

## Default

1. Show Akte stand: Request/Context, Buyer Map, Felt Problem, Open Ask, latest log tails, Default Status Notes.
2. If creating: write the required headings from the contract (bodies may be `_TBD_`).
3. If several matches: list paths and wait. Do not pick silently.
4. Offer next doors: `ci-diagnose`, `ci-frame`, `ci-live`.

## Do not

- Do not invent Buyer or Felt Problem when the operator gave none.
- Do not wipe Diagnose / Framing / Live logs.
- Do not require another command before this one.

## Output

Update or create `influence-akte.md` in the S03 Briefing path. Confirm the absolute path in chat.
