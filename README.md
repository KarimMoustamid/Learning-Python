# Learning Python 🐍

Python fundamentals from an experienced C# developer's perspective.
Every file is runnable and self-contained:

```bash
python 01-fundamentals/01_numbers.py
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
| 📋 | `06_booleans.py` | `True`/`False`, bool as an int, truthiness, `and`/`or` returning operands, short-circuit, `any()`/`all()` |
| 📋 | `07_conditionals_basics.py` | `if`/`elif`/`else`, indentation as syntax, nesting, truthiness, `pass`, common errors |
| 📋 | `08_conditionals_deep_dive.py` | Ternary, chained comparisons, `in`/`is`, `match`/`case`, walrus `:=`, guard clauses, precedence, pitfalls |
| 📋 | `09_lists.py` | Lists, indexing, slicing, `.append()`/`.insert()`/`.remove()`/`.pop()`, sorting, comprehensions |
| 📋 | `10_dicts.py` | Dict CRUD, `.get()`, `.items()`, `in` operator (vs `Dictionary<TKey,TValue>`) |
| 📋 | `11_loops.py` | `for`/`in`, `range()`, `enumerate()`, `zip()`, `while`, `break`/`continue`, `for`-`else` |
| 📋 | `12_functions.py` | `def`, default args, multiple returns, `*args`/`**kwargs`, lambdas, functions as values |
| 📋 | `13_operators.py` | Arithmetic (`**`, `//`), comparison, chained comparisons, logical (`and`/`or`/`not`), identity (`is`), membership (`in`) |

`✅` = studied · `📋` = not studied yet

## Notes on ordering

- `00` and `01`–`08` are the numbered study sequence.
- `09`–`13` are earlier drafts of topics not yet placed in the sequence — lists, dicts,
  loops, functions, operators. Renumber them freely as the track takes shape.

## Running the examples

```bash
# From the repo root
python 01-fundamentals/00_introduction.py

# Run every file in order
for f in 01-fundamentals/*.py; do echo "--- $f"; python "$f"; done

# Check which Python you're on (Windows also has the py launcher)
python --version
py -3 --version
```

Requires Python 3.10+ (section `08` uses `match`/`case`).
