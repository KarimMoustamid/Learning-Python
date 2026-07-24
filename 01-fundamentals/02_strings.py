"""
Python Strings 🧵
- Immutable, like C# string
- f-strings are the Pythonic equivalent of $"{x}" in C#
- Rich built-in methods: len, upper/lower, strip, split, join, replace
"""

name = "  Karim Moustamid  "

# ─── f-strings (best way to format in Python 3.6+) ────────────
# C# equivalent: Console.WriteLine($"Hello, {name}!")
print(f"Hello, {name}!")  # includes the extra spaces

# ─── Cleanup methods ──────────────────────────────────────────
clean = name.strip()           # like .Trim() in C#
print(f"Stripped: '{clean}'")

print(f"Upper:   {clean.upper()}")    # .ToUpper()
print(f"Lower:   {clean.lower()}")    # .ToLower()
print(f"Length:  {len(clean)}")       # .Length — len() works on any sequence

# ─── Split & Join ─────────────────────────────────────────────
# C#: "a,b,c".Split(',')  /  string.Join(", ", items)
csv = "apple,banana,cherry"
fruits = csv.split(",")               # → list ["apple", "banana", "cherry"]
print(f"\nSplit: {fruits}")

rejoined = " | ".join(fruits)         # join() is called ON the separator!
print(f"Joined: {rejoined}")

# ─── Slicing (like Span<T>/Substring, but way more powerful) ──
alphabet = "abcdefghijklmnopqrstuvwxyz"
print(f"\nFull:     {alphabet}")
print(f"First 5:  {alphabet[:5]}")         # "abcde"   — 0..4
print(f"Last 5:   {alphabet[-5:]}")        # "vwxyz"   — count from end
print(f"3 to 10:  {alphabet[3:10]}")       # "defghij"
print(f"Step 3:   {alphabet[::3]}")        # "adgjmpsvy"  — every 3rd

# ─── Replace & Find ───────────────────────────────────────────
sentence = "Python is great and Python is fun"
print(f"\nReplace:  {sentence.replace('Python', 'C#')}")
print(f"Find 'great': {sentence.find('great')}")  # index or -1 (like .IndexOf())
