"""
Python Operators ➕
Arithmetic, comparison, logical, assignment, identity, membership
"""

# ─── Arithmetic ────────────────────────────────────────────────
# Most work like C#, but Python adds ** (power) and // (floor division)

a, b = 15, 4

print(f"a = {a}, b = {b}")
print(f"  a + b  = {a + b}    # addition          (like C#)")
print(f"  a - b  = {a - b}    # subtraction       (like C#)")
print(f"  a * b  = {a * b}   # multiplication    (like C#)")
print(f"  a / b  = {a / b}    # true division     (always float — C#: a / (double)b)")
print(f"  a // b = {a // b}   # floor division    (like C#: a / b when both int)")
print(f"  a % b  = {a % b}    # modulo            (like C#: a % b)")
print(f"  a ** b = {a ** b}  # power (exponent)  (C#: Math.Pow(a, b))")

# ─── Comparison ────────────────────────────────────────────────
# Same as C#, but: == and != work by value by default (no .Equals() needed)

x, y = 10, 20

print(f"\nx = {x}, y = {y}")
print(f"  x == y → {x == y}    # equal to          (like C#)")
print(f"  x != y → {x != y}    # not equal to      (like C#)")
print(f"  x <  y → {x < y}     # less than         (like C#)")
print(f"  x >  y → {x > y}     # greater than      (like C#)")
print(f"  x <= y → {x <= y}    # less or equal     (like C#)")
print(f"  x >= y → {x >= y}    # greater or equal  (like C#)")

# Python exclusive: chained comparisons (C# can't do this)
# C#: if (10 < x && x < 30) ...
print(f"\n  10 < x < 30 → {10 < x < 30}    # chained — no && needed!")

# ─── Logical ───────────────────────────────────────────────────
# C#: &&, ||, !
# Python: and, or, not (words, not symbols)

age = 25
has_license = True

print(f"\nage = {age}, has_license = {has_license}")
print(f"  age >= 18 and has_license → {age >= 18 and has_license}   # like &&")
print(f"  age < 18 or not has_license → {age < 18 or not has_license}    # like || / !")

# ─── Assignment (shortcuts) ────────────────────────────────────
# Same as C#: +=, -=, *=, /=, //=, %=, **=

score = 10
print(f"\nscore = {score}")
score += 5     # like C#
print(f"  score += 5  → {score}")
score *= 2     # like C#
print(f"  score *= 2  → {score}")

# ─── Identity: is / is not ─────────────────────────────────────
# C#: referenceEquals — checks if two variables point to the same object
# ⚠ NOT the same as == (which checks value equality)

a_list = [1, 2, 3]
b_list = [1, 2, 3]
c_list = a_list  # same reference

print(f"\na_list == b_list → {a_list == b_list}    # same VALUE   (like .Equals())")
print(f"a_list is b_list → {a_list is b_list}  # same OBJECT?  (like ReferenceEquals)")
print(f"a_list is c_list → {a_list is c_list}  # same OBJECT — c_list points to a_list")

# Practical use: checking for None (never use == None)
value = None
print(f"\n  value is None → {value is None}    # ✅ idiomatic")
print(f"  value == None → {value == None}    # ❌ works but not Pythonic")

# ─── Membership: in / not in ────────────────────────────────────
# C#: .Contains() — Python uses 'in' keyword
fruits = ["apple", "banana", "cherry"]
print(f"\nfruits = {fruits}")
print(f"  'apple' in fruits  → {'apple' in fruits}    # like .Contains()")
print(f"  'mango' in fruits  → {'mango' in fruits}")
print(f"  'mango' not in fruits → {'mango' not in fruits}")

# Works on strings too (substring check)
print(f"\n  'Py' in 'Python' → {'Py' in 'Python'}    # substring check")
