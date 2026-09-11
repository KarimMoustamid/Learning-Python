"""
Python Conditionals — Deep Dive 🔀🔬
- Conditional expressions (ternary), chained comparisons
- in / is / not, truthiness as a design tool
- match/case (3.10+), the walrus operator, guard clauses
- Precedence and the pitfalls that actually bite
"""

# ─── Conditional expression (ternary) ──────────────────────────
# C#:  var status = age >= 18 ? "Adult" : "Minor";
# Py:  status = "Adult" if age >= 18 else "Minor"     ← reads like English
age = 20
print("─── Ternary ───────────────────────────────────────────────")
print(f"  age >= 18 ? 'Adult' : 'Minor'  →  {('Adult' if age >= 18 else 'Minor')!r}")

# It's an EXPRESSION — usable anywhere, including inside f-strings
print(f"  inline: {age} is {'an adult' if age >= 18 else 'a minor'}")

# Nested ternaries work but harm readability — prefer elif or a dict
band = "child" if age < 13 else "teen" if age < 20 else "adult"
print(f"  nested: {band!r}   ← legal, but 3+ levels is a code smell")

# Default-value idiom you'll see everywhere
label = None
print(f"  'unknown' if label is None else label → {('unknown' if label is None else label)!r}")

# ─── Chained comparisons ───────────────────────────────────────
# C#: if (age >= 18 && age < 65)      ← repeat the variable
# Py: if 18 <= age < 65               ← ⭐ Python-only, evaluated once
print("\n─── Chained comparisons ───────────────────────────────────")
print(f"  18 <= age < 65        → {18 <= age < 65}")
print(f"  0 < age < 10          → {0 < age < 10}")
print(f"  age == 20 == 20       → {age == 20 == 20}")
print(f"  combined with or      → {18 <= age < 65 or age == 99}")
print("  Each operand is evaluated ONCE (matters when it's a function call).")

# ─── in / not in ───────────────────────────────────────────────
print("\n─── Membership in conditions ──────────────────────────────")
role = "admin"
blocked = ["spam", "bot"]
print(f"  role in ('admin','owner')     → {role in ('admin', 'owner')}")
print(f"  'spam' not in blocked         → {'spam' not in blocked}")
print(f"  'Py' in 'Python'              → {'Py' in 'Python'}")
print(f"  'k' in {{'name':'K'}}          → {'name' in {'name': 'K'}}   # dict → keys")
print("  C#: no single operator — it's .Contains() per type, and no 'not in'.")

# ─── is / is not ───────────────────────────────────────────────
# `is` compares IDENTITY (same object) — C#: ReferenceEquals
# `==` compares VALUE      — C#: .Equals()
print("\n─── is / is not ───────────────────────────────────────────")
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(f"  a == b  → {a == b}     # same value, different objects")
print(f"  a is b  → {a is b}    # not the same object")
print(f"  a is c  → {a is c}     # c points at the very same list")

missing = None
print(f"  missing is None      → {missing is None}    ← ✅ the idiom")
print(f"  missing is not None  → {missing is not None}")
print("  ⚠ Use 'is' ONLY for None (and sentinels). Never for numbers or strings —")
print("    CPython interns small ints/strings, so it appears to work until it doesn't.")

# ─── Truthiness as a design tool ───────────────────────────────
print("\n─── Truthiness-driven conditions ──────────────────────────")
inbox = []
user = {"name": "Karim"}


def safe_get(source, key):
    """Return the value, or None — never raise on a missing key."""
    return source.get(key) if isinstance(source, dict) else None


print(f"  if inbox:            → {bool(inbox)}     # empty list is falsy")
print(f"  if user:             → {bool(user)}      # non-empty dict is truthy")
print(f"  if safe_get(user,'name') → {bool(safe_get(user, 'name'))}")
print(f"  if safe_get(user,'age')  → {bool(safe_get(user, 'age'))}     # absent → None → falsy")
print("  ➜ Handles missing/empty/zero uniformly. Guard your inputs with it.")

# ─── any() / all() in conditions ───────────────────────────────
print("\n─── any() / all() ─────────────────────────────────────────")
checks = [3, 5, 7, 9]
print(f"  any(n > 100 for n in {checks})        → {any(n > 100 for n in checks)}")
print(f"  all(n > 0   for n in {checks})        → {all(n > 0 for n in checks)}")
print(f"  any(n % 2 == 0 for n in {checks})     → {any(n % 2 == 0 for n in checks)}   # any even?")
print("  C#: values.Any(x => ...) / values.All(x => ...)")
print("  ⭐ Generators short-circuit — the loop stops at the first decisive element.")

# ─── match / case (Python 3.10+) ───────────────────────────────
# Not a drop-in switch — it's structural PATTERN MATCHING.
# C# 8+ switch expressions with patterns are the closest cousin.

def describe(value):
    match value:
        case 0:
            return "zero"
        case int() if value < 0:          # guard clause
            return "negative int"
        case int():
            return "positive int"
        case str() if value.startswith("http"):
            return "url"
        case str():
            return "some string"
        case [first, second]:             # sequence pattern
            return f"list of exactly two: {first}, {second}"
        case {"type": kind}:              # mapping pattern
            return f"dict with type={kind}"
        case _:                           # wildcard — like default:
            return "something else"


print("\n─── match / case (3.10+) ──────────────────────────────────")
for sample in [0, -5, 7, "http://x.dev", "hi", [1, 2], {"type": "admin"}, 3.14, False]:
    print(f"  describe({sample!r:<16}) → {describe(sample)}")
print("  ⚠ Note describe(False) → 'zero': False == 0 because bool is a subclass of int!")
print("  ⚠ No fall-through, no break needed. Order matters — first match wins.")

# ─── Walrus operator := (3.8+) ─────────────────────────────────
# Assign AND test in one expression — useful when the value is expensive.
print("\n─── Walrus operator := ────────────────────────────────────")
data = [1, 2, 3, 4, 5]
if (n := len(data)) > 3:
    print(f"  if (n := len(data)) > 3 → n = {n}   ← computed once, used in the body")

# The killer use case: avoiding a double computation in a comprehension
numbers = ["12", "x", "34", "5"]
valid = [n for item in numbers if (n := item).isdigit()]
print(f"  comprehension with walrus → {valid}   ← n is bound AND reused in the output")

# while-read loops — the classic
attempts = 3
while (attempts := attempts - 1) >= 0:
    pass
print(f"  while (attempts := attempts - 1) >= 0 → ended at {attempts}")
print("  ⚠ Wrap it in parentheses. Readability suffers if you overuse it.")

# ─── Guard clauses ─────────────────────────────────────────────
# The professional alternative to deep nesting: bail out early.
def process_order(order):
    if not order:
        return "❌ no order"
    if not order.get("items"):
        return "❌ empty basket"
    if order.get("status") == "cancelled":
        return "❌ cancelled"
    return f"✅ processing {len(order['items'])} item(s)"


print("\n─── Guard clauses (early return) ──────────────────────────")
print(f"  {{}}                        → {process_order(None)}")
print(f"  {{'items': []}}              → {process_order({'items': []})}")
print(f"  {{'items': [1], 'status':'cancelled'}} → {process_order({'items': [1], 'status': 'cancelled'})}")
print(f"  {{'items': [1,2]}}            → {process_order({'items': [1, 2]})}")
print("  ➜ Flat and readable. Prefer this over if/if/if nesting.")

# ─── Precedence ────────────────────────────────────────────────
print("\n─── Operator precedence ───────────────────────────────────")
print(f"  not > and > or   (same relative order as C#: ! > && > ||)")
print(f"  True or False and False  → {True or False and False}   ← 'and' binds first")
print(f"  (True or False) and False→ {(True or False) and False}   ← parentheses change it")
print(f"  not True and False       → {not True and False}    ← (not True) and False")
print(f"  not (True and False)     → {not (True and False)}     ← different!")
print("  ⭐ When mixing and/or/not, add parentheses. Always.")

# ─── Pitfalls ──────────────────────────────────────────────────
print("\n─── Pitfalls that actually bite ───────────────────────────")

# 1. Float equality — never exact
price = 0.1 + 0.2
print(f"  1. {price} == 0.3 → {price == 0.3}   ← ❌ use math.isclose() or an epsilon")

# 2. `is` on non-None
x = 1000
y = 1000
print(f"  2. x is y → {x is y}   ← identity, not value. CPython may cache small ints!")

# 3. Truthiness vs explicit zero
quantity = 0
print(f"  3. if quantity: → {bool(quantity)}   ← 0 is falsy! 'if qty == 0' is different")
print(f"     missing vs zero need `is None`, not truthiness")

# 4. and/or return operands
cfg = {"retries": 0}
retries = cfg.get("retries") or 3
print(f"  4. get('retries') or 3 → {retries}   ← ❌ 0 silently became 3! use get(k, 3)")

# 5. Redundant comparison to True
flag = True
print(f"  5. if flag == True: → redundant; write `if flag:`")

print("""
─── The short version ─────────────────────────────────────
  ✅ if not items:              ✅ if value is None:
  ✅ 18 <= age < 65             ✅ 'x' in collection
  ✅ return early on bad input  ✅ any()/all() for collections
  ❌ if value == None:          ❌ x is 1000
  ❌ if flag == True:           ❌ a == 0.3 with floats
""")
