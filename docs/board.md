# Oracle — Sprint Board (offline mirror)

Offline mirror of the task board while the GitHub account is locked out (R-11, DEC-008).
Columns match the working agreement §6: `Backlog → Ready → In sprint → In progress → Review → Done`. Moving a card = cut its line, paste it under the new column, save,
commit. On GitHub restore this board is imported into GitHub Projects (paste all titles
at once into + Add item; Projects creates one card per line) and this file then becomes
a snapshot, not the live board.

Every card carries `ID — title · Pts · MoSCoW` so the burndown and sprint records can be
read off it directly.

## Backlog

* [ ] PB-10 — Commutativity conditions checked mechanically, three-valued answers · 8 · Should
* [ ] PB-15 — Register domain + deploy landing page over HTTPS · 3 · Should
* [ ] PB-17 — UML suite + test strategy draft (after elicitation) · 8 · Should
* [ ] PB-18 — Hi-fi prototype of the reading interface, accessible by construction · 8 · Could
* [ ] PB-19 — Portfolio assembly pass (B7 skeleton, declaration, referencing) · 5 · Should
* [ ] PB-20 — Presentation outline + slides draft · 3 · Could
* [ ] PB-21 — Tree spec v0.2 (B1–B7 gap backlog from the author report) · 3 · Should

## Ready

(empty — items are pulled into In sprint only at sprint planning)

## In sprint — Sprint 2 (Tue 24 Nov – Mon 30 Nov 2026; planning at Sprint 1 close 2026-11-22)

* [ ] PB-05b — Worksheet fixtures: 2–3 module worksheets encoded + per-fixture permission basis (split from PB-05 at Sprint 1 retro; material-logistics card) · 3 · Must
* [ ] PB-08 — Spoken overview demonstrated on the pullback fixture · 5 · Must
* [ ] PB-09 — Node/arrow navigation demonstrated on the pullback fixture · 5 · Should

## In progress

* [ ] PB-12 — Set up task board + Git repo, add supervisor, seed backlog + working agreement · 2 · Must — **blocked on R-11** (GitHub restore); local repo + board mirror live per DEC-008; carried outside the sprint commitments (retro action 1)

## Review

(empty — card sits here while the Definition of Done checklist is walked)

## Done

* [x] PB-13 — Run Sprint 0 ceremonies and record all four artefacts · 3 · Must — closed 2026-11-19 (review + retro written; burndown committed)
* [x] PB-06 — Hand-encode one real pullback square as structured data · 2 · Must — closed 2026-11-19 (D-01: Leinster BCT 5.1.17(b), fixture + JSON + provenance — `fixtures/diagrams/`)
* [ ] PB-14 — Ask the supervisor the two framing questions (Q-01, Q-02) · 1 · Must — blocked: every scheduled supervision meeting was cancelled (supervisor unavailable; see the worklog 2026-11-22 correction); provisional answers from the module materials are recorded in the decision log, to be confirmed at the viva
* [x] PB-07 — tikz-cd parser spike: D-01 source → nodes/edges/paths JSON, acceptance = match hand-encoded oracle · 5 · Must — closed 2026-11-22 at sprint close (**GO**: D-01 exact match 19 Nov head start; D-02 quoted-label support, also exact; write-up in `spikes/spike3-tikzcd/spike3-notes.md`)
* [x] PB-16 — Requirements elicitation record from the published-evidence base (interim path) · 5 · Should — closed 2026-11-22 (portfolio Chapter 4, evidence-based interim path per R-02 mitigation)

## Notes (spike and corpus status — not board columns)

- Spike 1 — pandoc MathML + MathJax explorer — DONE, reading lane GO (2026-11-18)
- Spike 2 — MathCAT 0.7.7 Nemeth braille lane — DONE, braille lane GO (2026-11-18, 16/16 checks)
- Fixture corpus v1 — DONE (5 problem sources + specimen tree; trees 2–5 authored blind with judgment report, `fixtures/author-report.md`; tree-format checker 5/5 PASS)
- Tree notation spec v0.1 — live (`fixtures/tree-spec.md`; spec-gap findings B1–B7 recorded for v0.2, PB-21)
- Diagram fixture D-01 (pullback square, Leinster BCT 5.1.17(b)) — DONE 2026-11-19; Sprint 1's PB-07 spike parses its tikz-cd against its hand-encoded JSON
- Diagram fixture D-02 (general pullback, Leinster Def. 5.1.15) — DONE 2026-11-19; parser extended for quoted labels with subscripts, exact match
- Sprint 1 closed 2026-11-22 (review + retrospective + burndown in `docs/sprints/sprint-1/`); PB-05 worksheet component split to PB-05b and carried to Sprint 2
