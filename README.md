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

## Process

Scrum, solo-adapted, one-week sprints. `docs/working-agreement.md` holds the roles,
ceremonies and Definition of Ready / Done; sprint records live in `docs/sprints/`, one
folder per sprint. AI tools were used as working aids only (research, retrieval,
organising); the project deliverable contains no AI components, and all AI use is
declared in the assessed portfolio per the module's declaration rules (DEC-006).

## Licence

Undecided (MIT or Apache-2.0, tracked in `docs/decision-log.md`). Fixture files carry
their own per-fixture provenance and source licences (e.g. Leinster diagrams,
CC BY-NC-SA 4.0) — see `fixtures/diagrams/README.md`.
