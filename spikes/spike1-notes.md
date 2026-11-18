\# Spike 1 — pandoc MathML + MathJax explorer (2026-11-18)



\## Tool versions

\- pandoc: pandoc 3.14

\- MathJax: 4 (CDN, tex-mml-chtml.js, a11y extensions on by default)



\## Test A — pandoc conversion (spike1-mathml.html)

\- Rendered correctly: quadratic YES / integral YES / matrix YES / sum YES

\- <math> count in source: 4

\- Anything mangled: nothing observed

\- Note: used --math-method=mathml (new syntax; old --mathml now deprecated)



\## Test B — MathJax explorer (spike1-explorer.html)

\- Fraction numerator dive, parts reachable: YES — numerator, -b, ±, sqrt all separate nodes

\- Integral limits separate nodes: YES — lower 0 and upper 1 separate; integrand enterable

\- Matrix rows/cells walkable, size announced: YES — row by row, cell by cell

\- Sum limits + summand reachable: YES — n=1, ∞, summand separate nodes

\- Speech ambiguities / verbosity: none noted on these four expressions

\- Accessibility menu present: YES — Speech / Braille / Explorer / Options submenus

\- Keys: Tab -> Enter -> arrows (Up/Down = levels, Left/Right = within level), Esc exits



\## Verdict

\- Reading lane: GO

\- Basis: owner-verified in browser, 2026-11-18

\- Carry into Phase 2:

&#x20; 1. Watch sqrt-scope speech ambiguity on longer expressions (known complaint, N04)

&#x20; 2. Fixtures should add harder structures: aligned derivations, nested fractions

&#x20; 3. Confirms bank R37-R40: MathJax 4 a11y on by default, no config needed

&#x20; 4. Next: Spike 2 braille lane (MathCAT) closes Phase 1

