SPEC — Expected-Structure Tree Notation v0.1 (the contract)
=============================================================

This SPEC is the complete contract. If a task instruction and this
SPEC ever seem to disagree, this file wins and you should note the
disagreement in your REPORT as a FLAG-candidate (a spec bug is a
finding too).

--------------------------------------------------------------------
1. PURPOSE
--------------------------------------------------------------------
An expected-structure tree records the presentation structure a
non-visual reader must receive — through audio navigation or
braille — to reconstruct a mathematical expression exactly as the
LaTeX source presents it. The tree is the expectation against
which converter output will later be judged; it is written before
and independently of any converter run.

--------------------------------------------------------------------
2. DERIVATION RULES
--------------------------------------------------------------------
R1  The LaTeX source is the sole input. Deriving the tree from
    rendered output, converter output, or another person's tree is
    out of contract.
R2  Presentation, not semantics: the tree records what is written.
    No simplification, expansion, evaluation, or reordering.
R3  Reading order is information: children are listed in the order
    a non-visual reader must receive them.
R4  Completeness: every part of the source that carries
    mathematical content must be represented. Spacing commands
    (\, \; \quad) and purely visual sizing (\big \Big \biggl) carry
    no content and are ignored.
R5  No guessing: any part you are not sure of is written as "..."
    and flagged in the REPORT. An omitted-with-flag element is a
    small, honest loss; a confident wrong element is corruption.

--------------------------------------------------------------------
3. ELEMENTS
--------------------------------------------------------------------
3.1  An element is an addressable unit of the expression: the
     whole expression (element 1) or a sub-part a reader must
     reach and hold (fraction, superscript, group, row, ...).
3.2  Numbering: element 1 = whole expression; continue in the
     order the parts appear in a top-down, left-to-right read of
     the source.
3.3  Reachability: every element's parent chain must lead back to
     element 1. An unreachable element is dead weight; delete it
     or fix its parent.
3.4  Granularity guidance: give a part its own element when a
     reader must "enter" it to continue (a fraction's num/den, a
     sup's base/exp, a group's interior, a matrix row). Runs of
     plain siblings stay inline as "- " lines. When in doubt,
     element-ize and justify in the REPORT.

--------------------------------------------------------------------
4. NODE TYPES
--------------------------------------------------------------------
4.1  Structural types (children via "role: type" lines, in reader
     order):

       eq      children: lhs, rhs
       frac    children: num, den
       sup     children: base, exp
       sub     children: base, sub
       subsup  children: base, sub, exp
       sum     children: lo, hi, body
       int     children: lo, hi, body
       lim     children: lo, body
       mat     children: positional rows, each row positional cells
       sqrt    children: radicand, then index if present

4.2  Container types (children via "- " positional sibling lines):

       group   delimiters that exist in the source: ( ) [ ] \{ \}
               \left...\right, | |, \| \|
       flat    an undelimited run of items

4.3  Leaf types (content on the line, no children):

       ident   a single letter or letter-like symbol (x, h, A, f,
               \alpha as "alpha", the d of \mathrm{d}x)
       num     a number (0, 1, 42, 3.5)
       op      an operator or relation: + - = < > \times \cdot
               \to \approx ...
       text    words from \text{...}

4.4  A construct with no listed type: choose the closest structural
     fit, or use flat/group with a REPORT justification, and raise
     a FLAG-candidate asking whether the spec should grow a type.
     Never invent a type silently.

--------------------------------------------------------------------
5. LINE FORMATS
--------------------------------------------------------------------
  element N — short description        block header
  N type                                root line of the block
    role: type                          structural child
    role: type  content                 leaf child
    - type                              positional sibling, structural
        ...children indented 2 more spaces...
    - item                              positional sibling, leaf
    role: element N                     child written as its own
                                        element block below (ref)
    - element N                         positional sibling written as
                                        its own element block (ref)
    same: element N                     element identical to an
                                        earlier one (say which);
                                        may fill a role or sibling
                                        slot, e.g. "base: same:
                                        element 5"
    ...                                 not checked (must be
                                        justified in REPORT)

Shallow children (one or two levels) are usually written inline with
their children indented under them; deep or reused parts get their
own element blocks and are referenced by number.

Indentation is 2 spaces per depth level. Content is plain ASCII;
comparison normalizes: '↔′  -↔−  *↔⋅  inf↔∞  pi↔π  !=↔≠  ->↔→

--------------------------------------------------------------------
6. SPECIAL CASES
--------------------------------------------------------------------
6.1  DERIVATIVES: \frac{d}{dx} or \frac{\partial y}{\partial x}
     are fracs like any other — presentation, not semantics. The
     d's are idents.
6.2  FUNCTION APPLICATION: \sin, \cos, \ln, \log, \exp, \max are
     op nodes (they operate), followed by their argument as
     siblings/children in reading order. \sin^2 x: sup with base
     op sin, exp num 2, then the argument continues at the parent
     level — justify your choice in the REPORT.
6.3  SUBSCRIPTED/SUPERSCRIPTED OPERATORS: \sum_{i=1}^{n} → sum
     with lo/hi/body. If a subscript or superscript attaches to a
     plain ident, use sub/subsup.
6.4  MATRICES: one element per matrix; each row a positional
     sibling; each cell a positional sibling inside its row; an
     empty cell still gets a line ("- flat" or "- ..."). The row
     and cell counts ARE the structure — getting them wrong is a
     structural FAIL, not a typo.
6.5  ELLIPSES: \cdots / \dots / \ldots are op nodes with content
     "..." (three dots as content is different from the reserved
     "..." skip marker: as content it sits in a leaf line like
     "- op  ..."). If that is confusing in place, justify in the
     REPORT.
6.6  CASES / PIECEWISE (\begin{cases}): treat like a mat whose
     rows have two cells (value, condition), and FLAG it — v0.1
     has no dedicated type; note the gap.

--------------------------------------------------------------------
7. JUDGMENTS (used later when converter output is compared)
--------------------------------------------------------------------
PASS  output matches the expected structure
FAIL  expected information is missing (silent loss)
FLAG  ambiguous; human adjudication required

Your trees feed the PASS/FAIL side. Your REPORT feeds the FLAG side.
Both matter.

--------------------------------------------------------------------
8. CHANGELOG
--------------------------------------------------------------------
v0.1 — initial notation spec for the expected-structure trees. Known gaps: cases
environments, \binom, align environments. Expect them to be FLAGs,
not guesses.
