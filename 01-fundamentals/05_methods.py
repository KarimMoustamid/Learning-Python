"""
Python Methods 🛠
- A method is a function BOUND to an object:  object.method()
- A plain function stands alone:              function(object)
- str ships with ~45 methods (C#: instance methods on the string class)
- ⚠ Every string method RETURNS A NEW STRING — strings are immutable
"""

# ─── Function vs method ────────────────────────────────────────
# len(s)        → a built-in FUNCTION taking a string
# s.upper()     → a METHOD belonging to that string object
# Same split as C#: Math.Abs(x) is static, x.ToString() is an instance method.
text = "  hello world  "
print("─── Function vs method ────────────────────────────────────")
print(f"  len(text)          = {len(text)}    ← function (no object involved)")
print(f"  text.upper()       = {text.upper()!r}    ← method (bound to text)")

# ─── Discovering methods ───────────────────────────────────────
# C#: IntelliSense.  Python: dir() and help() at runtime.
methods = [m for m in dir(str) if not m.startswith("_")]
print(f"\n─── Discovery ─────────────────────────────────────────────")
print(f"  str has {len(methods)} public methods")
print(f"  some: {', '.join(methods[:12])} ...")
print("  dir(str)     → all attributes (C#: reflection)")
print("  help(str.split) → inline docs (works on anything)")
print(f"  'abc'.upper.__doc__ → {(lambda: 'abc'.upper.__doc__)()!r}")

# ─── Case methods ──────────────────────────────────────────────
name = "karim moustamid"
print("\n─── Case ──────────────────────────────────────────────────")
print(f"  .upper()      {name.upper()!r}      # C#: ToUpper()")
print(f"  .lower()      {name.lower()!r}")
print(f"  .title()      {name.title()!r}      # C#: TextInfo.ToTitleCase()")
print(f"  .capitalize() {name.capitalize()!r}")
print(f"  .swapcase()   {name.swapcase()!r}")
print(f"  .casefold()   {'STRASSE'.casefold()!r}   # aggressive lower, for comparisons")
print("  ⚠ .upper()/.lower() don't fix data — case-insensitive compare needs .casefold()")

# ─── Whitespace ────────────────────────────────────────────────
print("\n─── Whitespace ────────────────────────────────────────────")
print(f"  text                 = {text!r}")
print(f"  .strip()             = {text.strip()!r}    # C#: Trim()")
print(f"  .lstrip()            = {text.lstrip()!r}    # C#: TrimStart()")
print(f"  .rstrip()            = {text.rstrip()!r}    # C#: TrimEnd()")
print(f"  .strip('*')          = {'**hi**'.strip('*')!r}      # strip specific chars, not just space")

# ─── Searching ─────────────────────────────────────────────────
sentence = "the quick brown fox jumps over the lazy dog"
print("\n─── Searching ─────────────────────────────────────────────")
print(f"  sentence.find('the')        = {sentence.find('the')}    # C#: IndexOf()")
print(f"  sentence.rfind('the')       = {sentence.rfind('the')}    # last occurrence")
print(f"  sentence.find('zzz')        = {sentence.find('zzz')}   ← -1 when missing (no exception!)")
print(f"  sentence.index('the')       = {sentence.index('the')}    # like find() but RAISES if missing")
print(f"  sentence.count('the')       = {sentence.count('the')}    # C#: no direct equivalent")
print(f"  sentence.startswith('the')  = {sentence.startswith('the')}")
print(f"  sentence.endswith('dog')    = {sentence.endswith('dog')}")
print(f"  .startswith(('a','the'))    = {sentence.startswith(('a', 'the'))}   ← tuple = any-of")
print("  ⚠ find() returns -1; index() raises ValueError — pick deliberately.")

# ─── Splitting & joining ───────────────────────────────────────
# THE most-used pair in real code (parsing CSVs, log lines, paths).
csv = "apple,banana,cherry,date"
parts = csv.split(",")
print("\n─── Splitting & joining ───────────────────────────────────")
print(f"  csv                     = {csv!r}")
print(f"  .split(',')             = {parts}   # C#: Split(',') → string[]")
print(f"  .rsplit(',', 1)         = {csv.rsplit(',', 1)}   # split from the RIGHT, max 1")
print(f"  .split(',', 2)          = {csv.split(',', 2)}   # maxsplit")
print(f"  'a b  c'.split()        = {'a b  c'.split()}   ← no arg = split on ANY whitespace")
print(f"  ' | '.join(parts)       = {' | '.join(parts)!r}   # C#: string.Join()")
multiline = "line1\nline2"
print(f"  {multiline!r}.splitlines() = {multiline.splitlines()}")
print(f"  'a=b=c'.partition('=')  = {'a=b=c'.partition('=')}   # (before, sep, after)")
print("  ⚠ join() is called ON THE SEPARATOR, and the list goes in — backwards vs C#!")

# ─── Replacing ─────────────────────────────────────────────────
print("\n─── Replacing ─────────────────────────────────────────────")
raw = "2026-09-11"
print(f"  'aaa'.replace('a','b')          = {'aaa'.replace('a', 'b')!r}")
print(f"  'aaa'.replace('a','b',1)        = {'aaa'.replace('a', 'b', 1)!r}   # only first N")
print(f"  raw.replace('-', '/', 1)        = {raw.replace('-', '/', 1)!r}")
print(f"  'test_file.py'.removeprefix('test_') = {'test_file.py'.removeprefix('test_')!r}   # 3.9+")
print(f"  'test_file.py'.removesuffix('.py')   = {'test_file.py'.removesuffix('.py')!r}   # 3.9+")
print("  C#: Replace() has no count param — and there's no RemovePrefix/RemoveSuffix.")

# ─── Predicates (is... — they return bool) ─────────────────────
print("\n─── Predicates ────────────────────────────────────────────")
samples = ["hello", "Hello World", "abc123", "12345", "   ", "", "héllo"]
for sample in samples:
    print(f"  {sample!r:<16} isalpha={str(sample.isalpha()):<6} "
          f"isdigit={str(sample.isdigit()):<6} "
          f"isalnum={str(sample.isalnum()):<6} "
          f"isspace={str(sample.isspace()):<6} "
          f"isascii={str(sample.isascii()):<6}")
print(f"\n  'abc123'.isidentifier() = {'abc123'.isidentifier()}   ← valid variable name?")

# ─── Padding & alignment ───────────────────────────────────────
print("\n─── Padding ───────────────────────────────────────────────")
print(f"  '42'.zfill(5)    = {'42'.zfill(5)!r}     # C#: PadLeft(5,'0')")
print(f"  'hi'.center(10)  = {'hi'.center(10)!r}     # C#: no equivalent")
print(f"  'hi'.ljust(10,'.') = {'hi'.ljust(10, '.')!r}")
print(f"  'hi'.rjust(10,'.') = {'hi'.rjust(10, '.')!r}")
print("  f-strings do all of this better:  f\"{value:>10}\"")

# ─── Chaining ──────────────────────────────────────────────────
# Every method returns a new string, so you can chain (like LINQ / StringBuilder)
messy = "   KARIM   moustamid  "
print("\n─── Chaining ──────────────────────────────────────────────")
print(f"  input            = {messy!r}")
print(f"  stripped         = {messy.strip()!r}")
print(f"  stripped.lower() = {messy.strip().lower()!r}")
clean = messy.strip().lower().replace("  ", " ").title()
print(f"  chained          = {clean!r}")
print("  ➜ .strip().lower().replace(...).title() — left to right, each returns a str")

# ─── C# → Python method map ────────────────────────────────────
print("""
─── C# → Python cheat sheet ───────────────────────────────
  Trim()          → .strip()          ToUpper()   → .upper()
  TrimStart()     → .lstrip()         ToLower()   → .lower()
  Substring(a,b)  → s[a:a+b]          IndexOf()   → .find()
  Replace()       → .replace()        Split()     → .split()
  string.Join()   → 'sep'.join(list)  StartsWith()→ .startswith()
  Contains()      → 'x' in s          PadLeft()   → .zfill()/.rjust()
""")
