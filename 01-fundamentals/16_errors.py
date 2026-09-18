"""
Python Errors & Exceptions ⚠️
- try / except / else / finally — C# try/catch/finally with a twist
- Exceptions are THE error channel in Python. There is no TryParse / TryGetValue
  culture: you attempt the operation and catch the failure.
- EAFP — "Easier to Ask Forgiveness than Permission"
- Written for an experienced C# developer
- Run it:  python 01-fundamentals/16_errors.py
"""

# ─── try / except — the basics ───────────────────────────────
# C#:  try { ... } catch (FormatException ex) { ... }
print("─── try / except ─────────────────────────────────────────")

try:
    age = int("not a number")
except ValueError as err:                 # `as err` — like `catch (E ex)` in C#
    print(f"  int('not a number') → {type(err).__name__}: {err}")

try:
    numbers = [1, 2, 3]
    print(numbers[99])
except IndexError as err:
    print(f"  numbers[99]         → {type(err).__name__}: {err}")

# ─── One block, several handlers ─────────────────────────────
# C#: multiple `catch` clauses, most-specific first. Same idea here,
# but the first matching block wins — Python does not reorder for you.
print("\n─── Multiple handlers ────────────────────────────────────")


def parse_ratio(text):
    try:
        return 100 / int(text)
    except (ValueError, ZeroDivisionError) as err:      # tuple = one handler, two types
        return f"{type(err).__name__}: {err}"


print(f"  parse_ratio('4')     → {parse_ratio('4')}")
print(f"  parse_ratio('abc')   → {parse_ratio('abc')}")
print(f"  parse_ratio('0')     → {parse_ratio('0')}")

# ─── ⚠ The bare except anti-pattern ──────────────────────────
print("\n─── ⚠ Never write a bare `except:` ───────────────────────")
print("""
  except:            ← catches EVERYTHING, including KeyboardInterrupt (Ctrl-C)
                       and SystemExit. You can no longer stop the program.
  except Exception:  ← catches application errors only. Still usually too broad.

  The right move is to name the exception you can actually handle:
      except ValueError:
      except (TimeoutError, ConnectionError):

  If you must catch broadly, at least log it and re-raise:
      except Exception:
          logger.exception("unexpected failure in fetch_embeddings")
          raise
""")

# ─── else and finally ────────────────────────────────────────
# `else` runs only when NO exception occurred — handy to keep the try block
# as narrow as possible so you don't accidentally swallow errors from
# follow-up work. C# has no equivalent.
# `finally` is exactly C# finally / the body of a `using` block.
print("─── else and finally ─────────────────────────────────────")


def read_setting(raw):
    try:
        value = int(raw)                   # try: only the risky line
    except ValueError:
        print(f"    '{raw}' invalid → falling back")
        return 0
    else:
        print(f"    '{raw}' parsed fine → {value}")    # runs only on success
        return value
    finally:
        print(f"    finally always runs (raw={raw!r})")  # always, even after return


print("  read_setting('42'):")
print(f"  returned {read_setting('42')}\n")
print("  read_setting('oops'):")
print(f"  returned {read_setting('oops')}")

# ─── The exception hierarchy ─────────────────────────────────
print("\n─── The hierarchy (know the top of it) ───────────────────")
print("""
  BaseException
  ├── SystemExit            ← raised by sys.exit()
  ├── KeyboardInterrupt     ← Ctrl-C        (never catch these two blindly)
  └── Exception             ← everything you should care about
      ├── ArithmeticError → ZeroDivisionError
      ├── LookupError     → KeyError, IndexError
      ├── ValueError            right type, wrong value   ('abc' as int)
      ├── TypeError             wrong type entirely       (1 + 'a')
      ├── AttributeError        no such method/attribute
      ├── NameError → UnboundLocalError
      ├── OSError → FileNotFoundError, PermissionError, ConnectionError
      ├── TimeoutError
      └── RuntimeError → RecursionError, NotImplementedError
""")

# Catching a PARENT catches its children — useful, and a footgun
print("─── Catching a parent catches its children ───────────────")
for bad in ("abc", 0, None):
    try:
        result = 10 / bad
    except Exception as err:               # ValueError, ZeroDivisionError, TypeError
        print(f"  10 / {bad!r:<6} → {type(err).__name__}")

# ─── Raising ─────────────────────────────────────────────────
print("\n─── Raising ──────────────────────────────────────────────")


def set_temperature(value):
    """Validate like an SDK would — raise early, raise specifically."""
    if not isinstance(value, (int, float)):
        raise TypeError(f"temperature must be numeric, got {type(value).__name__}")
    if not 0 <= value <= 2:
        raise ValueError(f"temperature must be between 0 and 2, got {value}")
    return value


print(f"  set_temperature(0.7)  → {set_temperature(0.7)}")

for bad in ("hot", 5):
    try:
        set_temperature(bad)
    except (TypeError, ValueError) as err:
        print(f"  set_temperature({bad!r}) → {type(err).__name__}: {err}")

# ─── Exception chaining — C# InnerException ──────────────────
# `raise X from Y` preserves the original as __cause__, exactly like
# `throw new X("...", innerException)`. Without it you lose the root cause.
print("\n─── raise ... from ... (C# InnerException) ───────────────")


def load_model_config(payload: dict):
    try:
        return {"model": payload["model"], "temp": float(payload["temperature"])}
    except (KeyError, ValueError) as err:
        raise RuntimeError("model config is invalid") from err   # keep the cause


try:
    load_model_config({"model": "gpt-4o", "temperature": "warm"})
except RuntimeError as err:
    print(f"  caught:   {type(err).__name__}: {err}")
    print(f"  __cause__: {type(err.__cause__).__name__}: {err.__cause__}")

# ─── Custom exception types ──────────────────────────────────
# C#: a class deriving from Exception. Python: subclass Exception (NOT
# BaseException). Give it a good __init__ and it doubles as a value object.
print("\n─── Custom exceptions ────────────────────────────────────")


class FoundryError(Exception):
    """Base class for anything this app raises on its own terms."""


class RateLimitError(FoundryError):
    """The service asked us to slow down."""

    def __init__(self, retry_after: int):
        super().__init__(f"rate limited — retry after {retry_after}s")
        self.retry_after = retry_after        # attach structured data


try:
    raise RateLimitError(retry_after=20)
except FoundryError as err:                   # catching the base catches the child
    print(f"  {type(err).__name__}: {err}")
    print(f"  structured field: err.retry_after = {err.retry_after}")

print("""
  Why a custom base class pays off: callers can write one line —
      except FoundryError:
  to handle everything your library raises, while still being able to catch
  RateLimitError specifically. That is how the Azure SDK is organised
  (azure.core.exceptions.HttpResponseError and friends).
""")

# ─── EAFP vs LBYL ────────────────────────────────────────────
# LBYL — Look Before You Leap  — the C# TryGetValue style
# EAFP — Easier to Ask Forgiveness than Permission — the Python style
print("─── EAFP vs LBYL ─────────────────────────────────────────")

config = {"model": "gpt-4o"}

# LBYL: check first, then act — two lookups, and a race in concurrent code
if "temperature" in config:
    lbyl = config["temperature"]
else:
    lbyl = 0.7

# EAFP: just try it — one lookup, no window between check and use
try:
    eafp = config["temperature"]
except KeyError:
    eafp = 0.7

print(f"  LBYL result: {lbyl}")
print(f"  EAFP result: {eafp}")
print("""
  For a plain dict the idiomatic answer is actually neither —
      config.get("temperature", 0.7)
  EAFP earns its place for files, network calls, and parsing, where checking
  first means a TOCTOU race or a doubled round trip.
""")

# ─── with — context managers, the try/finally replacement ────
print("─── `with`: deterministic cleanup (C# `using`) ───────────")

import tempfile
from pathlib import Path

# C#: using var f = File.CreateText(path);
# Python: with open(path, "w") as f:
with tempfile.TemporaryDirectory() as tmpdir:
    path = Path(tmpdir) / "notes.txt"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write("first line\n")
    print(f"  wrote {path.name}, closed automatically (even on exception)")

    with open(path, encoding="utf-8") as handle:
        print(f"  read back: {handle.read().strip()!r}")
print("  temp dir cleaned up on exiting the first `with` block")

# Rolling your own: implement __enter__ / __exit__ (full detail in 18_oop.py)
print("\n─── Rolling your own context manager ─────────────────────")

from contextlib import contextmanager


@contextmanager
def timed_log(label):
    print(f"    ▶ {label} started")
    try:
        yield "resource"                   # the body of the `with` runs here
    finally:
        print(f"    ■ {label} finished (cleanup always runs)")


with timed_log("call model") as resource:
    print(f"    ...doing work with {resource}...")

# ─── Practical: retry with backoff ───────────────────────────
# The single most reused pattern in cloud code — 429s and transient
# timeouts are normal, and every Azure SDK example contains a version of it.
print("\n─── Practical: retry with backoff ────────────────────────")

attempts = {"count": 0}


def flaky_call():
    """Fails twice, then succeeds — stands in for a network call."""
    attempts["count"] += 1
    if attempts["count"] < 3:
        raise RateLimitError(retry_after=attempts["count"])
    return {"status": "ok", "tokens": 128}


import time

result = None
for attempt in range(1, 6):
    try:
        result = flaky_call()
        print(f"  attempt {attempt}: success → {result}")
        break                                   # `for`-`else` would also work here
    except RateLimitError as err:
        wait = min(2 ** attempt, 10)            # exponential backoff, capped
        print(f"  attempt {attempt}: {err}  → sleeping {wait}s")
        time.sleep(0.02)                        # shortened so this file runs fast
else:
    print("  all attempts exhausted")

print("""
  ─── Summary ──────────────────────────────────────────────
  1. Name the exception you can handle. A bare `except:` is a bug.
  2. `else` = ran clean, `finally` = always.
  3. Catch a parent to catch its children — useful, but be deliberate.
  4. `raise ... from err` preserves the cause (C# InnerException).
  5. Subclass Exception (never BaseException) for your own error types.
  6. Prefer EAFP around IO and network; .get() for plain dicts.
  7. `with` replaces try/finally for anything that must be cleaned up.
  8. Retry with capped exponential backoff around every network call.
""")
