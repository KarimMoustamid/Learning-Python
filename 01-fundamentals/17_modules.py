"""
Python Modules & Packages 📚
- A module is one .py file. A package is a folder of them.
- `import` is the C# `using`, but it *runs* the file the first time
- The stdlib is enormous — know the dozen modules that matter for Azure work
- Written for an experienced C# developer
- Run it:  python 01-fundamentals/17_modules.py
"""

# ─── The import forms ────────────────────────────────────────
# C#:  using System.Text.Json;
import json                                  # 1. whole module — best default

# C#: static import of specific members
from pathlib import Path                     # 2. one name out of the module

# C#: using JsonAlias = System.Text.Json;  →  import ... as ...
import datetime as dt                        # 3. alias — used HARD by the ecosystem
                                             #    (import pandas as pd, numpy as np)

from urllib.parse import urlparse as parse_url   # 4. aliased single name

print("─── Import forms ─────────────────────────────────────────")
print(f"  json.dumps(...)        → {json.dumps({'a': 1})}")
print(f"  Path('x/y').name       → {Path('x/y').name}")
print(f"  dt.date.today()        → {dt.date.today()}")
print(f"  parse_url(host)        → {parse_url('https://ai.azure.com/x').netloc}")

print("""
  House rules:
    import module                     ← prefer this; the reader always knows
                                        where a name came from
    from module import name           ← fine for very common names (Path)
    from module import *              ← never. It dumps unknown names into your
                                        namespace and hides where things live
""")

# ─── Importing is executing ──────────────────────────────────
# A module's top-level code runs ONCE, the first time it is imported.
# Every later `import` gets the cached object from sys.modules — so the
# second import is nearly free, and you always get the SAME object.
print("─── An import runs the file top to bottom ────────────────")

import sys

print(f"  json imported at the top → cached in sys.modules: {'json' in sys.modules}")

import json as json_again                        # already imported → hands back the cache

print(f"  json is json_again       → {json is json_again}")
print("  That is why a module with print side effects is a bad module:")
print("  the side effects fire on the first import, from somewhere you didn't expect.")

# ─── Your own module: the helpers/ package ───────────────────
# Look at the folder next to this file:
#   01-fundamentals/helpers/__init__.py     ← marks it a PACKAGE
#   01-fundamentals/helpers/text_tools.py   ← a module inside the package
#
# When you run `python 01-fundamentals/17_modules.py`, Python puts the
# SCRIPT'S directory (01-fundamentals/) on sys.path — so `helpers` is
# importable with no path fiddling.

print("\n─── Importing your own package ───────────────────────────")

from helpers import slugify, word_count          # re-exported by helpers/__init__.py
from helpers.text_tools import truncate          # reaching into the module directly

print(f"  slugify('Hello, Azure Foundry!') → {slugify('Hello, Azure Foundry!')}")
print(f"  word_count('a b c d')            → {word_count('a b c d')}")
print(f"  truncate('long sentence here')   → {truncate('long sentence here', 10)}")

import helpers

print(f"  helpers.__version__ = {helpers.__version__}")
print(f"  helpers.__all__     = {helpers.__all__}")

# ─── __name__ == "__main__" — the entry point guard ──────────
# C#: static void Main() — one entry point per assembly.
# Python: no entry point. EVERY .py file can be run or imported, so the file
# has to ask "am I the program, or am I a library?"
print("\n─── if __name__ == '__main__' ────────────────────────────")
print(f"  running as a script → __name__ == {__name__!r}")
print(f"  if imported        → __name__ == '17_modules'")
print("""
  Then in your file:

      def main():
          ...

      if __name__ == "__main__":      # only when run directly
          main()

  This is what makes a file usable as BOTH a script and an import.
  helpers/text_tools.py does exactly this — run it and its self-test fires:
      python 01-fundamentals/helpers/text_tools.py
""")

# ─── sys.path — how Python finds modules ─────────────────────
# C#: the compiler resolves references at build time.
# Python: the interpreter searches sys.path at runtime, in order.
print("─── sys.path: where Python looks ─────────────────────────")

for index, entry in enumerate(sys.path[:4]):
    shown = entry if entry else "(current directory)"
    if len(shown) > 62:
        shown = "..." + shown[-59:]
    print(f"  [{index}] {shown}")
print("  ...")
print("""
  Order: the script's own directory first, then PYTHONPATH, then the
  standard library, then site-packages (your installed packages).

  ⚠ Two files named json.py or a folder named helpers/ in your project can
    shadow the real thing. That failure looks like "module has no attribute
    dumps" and confuses people for hours. Name collisions are the classic
    source of mysterious ImportError.
""")

# ─── Where am I running from? ────────────────────────────────
print("─── Know your interpreter ────────────────────────────────")
print(f"  sys.executable    {sys.executable}")
print(f"  sys.version       {sys.version.split()[0]}")
print(f"  site-packages     {sys.prefix}")
print("""
  If this points at /usr/bin/python3 you are on the macOS system Python —
  wrong interpreter, wrong packages. That is what a virtual environment fixes.
""")

# ─── Virtual environments ────────────────────────────────────
print("─── Virtual environments ─────────────────────────────────")
print("""
  A venv is a private site-packages folder per project. C# has this built in
  (project-level NuGet restore); Python makes you opt in.

      # create it once, from the project root
      python3 -m venv .venv
      # or, much faster, with uv:
      uv venv --python 3.12 .venv

      # activate it (per shell session)
      source .venv/bin/activate          # macOS / Linux
      .venv\\Scripts\\activate             # Windows PowerShell

      # then install into it
      pip install ipython
      pip freeze > requirements.txt      # the lockfile, like packages.lock.json

  Without activating, call the interpreter by path — always unambiguous:
      .venv/bin/python 01-fundamentals/17_modules.py

  ⚠ Never `pip install` into the system Python. On macOS the system Python is
    reserved for the OS; installing into it breaks tools and needs sudo.
""")

# ─── The stdlib modules that matter for Azure AI work ────────
print("─── Stdlib worth memorising ──────────────────────────────")

stdlib = [
    ("json",        "parse/serialise API payloads — you will use this daily"),
    ("os",          "environment variables: os.environ['AZURE_OPENAI_KEY']"),
    ("pathlib",     "Path objects instead of string concatenation"),
    ("datetime",    "timestamps, timezones, duration arithmetic"),
    ("logging",     "real logging; print() is not logging"),
    ("typing",      "type hints: list[str], dict[str, int], Optional[...]"),
    ("dataclasses", "@dataclass for plain data holders — see 18_oop.py"),
    ("itertools",   "chain, groupby, islice — lazy sequence building blocks"),
    ("collections", "defaultdict, Counter, deque, namedtuple"),
    ("functools",   "lru_cache, partial, wraps (for decorators)"),
    ("asyncio",     "async/await for concurrent API calls"),
    ("re",          "regex"),
    ("uuid",        "generate ids: str(uuid.uuid4())"),
    ("statistics",  "mean, median, stdev — quick metrics without numpy"),
]
print(f"  {'module':<14} {'why you care'}")
print(f"  {'-' * 14} {'-' * 46}")
for module, why in stdlib:
    print(f"  {module:<14} {why}")

# Prove one works right now
import os

os.environ["DEMO_FOUNDRY_ENDPOINT"] = "https://demo.services.ai.azure.com"
print(f"\n  os.environ demo → {os.environ.get('DEMO_FOUNDRY_ENDPOINT')}")

# ─── Third-party packages ────────────────────────────────────
print("\n─── Third-party packages (pip install) ───────────────────")

try:
    from importlib.metadata import version

    installed = [(name, version(name)) for name in ("ipython", "traitlets")]
    for name, ver in installed:
        print(f"  {name:<12} {ver}")
except Exception as err:
    print(f"  could not read package metadata: {err}")

print("""
  The Azure SDK is a set of wheels you install, not one blob:

      pip install azure-ai-projects azure-identity openai
      pip install azure-ai-inference azure-search-documents

  Each package versions independently, so pin them in requirements.txt.
""")

print("""
  ─── Summary ──────────────────────────────────────────────
  1. `import module` by default; `from module import name` for very common
     names; never `from module import *`.
  2. An import executes the file once and caches it in sys.modules.
  3. __name__ == "__main__" is how one file is both script and library.
  4. sys.path is searched at runtime — name collisions shadow real modules.
  5. One venv per project. Never install into the system Python.
  6. json, os, pathlib, datetime, logging, typing are the daily drivers.
  7. Print sys.executable when anything about a package is confusing.
""")
