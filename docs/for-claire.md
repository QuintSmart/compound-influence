# Compound Influence — early share for Claire

Hi Claire — this is an early, **public** build of **Compound Influence**: your book’s influence/pricing doors as agent skills (Cursor and Claude Code).

It is **not** a polished product. Expect sharp edges. Feedback on the *method mapping* (does this feel true to the book?) matters more than UI polish.

**Repo:** [https://github.com/QuintSmart/compound-influence](https://github.com/QuintSmart/compound-influence)

## What you get

| Door | What it does |
| --- | --- |
| Fast: `ci-diagnose`, `ci-frame`, `ci-live`, `ci-akte` | Quick scan, one-shot rewrite, live reply options, optional case file |
| Deep: `ci-pcg`, `ci-hic`, `ci-buyer`, `ci-mirror`, `ci-default` | Pain/Cost/Gain beat-by-beat, H–I–CTA drill, buyer map, mirror-only, default + small ask |

Help table: open `commands/ci-help.md` or ask the agent for `/ci-help`.

Framework cards live under `references/` (bundled — you do not need anyone else’s vault).

---

## Path A — Claude Code (recommended if you do not use Cursor)

**You do not need Python for this path.**

### 1. Get the code

**Option 1 — Download ZIP (no Git, no Python):**

1. Open [github.com/QuintSmart/compound-influence](https://github.com/QuintSmart/compound-influence).
2. Click the green **Code** button → **Download ZIP**.
3. Unzip somewhere easy, e.g. `Documents/compound-influence`.

**Option 2 — Git (if you already use it):**

```bash
git clone https://github.com/QuintSmart/compound-influence.git
cd compound-influence
```

### 2. Install Claude Code

Install [Claude Code](https://docs.anthropic.com/en/docs/claude-code) and sign in with your Anthropic account.

### 3. Open this folder

From a terminal in the unzipped / cloned folder:

```bash
cd /path/to/compound-influence
claude
```

Or open that same folder in your IDE with Claude Code / Claude connected.

`CLAUDE.md` in the repo root tells Claude how to load the skills and cards. Working **inside this folder** is enough — no extra install script required.

### 4. First prompts to try

```text
Read commands/ci-help.md and summarize the doors in plain English.
```

```text
Run ci-pcg on samples/demo-offer-brief.md. Work ohne Akte (chat only, no file write-back).
```

```text
Run ci-frame on this draft: "<paste a short pitch>". Ohne Akte.
```

---

## Path B — Cursor (optional)

Cursor’s local plugin install normally uses a small Python script. If you do not have Python:

1. Still download or clone this repo (as in Path A).
2. **Manually copy** the whole folder to:

   `~/.cursor/plugins/local/compound-influence`

   On a Mac you can do that in Finder (press Cmd+Shift+G and go to `~/.cursor/plugins/local/`), or in Terminal:

   ```bash
   mkdir -p ~/.cursor/plugins/local
   cp -R /path/to/compound-influence ~/.cursor/plugins/local/compound-influence
   ```

3. In Cursor: enable the local plugin **Compound Influence** → **Reload Window**.
4. Try `/ci-help`, then `/ci-pcg` on `samples/demo-offer-brief.md` with **ohne Akte**.

### If you already have Python 3

```bash
cd /path/to/compound-influence
python3 scripts/install.py --target cursor   # or --target both
```

macOS usually already has `python3`. Check with `python3 --version`. If missing, install from [python.org](https://www.python.org/downloads/) or `brew install python` — only needed for the script / tests, not for Path A.

---

## Akte (case file) — skip for first runs

Skills can run **ohne Akte** (chat only). Say: `ohne Akte` / `skip` / `kein Write-back`.

If you later want a sandbox case file on disk (still no Python required):

```bash
mkdir -p "$HOME/Documents/compound-influence-sandbox/S03 QuintSmart/300-399 Projects/demo/Briefing"
export COMPOUND_INFLUENCE_VAULT="$HOME/Documents/compound-influence-sandbox"
```

Then ask the agent to create `influence-akte.md` under that Briefing folder. Never store a live Akte inside this git checkout.

---

## Smoke checklist (10 minutes)

1. `ci-help` — doors make sense?
2. `ci-pcg` on `samples/demo-offer-brief.md` — ohne Akte — does the beat rhythm feel right?
3. `ci-frame` on a short draft of yours — ohne Akte.
4. Reply with what feels true to the book vs. what feels off or missing.

## Contact

Sebastian Kamilli — questions and feedback welcome on the method, naming, and coaching flow.
