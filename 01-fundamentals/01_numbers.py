"""
Python Numbers 🔢
- Three numeric types built in: int, float, complex
- int is ARBITRARY precision — it never overflows (C#: like BigInteger, always)
- float is a 64-bit double (C#: double). Python has NO 32-bit float.
- Need exact decimals (money)? Use the `decimal` module (C#: decimal)
"""

import math
from decimal import Decimal

# ─── The three numeric types ───────────────────────────────────
# C# has int, long, float, double, decimal. Python has ONE int and ONE float.
count = 42          # int     — C# int / long / BigInteger, all merged into one
price = 19.99       # float   — exactly C# double (64-bit)
z = 3 + 4j          # complex — like C# System.Numerics.Complex

print("─── The three numeric types ───────────────────────────────")
for value in (count, price, z):
    print(f"  {str(value):<8} → type: {type(value).__name__}")

# No overflow, no suffixes, no wrapping. C# would need BigInteger for this.
big = 2 ** 100
print(f"\n  2 ** 100 = {big}")
print(f"  type: {type(big).__name__}   ← still a plain int, no overflow")

# ─── Arithmetic ────────────────────────────────────────────────
a, b = 7, 2
print(f"\n─── Arithmetic (a = {a}, b = {b}) ──────────────────────────")
print(f"  a + b  = {a + b:<6}  # addition          (like C#)")
print(f"  a - b  = {a - b:<6}  # subtraction       (like C#)")
print(f"  a * b  = {a * b:<6}  # multiplication    (like C#)")
print(f"  a / b  = {a / b:<6}  # TRUE division → ALWAYS a float")
print(f"  a // b = {a // b:<6}  # floor division    (C#: a / b on ints)")
print(f"  a % b  = {a % b:<6}  # modulo            (like C#)")
print(f"  a ** b = {a ** b:<6}  # power             (C#: Math.Pow(a, b))")

# ─── The division trap coming from C# ──────────────────────────
print("""
─── ⚠ Division traps from C# ──────────────────────────────
  C#:  7 / 2   → 3      int / int truncates
  Py:  7 / 2   → 3.5    ALWAYS float — use // to get C# behaviour
  Py:  7 // 2  → 3

  Negative numbers round the OTHER way:
  C#: -7 / 2   → -3     truncates toward zero
  Py: -7 // 2  → -4     floors toward -infinity
""")
print(f"  -7 // 2 = {-7 // 2}    (floor, not truncate)")
print(f"  -7 % 3  = {-7 % 3}     (C# gives -1 — here the sign follows the divisor)")

# ─── Float precision ───────────────────────────────────────────
# Same IEEE-754 double as C#, so exactly the same surprises.
print("\n─── Float precision ───────────────────────────────────────")
print(f"  0.1 + 0.2          = {0.1 + 0.2}")
print(f"  (0.1 + 0.2) == 0.3 ? {0.1 + 0.2 == 0.3}   ← False! (same as C# double)")
print(f"  math.isclose(...)    {math.isclose(0.1 + 0.2, 0.3)}   ← ✅ the right way")

# ─── Exact decimals (money) ────────────────────────────────────
# C#: decimal. Python: Decimal — always build it from a STRING, never a float.
print("\n─── Exact decimals (money) ────────────────────────────────")
print(f"  Decimal('0.1') + Decimal('0.2') = {Decimal('0.1') + Decimal('0.2')}")
print(f"  == Decimal('0.3') ?               {Decimal('0.1') + Decimal('0.2') == Decimal('0.3')}   ← ✅")
print(f"  ⚠ Decimal(0.1) is WRONG → {Decimal(0.1)}  (the float error is baked in)")

# ─── Rounding ──────────────────────────────────────────────────
print("\n─── Rounding ──────────────────────────────────────────────")
print(f"  round(2.5)      = {round(2.5)}     ← banker's rounding! rounds to EVEN")
print(f"  round(3.5)      = {round(3.5)}")
print(f"  round(-3.7)     = {round(-3.7)}     ← not floor()")
print(f"  round(2.675, 2) = {round(2.675, 2)}  ← 2.67, not 2.68 (float representation)")
print("  C# Math.Round() also rounds to even by default — same trap.")

# ─── Numeric literals ──────────────────────────────────────────
# Underscores are pure syntax sugar (C# 7+ has them too).
print("\n─── Numeric literals ──────────────────────────────────────")
print(f"  1_000_000 = {1_000_000:>12,}   # underscores = readability")
print(f"  0b1010    = {0b1010:>12}   # binary")
print(f"  0o17      = {0o17:>12}   # octal   (C# has no literal for this)")
print(f"  0xFF      = {0xFF:>12}   # hex")
print(f"  1e6       = {1e6:>12,.0f}   # scientific notation")
print(f"  1.5e-3    = {1.5e-3:>12}   # tiny float")

# ─── Conversions ───────────────────────────────────────────────
print("\n─── Conversions ───────────────────────────────────────────")
print(f"  int('42')        = {int('42')}")
print(f"  int(3.99)        = {int(3.99)}      ← TRUNCATES toward zero, no rounding")
print(f"  float('1.5')     = {float('1.5')}")
print(f"  int('0xFF', 16)  = {int('0xFF', 16)}     ← parse with an explicit base")
print(f"  str(42)          = {str(42)!r}")
print(f"  bool(0)          = {bool(0)}     ← 0 and 0.0 are falsy")
print(f"  bool(0.1)        = {bool(0.1)}   ← any non-zero float is truthy")
print("  ⚠ int('4.2') raises ValueError — convert to float first, then int.")

# ─── Built-in numeric helpers ──────────────────────────────────
print("\n─── Built-in numeric helpers ──────────────────────────────")
nums = [3, 1, 4, 1, 5]
print(f"  abs(-7)              = {abs(-7)}")
print(f"  min({nums})      = {min(nums)}")
print(f"  max({nums})      = {max(nums)}")
print(f"  sum({nums})      = {sum(nums)}")
print(f"  divmod(37, 5)        = {divmod(37, 5)}   ← (quotient, remainder) in one call")
print(f"  pow(2, 8)            = {pow(2, 8)}      # same as 2 ** 8")
print(f"  isinstance(42, int)  = {isinstance(42, int)}")
print(f"  isinstance(42, float)= {isinstance(42, float)}")
print(f"  isinstance(True, int)= {isinstance(True, int)}   ← ⚠ bool IS a subclass of int!")

# ─── The math module ───────────────────────────────────────────
print("\n─── The math module ───────────────────────────────────────")
print(f"  math.sqrt(16)   = {math.sqrt(16)}")
print(f"  math.floor(3.7) = {math.floor(3.7)}     ← always toward -infinity")
print(f"  math.ceil(3.2)  = {math.ceil(3.2)}")
print(f"  round(3.7)      = {round(3.7)}     ← different rules from floor()")
print(f"  math.pi         = {math.pi:.6f}")
print("  C#: Math.Sqrt / Math.Floor / Math.Ceiling / Math.PI")

# ─── Formatting numbers ────────────────────────────────────────
# Python 3.6+ f-string format specs — far nicer than C# ToString("N2")
print("\n─── Formatting numbers ────────────────────────────────────")
print(f"  {{:,}}    1234567 → {1234567:,}")
print(f"  {{:.2f}}    3.14159 → {3.14159:.2f}")
print(f"  {{:>8}}     42      → '{42:>8}'   (right-align)")
print(f"  {{:<8}}     42      → '{42:<8}'   (left-align)")
print(f"  {{:^8}}     42      → '{42:^8}'   (centred)")
print(f"  {{:05d}}     42      → {42:05d}      (zero-padded)")
print(f"  {{:+.2f}}    3.14159 → {3.14159:+.2f}    (forced sign)")
print(f"  {{:.1%}}     0.87    → {0.87:.1%}   (percent)")
print(f"  {{:x}}/{{:b}}  255     → {255:x} / {255:b}")
