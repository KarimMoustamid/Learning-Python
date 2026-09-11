"""
Python Strings — Deep Dive & Built-ins 🧵🔬
- Slicing: the most powerful thing you get for free
- Built-in functions that operate on strings
- repr vs str, Unicode, encoding
- Advanced f-string formatting
"""

from datetime import datetime

# ─── Slicing in full ───────────────────────────────────────────
# s[start:stop:step] — stop is EXCLUSIVE. Any part can be omitted.
# C#: Substring() + manual math, or Span<T>. Python does it in one expression.
s = "abcdefghij"          # indices 0..9
print("─── Slicing ───────────────────────────────────────────────")
print(f"  s              = {s!r}")
print(f"  s[2:5]         = {s[2:5]!r}     # index 2,3,4  (5 excluded)")
print(f"  s[:3]          = {s[:3]!r}     # from the start")
print(f"  s[7:]          = {s[7:]!r}     # to the end")
print(f"  s[:]           = {s[:]!r}     # a full COPY")
print(f"  s[-3:]         = {s[-3:]!r}     # last 3")
print(f"  s[:-3]         = {s[:-3]!r}     # everything but the last 3")
print(f"  s[::2]         = {s[::2]!r}     # every 2nd char")
print(f"  s[1::2]        = {s[1::2]!r}     # every 2nd, starting at 1")
print(f"  s[::-1]        = {s[::-1]!r}     # ⭐ REVERSED (the idiomatic trick)")
print(f"  s[8:2:-1]      = {s[8:2:-1]!r}     # backwards from 8 down to 3")

# Slices CLAMP instead of throwing — very different from C#
print(f"\n  s[100]         → IndexError (out of range)")
print(f"  s[5:100]       = {s[5:100]!r}   ← ✅ slice just stops at the end, no error")
print(f"  s[100:]        = {s[100:]!r}        ← empty, still no error")

# ─── Iterating ─────────────────────────────────────────────────
# A string is a sequence — loop over it directly (C#: foreach (char c in s))
print("\n─── Iterating ─────────────────────────────────────────────")
print("  for ch in 'Python':        ", end="")
for ch in "Python":
    print(ch, end=" ")
print()

print("  enumerate('abc'):          ", end="")
for i, ch in enumerate("abc"):
    print(f"{i}:{ch}", end=" ")
print()

print(f"  reversed('abc')            → {''.join(reversed('abc'))!r}")
print(f"  list('abc')                → {list('abc')}   # str → list of chars")

# ─── Built-in functions that work on strings ───────────────────
print("\n─── Built-ins ─────────────────────────────────────────────")
word = "Python"
print(f"  len('{word}')          = {len(word)}")
print(f"  min('{word}')          = {min(word)!r}      ← lowest code point")
print(f"  max('{word}')          = {max(word)!r}      ← highest code point")
print(f"  sorted('cba')       = {sorted('cba')}      # returns a LIST")
print(f"  ''.join(sorted('cba')) = {''.join(sorted('cba'))!r}   ← back to str")
print(f"  ord('A')            = {ord('A')}      # char → code point   (C#: (int)'A')")
print(f"  chr(65)             = {chr(65)!r}      # code point → char   (C#: (char)65)")
print(f"  str(42)             = {str(42)!r}     # same as 42.ToString()")
print(f"  repr('a')           = {repr('a')}    # debug representation")
print(f"  ascii('é')          = {ascii('é')!r}    # escape non-ASCII")
print(f"  hash('abc')         = {hash('abc')}   # dict key ingredient")
print(f"  bool('') / bool('x')= {bool('')} / {bool('x')}   ← '' is falsy")
print(f"  any('a') / all('a') = {any('a')} / {all('a')}")
print(f"  zip('abc', '123')   → {list(zip('abc', '123'))}   # pairs up chars")

# ─── repr vs str ───────────────────────────────────────────────
# str()  → human-readable, for the user
# repr() → unambiguous, for the developer (shows quotes and escapes)
# C#: str is ToString(); repr is closer to what the debugger shows you.
print("\n─── repr vs str ───────────────────────────────────────────")
tricky = "tab\there\nnewline"
print(f"  print(str(tricky))   → {tricky}")
print(f"  print(repr(tricky))  → {repr(tricky)}   ← escapes visible")
print(f"  In an f-string: {{x!r}} gives repr → {tricky!r}")

# ─── Unicode & encoding ────────────────────────────────────────
# Python 3 str = TEXT (unicode code points). bytes = raw DATA.
# C#: string is UTF-16 under the hood, and byte[] is a separate thing.
# Text -> bytes is .encode(); bytes -> text is .decode().
text = "héllo"
encoded = text.encode("utf-8")
print("\n─── Unicode & encoding ────────────────────────────────────")
print(f"  text                = {text!r}  (a str)")
print(f"  text.encode('utf-8')= {encoded}  (bytes!)")
print(f"  bytes.decode()      = {encoded.decode('utf-8')!r}  (back to str)")
print(f"  len(text)           = {len(text)}      ← characters")
print(f"  len(encoded)        = {len(encoded)}      ← BYTES (é takes 2 in UTF-8)")
print(f"  ord('é')            = {ord('é')}    ← code point")
print(f"  chr({ord('é')})              = {chr(ord('é'))!r}")
print(f"  b'abc' is bytes     → {isinstance(b'abc', bytes)}")
print("  ⚠ Never mix str and bytes — TypeError: can only concatenate str to str")

# ─── Comparison & identity ─────────────────────────────────────
print("\n─── Comparison & identity ─────────────────────────────────")
print(f"  'abc' == 'abc'   → {'abc' == 'abc'}     # value equality")
print(f"  'abc' < 'abd'    → {'abc' < 'abd'}     # lexicographic")
print(f"  sorted(['b','a','C']) → {sorted(['b', 'a', 'C'])}   ← 'C' first (uppercase)")
print(f"  sorted(..., key=str.lower) → {sorted(['b', 'a', 'C'], key=str.lower)}   ← case-insensitive")
print("  ⚠ NEVER use 'is' to compare strings — it compares identity, not content.")

a = "hello"
b = "hello"
c = "".join(["hel", "lo"])
print(f"\n  a = 'hello'; b = 'hello'")
print(f"  a is b → {a is b}   ← literals got interned (an implementation detail!)")
print(f"  a is c → {a is c}   ← same text, different object. Don't rely on 'is' here.")
print(f"  a == c → {a == c}   ← ✅ this is what you always want")

# ─── Advanced f-string formatting ──────────────────────────────
# [[fill]align][sign][#][0][width][,][.precision][type]
price, ratio, code = 1234.5678, 0.8712, 255
width = 12
print("\n─── f-string format specs ─────────────────────────────────")
print(f"  {{:>12}}      {price:>12}")
print(f"  {{:<12}}|     {price:<12}|")
print(f"  {{:^12}}|     {price:^12}|")
print(f"  {{:*^12}}|     {price:*^12}|     ← custom fill character")
print(f"  {{:,.2f}}     {price:,.2f}   # thousands + precision")
print(f"  {{:.2%}}      {ratio:.2%}")
print(f"  {{:+.1f}}     {price:+.1f}   # forced sign")
print(f"  {{:08.2f}}    {price:08.2f}")
print(f"  {{:x}} / {{:X}} / {{:o}} / {{:b}}   {code:x} / {code:X} / {code:o} / {code:b}")
print(f"  {{:{width}.2f}}  {price:{width}.2f}   ← nested field for width (variable!)")
print(f"  {{:e}}        {price:e}   # scientific")
print(f"  {{:g}}        {price:g}   # shortest form")

# Dates format directly inside f-strings — no ToString("yyyy-MM-dd") needed
now = datetime(2026, 9, 11, 14, 30, 5)
print(f"\n  {{:%Y-%m-%d}}        {now:%Y-%m-%d}")
print(f"  {{:%d %b %Y}}        {now:%d %b %Y}")
print(f"  {{:%H:%M:%S}}        {now:%H:%M:%S}")
print(f"  {{:%A, %B %d}}       {now:%A, %B %d}")

# ─── Performance note ──────────────────────────────────────────
print("""
─── Performance ───────────────────────────────────────────
  Strings are immutable, so every operation builds a NEW string.

  ❌ result = ""                          # O(n²) — copies the whole
     for w in words:                      #      string every iteration
         result += w

  ✅ result = "".join(words)              # O(n) — one allocation
     # C# equivalent: string.Join() or a StringBuilder
""")
