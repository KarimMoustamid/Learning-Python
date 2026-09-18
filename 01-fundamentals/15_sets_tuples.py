"""
Python Tuples & Sets 📦🎯
- Tuple → like C# ValueTuple / immutable record: fixed size, immutable, hashable
- Set   → like C# HashSet<T>: unordered, unique, O(1) membership tests
- Both are built-in literals — no import, no `new`, no generics
- Written for an experienced C# developer
- Run it:  python 01-fundamentals/15_sets_tuples.py
"""

# ═══ PART 1 — TUPLES ═════════════════════════════════════════

# ─── Creating tuples ─────────────────────────────────────────
point = (3, 5)                            # like C# (int, int) value tuple
rgb = (255, 128, 0)
mixed = ("Karim", 8, True)                # heterogeneous, like List<object> but fixed
empty = ()
one = (42,)                               # ⚠ trailing comma REQUIRED for 1-element
not_a_tuple = (42)                        # ← this is just the int 42 in brackets

print("─── Creating tuples ──────────────────────────────────────")
print(f"  point       = {point}")
print(f"  rgb         = {rgb}")
print(f"  mixed       = {mixed}")
print(f"  empty       = {empty}")
print(f"  one         = {one}      type: {type(one).__name__}")
print(f"  (42) alone  = {not_a_tuple}      type: {type(not_a_tuple).__name__}  ← not a tuple!")

# ─── Indexing & slicing — identical to lists and strings ─────
print("\n─── Indexing and slicing ─────────────────────────────────")
print(f"  rgb[0]     = {rgb[0]}")
print(f"  rgb[-1]    = {rgb[-1]}")
print(f"  rgb[:2]    = {rgb[:2]}          # slicing a tuple yields a tuple")

# ─── Immutability ────────────────────────────────────────────
print("\n─── Immutable: you cannot change a tuple in place ────────")
try:
    rgb[0] = 0
except TypeError as err:
    print(f"  rgb[0] = 0 → TypeError: {err}")
print("  C#: same as a readonly struct / record with init-only properties")

# ─── Unpacking — where tuples really earn their keep ─────────
# This is the idiomatic Python way to return multiple values, and to swap.

print("\n─── Unpacking ────────────────────────────────────────────")
x, y = point
print(f"  x, y = point          → x={x}  y={y}")

name, years, active = mixed
print(f"  name, years, active   → {name}, {years}, {active}")

# Swap with no temp variable (C#: (a, b) = (b, a) — same idea, no ceremony)
a, b = 1, 2
a, b = b, a
print(f"  swap without a temp   → a={a}  b={b}")

# Star-unpacking: grab the rest into a list
first, *rest = (1, 2, 3, 4, 5)
print(f"  first, *rest          → first={first}  rest={rest}")

*init, last = (1, 2, 3, 4, 5)
print(f"  *init, last           → init={init}  last={last}")

# Unpacking in a loop — the pattern behind dict.items() and enumerate()
users = [("karim", "dev"), ("maria", "architect"), ("ahmed", "manager")]
print("\n  for name, role in users:")
for name, role in users:
    print(f"    {name:<8} → {role}")

# ─── Tuples as dict keys (hashable) ──────────────────────────
# A tuple of immutable values is hashable, so it can be a key.
# A list cannot — this is the classic "why use a tuple" answer.

print("\n─── Tuples are hashable → usable as dict keys ────────────")
grid = {
    (0, 0): "origin",
    (1, 0): "east",
    (0, 1): "north",
}
print(f"  grid[(1, 0)] = {grid[(1, 0)]}")

try:
    broken = {[1, 2]: "nope"}
except TypeError as err:
    print(f"  {{[1, 2]: 'nope'}} → TypeError: {err}")
    print("  ↑ lists are mutable, so they are unhashable and cannot be keys")

# ─── Named tuples — the ValueTuple with names ────────────────
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])        # like a small immutable record
p = Point(3, 5)
print("\n─── namedtuple: readable field names ─────────────────────")
print(f"  p        = {p}")
print(f"  p.x      = {p.x}      p.y = {p.y}")
print(f"  p[0]     = {p[0]}      ← still works positionally, it IS a tuple")
print(f"  as dict  = {p._asdict()}")
print("  Modern alternative: @dataclass(frozen=True) — see 18_oop.py")

# ═══ PART 2 — SETS ═══════════════════════════════════════════

# ─── Creating sets ───────────────────────────────────────────
# Curly braces with no colons = a set, NOT a dict. Careful.
fruits = {"apple", "banana", "cherry"}
from_list = set([1, 2, 2, 3, 3, 3])            # dedupes automatically
empty_set = set()                              # ⚠ {} is an empty DICT, not a set

print("\n═══ PART 2 — SETS ═════════════════════════════════════════")
print("─── Creating sets ────────────────────────────────────────")
print(f"  fruits          = {sorted(fruits)}   ← sorted() here only for stable output")
print(f"  set([1,2,2,3,3,3]) = {sorted(from_list)}   ← duplicates removed")
print(f"  set()           = {empty_set}          ← use set() for empty, {{}} is a dict")
print(f"  type({{}})       = {type({}).__name__}  ⚠ braces alone make a dict")

# ─── Deduplication — the everyday use case ───────────────────
print("\n─── Deduplicating a list (order is NOT preserved) ────────")
raw = ["b", "a", "b", "c", "a", "d"]
print(f"  list first → set      → {sorted(set(raw))}")
print("  Want dedup WITH order preserved?")
ordered = list(dict.fromkeys(raw))             # dicts keep insertion order (3.7+)
print(f"  list(dict.fromkeys(..)) → {ordered}   ← the idiom to remember")

# ─── Membership is O(1) — the performance argument ───────────
# `in` on a list scans every element. `in` on a set hashes and jumps.
print("\n─── Membership: sets are O(1), lists are O(n) ────────────")
big_list = list(range(1_000_000))
big_set = set(big_list)

import time

start = time.perf_counter()
found_list = 999_999 in big_list
list_ms = (time.perf_counter() - start) * 1000

start = time.perf_counter()
found_set = 999_999 in big_set
set_ms = (time.perf_counter() - start) * 1000

print(f"  x in list → {found_list}   (~{list_ms:.2f} ms)")
print(f"  x in set  → {found_set}   (~{set_ms:.4f} ms)")
print("  ← exact numbers vary by machine; the ratio is the lesson")
print("  C#: exactly why you reach for HashSet<T> instead of List<T>.Contains()")

# ─── Set algebra — the reason sets exist ─────────────────────
# C#: HashSet<T> has UnionWith, IntersectWith, ExceptWith, SymmetricExceptWith.
# Python gives you operators, which compose far more readably.

print("\n─── Set algebra (operators, not method calls) ────────────")
backend = {"karim", "maria", "ahmed"}
frontend = {"maria", "sara", "ahmed"}

print(f"  backend        = {sorted(backend)}")
print(f"  frontend       = {sorted(frontend)}")
print(f"  union       a|b = {sorted(backend | frontend)}")
print(f"  intersect   a&b = {sorted(backend & frontend)}")
print(f"  difference  a-b = {sorted(backend - frontend)}")
print(f"  sym.diff    a^b = {sorted(backend ^ frontend)}")

print(f"\n  subset:      {{'karim'}} <= backend → {({'karim'} <= backend)}")
print(f"  superset:    backend >= {{'karim','maria'}} → {backend >= {'karim', 'maria'}}")
print(f"  disjoint:    backend.isdisjoint(frontend) → {backend.isdisjoint(frontend)}")

# ─── Mutating sets ───────────────────────────────────────────
print("\n─── Mutating sets ────────────────────────────────────────")
skills = {"python", "sql"}
skills.add("azure")                        # like HashSet<T>.Add()
skills.update(["ai", "python"])            # bulk add; "python" already there
print(f"  after add/update: {sorted(skills)}")

skills.discard("sql")                      # discard = no error if missing
skills.discard("nope")
print(f"  after discard:    {sorted(skills)}")

try:
    skills.remove("nope")                  # remove = KeyError if missing
except KeyError as err:
    print(f"  remove('nope') → KeyError: {err}   ← use discard() to be safe")

# ─── frozenset — an immutable, hashable set ──────────────────
print("\n─── frozenset: immutable set, so it can be a dict key ───")
fs = frozenset(["a", "b", "c"])
print(f"  fs = {sorted(fs)}   type: {type(fs).__name__}")
try:
    fs.add("d")
except AttributeError as err:
    print(f"  fs.add('d') → AttributeError: {err}")
roles = {fs: "read-only group"}
print(f"  used as dict key → {roles[fs]}")

# ─── Practical: comparing API payload keys ───────────────────
# A realistic use: diff two versions of a config or API response to see
# exactly which fields were added and removed.

print("\n─── Practical: diff two payload schemas ──────────────────")
expected_fields = {"id", "model", "messages", "temperature", "stream"}
actual_fields = {"id", "model", "messages", "stream", "top_p"}

missing = expected_fields - actual_fields
unexpected = actual_fields - expected_fields
print(f"  expected  : {sorted(expected_fields)}")
print(f"  actual    : {sorted(actual_fields)}")
print(f"  missing   : {sorted(missing)}")
print(f"  unexpected: {sorted(unexpected)}")

print("""
  ─── Choosing between them ────────────────────────────────
  list   → ordered, mutable, allows duplicates        (C# List<T>)
  tuple  → ordered, immutable, hashable               (C# ValueTuple)
  set    → unordered, unique, O(1) membership          (C# HashSet<T>)
  dict   → keyed lookup, insertion-ordered             (C# Dictionary<TK,TV>)

  Rule of thumb:
    fixed group of values that never changes  → tuple
    "is this in that collection?" questions   → set
    ordered sequence you will edit            → list
    looking something up by name/id           → dict
""")
