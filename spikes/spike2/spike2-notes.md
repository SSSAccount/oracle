\# Spike 2 — MathCAT 0.7.7 Nemeth braille lane (2026-11-18)



\## Tool versions

\- pandoc: pandoc 3.14

\- Python: Python 3.13.17

\- MathCAT: 0.7.7 (official DAISY release, libmathcat\_py-64-3.13-win.zip + Rules.zip)



\## Result

\- 16 PASS / 0 FAIL / 0 FLAG — Braille lane: GO

\- All 4 structures produced speech + Nemeth (quadratic, integral, matrix, sum)

\- Regression probes (Ali et al. R01 silent-loss cases): a+b+c keeps all operands

&#x20; and both plus signs; sin(x) says "sine x" — no silent loss

\- Files: spikes/spike2/{spike2-results.txt, spike2-nemeth.brf, spike2-raw-latex.brf}



\## Findings carried into Phase 2

1\. Matrix Nemeth uses linear layout with 8-dot row separator (⣍, dots 13478) —

&#x20;  verified as MathCAT's deliberate design (Nemeth\_Rules.yaml, daisy/MathCAT#43).

2\. Oracle lesson: Nemeth cell ⠼ (dots 3456) is dual-use (numeric indicator AND

&#x20;  fraction close) — checkers must count unambiguous indicators only.

3\. .brf outputs hold Unicode braille (UTF-8); physical BRF translation is Phase 3.



\## Verdict

\- Braille lane: GO — Phase 1 complete (reading lane GO + braille lane GO)

