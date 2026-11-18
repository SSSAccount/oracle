

Total time: one authoring session



\## Per-problem



\### problem2 (integral)



\- Difficulty (1 easy – 5 hard): 2

\- Judgment calls (one line each — what you decided and why):

&#x20; - Upper limit pi/2 is written with a slash in the source, not \\frac → flat \[pi, op /, 2]; the slash is what is written.

&#x20; - dx after the integrand: d and x are idents (spec 4.3); the \\, before dx is spacing, ignored (R4); dx kept INSIDE the int body as juxtaposition flat \[frac]\[dx] because v0.1's int has only lo/hi/body.

&#x20; - \\sin recorded as an op node with its argument as following siblings (spec 6.2), so the numerator is the flat run \[2, sin, x].

&#x20; - \\sin^{2}x: sup with base op sin and exp 2, argument x continuing at the parent (denominator) level (spec 6.2).

\- FLAG-candidates (ambiguities you want the adjudicator to see):

&#x20; - Slash division (pi/2): v0.1 has no inline-slash fraction; chose flat + op "/". Should the notation grow a slash-frac type?

&#x20; - The differential dx: inside the int body (chosen) or a dedicated child role on int? v0.1 is silent.

\- Deliberate "..." skips and why:

&#x20; - None — every part of the source was recorded.



\### problem3 (matrices)



\- Difficulty: 3

\- Judgment calls:

&#x20; - LHS is a sup whose base is the whole pmatrix (source writes \\end{pmatrix}^{2}); the matrix is the base, not a sibling.

&#x20; - Rows as "- flat" positional siblings with cells as positional siblings inside (spec 6.4 / TASK-CARD D7); no dedicated row type exists, flat is the closest container.

&#x20; - Single-ident cells written directly as leaves ("- ident a"); multi-item cells element-ized (elements 5–8) because a reader must enter them and it keeps the row shape readable.

&#x20; - bc, ab, bd, ac, cd recorded as juxtaposed ident runs inside cell flats — implicit multiplication is juxtaposition, no operator invented.

&#x20; - The pmatrix parentheses are the matrix's own delimiters, carried by the mat node; no separate group wrapper invented.

&#x20; - RHS recorded exactly as written — the square is not expanded, nothing combines.

\- FLAG-candidates:

&#x20; - Matrix rows: spec has no "row" type; used flat. Should v0.1 grow row/cell types?

&#x20; - Should the pmatrix's parentheses be recorded explicitly (mat has no delimiter field in v0.1)?

\- "..." skips:

&#x20; - None.



\### problem4 (series)



\- Difficulty: 3

\- Judgment calls:

&#x20; - \\, between the fraction and (x-a)^n is spacing, ignored (R4); body is the juxtaposition flat \[frac]\[(x-a)^n].

&#x20; - f^{(n)}: the source puts real parentheses around n in the exponent → exp is a group \[n], not a bare ident.

&#x20; - f^{(n)}(a): f is an ident (not a listed function op), so the numerator is the flat \[f^(n)]\[(a)] with (a) a real group — presentation, no function-application structure invented.

&#x20; - n!: factorial recorded as op "!" following ident n in a flat; closest existing type for a postfix operator.

&#x20; - Upper limit \\infty recorded as ident with content "inf" (grader normalization inf↔∞).

&#x20; - Lower limit n=0 as the flat run \[n, =, 0], mirroring the specimen's "h -> 0".

\- FLAG-candidates:

&#x20; - Function application by a plain ident, f(a): spec 6.2 covers named ops (\\sin etc.) but is silent on ident-applied-to-argument; chose juxtaposition flat.

&#x20; - Postfix "!": op (chosen) or a new postfix marker type?

\- "..." skips:

&#x20; - None.



\### problem5 (telescoping sum)



\- Difficulty: 4

\- Judgment calls:

&#x20; - Chained equality S\_N = sum = 1 - 1/(N+1): v0.1's eq has only lhs/rhs, so the chain is right-nested — element 1 is S\_N = (rest), and the rest is itself an eq. Reading order is preserved: S\_N, then the sum, then the closed form.

&#x20; - S\_{N} is a sub with base ident S (spec 6.3: subscript on a plain ident).

&#x20; - \\left( \\right) around the summand are real delimiters → group (delimiter rule); the group is the sum's body.

&#x20; - 1/(n+1) and 1/(N+1): the source writes NO parentheses around n+1 / N+1 in the denominators → den is the flat run \[n, +, 1] / \[N, +, 1]; no group invented.

&#x20; - The two fractions 1/n and 1/(n+1) are not identical, so no "same" reference.

&#x20; - No telescoping or evaluation; the middle sum is kept — dropping it would be a silent loss.

\- FLAG-candidates:

&#x20; - Chained equality: right-nested eq chosen; a flat with op "=" siblings is a defensible alternative. v0.1 has no chain type — most likely divergence point with a second blind author.

\- "..." skips:

&#x20; - None.



\## Summary



\- Hardest problem and why: problem5 — the chained equality has no v0.1 type; the nesting choice is a genuine judgment call, unlike the others which follow explicit spec rules.

\- Any notation you wished existed (spec gaps): chain-eq type; mat row/cell types; explicit delimiter field for matrix environments; postfix-operator type; slash-fraction type; function-application type for plain idents.

\- Anything you were tempted to simplify but didn't: problem5's summand (recorded in full, not collapsed; the middle of the chain kept); problem3's RHS (matrix product not expanded or verified — recorded as written); problem2's sin^2 x (not rewritten as (sin x)^2).

\- Confidence that another blind author would produce the same trees (1–5, per problem): P2 4  P3 4  P4 4  P5 3



\## Spec bugs



\- No disagreement found between TASK-CARD and SPEC for these four problems.

\- Checker observation (a finding, not a failure): tree\_format\_check.py's element-1 type check (the `if n == 1 ... pass` branch) is dead code — it accepts any type for element 1 with no effect. Looks like an unfinished rule; harmless here.

\- All four trees were hand-traced against the checker's mechanical rules (A1–A6, roles, reachability); no execution environment was available in this session, so the checker should still be run before commit, as the ritual requires.

