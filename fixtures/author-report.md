# Author report — corpus v1 (trees 2–5)

Written in one sitting, straight after finishing the trees. The difficulty ratings are my
own 1–5 gut call.

## problem2 (integral) — difficulty 2

- pi/2: the source uses a slash, not \frac, so I kept it flat: [pi, op /, 2]. The slash is what is written.
- dx: d and x are idents (spec 4.3); the \, before dx is spacing, ignored (R4). I kept dx inside the int body as the juxtaposition flat [frac][dx], because v0.1's int has only lo/hi/body.
- \sin: recorded as an op node with its argument as following siblings (spec 6.2), so the numerator is the flat run [2, sin, x].
- \sin^{2}x: sup with base op sin and exp 2, with the argument x continuing at the parent (denominator) level (spec 6.2 again).

Things the adjudicator should look at:

- Slash division (pi/2): v0.1 has no inline-slash fraction. I went flat + op "/". Should the notation grow a slash-frac type?
- The differential dx: inside the int body (what I chose) or a dedicated child role on int? v0.1 is silent.

Deliberate "..." skips: none — every part of the source was recorded.

## problem3 (matrices) — difficulty 3

- The LHS is a sup whose base is the whole pmatrix (the source writes \end{pmatrix}^{2}); the matrix is the base, not a sibling.
- Rows as "- flat" positional siblings with the cells as positional siblings inside (spec 6.4 / TASK-CARD D7); there is no dedicated row type, so flat is the closest container.
- Single-ident cells I wrote directly as leaves ("- ident a"); multi-item cells I element-ised (elements 5–8), because a reader has to enter them and it keeps the row shape readable.
- bc, ab, bd, ac, cd recorded as juxtaposed ident runs inside the cell flats — implicit multiplication is juxtaposition, no operator invented.
- The pmatrix parentheses are the matrix's own delimiters, carried by the mat node; no separate group wrapper invented.
- The RHS recorded exactly as written — the square is not expanded, nothing combines.

Things the adjudicator should look at:

- Matrix rows: the spec has no "row" type; I used flat. Should v0.1 grow row/cell types?
- Should the pmatrix's parentheses be recorded explicitly (mat has no delimiter field in v0.1)?

Deliberate "..." skips: none.

## problem4 (series) — difficulty 3

- The \, between the fraction and (x-a)^n is spacing, ignored (R4); the body is the juxtaposition flat [frac][(x-a)^n].
- f^{(n)}: the source puts real parentheses around the n in the exponent, so the exp is a group [n], not a bare ident.
- f^{(n)}(a): f is an ident (not a listed function op), so the numerator is the flat [f^(n)][(a)] with (a) a real group — presentation only, no function-application structure invented.
- n!: factorial as op "!" following the ident n in a flat; the closest existing type for a postfix operator.
- The upper limit \infty recorded as an ident with content "inf" (grader normalisation inf↔∞).
- The lower limit n=0 as the flat run [n, =, 0], mirroring the specimen's "h -> 0".

Things the adjudicator should look at:

- Function application by a plain ident, f(a): spec 6.2 covers named ops (\sin etc.) but is silent on an ident applied to an argument; I chose juxtaposition flat.
- Postfix "!": op (what I chose) or a new postfix marker type?

Deliberate "..." skips: none.

## problem5 (telescoping sum) — difficulty 4

- The chained equality S_N = sum = 1 - 1/(N+1): v0.1's eq has only lhs/rhs, so the chain is right-nested — element 1 is S_N = (rest), and the rest is itself an eq. The reading order is preserved: S_N, then the sum, then the closed form.
- S_{N} is a sub with base ident S (spec 6.3: subscript on a plain ident).
- The \left( \right) around the summand are real delimiters, so the group is the sum's body (delimiter rule).
- 1/(n+1) and 1/(N+1): the source writes no parentheses around n+1 / N+1 in the denominators, so the den is the flat run [n, +, 1] / [N, +, 1]; no group invented.
- The two fractions 1/n and 1/(n+1) are not identical, so no "same" reference.
- No telescoping or evaluation: the middle sum is kept — dropping it would be a silent loss.

Things the adjudicator should look at:

- Chained equality: I chose right-nested eq; a flat with op "=" siblings is a defensible alternative. v0.1 has no chain type, and this is the most likely divergence point with a second blind author.

Deliberate "..." skips: none.

## Summary

- Hardest problem and why: problem5 — the chained equality has no v0.1 type, so the nesting choice is a genuine judgment call, unlike the others which follow explicit spec rules.
- Notation I wished existed (spec gaps): a chain-eq type; mat row/cell types; an explicit delimiter field for matrix environments; a postfix-operator type; a slash-fraction type; function application for plain idents.
- Tempted to simplify but didn't: problem5's summand (recorded in full, not collapsed; the middle of the chain kept); problem3's RHS (matrix product not expanded or verified — recorded as written); problem2's sin^2 x (not rewritten as (sin x)^2).
- Would another blind author produce the same trees? My confidence, 1–5 per problem: P2 4, P3 4, P4 4, P5 3.

## Spec notes

- No disagreement found between TASK-CARD and SPEC for these four problems.
- One checker observation (a finding, not a failure): tree_format_check.py's element-1 type check (the `if n == 1 ... pass` branch) is dead code — it accepts any type for element 1 with no effect. It looks unfinished; harmless here.
- All four trees were hand-traced against the checker's mechanical rules (A1–A6, roles, reachability); no execution environment was at hand in that session, so the checker still needs a run before commit, as the ritual requires.
