"""
Python Introduction 🐍
Why learn Python, and the Python 2 vs Python 3 question
- Written for an experienced C# developer
- Run it:  python 01-fundamentals/00_introduction.py
"""

import sys

# ─── Why Python? ───────────────────────────────────────────────
# You already program. The question isn't "can I learn Python" — it's
# "what does Python buy me that C# doesn't?"

reasons = [
    ("Readability",   "Syntax is close to pseudocode. Less ceremony than C# — "
                      "no braces, no semicolons, no type declarations."),
    ("Batteries incl.", "Rich standard library (json, csv, pathlib, datetime) — "
                      "and pip makes third-party code one command away."),
    ("AI / ML",       "PyTorch, TensorFlow, scikit-learn, LangChain all speak Python "
                      "first. This is the language of AI work."),
    ("Data & scripts", "pandas, numpy, matplotlib. Glue scripts, automation, "
                      "and data pipelines that would be painful in C#."),
    ("Cloud & DevOps", "Azure SDK for Python, AWS boto3, Terraform/CDK tooling, "
                      "Docker/CI scripting — the lingua franca of ops."),
    ("Job market",    "Consistently top-3 in TIOBE/StackOverflow. Broad demand "
                      "across backend, data, AI, and QA."),
]

print("─── Why Python? ──────────────────────────────────────────")
for topic, detail in reasons:
    print(f"  {topic:<16} {detail}")

# C# vs Python, side by side — same program, twice
# C#:  var names = new List<string> { "Karim", "Python" };
#      foreach (var n in names) { Console.WriteLine(n.ToUpper()); }
# Python:
names = ["Karim", "Python"]
for n in names:
    print(f"  {n.upper()}", end=" ")          # end="" = no newline (C#: Console.Write)
print("   ← same loop, a third of the code\n")

# ─── Python 2 vs Python 3 ──────────────────────────────────────
# Python 2 was released in 2000, Python 3 in 2008.
# Python 2 reached END OF LIFE on 1 January 2020 — no more security fixes.
#
# If you're starting today, the answer is Python 3. Always.
# You only care about this if you maintain legacy code.

print("─── Python 2 vs Python 3 ─────────────────────────────────")

differences = [
    ("print",       "print x",                    "print(x)"),
    ("Strings",     "ASCII bytes by default",     "Unicode by default"),
    ("Division",    "5 / 2 == 2  (integer!)",     "5 / 2 == 2.5  (true division)"),
    ("Integer div", "5 / 2   → 2",                "5 // 2  → 2"),
    ("Iterators",   ".keys() returns a list",     ".keys() returns a view"),
    ("Input",       "raw_input()",                "input()"),
    ("Exceptions",  "except E, e:",               "except E as e:"),
    ("Int range",   "int and long separate",      "int is unbounded — one type"),
    ("Unicode",     "u\"text\" to opt in",          "\"text\" is unicode by default"),
]

print(f"  {'Topic':<12} {'Python 2':<28} {'Python 3':<26}")
print(f"  {'-' * 12} {'-' * 28} {'-' * 26}")
for topic, py2, py3 in differences:
    print(f"  {topic:<12} {py2:<28} {py3:<26}")

print("""
  The three that bite people migrating legacy code:
    1. print — was a statement, now a function (needs parentheses)
    2. / — was integer division for ints, now always returns a float
    3. strings — were bytes, now unicode by default
""")

# ─── Proof: which Python am I running? ─────────────────────────
# Never guess. Check at runtime.
# C# equivalent: System.Environment.Version

v = sys.version_info
print("─── Your interpreter ─────────────────────────────────────")
print(f"  sys.version          {sys.version.split()[0]}")
print(f"  major.minor          {v.major}.{v.minor}")

if v.major == 3:
    print("  ✅ Python 3 — you're good.")
else:
    print("  ❌ Python 2 detected — it's been dead since 2020. Upgrade.")

# A dependency-free way to guard a script (put at the top of your files):
#   if sys.version_info < (3, 8):
#       raise SystemExit("This script requires Python 3.8+")
#
# Or declare it for tooling with a shebang + version marker:
#   #!/usr/bin/env python3

# ─── Hmm, but the "python" command? ────────────────────────────
print("""
  ─── Naming gotcha ────────────────────────────────────────
  On many systems `python` used to mean Python 2 and `python3` meant Python 3.
  Modern installers (and this machine) point `python` at Python 3.
  Verify with:  python --version
  On Windows, use the `py` launcher:  py -3 --version
""")
