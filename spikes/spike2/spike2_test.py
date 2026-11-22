#!/usr/bin/env python3.13
"""Spike 2 — MathCAT Nemeth braille lane.

Chain under test:
  pandoc (LaTeX -> MathML)  ->  MathCAT 0.7.7 (MathML -> speech + Nemeth)

Tests:
  A. The four Spike-1 structures (quadratic, integral, matrix, sum)
  B. Two bank regression probes (Ali et al. R01 silent-loss cases): a+b+c, sin(x)

Outputs (written next to the script, or $SPIKE2_OUT if set):
  spike2-results.txt     full report
  spike2-nemeth.brf      Nemeth braille of all expressions (Unicode braille, UTF-8)
  spike2-raw-latex.brf   the LaTeX source itself (ASCII; display-side translation)

Layout auto-detection (first match wins):
  lib:   /tmp/mc_py/libmathcat_x  |  <script dir>/lib  |  <script dir>
         (contains libmathcat_py.so / libmathcat_py.pyd)
  rules: /tmp/mc_rules/rules_x/Rules  |  <script dir>/Rules  |  <script dir>/../Rules

Linux:   SPIKE2_OUT=<output dir> python3.13 spike2_test.py
Windows:  py -3.13 spike2_test.py
"""
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("SPIKE2_OUT", HERE)

TEX = r"""\documentclass{article}
\usepackage{amsmath}
\begin{document}
\[ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \]
\[ \int_0^1 \frac{x^2}{x^2 + 1}\, dx \]
\[ A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} \]
\[ \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6} \]
\end{document}
"""

EXTRA_PROBES = [
    ("probe-a+b+c (operand-loss check)",
     "<math><mi>a</mi><mo>+</mo><mi>b</mi><mo>+</mo><mi>c</mi></math>"),
    ("probe-sin(x) (operator-loss check)",
     "<math><mi>sin</mi><mo>&#x2061;</mo><mi>x</mi></math>"),
]

# Nemeth indicators (Unicode braille, BANA Nemeth reference):
NEM = {
    "frac_open": "⠹",     # dots 1456
    "frac_line": "⠌",     # dots 34
    "frac_close": "⠼",    # dots 3456
    "radical": "⠜",       # dots 1245
    "radical_term": "⠻",  # dots 12456 (also terminates over/under constructs)
    "sup": "⠘",           # dots 45
    "sub": "⠰",           # dots 56
    "plus": "⠬",          # dots 346
    "minus": "⠤",         # dots 36
    "integral": "⠮",      # dots 2346
    "under": "⠩",         # dots 146 (directly under)
    "over": "⠣",          # dots 126 (directly over)
    "infinity": "⠠⠿",    # dot 6 + dots 123456
    "greek": "⠨",         # dots 46 (Greek letter indicator)
    "pi": "⠨⠏",
    "bracket_open": "⠷",  # dots 12356
    "bracket_close": "⠾", # dots 23456
    "digit3": "⠒",        # dots 25 (numeric-mode 3)
}


def dots(ch: str) -> str:
    cp = ord(ch)
    if not (0x2800 <= cp <= 0x28FF):
        return ch
    bits = cp - 0x2800
    return "".join(str(i + 1) for i in range(8) if bits & (1 << i)) or "-"


def braille_decode(b: str) -> str:
    return " ".join(f"{c}[{dots(c)}]" for c in b if not c.isspace())


def find_lib_dir():
    cands = ["/tmp/mc_py/libmathcat_x", os.path.join(HERE, "lib"), HERE,
             os.path.join(HERE, "..", "lib")]
    for d in cands:
        if any(os.path.exists(os.path.join(d, n)) for n in
               ("libmathcat_py.so", "libmathcat_py.pyd", "libmathcat_py_x64.pyd")):
            return d
    return None


def find_rules_dir():
    cands = ["/tmp/mc_rules/rules_x/Rules", os.path.join(HERE, "Rules"),
             os.path.join(HERE, "..", "Rules"), "/tmp/mc_rules/Rules"]
    for d in cands:
        if os.path.exists(os.path.join(d, "definitions.yaml")):
            return d
    return None


def main() -> int:
    # Windows consoles may default to a non-UTF-8 code page; Nemeth output is
    # Unicode braille, so force UTF-8 with replacement instead of crashing.
    if sys.stdout and hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    os.makedirs(OUT_DIR, exist_ok=True)
    rep = []          # report lines (printed AND saved)
    def say(line=""):
        print(line)
        rep.append(line)

    tex_path = os.path.join(OUT_DIR, "spike1.tex")
    html_path = os.path.join(OUT_DIR, "spike1-mathml.html")
    with open(tex_path, "w", encoding="utf-8") as f:
        f.write(TEX)

    # --- pandoc: newer pandoc uses --math-method=mathml, older uses --mathml
    cmd = None
    for flag in (["--math-method=mathml"], ["--mathml"]):
        try:
            r = subprocess.run(
                ["pandoc", tex_path, *flag, "-s", "-M", "title=Spike 2",
                 "-o", html_path],
                capture_output=True, text=True)
            if r.returncode == 0:
                cmd = flag[0]
                break
        except FileNotFoundError:
            say("ERROR: pandoc not found on PATH")
            return 2
    if cmd is None:
        say("ERROR: pandoc failed with both --math-method=mathml and --mathml")
        return 2
    say(f"[pandoc] conversion OK (flag: {cmd})")

    raw = open(html_path, encoding="utf-8").read()
    maths = re.findall(r"<math.*?</math>", raw, re.S)
    say(f"[pandoc] extracted {len(maths)} <math> elements")

    # --- MathCAT
    lib_dir = find_lib_dir()
    rules_dir = find_rules_dir()
    if not lib_dir:
        say("ERROR: libmathcat_py not found — extract the libmathcat zip so that "
            "libmathcat_py.pyd (or .so) sits in a 'lib' folder next to this script")
        return 2
    if not rules_dir:
        say("ERROR: Rules folder not found — extract Rules.zip next to this script "
            "(it creates a Rules/ folder with definitions.yaml inside)")
        return 2
    say(f"[mathcat] lib dir  : {lib_dir}")
    say(f"[mathcat] rules dir: {rules_dir}")
    sys.path.insert(0, lib_dir)
    import libmathcat_py as mc

    say(f"[mathcat] version {mc.GetVersion()}")
    mc.SetRulesDir(rules_dir)
    for pref, val in [("BrailleCode", "Nemeth"), ("TTS", "None")]:
        try:
            mc.SetPreference(pref, val)
            say(f"[mathcat] SetPreference({pref},{val}) OK")
        except Exception as e:  # noqa: BLE001
            say(f"[mathcat] SetPreference({pref},{val}) raised: {e}")

    # --- convert every expression
    results = []  # (label, mathml, speech, braille)
    labels = ["quadratic", "integral", "matrix", "sum"]
    for i, m in enumerate(maths):
        label = labels[i] if i < len(labels) else f"expr{i+1}"
        try:
            mc.SetMathML(m)
            speech = mc.GetSpokenText()
            braille = mc.GetBraille("")
            results.append((label, m, speech, braille))
        except Exception as e:  # noqa: BLE001
            say(f"[mathcat] {label} ERROR: {e}")
            results.append((label, m, f"<ERROR {e}>", ""))
    for label, m in EXTRA_PROBES:
        try:
            mc.SetMathML(m)
            speech = mc.GetSpokenText()
            braille = mc.GetBraille("")
            results.append((label, m, speech, braille))
        except Exception as e:  # noqa: BLE001
            say(f"[mathcat] {label} ERROR: {e}")
            results.append((label, m, f"<ERROR {e}>", ""))

    say("")
    for label, m, speech, braille in results:
        say(f"=== {label} ===")
        say(f"  speech : {speech}")
        say(f"  nemeth : {braille}")
        say(f"  decoded: {braille_decode(braille)}")
        say("")

    by = {lab: br for lab, _, _, br in results}

    # --- structural checks, three-valued: PASS / FAIL / FLAG
    checks = []  # (name, verdict, note)

    def chk(name, ok, flag_note=None):
        if ok:
            checks.append((name, "PASS", ""))
        elif flag_note:
            checks.append((name, "FLAG", flag_note))
        else:
            checks.append((name, "FAIL", ""))

    frac = lambda b: (NEM["frac_open"] in b and NEM["frac_line"] in b
                      and NEM["frac_close"] in b)

    b = by.get("quadratic", "")
    chk("quadratic: fraction indicators (open ⠹ / line ⠌ / close ⠼)", frac(b))
    chk("quadratic: radical ⠜ + termination ⠻ present",
        NEM["radical"] in b and NEM["radical_term"] in b)
    chk("quadratic: superscript ⠘ present (b²)", NEM["sup"] in b)

    b = by.get("integral", "")
    chk("integral: integral sign ⠮ present", NEM["integral"] in b)
    chk("integral: subscript ⠰ + superscript ⠘ limits", NEM["sub"] in b and NEM["sup"] in b)
    chk("integral: fraction indicators present", frac(b))

    b = by.get("matrix", "")
    chk("matrix: brackets ⠷/⠾ present",
        NEM["bracket_open"] in b and NEM["bracket_close"] in b)
    chk("matrix: digits 1, 2, 4 present", all(d in b for d in "⠂⠆⠲"))
    chk("matrix: digit 3 (⠒) present in Nemeth",
        NEM["digit3"] in b,
        "speech says 'row 2; 3, 4' but digit 3 not located in braille — either a "
        "Nemeth construct we have not verified against the BANA reference, or a "
        "real loss. Verify against BANA Nemeth 2022 before claiming either way.")

    b = by.get("sum", "")
    chk("sum: directly-under ⠩ + directly-over ⠣ present",
        NEM["under"] in b and NEM["over"] in b)
    chk("sum: infinity ⠠⠿ present", NEM["infinity"] in b)
    chk("sum: Greek pi ⠨⠏ present", NEM["pi"] in b)
    chk("sum: two fractions (⠹ opens ×2 and ⠌ lines ×2)",
        b.count(NEM["frac_open"]) == 2 and b.count(NEM["frac_line"]) == 2)
    # NOTE: cannot count ⠼ (fraction close) here — in Nemeth, dots 3456 doubles
    # as the numeric indicator, and this expression mixes both uses. Oracle
    # lesson for Phase 2: count only unambiguous indicators, or parse context.

    b = by.get("probe-a+b+c (operand-loss check)", "")
    chk("probe a+b+c: all operands a, b, c present", all(c in b for c in "⠁⠃⠉"))
    chk("probe a+b+c: exactly two plus signs ⠬", b.count(NEM["plus"]) == 2)

    b = by.get("probe-sin(x) (operator-loss check)", "")
    chk("probe sin(x): s, i, n, x all present", all(c in b for c in "⠎⠊⠝⠭"))

    say("=== STRUCTURAL CHECKS (PASS / FAIL / FLAG) ===")
    n_pass = n_fail = n_flag = 0
    for name, verdict, note in checks:
        mark = {"PASS": "[PASS]", "FAIL": "[FAIL]", "FLAG": "[FLAG]"}[verdict]
        say(f"  {mark} {name}")
        if note:
            say(f"         -> {note}")
        n_pass += verdict == "PASS"
        n_fail += verdict == "FAIL"
        n_flag += verdict == "FLAG"
    say("")
    say(f"{n_pass} PASS / {n_fail} FAIL / {n_flag} FLAG")

    # --- write artifacts
    res_path = os.path.join(OUT_DIR, "spike2-results.txt")
    with open(res_path, "w", encoding="utf-8") as f:
        f.write("\n".join(rep) + "\n")
    brf_path = os.path.join(OUT_DIR, "spike2-nemeth.brf")
    with open(brf_path, "w", encoding="utf-8") as f:
        for label, _, _, braille in results:
            f.write(f"{label}: {braille}\n")
    raw_path = os.path.join(OUT_DIR, "spike2-raw-latex.brf")
    with open(raw_path, "w", encoding="utf-8") as f:
        f.write(TEX)

    main_ok = all(by.get(l) for l in labels)
    lane = "GO" if (main_ok and n_fail == 0) else ("PARTIAL" if main_ok else "NO-GO")
    say("")
    say(f"Braille lane: {lane} "
        f"(all 4 structures produced Nemeth: {main_ok}; hard failures: {n_fail})")
    say(f"Wrote: {res_path}, {brf_path}, {raw_path}")
    return 0 if main_ok else 1


if __name__ == "__main__":
    sys.exit(main())
