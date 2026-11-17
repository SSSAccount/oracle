# Oracle — Decision Log

Every consequential choice: what, why, evidence basis, status. New entries append at the
bottom; nothing is ever deleted — superseded entries are marked.

| ID | Date | Decision | Why | Evidence / basis | Status |
|---|---|---|---|---|---|
| DEC-001 | 2026-11-16 | Adopt solo-adapted Scrum (one-week sprints) as the project-management layer, justified against Kanban | Module artefacts are Scrum-shaped; research spikes handled by the one-spike-per-sprint rule | Methodology draft §4; working agreement §1 | Active |
| DEC-002 | 2026-11-16 | Adopt the two-layer methodology: single-cycle design-based research inside Scrum | Research legitimacy + module compliance; both iterative, both demand reflection | Methodology draft §2–§3 | Active |
| DEC-003 | 2026-11-16 | Task board tool: GitHub Projects (repo-integrated) | Board and repo in one place; story points and automation native; free for private repos | Comparison vs Trello in Sprint 0 planning | Active — revisit if board friction shows |
| DEC-004 | 2026-11-16 | Repository host: GitHub, private during development, public when licence decided | Supervisor access + commit history as process evidence; visibility switch is one setting | Supervisor added as collaborator | Active |
| DEC-005 | 2026-11-16 | Working language: Python for the intake/checking prototype; web-based speech navigation layer | Mature TikZ-parsing tooling; fastest path from evidence to prototype; screen-reader compatibility in the browser | B2 tech-selection rationale (Build Pack §6); to be validated by the PB-07 spike | Working recommendation — validate in Sprint 1 |
| DEC-006 | 2026-11-16 | AI boundary: no AI components in the deliverable; AI tools as declared working aids only | Mathematical exactness is non-negotiable; deterministic failures are systematic, not stochastic | Owner decision 2026-11-16; methodology draft §6 | Active |
| DEC-007 | 2026-11-16 | Three-valued checker answers (verified / refuted / unknown) from the start | Claim-uncertainty discipline; matches the working definition of uncertainty | Problem Statement v1 §5; DEC-007 in project records | Active |
| DEC-008 | 2026-11-17 | Sprint 0 runs local-first until GitHub restores account access: repo lives on the owner's machine, board lives in docs/board.md, daily cloud-drive backup; on restore: single push + board import + supervisor added | Locked out by failed 2FA SMS delivery (Twilio → Sri Lanka), recovery codes misplaced, no passkey; support ticket filed; sprint cannot wait | Risk R-11; Scrum values "working artefacts over waiting"; Principle 12 (tune the process) | Active — temporary, closes on restore |

## Pending (questions, not yet decisions)

| ID | Question | Asked of | Status |
|---|---|---|---|
| Q-01 | How do team-worded artefacts (Team Contribution Record, pair ceremonies, Section A contribution wording) map onto the solo arrangement? | Supervisor | To ask at Meeting 1 |
| Q-02 | Who occupies the client role for requirements elicitation? | Supervisor | To ask at Meeting 1 |
