# Sprint 1 — Planning

**Date:** 2026-11-19 (Thursday, planned at Sprint 0 close per DEC-009) · **Sprint:** 1 · **Sprint dates:** Fri 20 Nov – Sun 22 Nov 2026

## Sprint goal (one sentence)

> The intake lane's feasibility is tested against a real diagram — a tikz-cd parser turns one real fixture into nodes/edges/paths JSON that matches the hand-encoded oracle — and the fixture set plus requirements evidence grows around it.

## Sprint backlog

| Item | Story / task | Pts | Owner notes |
|---|---|---|---|
| PB-07 | Smallest tikz-cd parser spike: one real diagram (fixture D-01) from source to nodes/edges/paths JSON | 5 | **This sprint's research spike.** Acceptance: parse `fixtures/diagrams/pullback-intersection.tex` and match the hand-encoded JSON exactly — nodes (labels, row, col), edges (from, to, direction, style=hook). Spike outcome recorded as GO/NO-GO with evidence (DEC-005 validation gate). Runs in `spikes/spike3-tikzcd/` |
| PB-05 | Fixture set assembly: 2–3 real worksheet documents + 2–3 advanced-math documents with commutative diagrams | 5 | Extends the D-01 pattern: provenance + permission basis per fixture. Worksheet sources are owner-held (module worksheets); advanced-math candidates identified during assembly, arXiv-licensed sources preferred |
| PB-16 | Requirements elicitation record, drafted from the published-evidence base | 5 | **Carries a known dependency:** Q-02 (client role) — if unanswered at planning, the record is built from the published evidence and labelled accordingly (interim, per R-02 mitigation). Not blocked: the evidence base (the published research synthesis) exists either way |

Capacity check: committed **15 pts** over 3 days — deliberately over-committed vs the Sprint 0 calibration (5/8 done, 8-pts-first-sprint baseline), for two reasons: (a) the retro action on partitioning says committed points should cover controllable work; all three cards are controllable; (b) the CW1 deadline (Mon 23 Nov) makes Sprint 1 a hard box. Fallback order if time runs short: PB-07 first (the goal), then PB-05 (feeds evaluation), then PB-16 (has an interim path). The A3/A4 meetings would have landed inside the sprint as external checkpoints; every scheduled meeting was cancelled, so the sprint ran against its goal and the module's assessment requirements instead.

Research spike this sprint: **PB-07** (the one open-ended item; PB-05 and PB-16 are bounded).

## Retro actions carried in (from Sprint 0 retrospective)

1. **Partition externally-blocked work** — applied in this planning: no externally-blocked card is in the committed set; PB-12 and PB-14 sit outside the sprint commitment (below).
2. **PB-07 acceptance = match fixture D-01's JSON** — applied: written into the card above as the spike's acceptance test.
3. **Spec v0.2 backlog (B1–B7) → product backlog** — done: added as PB-21 (Should, 3 pts) in the same commit as this planning.

## Carried cards outside the commitment (blocked / external)

| Item | State |
|---|---|
| PB-12 | Blocked on R-11 (GitHub restore); on restore: single push + Projects board import + supervisor add. Zero sprint cost. |
| PB-14 | Blocked — the scheduled A2 meeting was cancelled (no supervision meeting possible); answers resolved provisionally from module materials, held for the viva; gates PB-04 only, not PB-16's interim path. |

## Risks checked this sprint

- **R-02 (client role):** PB-16's interim path (evidence-base record, labelled) means the sprint goal does not depend on the supervisor's answer (none was possible — provisional resolution in the decision log).
- **R-11 (GitHub):** PB-12 carried outside commitment; DEC-008 regime continues (daily cloud backup).
- **DEC-005 risk (parser feasibility):** the spike exists to retire this risk; NO-GO would trigger the recorded fallback (hand-encoding lane or an existing parser, re-decision in the log) — the sprint goal is written so a clean NO-GO still closes the goal ("feasibility **tested**", not "parser built").
- **CW1 deadline compression (DEC-009):** Sprint 1 must be fully recorded by Sun 22 Nov. CW1 assembly items (portfolio Sat 21, freeze Sun 22) run in parallel and are outside the sprint commitment — they are the owner's calendar, not sprint cards.

## Definition of Done reminders for this sprint

- Spike cards: written up + committed = done; a NO-GO with evidence is a completed spike.
- Every commit references its PB ID; the tree-format checker (`tools/tree_format_check.py`) stays green on corpus v1.
- Board, worklog and stand-up log updated at sprint close (Sun 22 Nov).
