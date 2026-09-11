"""
Python Strings Basics 🧵
- Single and double quotes are IDENTICAL (C# only gives you "")
- Strings are immutable, exactly like C# string
- f-strings are the modern way to build text (C#: $"{x}")
"""

# ─── Creating strings ──────────────────────────────────────────
# There is NO difference between ' and " in Python — pick one and be consistent.
single = 'hello'
double = "hello"

print("─── Creating strings ──────────────────────────────────────")
print(f"  'hello' == \"hello\"  → {single == double}   ← no char type, always str")

# This is the big usability win over C#:
apostrophe = "It's easy"          # no escaping needed
quoted = 'He said "hi"'           # pick whichever quote avoids escapes
print(f"  apostrophe = {apostrophe!r}")
print(f"  quoted     = {quoted!r}")

# ─── Escape sequences ──────────────────────────────────────────
# Same backslash idea as C#.
newline_demo = "Line1\nLine2"
tab_demo = "Col1\tCol2"
backslash_demo = "C:\\Users\\dev"
e_acute = "\u00e9"

print("\n─── Escape sequences ──────────────────────────────────────")
print("  \\n  newline      →  " + repr(newline_demo))
print("  \\t  tab          →  " + repr(tab_demo))
print("  \\\\  backslash    →  " + repr(backslash_demo))
print("  \\uXXXX unicode   →  " + repr(e_acute) + "   (that's the letter e with an accent)")
print("  \\' and \\\" escape quotes when you need both kinds nested.")

print("\n  Printing 'Line1\\nLine2' actually renders as:")
print("  " + newline_demo)

# ─── Raw strings ───────────────────────────────────────────────
# Prefix with r to switch escaping OFF entirely — no more "C:\\Users\\dev"
raw_path = r"C:\Users\dev"
print("\n─── Raw strings ───────────────────────────────────────────")
print(f"  normal:  {backslash_demo!r}")
print(f"  raw:     {raw_path!r}   ← r'...' keeps backslashes literal")
print("  Also the sane way to write regex patterns.")

# ─── Multi-line strings ────────────────────────────────────────
# Triple quotes = multi-line literal. A triple-quoted string as the FIRST
# statement of a file or function is a docstring (like C#'s /// <summary>).
address = """123 Main Street
Springfield
""".rstrip()

print("\n─── Multi-line strings ────────────────────────────────────")
print("  address =")
print(f"  {address}")
print(f"  spans {len(address.splitlines())} lines")

# ─── Concatenation & repetition ────────────────────────────────
print("\n─── Concatenation & repetition ────────────────────────────")
print(f"  'Hello' + ' ' + 'World' → {('Hello' + ' ' + 'World')!r}   (like C#)")
print(f"  'ab' * 3                → {('ab' * 3)!r}       (* repeats — C# has no operator)")

# Adjacent literals are glued at parse time — handy for long messages
long_message = ("This is one logical string "
                "written across two source lines.")
print(f"  adjacent literals       → {long_message!r}")

greeting = "Hello"
greeting += ", Karim"          # like C# (+=)
print(f"  += appends              → {greeting!r}")

# ─── f-strings (the modern way) ────────────────────────────────
# C#:  $"Hello {name}, you are {age}"
# Py:  f"Hello {name}, you are {age}"
name, age = "Karim", 30
sentence = f"Hello {name}, you are {age}"

print("\n─── f-strings ─────────────────────────────────────────────")
print(f"  simple:          {sentence}")
print(f"  expressions:     {2 + 3} / {name.upper()} / {len(name)}")
print(f"  format specs:    {3.14159:.2f}   {42:>6}   {0.87:.1%}")
print(f"  debug shorthand: {name=}  {age=}    ← 3.8+, prints name=value")
print(f"  repr conversion: {name!r}   (shows the quotes)")

# Legacy ways — you WILL meet these in older codebases
print(f"\n  .format():  {'Hello, {}!'.format(name)}")
print(f"  % legacy:   {'Hello, %s!' % name}")
print("  C#'s closest cousin to .format() is string.Format().")

# ─── Conversion ────────────────────────────────────────────────
print("\n─── Conversion ────────────────────────────────────────────")
print(f"  str(42)      = {str(42)!r}     # C#: 42.ToString()")
print(f"  str(3.5)     = {str(3.5)!r}")
print(f"  str(True)    = {str(True)!r}      # note the capital T")
print(f"  str(None)    = {str(None)!r}")
print(f"  int('42')    = {int('42')}")
print(f"  float('1.5') = {float('1.5')}")
print("  ⚠ int('4.2') raises ValueError — convert to float() first, then int().")

# ─── len() ─────────────────────────────────────────────────────
# C#: str.Length (property)   →   Py: len(str) (function, works on any sequence)
short = "Karim"
path = "C:\\Users"
print("\n─── len() ─────────────────────────────────────────────────")
print(f"  len({short!r})       = {len(short)}")
print(f"  len('')              = {len('')}")
print(f"  len('héllo')         = {len('héllo')}   ← counts CHARACTERS, not bytes")
print(f"  len({path!r})  = {len(path)}   ← each backslash is ONE character")

# ─── Indexing ──────────────────────────────────────────────────
# Zero-indexed exactly like C#, PLUS negative indexes counting from the end.
word = "Python"
print("\n─── Indexing ──────────────────────────────────────────────")
print(f"  word = {word!r}")
print(f"  word[0]  = {word[0]!r}    ← first")
print(f"  word[1]  = {word[1]!r}")
print(f"  word[-1] = {word[-1]!r}    ← last  (no C# equivalent!)")
print(f"  word[-2] = {word[-2]!r}")
print("  Out of range → IndexError (C#: IndexOutOfRangeException).")

# ─── Membership ────────────────────────────────────────────────
# C#: str.Contains("Py")   →   Py: "Py" in str
print("\n─── Membership ────────────────────────────────────────────")
print(f"  'Py' in 'Python'    → {'Py' in 'Python'}    # C#: .Contains()")
print(f"  'py' in 'Python'    → {'py' in 'Python'}    ← case-SENSITIVE")
print(f"  'Java' not in word  → {'Java' not in word}")

# ─── Comparison ────────────────────────────────────────────────
print("\n─── Comparison ────────────────────────────────────────────")
print(f"  'abc' == 'abc'  → {'abc' == 'abc'}    # by VALUE — no .Equals() needed")
print(f"  'a' < 'b'       → {'a' < 'b'}    # lexicographic, like C#")
print(f"  'Z' < 'a'       → {'Z' < 'a'}    ← ⚠ uppercase sorts BEFORE lowercase (code points)")

# ─── Immutability ──────────────────────────────────────────────
# Same story as C#: you never edit a string in place, you build a new one.
print("\n─── Immutability ──────────────────────────────────────────")
word2 = "hello"
try:
    word2[0] = "H"          # TypeError — strings are immutable, like C#
except TypeError as e:
    print(f"  word2[0] = 'H' → TypeError: {e}")
word2 = "H" + word2[1:]     # rebind the name to a NEW string instead
print(f"  rebuilt: {word2!r}")
print("  ➜ slicing, .upper(), .replace() etc. all RETURN new strings.")
