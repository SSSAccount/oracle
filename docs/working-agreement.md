# Oracle — Working Agreement (solo-adapted Scrum)

Version 1.0 · Adopted: 2026-11-16 (Sprint 0) · Owner: [your name]
Review cadence: revisited at each retrospective; changes recorded in the decision log.

This working agreement is the project's constitution: it says how the work is scheduled,
prioritised, recorded and reviewed. It adapts Scrum for one person holding every role, and
states every adaptation openly rather than silently dropping it. The framework choice itself
— Scrum over Kanban — is justified in the methodology document (see `docs/` companion
material and the project portfolio); this agreement records the operational rules.

## 1. Why Scrum (and what it is adapted from)

The module's own artefacts are Scrum-shaped: weekly supervision meetings act as sprint
reviews, and the portfolio requires sprint goals, backlogs, review notes and retrospectives.
Kanban (continuous flow, no time-boxes) was considered and rejected as the primary framework
because research spikes with unpredictable duration would constantly overflow a flat queue,
and the assessment explicitly marks sprint artefacts. One Kanban idea is kept deliberately:
**each sprint carries at most one open-ended research spike** alongside bounded tasks, and
the sprint review re-plans honestly rather than hiding the variance.

## 2. Roles (one person, three hats)

| Role | Held by | In practice |
|---|---|---|
| Product Owner | The developer | Prioritises the backlog against the evidence base and module outcomes; the supervisor acts as stakeholder/adviser, not owner |
| Scrum Master | The developer | Protects the process: runs the retrospective honestly, keeps the board current, enforces the Definition of Done |
| Developer | The developer | Does the work |

Wearing three hats is the adaptation; the guard against its failure mode (self-approval
drift) is that the **supervisor reviews the artefacts weekly** — the review is external even
though the roles are internal.

## 3. Cadence and ceremonies

One-week sprints, Monday to Sunday. Supervision meeting = sprint review.

| Ceremony | When | Solo form | Artefact produced |
|---|---|---|---|
| Sprint planning | Monday | Pull items from the product backlog into the sprint backlog; write the sprint goal | `docs/sprints/sprint-N/planning.md` |
| Daily stand-up | Every working day | Written, three lines: yesterday / today / blockers | `docs/sprints/sprint-N/standup-log.md` (committed) |
| Sprint review | Weekly supervision meeting | Demonstrate the increment against the sprint goal; update the burndown interpretation | `docs/sprints/sprint-N/review.md` |
| Retrospective | End of sprint (before next planning) | Written: what worked / what didn't / max 3 actions | `docs/sprints/sprint-N/retrospective.md` |

Rules that make the records count:

- The stand-up log is **daily and boring** — three lines, committed, every working day.
  Missing days are left missing; the log is never backfilled.
- The burndown is **generated from the board's story points**, never drawn by hand.
  The sprint review interprets it (what the slope says about estimation).
- Retro actions are **at most three**, and they appear as cards in the next sprint —
  follow-up is checked by the markers.
- Commit messages reference backlog item IDs (e.g. `PB-07`) so the Git history and the
  board tell one story.

## 4. Definition of Ready (for a backlog item to enter a sprint)

1. Stated as a user story or a concrete task with a clear output.
2. Acceptance criteria written and testable.
3. Estimated in story points (fibonacci: 1, 2, 3, 5, 8).
4. Dependencies identified; no item enters the sprint blocked on an unanswered question
   that could have been asked first.
5. Evidence-linked where the item makes or supports a claim (cite the evidence row).

## 5. Definition of Done (for a sprint item to count as complete)

1. Implemented and committed (or, for research items, written up and committed).
2. Tested where applicable (see test strategy, added in a later sprint).
3. Recorded in the worklog (`docs/worklog.md`).
4. Updated on the task board (column moved, points burned).
5. Where the item feeds an assessed artefact: classified under the module's AI/permissions
   rules **before** it enters the portfolio.

## 6. Task board columns

`Backlog → Ready → In sprint → In progress → Review → Done`

The board (GitHub Projects or Trello — decision recorded in the decision log) carries:
story points on every card, MoSCoW priority on every backlog item, and the current sprint's
retro-action cards visible at the top.

## 7. Estimation

Fibonacci story points. The unit of comparison is "one focused day of familiar work = 3
points". Estimates are calibration instruments, not promises: the burndown exists to show
how good they become.

## 8. Evidence and honesty rules (from the project records)

- Every design decision cites an evidence-table row or is marked provisional.
- Tool-synthesised claims are labelled as such until the underlying source is read.
- No participant claims without real participants.
- No backdating of any artefact, ever. The commit history is the process record.

## 9. AI-tool boundary (declared use)

AI tools are used as working aids: research retrieval, organising notes, drafting assistance
for private working documents. The project **deliverable contains no AI components** — every
layer (intake, structured data, speech protocol, checking) is deterministic and verifiable.
The assessed portfolio declares AI use explicitly, per module rules.

## 10. Open questions (tracked, not blocking)

- Solo-project adaptations of team-worded artefacts (Team Contribution Record, pair
  ceremonies) — **to be asked of the supervisor**.
- Who occupies the client role for requirements elicitation — **to be asked of the
  supervisor**.

Answers land in the decision log and this agreement is revised the same week.
