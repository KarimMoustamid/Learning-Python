"""
Python Variables & Types
- C# is statically typed; Python is dynamically typed
- You don't declare types — they're inferred at runtime
- Use type() to check what type a value has
"""

# ─── Basic Types ───────────────────────────────────────────────

name = "Karim"           # str (like string in C#)
age = 30                 # int (like int — but unbounded, no overflow)
height = 1.78            # float (like double in C#, not float!)
is_learning = True       # bool (True/False — capital letters!)
favorite_language = None # NoneType (like null in C#)

# Python's print() can take multiple args — no string concat needed
print("name:", name, "| type:", type(name))
print("age:", age, "| type:", type(age))
print("height:", height, "| type:", type(height))
print("is_learning:", is_learning, "| type:", type(is_learning))
print("favorite_language:", favorite_language, "| type:", type(favorite_language))

# ─── Dynamic Typing ────────────────────────────────────────────
# In C#: string x = "hello"; x = 42; ❌ compiler error
# In Python: the variable just points to whatever you assign

x = "Now I'm a string"
print(f"\nx = {x!r}  ➜  type: {type(x).__name__}")

x = 42
print(f"x = {x}      ➜  type: {type(x).__name__}")

x = 3.14
print(f"x = {x}   ➜  type: {type(x).__name__}")
