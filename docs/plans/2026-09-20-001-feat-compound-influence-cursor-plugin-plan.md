---
title: Compound Influence Cursor Plugin - Plan
type: feat
date: 2026-09-20
topic: compound-influence-cursor-plugin
artifact_contract: ce-unified-plan/v1
artifact_readiness: requirements-only
product_contract_source: ce-brainstorm
execution: code
target_repo: compound-influence
heimat_slug: compound-influence
---

# Compound Influence Cursor Plugin - Plan

## Goal Capsule

- **Objective:** Ein eigenständiges Cursor-Plugin (`compound-influence`, c4-Form) liefern, das QuintSmart-Mandantenarbeit zu Angebot, Pricing und internem Buy-in über vier Commands und eine weiche PKMS-S03-Briefing-Akte compoundet.
- **Product authority:** Session-settled Product Contract. Dieses Artifact owns Plugin-Verhalten und Akte-Vertrag. Loop-Orchestrator als Haupt-Einstieg, Pricing-Rechner und Arena-Defaults für AI:mpulskraft/Karriere sind nicht aktiver Scope.
- **Open blockers:** Keine (Resolve Before Planning leer).

## Product Contract

### Summary

`compound-influence` ist ein lokales Cursor-Plugin mit vier gleichberechtigten Slash-Commands: Pre-Pitch-Diagnose, Message-Framing, Live-Verhandlung und Briefing-Akte.
Eine weiche Briefing-Akte in PKMS S03 (Mandantenprojekt) ist das Langzeitgedächtnis; brauchbare Outputs werden standardmäßig zurückgeschrieben.
Methodenkarten (Claire Wang / Price of Influence, Voss/Negotiation, ggf. GASP/SCR) liegen gebündelt im Plugin-Repo, nicht live aus dem Vault.

### Problem Frame

Angebot, Pricing und internes Buy-in bei Mandanten scheitern oft nicht an fehlender Logik, sondern an falschem Buyer-Value, fehlendem Felt Problem oder Framing in der eigenen statt der Buyer-Sprache.
Claire Wang und vorhandene PKMS-Negotiation-Bausteine (u. a. Voss) liefern Frameworks, aber kein wiederkehrendes Cursor-Betriebssystem.
Ohne Akte versanden Diagnosen und Live-Antworten zwischen Sessions; ohne Commands bleibt Wissen in Literature Notes stecken.

### Key Decisions

- **Alle vier Surfaces in einem Plugin** — Diagnose, Framing, Live, Akte. (session-settled: user-directed — chosen over single-surface V1: ein Schnitt ohne die anderen Surfaces zerbricht den Loop.) Governs R1, R2, R3, R4.
- **Hybrid-Einstieg** — vier gleichberechtigte Commands; Akte weich gekoppelt, nicht Pflicht-Gate. (session-settled: user-approved — chosen over Akte-Pflicht / reines 4 ohne Prompt: Flexibilität plus Kohärenz.) Governs R5, R6.
- **Ansatz A: Command Pack + Akte-Contract** — c4/cw-förmig, kein Loop-Orchestrator als Default. (session-settled: user-directed — chosen over B Loop-first / C Negotiation-first / A+Loop von Tag 1.) Governs R1, R2, R3, R4, R5, R6, R7.
- **Eigenes Repo `compound-influence`** — Produkt-Heimat wie `compound-4mat`. (session-settled: user-directed — chosen over KI-OS-Plugin-Hülle.) Governs R14.
- **Arena QuintSmart/Mandanten** — Defaults und Beispiele für Stakeholder-Buy-in und Angebot/Pricing. (session-settled: user-directed — chosen over neutral / AI:mpulskraft / Karriere.) Governs R10.
- **Akte in PKMS S03** — Mandantenprojekt im Vault. (session-settled: user-directed — chosen over Workspace / Plugin-lokal / immer fragen.) Governs R8, R9.
- **Frameworks gebündelt im Repo** — standalone Skills/Karten; PKMS hält Akten, nicht Methodik. (session-settled: user-directed — chosen over live-PKMS / Hybrid-Lookup.) Governs R11.
- **Erfolg = wiederkehrender Loop** — dieselbe Akte über Sessions, Default-Status aufbauen. (session-settled: user-directed — chosen over One-Shot-Text / nur Live-Replik.) Governs R12, R13.
- **Write-back Default** — brauchbare Diagnose-, Framing- und Live-Outputs landen in der Akte; Ablehnen möglich. (session-settled: user-directed — chosen over nur Nachfrage / Live ephemer.) Governs R9, R13.

<!-- ce-section: work-relationships -->
### How This Work Fits Together

Dieses Artifact owns das **Cursor-Plugin `compound-influence`** und den **Akte-Vertrag** (Verhalten, Surfaces, Write-back).
Die breitere Influence-/Pricing-Landschaft ist aktuelles Verständnis, kein Roadmap-Commit.

- **Optionaler Loop-Command** (Diagnose→Framing in einem Durchlauf)
  - Depends on: die vier Commands und der Akte-Vertrag
  - Still to decide: ob und wann als fünfter Command
- **KI-OS Routing-Zeiger** (wann Plugin vs. Paritäts-Skill)
  - Can proceed independently of: Plugin-MVP
- **Weitere Arena-Kalibrierungen** (AI:mpulskraft, Karriere)
  - Depends on: stabile Akte + Commands
  - Still to decide: ob eigene Defaults oder nur Akte-Felder

### Actors

- A1. **Operator** — QuintSmart; öffnet Commands vor Angebot, Pricing oder Buy-in.
- A2. **Cursor-Agent** — führt Skills aus, liest Framework-Karten, schreibt Akte nach Freigabe-Logik (Default Write-back mit Ablehnen).
- A3. **PKMS (S03)** — speichert Briefing-Akten pro Mandantenprojekt.
- A4. **Plugin-Checkout `compound-influence`** — kanonische Skills, Commands, Framework-Karten.

### Key Flows

- F1. **Akte anlegen oder öffnen**
  - **Trigger:** A1 startet den Akte-Command oder ein anderer Command fragt nach bestehender Akte.
  - **Actors:** A1, A2, A3
  - **Steps:** Mandanten-/Projektkontext klären; bestehende S03-Akte wählen oder neue anlegen; Schema-Felder (Buyer, Felt Problem, Wants/Fears/Constraints, nächster Ask, Verlauf) sichtbar machen.
  - **Covered by:** R4, R5, R7, R8
- F2. **Pre-Pitch-Diagnose**
  - **Trigger:** A1 prüft vor Pitch, ob Buyer und Felt Problem stimmen.
  - **Actors:** A1, A2, A3, A4
  - **Steps:** Optional Akte laden; Diagnosefragen (Buyer, Urgency, Upside vs. Risk, Pain/Cost/Gain); Ergebnis in Chat; Default Write-back in Akte (Ablehnen möglich).
  - **Covered by:** R1, R6, R7, R9, R10, R11, R13
- F3. **Message-Framing**
  - **Trigger:** A1 hat Entwurf (Mail, Angebot, Talking Points) und braucht Buyer-Sprache.
  - **Actors:** A1, A2, A3, A4
  - **Steps:** Optional Akte laden; Headline–Insights–CTA / Speak-their-language anwenden; umgeschriebene Version liefern; Default Write-back.
  - **Covered by:** R2, R6, R7, R9, R11, R13
- F4. **Live-Verhandlung**
  - **Trigger:** A1 braucht in einem heiklen Moment eine Replik (Pricing-Pushback, Buy-in-Widerstand).
  - **Actors:** A1, A2, A3, A4
  - **Steps:** Situation + Gegenstimme; Wang/Voss-Karten; Antwortoptionen; Default Write-back in Akte.
  - **Covered by:** R3, R6, R7, R9, R11, R13
- F5. **Wiederkehrender Loop**
  - **Trigger:** A1 öffnet dieselbe Mandanten-Akte in einer späteren Session.
  - **Actors:** A1, A2, A3
  - **Steps:** Akte laden; Verlauf und offenen Ask sehen; einen der Commands aus F2–F4 nutzen; Write-back compoundet Default-Status.
  - **Covered by:** R7, R8, R12, R13

### Requirements

**Surfaces**

- R1. Ein Slash-Command führt Pre-Pitch-Diagnose (Buyer, Felt Problem / Pain-Cost-Gain, strukturelle Ablehnung vs. Sweetening).
- R2. Ein Slash-Command führt Message-Framing (Buyer-Sprache, Headline–Insights–CTA, Destination-before-route).
- R3. Ein Slash-Command führt Live-Verhandlungshilfe (Antwortoptionen aus gebündelten Wang- und Negotiation-Karten).
- R4. Ein Slash-Command legt Briefing-Akten an oder öffnet sie und zeigt den Akte-Stand.

**Akte und Einstieg**

- R5. Jeder Command kann ohne Akte laufen; wenn eine passende S03-Akte existiert oder sinnvoll ist, bietet der Agent Nutzung / Neuanlage / Weiter ohne Akte an.
- R6. Die vier Commands sind gleichberechtigte Einstiege; keiner erzwingt die Reihenfolge der anderen.
- R7. Alle Commands teilen denselben Akte-Vertrag (Felder, Write-back-Verhalten, S03-Heimat), damit Outputs zwischen Surfaces kompatibel bleiben.
- R8. Neue Akten landen standardmäßig unter PKMS `S03 QuintSmart/…` im jeweiligen Mandanten-/Projektkontext (Pfadkonvention in Planning).
- R9. Brauchbare Outputs aus Diagnose, Framing und Live werden standardmäßig in die gewählte Akte geschrieben; A1 kann Write-back ablehnen oder überspringen.

**Inhalt und Kalibrierung**

- R10. Beispiele, Prompts und Default-Fragen sind auf QuintSmart-Mandanten (Angebot, Pricing, internes Buy-in) kalibriert.
- R11. Kern-Frameworks liegen als Karten/Skills im Plugin-Repo (mind. Price-of-Influence-Stufen und Negotiation-Grundlagen aus dem gebündelten Set); Live-Lookup der Literature Notes ist nicht erforderlich für den Kernlauf.
- R12. Die Akte speichert genug Verlauf und offenen Ask, dass eine spätere Session denselben Mandanten-Kontext fortsetzen kann ohne Neuaufnahme von Null.
- R13. Write-back und Akte-Felder sind so geschnitten, dass wiederholte Nutzung denselben Stakeholder-Kontext verdichtet (Default-Pfad), nicht nur Einzelschnipsel anhäuft.

**Packaging**

- R14. Das Produkt lebt im Git-Repo `compound-influence` und wird als lokales Cursor-Plugin (Skills + Commands, analog `compound-4mat`) installierbar.

### Scope Boundaries

- **In scope:** Vier Commands, Akte-Vertrag, S03-Write-back, gebündelte Framework-Karten, QuintSmart-Kalibrierung, c4-förmiges Plugin-Repo.
- **Out of scope:** Loop-Orchestrator als Haupt-Einstieg; Negotiation-first-Spine; Pricing-Rechner / Deal-Desk-Automatik; Arena-Defaults für AI:mpulskraft oder reine Karriere-Influence in V1; Live-Pflicht ohne Write-back-Option; Methodik nur via PKMS-Lookup.
- **Deferred to Planning:** Exakte Slash-Namen und Skill-IDs; konkrete S03-Unterpfad-Konvention; Akte-Markdown-Schema-Felder; Local-Plugin-Install/Link-Mechanik; welche Voss-/GASP-Karten exakt in V1 gebündelt werden; Ablehnen-UX-Wortlaut für Write-back.

### Acceptance Examples

- AE1. **Diagnose mit Write-back** — Given Mandantenprojekt mit S03-Akte, when A1 Diagnose ohne Wizard startet und Write-back nicht ablehnt, then Buyer/Felt-Problem-Ergebnis steht in der Akte und ist in einer Folgesession sichtbar.
- AE2. **Framing ohne Akte** — Given Entwurfstext und keine Akte, when A1 Framing startet und „ohne Akte“ wählt, then umgeschriebener Text erscheint; keine Vault-Schreibpflicht.
- AE3. **Live + Ablehnen** — Given Pricing-Pushback, when A1 Live-Command nutzt und Write-back ablehnt, then Antwortoptionen im Chat; Akte unverändert.
- AE4. **Wiederkehrender Loop** — Given Akte mit Verlauf aus früherer Session, when A1 Akte-Command öffnet, then offener Ask und letzte Diagnose/Framing-Einträge sind ohne Neuaufnahme nutzbar.

### Outstanding Questions

**Deferred to Planning**

- Exakte Command-/Skill-Namen und Prefix-Konvention.
- S03-Pfad- und Dateinamen-Schema für Briefing-Akten.
- Minimales vs. erweitertes Akte-Feldset.
- Umfang der V1-Framework-Karten (welche Voss-/GASP-Teile).
- Cursor Local-Plugin Apply (Kopie vs. Checkout), analog compound-writing/4mat-Betrieb.
