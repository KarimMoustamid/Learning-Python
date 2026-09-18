"""
Python Scope 🔭
- Where a name lives and how Python finds it: the LEGB rule
- Local → Enclosing → Global → Built-in
- Written for an experienced C# developer
- Run it:  python 01-fundamentals/14_scope.py
"""

# ─── No braces means no block scope ───────────────────────────
# In C#, a variable declared inside { } dies at the closing brace.
# In Python there are no braces — and if / for / while / try are NOT scopes.
# Only `def`, `class`, and `lambda` open a new scope.

if True:
    leaked_from_if = "declared inside if"

for counter in range(3):
    leaked_from_for = "declared inside for"

print("─── No braces means no block scope ───────────────────────")
print(f"  leaked_from_if:      {leaked_from_if}")
print(f"  leaked_from_for:     {leaked_from_for}")
print(f"  counter after loop:  {counter}   # loop variable survives the loop")

print("""
  C#: a variable declared inside { } is invisible outside it.
  Python: only `def` / `class` / `lambda` create a scope.
  Practical upshot — you can declare a variable inside an `if` branch and
  use it after, but don't. Keep declarations at the top of the function.
""")

# ─── Functions DO create a scope ──────────────────────────────
print("─── Functions do create a scope ──────────────────────────")


def function_scope():
    inside = "only visible in here"
    print(f"  inside the function:  {inside}")


function_scope()

try:
    print(inside)                     # NameError (exceptions get chapter 16)
except NameError as err:
    print(f"  outside the function: NameError → {err}")

# ─── LEGB: how Python resolves a name ────────────────────────
# Python looks for a name in this order and stops at the first hit:
#   L ocal → E nclosing → G lobal → B uilt-in

print("\n─── LEGB: Local → Enclosing → Global → Built-in ──────────")

colour = "global"


def outer():
    colour = "enclosing"

    def inner():
        # colour = "local"            # ← uncomment to shadow again
        print(f"  inner() sees:      {colour}")

    inner()
    print(f"  outer() sees:      {colour}")


outer()
print(f"  module level sees: {colour}")

# Built-in is the last resort — `len` is defined nowhere above
def uses_builtin():
    print(f"  built-in fallback: len('abc') = {len('abc')}")


uses_builtin()

# ─── Read is free, write needs `global` ───────────────────────
# The asymmetry that trips up every C# developer:
#   reading  a global inside a function → works
#   assigning to it                     → creates a NEW local, silently

print("\n─── Reading a global is free, assigning needs `global` ───")

hits = 0


def increment_wrong():
    hits = 1              # ← new LOCAL variable; the global is untouched


def increment_right():
    global hits           # C# has no equivalent — you'd use a field or `ref`
    hits += 1


increment_wrong()
print(f"  after increment_wrong():   hits = {hits}   ← unchanged, no error either")

increment_right()
increment_right()
print(f"  after 2x increment_right(): hits = {hits}")

print("""
  ⚠ increment_wrong() does not raise — it just quietly does nothing you
    wanted. Python has no `UnboundLocalError` to save you here because the
    name was assigned (so it IS local), it's simply discarded on return.
  Rule of thumb: if a function needs `global`, pass the value in and
  return the new value instead. `global` is a code smell in most code.
""")

# ─── Closures and `nonlocal` ──────────────────────────────────
# A closure is a nested function that keeps a live reference to a variable
# from its enclosing function. In C# you get this free with lambdas and
# local functions — same idea, but Python needs `nonlocal` to *rebind*.

print("─── Closures and `nonlocal` ──────────────────────────────")


def make_counter(start=0):
    """Return a function that counts up — state lives in the closure."""
    count = start

    def step(by=1):
        nonlocal count        # ← reach into the enclosing scope to rebind it
        count += by
        return count

    return step


c1 = make_counter()
c2 = make_counter(100)          # ← independent closure, independent state

print(f"  c1() = {c1()}   c1() = {c1()}   c1() = {c1()}")
print(f"  c2(10) = {c2(10)}   ← separate closure, separate `count`")
print(f"  c1() = {c1()}   ← unaffected by c2")

# ⚠ Mutating a captured container works WITHOUT nonlocal — only rebinding needs it
def make_logger(prefix):
    entries = []                  # a list, not a scalar

    def log(msg):
        entries.append(f"{prefix}: {msg}")   # mutation, not rebinding → no nonlocal
        return len(entries)

    return log, entries


log, entries = make_logger("foundry")
log("client built")
log("embedding requested")
print(f"\n  {entries}")
print("  ↑ mutation of a captured list needs no `nonlocal`; `x = ...` does")

# ─── The mutable default argument trap ───────────────────────
print("\n─── ⚠ The mutable default argument trap ──────────────────")
# Default values are evaluated ONCE, when the `def` statement executes —
# not per call. A mutable default is therefore shared by every call.


def add_bad(item, basket=[]):
    basket.append(item)
    return basket


print(f"  add_bad('apple')  → {add_bad('apple')}")
print(f"  add_bad('banana') → {add_bad('banana')}   ← 'apple' is still in there!")


def add_good(item, basket=None):
    if basket is None:            # C# default values are per-call; Python's are not
        basket = []
    basket.append(item)
    return basket


print(f"  add_good('apple')  → {add_good('apple')}")
print(f"  add_good('banana') → {add_good('banana')}   ← fresh list every call")

# ─── Comprehensions have their own scope ─────────────────────
print("\n─── Comprehensions have their own scope ──────────────────")

squares = [n * n for n in range(5)]
print(f"  squares = {squares}")

try:
    print(n)
except NameError:
    print("  `n` does not leak out of a comprehension ← unlike a plain for loop")

# ─── Practical: a closure-based config holder ────────────────
# This shape — capture connection details once, return a small function —
# is exactly how SDK wrappers around Azure AI Foundry tend to look.

print("\n─── Practical: closure-based client config ───────────────")


def make_endpoint_builder(endpoint, api_version="2024-10-21"):
    stats = {"calls": 0}

    def build(path):
        stats["calls"] += 1
        return {"url": f"{endpoint}/{path}", "api_version": api_version,
                "call": stats["calls"]}

    return build, stats


build, stats = make_endpoint_builder("https://my-foundry.services.ai.azure.com")
print(f"  {build('models')}")
print(f"  {build('chat/completions')}")
print(f"  calls made: {stats['calls']}")

print("""
  ─── Summary ──────────────────────────────────────────────
  1. Only def / class / lambda create a scope. if / for / while / try do not.
  2. Name resolution is LEGB: Local, Enclosing, Global, Built-in.
  3. Reading a global is free; assigning to one needs `global` (and usually
     signals a design problem).
  4. Rebinding an enclosing variable needs `nonlocal`; mutating it does not.
  5. Never use a mutable default argument — use None and build inside.
  6. Comprehensions are scoped; plain for loops are not.
""")
