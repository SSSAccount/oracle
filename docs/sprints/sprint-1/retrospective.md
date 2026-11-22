# Sprint 1 — Retrospective

**Date:** 2026-11-22 (Sunday, sprint close) · **Format:** written, honest, short.

## What worked

- **The oracle-first discipline survived contact with a second artefact type.** The D-01 hand-encoded JSON (written before the parser existed) caught a real parser bug on first comparison — the parser initially omitted edge ids, and the exact-match comparison refused to pass until it was fixed. The same author-before-parse rule that validated the expression trees paid off again, unchanged, on diagrams.
- **Head-start recording.** The spike ran the day before the sprint formally opened; recording it as a dated head start (in the spike notes and the review) rather than folding it into day 1 kept the sprint history readable and honest while still retiring the core risk early.
- **The two-track pattern.** Sprint commitment (engineering cards) and the CW1 assembly track (portfolio) ran in parallel without contaminating each other — the planning's fallback order was never needed because the tracks never competed for the same hours.

## What did not work

- **Fixture material gathering was the wrong shape of card.** PB-05 mixed engineering (extend the parser for D-02 — done) with material logistics (collect worksheets, clear permissions — not done). The engineering half finished in a day; the logistics half depends on owner-held material and a permission pass that a sprint box cannot compress. The card should have been split at planning.
- **The stand-up log again fell behind.** Rows were written at close rather than nightly — the same slip as Sprint 0, now a pattern. The working-agreement rule needs either a lighter format that survives exam week or an honest amendment at the Sprint 2 planning.
- **Supervisor-facing artefacts waited on the GitHub lockout.** The Google Document, the GitHub push and the board import (the three things a supervisor actually inspects) are all still pending on external conditions (account restore, owner action) — the offline-first regime protected the work but not the visibility of the work.

## What I learned (feeds CW2 and the design principles)

- A "GO" spike is only as strong as its scope boundary. Writing down exactly which constructs D-01 does *not* exercise (arrow labels, bending, shorthands, separators) made the GO claim precise and turned the fixture set into a graded coverage ladder rather than a binary pass.
- Over-commitment with a written fallback order is a different thing from over-commitment without one. The fallback order was never used, but its existence is what made committing 15 pts against a 5-pt calibration defensible.
- External-dependency risk compounds quietly: the lockout stayed cheap because every artefact existed offline-first; keeping that property as the repo grows is an explicit design constraint, not luck.

## Actions carried into Sprint 2 (maximum three — each becomes a board card)

1. **Split material-logistics cards from engineering cards at planning** — any card whose core is gathering/clearing external material gets its own card with an explicit material list, so a blocked logistics card never drags an engineering card's burndown (PB-05 split applied at Sprint 2 planning).
2. **Sprint 2 opens with the supervisor-visible spine live** — Google Doc created and shared, repo pushed, Projects board imported; visibility debt is paid before new engineering starts (owner actions, step by step).
3. **Each new fixture lands with its construct-coverage note in the fixture README as part of the card's DoD** — coverage grows as a documented ladder (construct set exercised + parser status per fixture), making PB-11's three-valued fidelity check straightforward to scope as the corpus grows.
