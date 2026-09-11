"""
Python Booleans ✅
- True / False — CAPITALISED (C#: true / false)
- bool is a subclass of int:  True == 1, False == 0
- and / or / not instead of && / || / !
- ⚠ and/or return OPERANDS, not necessarily a bool — the biggest C# culture shock
"""

# ─── Literals ──────────────────────────────────────────────────
is_active = True
is_deleted = False

print("─── Boolean literals ──────────────────────────────────────")
print(f"  is_active  = {is_active}      ← capital T (C#: true)")
print(f"  is_deleted = {is_deleted}     ← capital F (C#: false)")
print(f"  type       = {type(is_active).__name__}")
print("  ⚠ true / false / TRUE will raise NameError — Python is case-sensitive here.")

# ─── bool is a subclass of int ─────────────────────────────────
# C#: bool is its own type, not convertible to int without a cast.
# Py: True IS 1. This is why sum() over booleans counts things.
print("\n─── bool is an int ────────────────────────────────────────")
print(f"  True == 1        → {True == 1}")
print(f"  False == 0       → {False == 0}")
print(f"  True + True      → {True + True}     ← yes, really")
print(f"  isinstance(True, int) → {isinstance(True, int)}")
print(f"  sum([True,True,False,True]) = {sum([True, True, False, True])}   ← counting idiom")
print(f"  ['no','yes'][True] = {['no', 'yes'][True]!r}   ← bool as a list index (fun, but don't)")

# ─── bool() and truthiness ─────────────────────────────────────
# ⭐ THE core concept: in a condition, Python evaluates any object's "truthiness".
# Falsy values → False. Almost everything else → True.
falsy = [False, None, 0, 0.0, 0j, "", [], (), {}, set(), range(0)]
print("\n─── Falsy values ──────────────────────────────────────────")
for value in falsy:
    print(f"  bool({value!r:<10}) = {bool(value)}")
print("\n  The full falsy list: False, None, 0, 0.0, 0j, '', [], (), {}, set(), range(0)")
print("  Anything else is truthy — including these traps:")

truthy = ["False", "0", " ", [0], [None], {"a": 0}, -1]
print()
for value in truthy:
    print(f"  bool({value!r:<12}) = {bool(value)}")
print("  ⚠ 'False' is a non-empty STRING → truthy! '' is the only falsy string.")
print("  ⚠ [0] is a non-empty LIST → truthy! The 0 inside doesn't matter.")

# ─── Comparisons produce bools ─────────────────────────────────
print("\n─── Comparisons return bool ───────────────────────────────")
x, y = 10, 20
print(f"  x == y → {x == y}      x != y → {x != y}")
print(f"  x <  y → {x < y}       x >= y → {x >= y}")
print(f"  type(x == y).__name__ = {type(x == y).__name__}")

# ─── not ───────────────────────────────────────────────────────
print("\n─── not ───────────────────────────────────────────────────")
print(f"  not True        → {not True}     # C#: !")
print(f"  not False       → {not False}")
print(f"  not ''          → {not ''}     # truthiness applies")
print(f"  not 0           → {not 0}")
print(f"  not [1,2]       → {not [1, 2]}")

# ─── and / or — and the operand surprise ───────────────────────
# C#: a && b is ALWAYS a bool.
# Py: a and b returns one of the OPERANDS, not a coerced bool.
print("\n─── and / or return OPERANDS ──────────────────────────────")
print(f"  True  and False → {True and False}")
print(f"  True  or  False → {True or False}")
print(f"  'a' and 'b'     → {'a' and 'b'!r}    ← returns 'b', not True!")
print(f"  'a' or  'b'     → {'a' or 'b'!r}    ← returns 'a', not True!")
print(f"  ''  and 'b'     → {'' and 'b'!r}     ← short-circuits on the falsy left")
print(f"  ''  or  'b'     → {'' or 'b'!r}    ← skips the falsy left")
print(f"  0   or  42      → {0 or 42}")
print(f"  None or 'guest' → {None or 'guest'!r}")

print("""
  Rules:
    a and b  → if a is falsy, return a;  else return b
    a or  b  → if a is truthy, return a; else return b
""")

# The famous use — a default value, in one line
user_input = ""
display_name = user_input or "anonymous"
print(f"  display_name = user_input or 'anonymous'")
print(f"  user_input = ''  → display_name = {display_name!r}")

config = {"host": "localhost", "port": 0}
port = config.get("port") or 8080          # ⚠ 0 is falsy — this silently overrides 0!
print(f"\n  config.get('port') or 8080 → {port}   ⚠ port 0 gets replaced! Use .get('port', 8080)")

# ─── Short-circuit evaluation ──────────────────────────────────
# Right-hand side is NOT evaluated when the result is already decided.
# This is how you guard against None/IndexError.
print("\n─── Short-circuit ─────────────────────────────────────────")
calls = []


def noisy(label, result):
    calls.append(label)
    return result


noisy("A", False) and noisy("B", True)
print(f"  False and X → evaluated: {calls}    ← B never ran (C#: same as &&)")
calls.clear()

noisy("A", True) or noisy("B", False)
print(f"  True  or  X → evaluated: {calls}    ← B never ran (C#: same as ||)")

# Practical guard: this would crash if the left side didn't short-circuit
data = {"user": {"name": "Karim"}}
print(f"\n  data.get('user') and data['user'].get('name') → {data.get('user') and data['user'].get('name')!r}")
print(f"  missing key guarded the same way → {(data.get('nope') and data['nope'].get('name'))!r}")

# ─── any() / all() ─────────────────────────────────────────────
# C#: values.Any(...) / values.All(...) from LINQ
print("\n─── any() / all() ─────────────────────────────────────────")
nums = [2, 4, 6, 8]
mixed = [2, 3, 6, 8]
print(f"  any([0, '', False])        = {any([0, '', False])}")
print(f"  all([1, 'x', True])        = {all([1, 'x', True])}")
print(f"  all({nums})       = {all(nums)}   ← all truthy")
print(f"  all({mixed})      = {all(mixed)}   ← 3 is truthy too (non-zero int)")
print(f"  any(n % 2 for n in {mixed}) = {any(n % 2 for n in mixed)}   # any odd?")
print(f"  all(n % 2 == 0 for n in {mixed}) = {all(n % 2 == 0 for n in mixed)}   # all even?")

# ─── Booleans in output ────────────────────────────────────────
print("\n─── Formatting ────────────────────────────────────────────")
score = 85
print(f"  passed={score >= 60}          # C#: .ToString() gives 'True' too")
print(f"  lower: {str(score >= 60).lower()}")

# ─── Pitfalls ──────────────────────────────────────────────────
print("""
─── Pitfalls coming from C# ───────────────────────────────
  1. 'False' (string) is TRUTHY — only '' is falsy.
  2. value == True is redundant; write `if value:`. It also breaks on
     truthy non-bools like 1 or 'x'.
  3. `not` binds tighter than `and`/`or`: not a and b  ==  (not a) and b
  4. and/or return operands — don't chain them expecting a strict bool.
  5. 0, 0.0, '', [], {} are all falsy — `if x:` is NOT the same as `if x == 0`.
  6. There is no implicit int↔bool conversion in the other direction:
     True + 1 == 2 works, but `if 2:` is a truthiness test, not a comparison.
""")
