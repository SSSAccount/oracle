# Spike 3 (PB-07) — smallest tikz-cd parser: GO

**Date:** 2026-11-19 (head start on Sprint 1; the sprint runs 20–22 Nov) · **Card:** PB-07 · **Decision gate:** DEC-005 (Python working recommendation)

## Question

Can a minimal Python parser turn a real tikz-cd diagram's LaTeX source into
nodes/edges/paths JSON that exactly matches a hand-encoded oracle — i.e. is
the intake lane feasible with the chosen technology?

## Method (the oracle discipline, applied to diagrams)

1. **Oracle first (PB-06, done before this spike):** fixture D-01 — the
   intersection-of-subsets pullback square from Leinster, *Basic Category
   Theory* (arXiv 1612.09375, Examples 5.1.17(b), p. 117, CC BY-NC-SA 4.0) —
   hand-encoded as `fixtures/diagrams/pullback-intersection.json` from the
   book's arXiv LaTeX source. Paths (p1 row-major node reading; p2/p3
   arrow-following branches) were also hand-encoded **before** the parser
   derived them.
2. **Parser second:** `spikes/spike3-tikzcd/parse_tikzcd.py` (~140 lines,
   stdlib only). It sees only the tikz-cd environment body. Grammar:
   `\\` splits rows, `&` splits cells, `\\arrow[opts]{dir}` specs are
   extracted per cell, direction letters resolved as relative grid
   references (r/l/d/u), node ids assigned row-major. Paths derived
   independently: p1 = row-major node reading; arrow-following paths =
   source-order DFS from in-degree-0 nodes.
3. **Comparison is exact, not fuzzy:** field-by-field equality against the
   oracle JSON (labels, rows, cols, from/to, direction, style, path
   traversals and edge lists). The comparison runs inside the tool; exit
   code 2 = FAIL with the first differing field printed.

## Result

```
$ python3 spikes/spike3-tikzcd/parse_tikzcd.py fixtures/diagrams/pullback-intersection.tex
parsed 4 nodes, 4 edges -> d01-parsed.json
ORACLE COMPARISON: PASS — nodes, edges and paths match fixture D-01
exactly (labels, rows, cols, from/to, direction, style; p1 row-major
reading, p2/p3 arrow-following branches)
```

**GO.** The smallest real diagram round-trips: source → parser → JSON ≡
hand-encoded oracle, on the first nontrivial attempt (one schema fix mid-run:
the parser initially omitted edge ids, which the oracle comparison caught —
the exact failure mode the oracle exists to catch).

## Scope boundaries (what GO does *not* claim)

- **One fixture, one construct set.** D-01 exercises: 2×2 grid, labels with
  `\cap`, four `\arrow[hook]{r|d}` specs, no arrow labels, no crossing/
  bending (targets reachable in one grid step), no `\rar`/`\dar` shorthands,
  no `column sep`/`row sep` options, no `|` cells, no math-mode node text
  beyond `\cap`. Every one of those is future work; PB-05's fixture set
  exists to grow the construct coverage incrementally, one accepted fixture
  at a time.
- **Paths were rule-derived, then matched.** The path rules (row-major p1;
  DFS arrow-following) were pinned in the oracle JSON's `path_rules` field
  before the parser implemented them — the same author-before-parse
  discipline as the trees, now for diagrams.
- **The oracle is one author.** The expression trees were authored blind and
  mechanically checked; diagram-structure cross-authoring is future work
  once more fixtures exist (the corpus must grow first — one fixture
  cannot be cross-authored meaningfully).

## Consequences

- **DEC-005 validated for the intake lane** on this construct set: Python +
  stdlib regex parsing suffices at this scale; no LaTeX toolchain needed in
  the loop (the parser reads source text, not rendered output — R2's
  sole-input rule extends cleanly from trees to diagrams).
- **The comparison harness pattern works for diagrams** and can become the
  PB-11 structural-fidelity check's diagram half: parse → compare →
  three-valued verdict, with "unknown" reserved for constructs the parser
  cannot yet see (out-of-scope constructs raise, never silently drop).
- **Next increment (Sprint 1, as planned):** PB-05 fixture growth — each new
  fixture either passes (parser grows) or honestly fails (construct gap
  recorded, three-valued "unknown" until closed).
