# Learning Python 🐍

Python fundamentals explained for an experienced **C# developer**, aimed at
writing Python for **Azure AI Foundry** and preparing for the
**Microsoft AI-901** certification.

Every file is runnable and self-contained — no test framework, no setup beyond
a virtual environment. Read a chapter, run it, change it, run it again.

## Setup (once)

The repo needs **Python 3.10+**. The macOS system `python3` is 3.9 and
**cannot run this repo** (`08_conditionals.py` uses `match`/`case`).

```bash
cd Learning-Python

# create the environment (uv is much faster; python3 -m venv also works)
uv venv --python 3.12 .venv

# activate it — or skip this and call .venv/bin/python directly
source .venv/bin/activate

# install what the chapters use
pip install ipython
```

## Progress

| Status | File | Concepts |
| -------- | ------ | ---------- |
| 📋 | `00_introduction.py` | Why Python, Python 2 vs Python 3, checking your interpreter |
| 📋 | `01_numbers.py` | int (unbounded), float, complex, `Decimal`, `/` vs `//`, rounding, literals, number formatting |
| 📋 | `02_variables_basics.py` | Assignment, dynamic typing, naming rules & PEP 8, multiple assignment, swap, `None`, `del`, names-are-references |
| 📋 | `03_strings_basics.py` | Quotes, escapes, raw & multi-line strings, concat, f-strings, `len()`, indexing, immutability |
| 📋 | `04_strings_deep_dive.py` | Slicing, built-in functions, `repr` vs `str`, Unicode & encode/decode, identity vs equality, format specs |
| 📋 | `05_methods.py` | Functions vs methods, `dir()`/`help()`, case/whitespace/search/split/join/replace/predicate/padding methods, chaining |
| 📋 | `06_operators.py` | Arithmetic (`**`, `//`), comparison, chained comparisons, logical (`and`/`or`/`not`), identity (`is`), membership (`in`) |
| 📋 | `07_booleans.py` | `True`/`False`, bool as an int, truthiness, `and`/`or` returning operands, short-circuit, `any()`/`all()` |
| 📋 | `08_conditionals.py` | `if`/`elif`/`else`, indentation as syntax, nesting, truthiness, `pass`, common errors, `match`/`case` |
| 📋 | `09_complex_logic.py` | Ternary, chained comparisons, `in`/`is`, walrus `:=`, guard clauses, precedence, pitfalls |
| 📋 | `10_loops.py` | `for`/`in`, `range()`, `enumerate()`, `zip()`, `while`, `break`/`continue`, `for`-`else` |
| 📋 | `11_lists.py` | Lists, indexing, slicing, `.append()`/`.insert()`/`.remove()`/`.pop()`, sorting, comprehensions |
| 📋 | `12_dicts.py` | Dict CRUD, `.get()`, `.items()`, `in` operator (vs `Dictionary<TKey,TValue>`) |
| 📋 | `13_functions.py` | `def`, default args, multiple returns, `*args`/`**kwargs`, lambdas, functions as values |
| 📋 | `14_scope.py` | No block scope, LEGB resolution, `global`/`nonlocal`, closures, the mutable-default trap, comprehension scope |
| 📋 | `15_sets_tuples.py` | Tuples (vs C# `ValueTuple`), unpacking, hashability, `namedtuple`; sets (vs `HashSet<T>`), dedup, O(1) membership, set algebra, `frozenset` |
| 📋 | `16_errors.py` | `try`/`except`/`else`/`finally`, the exception hierarchy, `raise ... from`, custom exceptions, EAFP vs LBYL, `with`, retry with backoff |
| 📋 | `17_modules.py` | Import forms, imports execute once, packages, `__name__ == "__main__"`, `sys.path`, virtual environments, stdlib tour, `pip` |
| 📋 | `18_oop.py` | Classes, `self`, instance vs class attributes, `@classmethod`/`@staticmethod`, `@property`, inheritance, dunders, `@dataclass`, ABC, composition |

`✅` = studied · `📋` = not studied yet

`01-fundamentals/helpers/` is a small package used **by** `17_modules.py` to
demonstrate real imports — it is not a chapter and is not part of the sequence.

## Notes on ordering

The sequence is pedagogical, not the order the topics were listed:

- **Operators before booleans** — comparison operators are what produce
  booleans, so it reads better to meet them first.
- **Booleans before conditionals, conditionals before complex logic** — `if`
  needs truthiness; the deep dive assumes the basics feel natural.
- **Loops before collections** — `range()`, `enumerate()` and `zip()` only need
  strings and ranges, and you then arrive at lists and dicts already knowing
  how to walk them.
- **Functions before scope** — scope is only interesting once there are
  functions to have one.
- **Scope before sets & tuples** — the immutable-default-argument trap and
  comprehension scoping in `14` set up the immutability discussion in `15`.
- **Errors after collections** — `KeyError`/`IndexError` are the exceptions you
  have actually met by then.
- **Modules then OOP last** — OOP is the capstone that pulls together scope,
  errors, and modules into one class.

## Running the examples

```bash
# from the repo root — use the venv interpreter
.venv/bin/python 01-fundamentals/00_introduction.py

# with the venv activated, plain python works too
python 01-fundamentals/00_introduction.py

# run every chapter in order
for f in 01-fundamentals/*.py; do echo "--- $f"; .venv/bin/python "$f" || break; done

# the helpers package has its own self-test
.venv/bin/python 01-fundamentals/helpers/text_tools.py
```

`16_errors.py` deliberately raises exceptions inside `try` blocks — the output
is full of error text, and that is the point. Exit code stays 0.

## Roadmap

Part 1 (this folder) is Python fundamentals. Still to come:

- **Part 2 — Python for AI development**: type hints, async/await, HTTP/REST
  with `requests`/`httpx`, `.env` and environment variables, secrets handling,
  parsing JSON API responses, SDK ergonomics.
- **Part 3 — Azure-oriented Python**: `azure-identity` (`DefaultAzureCredential`),
  Azure AI Foundry / Azure OpenAI client patterns, chat completions, embeddings
  and search, streaming, error handling and retries against real service limits.
- **Part 4 — Practice**: exercises, AI-focused worked examples, debugging drills,
  mini-projects, certification-style review questions.
- **Part 5 — Crash course**: a 3-hour revision pass over everything above,
  checked against the current official AI-901 objectives.
