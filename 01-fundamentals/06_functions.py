"""
Python Functions 🛠
- def instead of public/private returnType MethodName(...)
- No access modifiers (everything is public)
- First-class functions (you can pass them around like C# delegates/Action/Func)
"""

# ─── Basic function ───────────────────────────────────────────
# C#: public int Add(int a, int b) { return a + b; }
def add(a, b):
    """Return the sum of a and b."""   # docstring — like /// <summary>
    return a + b

result = add(3, 5)
print(f"add(3, 5) = {result}")

# ─── Default arguments ────────────────────────────────────────
# C#: public void Greet(string name, string greeting = "Hello")
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Karim")
greet("Karim", "Hola")           # positional
greet(greeting="Hej", name="K")  # keyword arguments (order doesn't matter)

# ─── Multiple return values (like C# tuples) ─────────────────
def divide(a, b):
    """Return (quotient, remainder)."""
    return a // b, a % b          # returns a tuple

quot, rem = divide(37, 5)        # tuple unpacking
print(f"\ndivide(37, 5) = ({quot}, {rem})")

# ─── *args (variable positional args — like params in C#) ────
def sum_all(*numbers):
    # C#: public int SumAll(params int[] numbers)
    return sum(numbers)

print(f"\nsum_all(1, 2, 3, 4, 5) = {sum_all(1, 2, 3, 4, 5)}")

# ─── **kwargs (variable keyword args) ────────────────────────
def print_user(**info):
    # C# doesn't have a direct equivalent — closest is Dictionary<string, object>
    for key, val in info.items():
        print(f"  {key}: {val}")

print("\nprint_user():")
print_user(name="Karim", role="Developer", years=8)

# ─── Functions as values ──────────────────────────────────────
# C#: Func<int, int> square = x => x * x;
square = lambda x: x * x        # lambda = one-line anonymous function
print(f"\nlambda square(6) = {square(6)}")

# Passing a function (like passing a delegate/Action)
def apply(func, value):
    return func(value)

print(f"apply(square, 7) = {apply(square, 7)}")
print(f"apply(lambda x: x.upper(), 'hello') = {apply(lambda x: x.upper(), 'hello')}")
