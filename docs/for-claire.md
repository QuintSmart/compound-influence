# Compound Influence — early share for Claire

Hi Claire — this is an early, private build of **Compound Influence**: your book’s influence/pricing doors as agent skills Sebastian can run in chat (Cursor today; Claude Code supported for guests).

It is **not** a polished product. Expect sharp edges. Feedback on the *method mapping* (does this feel true to the book?) matters more than UI polish.

## What you get

| Door | What it does |
| --- | --- |
| Fast: `ci-diagnose`, `ci-frame`, `ci-live`, `ci-akte` | Quick scan, one-shot rewrite, live reply options, optional case file |
| Deep: `ci-pcg`, `ci-hic`, `ci-buyer`, `ci-mirror`, `ci-default` | Pain/Cost/Gain beat-by-beat, H–I–CTA drill, buyer map, mirror-only, default + small ask |

Help table: open `commands/ci-help.md` or ask the agent for `/ci-help`.

Framework cards live under `references/` (bundled — you do not need Sebastian’s vault).

## Path A — Claude Code (recommended if you do not use Cursor)

1. Install [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and sign in.
2. Accept the GitHub invite to this private repo, then:

```bash
git clone https://github.com/QuintSmart/compound-influence.git
cd compound-influence
python3 scripts/install.py --target claude
```

3. From this folder, start Claude Code (`claude` in the terminal, or open the folder in your IDE with Claude).
4. First prompts to try:

```text
Read commands/ci-help.md and summarize the doors in plain English.
```

```text
Run ci-pcg on samples/demo-offer-brief.md. Work ohne Akte (chat only, no file write-back).
```

```text
Run ci-frame on this draft: "<paste a short pitch>". Ohne Akte.
```

`CLAUDE.md` in the repo root tells Claude how to load skills and cards.

## Path B — Cursor (optional)

```bash
python3 scripts/install.py --target cursor
```

Then enable the local plugin **Compound Influence** in Cursor and **Reload Window**. Same smoke prompts as above (`/ci-help`, `/ci-pcg`).

```bash
python3 scripts/install.py --target both   # Cursor + Claude Code
```

## Akte (case file) — skip for first runs

Skills can run **ohne Akte** (chat only). Say: `ohne Akte` / `skip` / `kein Write-back`.

If you later want a sandbox case file without Sebastian’s PKMS:

```bash
export COMPOUND_INFLUENCE_VAULT="$HOME/Documents/compound-influence-sandbox"
mkdir -p "$COMPOUND_INFLUENCE_VAULT/S03 QuintSmart/300-399 Projects/demo/Briefing"
```

Then ask the agent to create `influence-akte.md` under that Briefing folder. Never store a live Akte inside this git checkout.

## Smoke checklist (10 minutes)

1. `ci-help` — doors make sense?
2. `ci-pcg` on `samples/demo-offer-brief.md` — ohne Akte — does the beat rhythm feel right?
3. `ci-frame` on a short draft of yours — ohne Akte.
4. Reply with what feels true to the book vs. what feels off or missing.

## Repo access

Private GitHub: `QuintSmart/compound-influence`. You need a GitHub account invited as collaborator (email or username). Branch for this early share: `feat/compound-influence-v1` (or `main` once merged).

## Contact

Sebastian Kamilli — questions and feedback welcome on the method, naming, and coaching flow.
