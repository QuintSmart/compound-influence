# Compound Influence Context Contract

Load this file before reading or writing an Influence Akte. Every `ci-*` skill obeys it.

## Authority

1. This contract and the bundled cards under `references/`
2. The active `influence-akte.md`
3. The operator's current request
4. Chat history last

Plugin chrome naming stays `ci-*` / Compound Influence. Operator-facing prompts may be German. Arena default is QuintSmart Mandanten (Angebot, Pricing, Stakeholder-Buy-in).

## Locate the Akte (Local-Vault first)

1. Use a path the operator named (absolute or vault-relative).
2. Else, if the operator named a client/project slug, use  
   `S03 QuintSmart/300-399 Projects/<slug>/Briefing/influence-akte.md`  
   under the MyPKMS checkout (`~/Documents/GitHub/MyPKMS`, or `COMPOUND_INFLUENCE_VAULT`).
3. Else if exactly one `influence-akte.md` matches under known S03 Projects, use it.
4. Else if several match, ask which one. Do not pick silently.
5. Else offer: **create new Akte** / **weiter ohne Akte**.

Obsidian MCP is fallback only when the local vault path is unavailable.

Never store a live Akte inside the Compound Influence plugin checkout (repo or `~/.cursor/plugins/local/compound-influence`).

## Soft entry (not a gate)

Every command may run without an Akte. When a matching Akte exists or would help, offer:

- bestehende Akte nutzen
- neue Akte anlegen
- weiter ohne Akte

Skip phrases: `skip`, `ohne Akte`, `ablehnen`, `kein Write-back`.

## Write-back default

After a usable Diagnose, Frame, or Live result:

1. Default: append a dated entry to the matching log section on the active Akte.
2. Operator may refuse with a skip phrase — then leave the Akte unchanged.
3. Chat-only with an active Akte and no explicit skip is a fail for Diagnose/Frame when write-back was expected.
4. Live: if the operator says ablehnen / skip, leave the Akte unchanged (AE3).

## Required sections

Keep these headings in the Akte, even if a body is still thin:

- Request / Context
- Buyer Map
- Felt Problem (Pain / Cost / Gain)
- Wants / Fears / Constraints
- Open Ask
- Diagnose Log
- Framing Log
- Live Log
- Default Status Notes

Do not wipe prior log entries when appending. Compress for clarity; do not erase Open Ask history without an explicit confirm.

## Shared doors

The four commands are equal entries. None forces the order of the others. All share this contract.
