# Diagram fixtures (D-xx) — commutative diagrams for the intake lane

Each subdirectory groups a real commutative diagram with its provenance. This
README records the shared rules; per-fixture details live in the JSON.

| ID | File stem | Construct set exercised | Parser status |
|---|---|---|---|
| D-01 | `pullback-intersection` | 2×2 grid, `\cap` labels, 4 hook arrows, no arrow labels | PASS (spike 3) |
| D-02 | `pullback-general` | labeled arrows with subscripts (`p_1`, `p_2`, `t`, `s`), plain style | PASS (spike 3, label support added) |

## D-01 — `pullback-intersection` (PB-06, Sprint 0)

**What:** the intersection-of-subsets pullback square — 4 objects, 4 hooked
inclusion arrows, no labels.

**Source (verbatim, read from the arXiv LaTeX source):**

```latex
\xymatrix@M+.5ex{
  X \cap Y \ar@{^{(}->}[r] \ar@{^{(}->}[d]        &
  Y \ar@{^{(}->}[d]    \\
  X \ar@{^{(}->}[r]       &
  Z
}
```

Tom Leinster, *Basic Category Theory*, CUP 2014; arXiv edition 1612.09375,
Examples 5.1.17(b), book p. 117 (PDF p. 124; source `lims.tex:868-876`).

**Permission basis:** CC BY-NC-SA 4.0 (the arXiv edition's stated licence).
Academic, non-commercial use with this attribution; ShareAlike honoured by
keeping this notice attached to derivatives of the fixture.

**Hand-encoded JSON (`pullback-intersection.json`, the PB-06 deliverable):**
nodes carry (label, row, col); edges carry (from, to, direction, style). The
four arrows are all hooked inclusions `@{^{(}->}` (tikz-cd `hook`): n0→n1
(right), n0→n2 (down), n1→n3 (down), n2→n3 (right). Node order is row-major
matching the source's reading order. The `direction` field records the
original xymatrix cell-reference letter (`r`/`d`) verbatim from the source —
future converter output is compared against exactly these fields. This JSON
was written **before** any converter/parser work on diagrams (the PB-07
parser spike starts Sprint 1) — it is the oracle's expected-structure side,
authored from the LaTeX source alone.

**tikz-cd translation (`pullback-intersection.tex`):** same grid, same
hook style, `\begin{tikzcd}` syntax. It is the intake input for PB-07 — and
it doubles as evidence that the project's chosen representation format
(DEC-005: Python working recommendation) can carry the diagram's structure
without loss.

**Why this example:** canonical, textbook-standard, small (4 nodes / 4
edges / 0 labels — the smallest real instance of the pullback pattern),
and the blind-authored corpus validated the tree notation on expressions; D-01
extends the oracle methodology to diagrams, which is the project's actual
subject matter.

## D-02 — `pullback-general` (PB-05, Sprint 1)

**What:** the general pullback square, Definition 5.1.15 eq. (5.7) — 4
objects, 4 plain arrows, every arrow labeled (`p_2`, `p_1`, `t`, `s`).

**Source (verbatim, read from the arXiv LaTeX source, `lims.tex:705-713`):**

```latex
\xymatrix{
  P \ar[r]^{p_2} \ar[d]_{p_1}     &
  Y \ar[d]^t      \\
  X \ar[r]_s      &
  Z
}
```

Tom Leinster, *Basic Category Theory*, CUP 2014; arXiv edition 1612.09375,
Definition 5.1.15, eq. (5.7), book p. 114 (PDF p. 122).

**Permission basis:** CC BY-NC-SA 4.0, same as D-01 (attribution here and in
the JSON; non-commercial academic use; ShareAlike on derivatives).

**Oracle (`pullback-general.json`):** authored before parser label support
existed — the D-01 parser hardcoded `label: null`, and running it against
D-02 produced the first honest construct-gap failure. The parser then grew
quoted-label support (`"p_2"` in arrow options; placement modifiers `^ _`
and tikz-cd `'` are visual-only and not recorded), and both fixtures PASS.
Label subscripts are kept verbatim as source text (`p_2`, not p2) — the
intake lane records presentation, not semantics (R2).

**Why this example:** same book, same licence, next construct up: it is the
definition D-01 instantiates, and it is the smallest real diagram in the
corpus where *every* arrow carries a label — the shape the spoken-overview
requirement (PB-08) must handle ("4 objects, 4 arrows, each named").
