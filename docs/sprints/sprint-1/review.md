# Sprint 1 — Review

**Date:** 2026-11-22 (Sunday, sprint close per DEC-009) · **Against sprint goal:** *"The intake lane's feasibility is tested against a real diagram — a tikz-cd parser turns one real fixture into nodes/edges/paths JSON that matches the hand-encoded oracle — and the fixture set plus requirements evidence grows around it."*

## Demonstrated (increment vs goal)

- **Intake-lane feasibility proven (PB-07, GO):** `spikes/spike3-tikzcd/parse_tikzcd.py` (~140 lines, stdlib only) parses fixture D-01's tikz-cd source to nodes/edges/paths JSON matching the hand-encoded oracle **exactly** (labels, rows, cols, from/to, direction, style, path traversals) — and D-02 extended the parser to quoted labels with subscripts before also matching exactly. The spike ran 19 Nov as a head start (recorded as such in the spike notes); its write-up (scope boundaries, GO claim limits) completes the card's DoD at this close.
- **Fixture set grew (PB-05, partial):** D-01 (pullback-intersection) + D-02 (pullback-general, Leinster Def. 5.1.15) hand-encoded and parser-verified, with provenance and permission basis per fixture. Worksheet component (2–3 owner-held module worksheets) and the per-fixture permission pass remain — carried to Sprint 2 with a note, not closed.
- **Requirements evidence assembled (PB-16, done as interim):** Chapter 4 of the CW1 portfolio (SRS) drafted from the published-evidence base under the interim path allowed by R-02's mitigation — labelled as evidence-based elicitation pending the client-role answer (Q-02).
- **CW1 companion deliverables (outside the sprint commitment, CW1 assembly track):** portfolio (8 chapters, final assembly 22 Nov), hi-fi prototype + lo-fi wireframes + Figma recreation spec, competitor analysis, ethics form, landing page v2, viva deck, Google-document content pack — all assembled 19–22 Nov.

## Burndown

Points committed: 15 · Points completed: 10 (PB-07 5, PB-16 5) · Chart: `burndown.png` (generated from `board-export.csv` via `tools/burndown.py`, 3-day sprint axis).

**Interpretation (what the slope says):**

- Early slope: steep — the spike GO'd on 19 Nov (the day before the sprint formally opened; the head start is recorded in the spike notes), so the sprint's core risk retired before day 1.
- End state: 5 pts remain (PB-05). The worksheet component is owner-held material needing a permission-basis pass — bounded, known work, carried to Sprint 2 rather than rushed at sprint close.
- What this says about estimation: the deliberate over-commitment (15 pts against a 5-pts-done first sprint) was justified by the hard deadline box and by the partitioning rule: the controllable core (spike + elicitation) landed; the carried card is material-gathering, not engineering. Sprint 2 planning should keep fixture growth as a capacity-bounded card with an explicit fallback count.

## Agile events held in the sprint window

| Event | Date | Outcome |
|---|---|---|
| Sprint 1 planning | 19 Nov 2026 | 15 pts committed (PB-07, PB-05, PB-16); fallback order written; retro actions carried in and applied |
| Stand-ups | 20, 21, 22 Nov | Rows for all three days committed (`standup-log.md`); written at close — owned in the retrospective; exam day kept a light touch and says so |
| A3 supervision meeting (Sprint 1 progress) | Scheduled [date — invite] | Cancelled — [reason — from the cancellation message]; no meeting held |
| A4 review meeting (draft portfolio) | [date — owner records] | [outcome — owner records from meeting notes] |
| Sprint 1 review (this document) | 22 Nov 2026 | Goal met on the controllable core; PB-05 worksheet component carried |
| Sprint 1 retrospective | 22 Nov 2026 | Three actions into Sprint 2 (`retrospective.md`) |

## What was not done, and where it went

- **PB-05 worksheet component (carried):** 2–3 module worksheets to be added as fixtures with per-fixture permission basis. Owner-held material; carried to Sprint 2 as a bounded card.
- **A3/A4 meeting records:** no supervision meeting took place inside the sprint window — every scheduled meeting was cancelled (the record is in Appendix B of the portfolio); the questions meant for them are held for the viva.

## Board / Git / portfolio sync check (done before the scheduled review)

- [x] Board current — PB-07 → Done; PB-16 → Done (interim path, noted); PB-05 stays In sprint with carry note; PB-14 blocked (no supervision meeting possible — re-opened, see the worklog 22 Nov correction); PB-12 unchanged (blocked, R-11)
- [x] Stand-up log committed through sprint close
- [x] Draft portfolio updated — §7.3 refreshed from these records (portfolio v2, 22 Nov)

## Carried into Sprint 2

PB-05 worksheet component (bounded: 2–3 fixtures + permission pass), PB-12 (unblocks on R-11 restore — single push + Projects board import + supervisor add), and the retro actions below.
