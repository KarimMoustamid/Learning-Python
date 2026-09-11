"""
Python Variables Basics 📦
- No type declaration — you assign and Python infers the type at runtime
- A variable is a NAME bound to an object, not a typed box (unlike C#)
- A name can be rebound to a different type — that is perfectly legal here
"""

# ─── Assignment ────────────────────────────────────────────────
# C#: string name = "Karim";     ← type on the left, semicolon at the end
# Py: name = "Karim"             ← no type, no semicolon, no declaration
name = "Karim"
age = 30
height = 1.78
is_learning = True
nothing = None

print("─── Assignment ────────────────────────────────────────────")
print(f"  name        = {name!r}")
print(f"  age         = {age}")
print(f"  height      = {height}")
print(f"  is_learning = {is_learning}")
print(f"  nothing     = {nothing}   ← NoneType, like C# null")

# ─── Dynamic typing ────────────────────────────────────────────
# C#: int x = 5;  x = "hello";   → compile error, the type is fixed forever
# Py: the name just rebinds to a brand new object of a brand new type
x = 5
print("\n─── Dynamic typing ────────────────────────────────────────")
print(f"  x = {x!r:<8} type: {type(x).__name__}")
x = "hello"
print(f"  x = {x!r:<8} type: {type(x).__name__}")
x = [1, 2]
print(f"  x = {x!r:<8} type: {type(x).__name__}")
print("  The NAME stays 'x'. The OBJECT it points to changes.")

# ─── Hard naming rules (SyntaxError if broken) ─────────────────
#   ✅ must start with a letter or an underscore
#   ✅ may contain letters, digits, underscores
#   ✅ case-sensitive — Name, name and NAME are three different variables
#   ❌ cannot start with a digit        2fast = 1
#   ❌ no hyphens                       my-var = 1   (that's a subtraction!)
#   ❌ cannot be a reserved keyword     for = 1
import keyword

print("\n─── Naming rules ──────────────────────────────────────────")
print(f"  keyword.iskeyword('for')   = {keyword.iskeyword('for')}")
print(f"  keyword.iskeyword('data')  = {keyword.iskeyword('data')}")
print(f"  total keywords in 3.11:      {len(keyword.kwlist)}")

# ─── Naming conventions (PEP 8 — style, not enforced) ──────────
# C# uses camelCase / PascalCase. Python's habit is snake_case.
#   variables & functions   → snake_case        user_name, get_total()
#   classes                 → PascalCase        class OrderProcessor
#   constants               → UPPER_SNAKE_CASE  MAX_RETRIES
#   "private" / internal    → _leading_und      _cache
#   "dunder" (built-in)     → __double_und__    __init__, __name__
#   throwaway / unused      → _                 for _ in range(3)
print("\n─── Naming conventions (PEP 8) ────────────────────────────")
print("  variables/functions → snake_case        e.g. user_name, total_price")
print("  classes         → PascalCase        e.g. OrderProcessor")
print("  constants       → UPPER_SNAKE_CASE  e.g. MAX_RETRIES")
print("  private hint    → _leading_underscore  e.g. _cache")
print("  unused          → _")

# ─── Checking a variable's type ────────────────────────────────
print("\n─── Checking types ────────────────────────────────────────")
print(f"  type(age)                 = {type(age).__name__}")
print(f"  type(age).__name__        = {type(age).__name__!r}   ← the clean string form")
print(f"  isinstance(age, int)      = {isinstance(age, int)}")
print(f"  isinstance(age, str)      = {isinstance(age, str)}")
print(f"  isinstance(True, int)     = {isinstance(True, int)}   ← ⚠ bool is a subclass of int")

# ─── Multiple assignment ───────────────────────────────────────
print("\n─── Multiple assignment ───────────────────────────────────")
a, b, c = 1, 2, 3                    # tuple unpacking in one line
print(f"  a, b, c = 1, 2, 3   → a={a}, b={b}, c={c}")

first, second, *rest = [10, 20, 30, 40, 50]   # star collects the leftovers
print(f"  first, second, *rest = [10..50] → {first}, {second}, {rest}")

p = q = r = 0                        # chained — all three point to the same 0
print(f"  p = q = r = 0       → p={p}, q={q}, r={r}")

# ─── Swapping (no temp variable needed) ────────────────────────
# C#: var tmp = a; a = b; b = tmp;
print("\n─── Swapping ──────────────────────────────────────────────")
left, right = "left", "right"
print(f"  before: left={left!r}, right={right!r}")
left, right = right, left
print(f"  after:  left={left!r}, right={right!r}   ← one line, no temp")

# ─── Constants (convention only) ───────────────────────────────
# C#: const / readonly. Python has NO enforcement — UPPER_CASE is a promise.
MAX_RETRIES = 3
BASE_URL = "https://api.example.com"
print("\n─── Constants ─────────────────────────────────────────────")
print(f"  MAX_RETRIES = {MAX_RETRIES}   ← convention, nothing stops you changing it")
print(f"  BASE_URL    = {BASE_URL!r}")

# ─── None ──────────────────────────────────────────────────────
print("\n─── None ──────────────────────────────────────────────────")
result = None
print(f"  result                = {result}")
print(f"  type(result).__name__ = {type(result).__name__}")
print(f"  result is None        = {result is None}    ← ✅ always use 'is' with None")
print(f"  bool(None)            = {bool(None)}  ← None is falsy")
print("  A function with no explicit return gives you None back.")

# ─── del ───────────────────────────────────────────────────────
print("\n─── del ───────────────────────────────────────────────────")
temp = "gone in a moment"
print(f"  temp = {temp!r}")
del temp
try:
    print(temp)
except NameError as e:
    print(f"  after del temp → NameError: {e}")

# ─── Names are references, not boxes ───────────────────────────
# C# has value types (struct) and reference types (class).
# Python has only references — every name points at an object on the heap.
print("\n─── Names are references ──────────────────────────────────")
original = [1, 2, 3]
alias = original          # NOT a copy — both names point to the same list
alias.append(4)
print(f"  original = {original}")
print(f"  alias    = {alias}")
print(f"  same object? {original is alias}   ← mutating one changed 'both'")
print(f"  id(original) == id(alias): {id(original) == id(alias)}")

copy = original[:]        # slice = a real copy
copy.append(99)
print(f"\n  copy     = {copy}")
print(f"  original = {original}   ← untouched, it's a separate list now")

# Immutables (int, str, tuple) behave differently: you can never mutate them,
# so rebinding a name never disturbs anyone else holding the old value.
s1 = "hello"
s2 = s1
s1 = s1.upper()
print(f"\n  s1 = {s1!r}, s2 = {s2!r}   ← rebinding s1 left s2 alone (str is immutable)")
