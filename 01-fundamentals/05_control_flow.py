"""
Python Control Flow 🔀
- if/elif/else — no parentheses needed, no switch/case
- for loops iterate over sequences (not like C#'s for(int i=0;...))
- While loops work like C#
- range() is your best friend
"""

# ─── if / elif / else ──────────────────────────────────────────
# C#: if (x > 0) { ... } else if (x == 0) { ... } else { ... }
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"      # this runs (85 >= 80)
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score} → Grade: {grade}")

# Key differences from C#:
#   ❌ No parentheses around condition
#   ❌ No switch/case (Python 3.10+ has match/case)
#   ✅ Colon after condition
#   ✅ Indentation defines block (no curly braces)

# ─── Ternary (one-liner if/else) ──────────────────────────────
# C#: var status = age >= 18 ? "Adult" : "Minor";
age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Status: {status}")

# ─── for / in (like foreach in C#) ────────────────────────────
print("\n── for loop over list ──")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  {fruit}")

# ─── range() (like for(int i=0; i<N; i++)) ──────────────────
# range(stop)        → 0 .. stop-1
# range(start, stop) → start .. stop-1
# range(start, stop, step) → with step

print("\n── range(5) ──")
for i in range(5):
    print(f"  {i}", end=" ")

print("\n── range(2, 10, 3) ──")
for i in range(2, 10, 3):
    print(f"  {i}", end=" ")

# ─── Enumerate (like C#: foreach(var (i, item) in items.Select(...))) ──
print("\n\n── enumerate ──")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")

# ─── while ─────────────────────────────────────────────────────
print("\n── while loop ──")
count = 3
while count > 0:
    print(f"  T-minus {count}...")
    count -= 1
print("  Go!")
