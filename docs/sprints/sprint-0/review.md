# Sprint 0 — Review

**Date:** 2026-11-19 (Thursday, sprint close per DEC-009) · **Against sprint goal:** *"Project infrastructure stands, all Sprint 0 ceremonies are recorded, the two framing questions are asked, and one real pullback square is hand-encoded as structured data — the smallest end-to-end experiment exists on paper."*

## Demonstrated (increment vs goal)

- **Infrastructure stands (PB-12, partial):** local Git repository carrying the full sprint history; offline board mirror `docs/board.md`; working agreement, backlog, release plan, risk register, decision log all live. GitHub push + supervisor add remain blocked by the account lockout (R-11) — worked offline-first per DEC-008.
- **Ceremonies recorded (PB-13):** planning (17 Nov), stand-up rows for 17–19 Nov committed, this review, and the retrospective — all four artefacts exist in `docs/sprints/sprint-0/`.
- **Framing questions (PB-14, in progress):** Q-01 and Q-02 are prepared in the decision log and on today's A2 supervision agenda; delivery is at the meeting — the asking is the card's deliverable, so it cannot be marked Done before the meeting happens.
- **Pullback square hand-encoded (PB-06):** fixture D-01 — Leinster, *Basic Category Theory* (arXiv 1612.09375), Examples 5.1.17(b), p. 117, CC BY-NC-SA 4.0 — original xymatrix read from the book's arXiv LaTeX source, translated to tikz-cd, and encoded as nodes/edges JSON (4 nodes, 4 hook arrows) **before any diagram parser exists** (`fixtures/diagrams/`).
- **Beyond the goal (context for the supervision meeting):** both spikes GO (reading lane; braille lane 16/16 checks); fixture corpus v1 complete — five problem sources with expected trees, four authored blind with a judgment report, all five passing the tree-format checker.

## Burndown

Points committed: 8 · Points completed: 5 · Chart: `burndown.png` (generated from `board-export.csv` via `tools/burndown.py`, 3-day sprint axis).

**Interpretation (what the slope says):**

- Early slope: steep — the setup items landed on day 1 and the research-heavy items (spikes, corpus, trees) on days 2–3; work was never waiting on the blocked GitHub lane because DEC-008 kept it decoupled.
- End state: 3 pts remain (PB-12 ×2, PB-14 ×1). Both are **externally blocked** (GitHub support ticket; supervisor meeting), not unfinished work — the honest record is "carried, not closed".
- What this says about estimation: an 8-pt first sprint completing 5 pts with the remainder externally blocked is a reasonable calibration baseline; the unit ("one focused day = 3 pts") held for the bounded tasks. The tree authoring was outside the sprint commitment entirely — the sprint goal was met without it, which suggests the goal was set conservatively (acceptable for a setup sprint; Sprint 1 tests the calibration for real).

## What was not done, and where it went

- **PB-12 (2 pts, carried):** GitHub push + Projects import + supervisor collaborator — blocked by R-11 (2FA SMS delivery failure to Sri Lanka; support ticket open since 17 Nov). Contingency per DEC-008 is in force and daily-backed-up.
- **PB-14 (1 pt, in progress):** the questions exist and are agenda'd for today's A2 meeting; the card closes when they are actually asked and the answers (or "answer pending") land in the decision log.

## Board / Git / portfolio sync check (done before the supervision meeting)

- [x] Board current (columns + points match reality) — `docs/board.md` updated at close: PB-13, PB-06 → Done; PB-12 → Review (partial, blocked); PB-14 → In progress
- [x] Stand-up log committed through yesterday (and today's row written at close)
- [ ] Draft portfolio updated with this sprint's material — chapter drafts and sprint records exist; full Ch. 7 assembly is Sat 21 Nov per the CW1 assembly plan

## Carried into Sprint 1

PB-12 (unblocks on R-11 restore — single push + board import), PB-14 (closes at the A2 meeting today; answers feed the elicitation item PB-16).
