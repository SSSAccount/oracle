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
| `docs/design/` | Draft architecture and design diagrams |
| `fixtures/` | Expected-structure corpus v1: problem sources, the specimen tree, trees 2–5 authored blind, the author judgment report, the tree-notation spec v0.1; diagram fixtures D-01/D-02 with provenance |
| `spikes/` | Spike records: 1 MathML/MathJax reading lane, 2 MathCAT Nemeth braille lane, 3 tikz-cd parser |
| `site/` | Landing page source (deployed at the project domain) |
| `tools/` | Small deterministic helpers (tree format checker, burndown chart generator) |

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

Sprint 0 closed with the licence decision still open (no DEC entry; the working
agreement and backlog carry no licence card). To be decided in Sprint 1 and
recorded in `docs/decision-log.md` — MIT or Apache-2.0 under consideration.
Note: the *fixture* files carry their own per-fixture provenance and source
licences (e.g. Leinster diagrams, CC BY-NC-SA 4.0) — see `fixtures/diagrams/README.md`.
