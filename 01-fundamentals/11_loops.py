"""
Python Loops 🔁
- for iterates over a SEQUENCE (like C# foreach) — not counter arithmetic
- while works much like C#
- range() is what you reach for instead of  for (int i = 0; i < n; i++)
- break / continue / for-else
(Extracted from the old control-flow file — conditionals now live in 07/08.)
"""

# ─── for / in ──────────────────────────────────────────────────
# C#: foreach (var fruit in fruits) { Console.WriteLine(fruit); }
# Py: for fruit in fruits:  — no type, no braces, no parentheses
fruits = ["apple", "banana", "cherry"]
print("─── for over a list ───────────────────────────────────────")
for fruit in fruits:
    print(f"  {fruit}")

# Iterate a string (character by character)
print("\n─── for over a string ─────────────────────────────────────")
for ch in "Py":
    print(f"  {ch}", end="")
print()

# Iterate a dict — keys by default, .items() for both
scores = {"karim": 92, "maria": 88}
print("\n─── for over a dict ───────────────────────────────────────")
for key in scores:
    print(f"  key only:      {key}")
for key, value in scores.items():
    print(f"  .items():      {key} → {value}")

# ─── range() ───────────────────────────────────────────────────
# range(stop)               → 0 .. stop-1
# range(start, stop)        → start .. stop-1
# range(start, stop, step)  → with a step
print("\n─── range() ───────────────────────────────────────────────")
print("  range(5):           ", end="")
for i in range(5):
    print(i, end=" ")
print()
print("  range(2, 6):        ", end="")
for i in range(2, 6):
    print(i, end=" ")
print()
print("  range(0, 10, 3):    ", end="")
for i in range(0, 10, 3):
    print(i, end=" ")
print()
print("  range(5, 0, -1):    ", end="")
for i in range(5, 0, -1):
    print(i, end=" ")
print()

# range is LAZY — it doesn't build a list (C# has no equivalent out of the box)
r = range(1_000_000)
print(f"\n  range(1_000_000) is lazy → {r!r}, len = {len(r):,}")
print(f"  list(range(3)) → {list(range(3))}   ← materialise it if you really need a list")
print("  ⚠ range(5) is 0,1,2,3,4 — the stop value is EXCLUDED. Off-by-one lives here.")

# ─── enumerate() ───────────────────────────────────────────────
# C#: foreach (var (item, i) in items.Select((item, i) => (item, i)))
# Py: for i, item in enumerate(items) — you get the index for free
print("\n─── enumerate() ───────────────────────────────────────────")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

print("  starting at 1: ", end="")
for i, fruit in enumerate(fruits, start=1):
    print(f"{i}-{fruit}", end=" ")
print()

# ─── zip() ─────────────────────────────────────────────────────
# Walk several sequences in parallel (C#: Zip)
names = ["karim", "maria", "ahmed"]
roles = ["dev", "architect", "manager"]
print("\n─── zip() ─────────────────────────────────────────────────")
for name, role in zip(names, roles):
    print(f"  {name:<8} {role}")
print("  zip() stops at the SHORTEST sequence — no index errors.")

# ─── while ─────────────────────────────────────────────────────
print("\n─── while ─────────────────────────────────────────────────")
count = 3
while count > 0:
    print(f"  T-minus {count}...")
    count -= 1
print("  Go!")

# A while loop with a condition you control
attempts = 0
while attempts < 3:
    attempts += 1
print(f"\n  looped {attempts} times, then the condition went false")
print("  ⚠ while True: needs a break inside, or you're stuck forever.")

# ─── break / continue ──────────────────────────────────────────
print("\n─── break / continue ──────────────────────────────────────")
print("  break on 'banana': ", end="")
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit, end=" ")
print()

print("  continue (skip 'banana'): ", end="")
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit, end=" ")
print()
print("  C#: break / continue — identical semantics.")

# ─── for-else ──────────────────────────────────────────────────
# ⭐ Unique to Python: the else runs only if the loop finished WITHOUT break.
# Think of it as "no break happened" rather than "else".
print("\n─── for-else (no C# equivalent) ───────────────────────────")
for fruit in fruits:
    if fruit == "mango":
        print("  found mango")
        break
else:
    print("  loop completed with no break → mango was never found")

for fruit in fruits:
    if fruit == "cherry":
        print("  found cherry, breaking")
        break
else:
    print("  (this else is skipped because we broke out)")

# ─── Common idioms ─────────────────────────────────────────────
print("\n─── Common idioms ─────────────────────────────────────────")
prices = [10, 25, 40]
total = 0
for price in prices:
    total += price
print(f"  accumulator:   total = {total}   (or just: sum(prices) = {sum(prices)})")

target = 25
found = None
for i, price in enumerate(prices):
    if price == target:
        found = i
        break
print(f"  find-first:    {target} is at index {found}")

# Build a new list instead of mutating while iterating
loud = []
for fruit in fruits:
    loud.append(fruit.upper())
print(f"  transform:     {loud}   (or: {[f.upper() for f in fruits]})")

# ─── Pitfalls ──────────────────────────────────────────────────
print("""
─── Pitfalls ──────────────────────────────────────────────
  ❌ Don't mutate a list while looping over it:
       for f in fruits:
           fruits.remove(f)     # skips elements — iterate a COPY instead

  ❌ No counter-arithmetic for-loop:
       for (i = 0; i < n; i++)   →   for i in range(n)

  ⚠ Nested loops multiply: 3 x 4 iterations = 12. Keep them shallow.

  ⚠ for-else is easy to misread — if nobody on the team knows it,
     an explicit `found = False` flag is kinder.
""")
