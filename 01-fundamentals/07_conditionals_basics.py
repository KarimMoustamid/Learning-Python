"""
Python Conditionals — Basics 🔀
- if / else / elif — no parentheses needed, no braces, INDENTATION is the block
- `else if` from C# becomes `elif`
- No switch/case (Python 3.10+ has match/case — see the deep dive)
"""

# ─── if ────────────────────────────────────────────────────────
# C#:  if (temperature > 30) { Console.WriteLine("It's hot"); }
# Py:  if temperature > 30:  + indented body
temperature = 31

print("─── if ────────────────────────────────────────────────────")
if temperature > 30:
    print(f"  temperature is {temperature} → It's hot! 🔥")

# ─── if / else ─────────────────────────────────────────────────
age = 20
print("\n─── if / else ─────────────────────────────────────────────")
if age >= 18:
    print(f"  age {age} → adult")
else:
    print(f"  age {age} → minor")

# ─── if / elif / else ──────────────────────────────────────────
# `elif` = C#'s `else if`. Only the FIRST matching branch runs.
score = 85
print("\n─── if / elif / else ──────────────────────────────────────")
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"          # ← this one runs (85 >= 80)
elif score >= 70:
    grade = "C"
else:
    grade = "F"
print(f"  score {score} → grade {grade}")

# Order matters — this version is a bug: the first branch swallows everything
def bad_grade(s):
    if s >= 70:
        return "C"       # ❌ every score >= 70 lands here, even 95
    elif s >= 80:
        return "B"       # ← dead code, never reachable
    elif s >= 90:
        return "A"       # ← dead code, never reachable
    return "F"

print(f"  bad_grade(95) = {bad_grade(95)!r}   ← ⚠ elif order is a real bug source")

# ─── Squiggly vs curly ─────────────────────────────────────────
# ⭐ The single biggest syntax change from C#: NO BRACES.
# The block is defined by indentation. Dedent = end of block.
print("\n─── Block rules ───────────────────────────────────────────")
count = 5
if count > 0:
    print(f"  count = {count} is positive")
    print("  this line is still inside the if")
    # a comment or blank line does NOT end the block
print("  this line is outside (dedented back to column 0)")

print("""
  Rules for the block:
    ✅ colon  ':'  at the end of the condition line
    ✅ exactly 4 spaces of indent (PEP 8) — be consistent, tabs and
       spaces mixed is an error
    ❌ no { } braces
    ❌ no ; to put two statements on one line
    ⚠ indentation IS syntax → wrong indent = IndentationError
""")

# ─── Nesting ───────────────────────────────────────────────────
user = {"name": "Karim", "role": "admin", "active": True}
print("─── Nesting ───────────────────────────────────────────────")
if user["active"]:
    if user["role"] == "admin":
        if user["name"]:
            print(f"  active admin named {user['name']} → full access")
        else:
            print("  active admin with no name")
    else:
        print("  active non-admin")
else:
    print("  inactive user")
print("  ➜ nesting works, but 3+ levels is a smell — use `and` or a guard clause")

# ─── What can go in a condition ────────────────────────────────
x, y, items = 10, 20, [1, 2, 3]
print("\n─── Condition ingredients ─────────────────────────────────")
if x < y:
    print(f"  comparison      : x < y")

if x > 0 and y > 0:
    print(f"  and / or / not  : x > 0 and y > 0   (C#: && || !)")

if x in items or x == 10:
    print(f"  membership      : x in items")

value = None
if value is None:
    print(f"  identity        : value is None   ← ✅ never use == None")

if items:
    print(f"  truthiness      : if items:   ← empty list would be falsy")

# ─── Truthiness in conditions (very Pythonic) ──────────────────
print("\n─── Truthiness ────────────────────────────────────────────")
username = "karim"
empty = ""
print(f"  if username:  → {'taken' if username else 'missing'}   # prefer this")
print(f"  if len(username) > 0: → equivalent but noisy")
print(f"  if empty:     → {'taken' if empty else 'missing'}")

# ─── pass ──────────────────────────────────────────────────────
# A block can't be empty — use pass as a placeholder (C#: { } with nothing)
print("\n─── pass ──────────────────────────────────────────────────")
if temperature > 100:
    pass                 # TODO: handle this later
else:
    print("  temperature is sane (the if branch is a no-op via pass)")

# ─── Common errors ─────────────────────────────────────────────
print("\n─── Common errors ─────────────────────────────────────────")

try:
    exec("if True\n    pass")
except SyntaxError as e:
    print(f"  missing colon  → SyntaxError: {e.msg}")

try:
    exec("if 5 = 5:\n    pass")
except SyntaxError as e:
    print(f"  = instead of ==→ SyntaxError: {e.msg}   (C# gives you the same catch)")

try:
    exec("if True:\n    pass\n   pass")
except (SyntaxError, IndentationError) as e:
    print(f"  bad indent     → {type(e).__name__}: {e.msg}")

try:
    exec("x = 5\nif x > 1:\nprint('no indent')")
except (SyntaxError, IndentationError) as e:
    print(f"  no indent      → {type(e).__name__}: {e.msg}")

# ─── C# → Python cheat sheet ───────────────────────────────────
print("""
─── C# → Python ───────────────────────────────────────────
  if (x > 0) { ... }        →  if x > 0:
  else if (x == 0) { }      →  elif x == 0:
  else { }                  →  else:
  a && b   /  a || b  / !a  →  a and b / a or b / not a
  x is null / x == null     →  x is None
  switch / case             →  match / case   (3.10+ only)
  { }                       →  indentation
""")
