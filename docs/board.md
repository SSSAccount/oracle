# Oracle — Sprint Board (offline mirror)

Offline mirror of the task board while the GitHub account is locked out (R-11, DEC-008).
Columns match the working agreement §6: `Backlog → Ready → In sprint → In progress → Review → Done`. Moving a card = cut its line, paste it under the new column, save,
commit. On GitHub restore this board is imported into GitHub Projects (paste all titles
at once into + Add item; Projects creates one card per line) and this file then becomes
a snapshot, not the live board.

Every card carries `ID — title · Pts · MoSCoW` so the burndown and sprint records can be
read off it directly.

## Backlog

* \[ ] PB-08 — Spoken overview of a diagram ("5 objects, 7 arrows, 2 commuting conditions") · 3 · Must
* \[ ] PB-09 — Navigate object-by-object / arrow-by-arrow with path readings · 5 · Must
* \[ ] PB-10 — Commutativity conditions checked mechanically, three-valued answers · 8 · Should
* \[ ] PB-11 — Structural-fidelity check vs the diagram's mathematical content · 5 · Must
* \[ ] PB-15 — Register domain + deploy landing page over HTTPS · 3 · Should
* \[ ] PB-16 — Requirements elicitation record from the published-evidence base · 5 · Should
* \[ ] PB-17 — UML suite + test strategy draft (after elicitation) · 8 · Should
* \[ ] PB-18 — Hi-fi prototype of the reading interface, accessible by construction · 8 · Could
* \[ ] PB-19 — Portfolio assembly pass (B7 skeleton, declaration, referencing) · 5 · Should
* \[ ] PB-20 — Presentation outline + slides draft · 3 · Could

## Ready

(empty — items are pulled into In sprint only at sprint planning)

## In sprint — Sprint 0 (Tue 17 Nov – Sun 22 Nov 2026, 8 pts)

* \[ ] PB-12 — Set up task board + Git repo, add supervisor, seed backlog + working agreement · 2 · Must
* \[ ] PB-13 — Run Sprint 0 ceremonies and record all four artefacts · 3 · Must
* \[ ] PB-14 — Ask the supervisor the two framing questions (Q-01, Q-02) · 1 · Must
* \[ ] PB-06 — Hand-encode one real pullback square as structured data · 2 · Must

## In progress

(empty — at most one card here at a time; it moves here the day work starts, and to
Review the moment the code/docs exist)

## Review

(empty — card sits here while the Definition of Done checklist is walked)

## Done

(empty — cards land here only when the working agreement §5 checklist passes; first
expected: PB-12, once the repo is pushed to GitHub and the supervisor is added)

<!-- Sprint 0 note: PB-12 cannot reach Done until GitHub access is restored (push +
     supervisor add are part of the card). The stand-up log records this blocker daily

Spike 1 — pandoc MathML + MathJax explorer — DONE, reading lane GO (2026-11-18)

