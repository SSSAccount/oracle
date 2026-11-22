# Oracle — Decision Log

Every consequential choice: what, why, evidence basis, status. New entries append at the
bottom; nothing is ever deleted — superseded entries are marked.

| ID | Date | Decision | Why | Evidence / basis | Status |
|---|---|---|---|---|---|
| DEC-001 | 2026-11-16 | Adopt solo-adapted Scrum (one-week sprints) as the project-management layer, justified against Kanban | Module artefacts are Scrum-shaped; research spikes handled by the one-spike-per-sprint rule | Methodology draft §4; working agreement §1 | Active |
| DEC-002 | 2026-11-16 | Adopt the two-layer methodology: single-cycle design-based research inside Scrum | Research legitimacy + module compliance; both iterative, both demand reflection | Methodology draft §2–§3 | Active |
| DEC-003 | 2026-11-16 | Task board tool: GitHub Projects (repo-integrated) | Board and repo in one place; story points and automation native; free for private repos | Comparison vs Trello in Sprint 0 planning | Active — revisit if board friction shows |
| DEC-004 | 2026-11-16 | Repository host: GitHub, private during development, public when licence decided | Supervisor access + commit history as process evidence; visibility switch is one setting | Supervisor added as collaborator | Active |
| DEC-005 | 2026-11-16 | Working language: Python for the intake/checking prototype; web-based speech navigation layer | Mature TikZ-parsing tooling; fastest path from evidence to prototype; screen-reader compatibility in the browser | B2 tech-selection rationale (research-base notes); to be validated by the PB-07 spike | Working recommendation — validate in Sprint 1 |
| DEC-006 | 2026-11-16 | AI boundary: no AI components in the deliverable; AI tools as declared working aids only | Mathematical exactness is non-negotiable; deterministic failures are systematic, not stochastic | Owner decision 2026-11-16; methodology draft §6 | Active |
| DEC-007 | 2026-11-16 | Three-valued checker answers (verified / refuted / unknown) from the start | Claim-uncertainty discipline; matches the working definition of uncertainty | Problem Statement v1 §5; DEC-007 in project records | Active |
| DEC-008 | 2026-11-17 | Sprint 0 runs local-first until GitHub restores account access: repo lives on the owner's machine, board lives in docs/board.md, daily cloud-drive backup; on restore: single push + board import + supervisor added | Locked out by failed 2FA SMS delivery (Twilio → Sri Lanka), recovery codes misplaced, no passkey; support ticket filed; sprint cannot wait | Risk R-11; Scrum values "working artefacts over waiting"; Principle 12 (tune the process) | Active — temporary, closes on restore |

| DEC-009 | 2026-11-18 | Sprint calendar compressed: Sprint 0 closes Thu 19 Nov, Sprint 1 runs Fri 20 – Sun 22 Nov and completes fully recorded before the CW1 submission deadline of Mon 23 Nov; Sprints 2–4 (24 Nov – 14 Dec) appear in the portfolio as planned goals, dates and backlogs only | Full read of the CW1 specification (17 Nov) set submission at 23 Nov and vivas from 26 Nov; the original calendar placed Sprint 1 records after submission, which the spec structure (Sprints 0+1 fully recorded in Submission 1) forbids | CW1 specification Chapter 7, Table 24 (full spec read 17 Nov) | Active — release plan, board and Sprint 0 planning edited to match |

## Pending (questions, not yet decisions)

| ID | Question | Asked of | Status |
|---|---|---|---|
| Q-01 | How do team-worded artefacts (Team Contribution Record, pair ceremonies, Section A contribution wording) map onto the solo arrangement? | Supervisor | **Could not be asked — every scheduled supervision meeting was cancelled (tutor unavailability during the graduation week; supervisor overseas; no slot before the deadline). Resolved provisionally from the module's published materials; to be confirmed at the viva.** |
| Q-02 | Who occupies the client role for requirements elicitation? | Supervisor | **Could not be asked — every scheduled supervision meeting was cancelled (see Q-01). Resolved provisionally from the module proforma and group-allocation pack: the supervision arrangement holds the client role in principle; the published evidence base supplied the user needs. To be confirmed at the viva.** |

## DEC-012 — Ethics route updated to the single-document form
**Date:** 2026-11-22 · **Status:** Active
**Context:** The module originally required the UoW Research Ethics Consideration Application **Part A** (with Part B conditional on Part A's outcome). A recent module email replaced the two-part arrangement with a single whole form; the tutor's 19 Nov feedback list ("complete Part A") predates or uses the old naming.
**Decision:** Fill the new single ethics document in full (scope: no human participants, no personal data, licensed fixtures) instead of Part A + conditional Part B. The portfolio (§5.2) and the feedback-response record cite the single form; a prepared answer pack maps the old Part A/B questions onto the new form.
**Evidence:** Module email (22 Nov 2026) and the received single form (CSE UG Ethics Declaration v1.0); the earlier Part A draft (19 Nov) reused as source material.
