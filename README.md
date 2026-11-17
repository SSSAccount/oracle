# Oracle — Non-visual access to commutative diagrams

Oracle is a solo agile research-and-development project (module 5COSC021C — Agile Team Project).
Its goal: make the commutative diagrams of advanced mathematics independently **readable,
navigable and verifiable** by blind and low-vision students and researchers, by treating a
diagram's LaTeX source as structured data rather than as a picture to be described.

Working name: **Oracle** (final product naming is an open decision, tracked in the backlog).

## Problem statement (working)

> Blind and low-vision students and researchers of advanced mathematics cannot independently
> read, navigate or verify the commutative diagrams that pervade algebra, topology and
> category theory, because no tool converts diagram source into a non-visual representation
> that preserves the diagram's mathematical structure.

## Repository layout

| Path | Contents |
|---|---|
| `docs/` | Working agreement, product backlog, release plan, decision log, risk register, worklog, sprint board (offline mirror) |
| `docs/templates/` | Fill-in templates: stand-up log, sprint planning, review, retrospective |
| `docs/sprints/` | One folder per sprint: planning, daily log, review, retrospective, burndown data |
| `site/` | Landing page source (deployed at the project domain) |
| `tools/` | Small deterministic helpers (e.g. burndown chart generator) |

## Process, in one line

Scrum, solo-adapted, one-week sprints — `docs/working-agreement.md` holds the roles,
ceremonies, Definition of Ready / Definition of Done and the evidence rules. Sprint records
live in `docs/sprints/`, one folder per sprint.

## Honesty rules

- **Evidence first.** Design decisions cite the evidence base or are marked provisional.
- **Calibrated claims.** "Not found in sources searched" is not the same claim as "novel".
- **No backdating.** The commit history *is* the process record; never edit it to look tidier.
- **AI boundary.** AI tools are used as working aids only (research, retrieval, organising);
  the project deliverable contains no AI components. All AI use is declared in the assessed
  portfolio, per the module's declaration rules.

## Licence

To be decided in Sprint 0 — MIT or Apache-2.0 under consideration; the decision will be
recorded in `docs/decision-log.md` and applied to this repository.
