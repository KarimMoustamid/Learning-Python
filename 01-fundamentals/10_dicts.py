"""
Python Dictionaries 📖
- Like Dictionary<TKey, TValue> in C#, but with cleaner syntax
- Keys must be hashable (strings, numbers, tuples — just like C#)
- Python 3.7+: dicts preserve insertion order (like OrderedDictionary in C#)
"""

# ─── Creating dicts ──────────────────────────────────────────
# C#: new Dictionary<string, int> { { "apple", 5 }, { "banana", 3 } }
fruits = {
    "apple":  5,
    "banana": 3,
    "cherry": 8,
}
print(f"Fruits: {fruits}")
print(f"Type:   {type(fruits).__name__}")

# ─── Accessing values ────────────────────────────────────────
print(f"\nApples:  {fruits['apple']}")        # direct key access (⚠ throws KeyError if missing)
print(f"Bananas: {fruits.get('banana')}")     # .get() — returns None if missing
print(f"Mangos:  {fruits.get('mango', 0)}")   # .get() with default — returns 0 if missing

# ─── Adding / Updating ──────────────────────────────────────
fruits["mango"] = 12                  # add new key
fruits["apple"] = 6                   # update existing
print(f"\nAfter updates: {fruits}")

# ─── Removing ────────────────────────────────────────────────
del fruits["banana"]                  # delete a key (like .Remove() in C#)
popped = fruits.pop("cherry")         # pop returns the value, then removes
print(f"After del banana, pop cherry: {fruits}  (cherry was {popped})")

# ─── Iteration ───────────────────────────────────────────────
print("\n── Iterating ──")
for key in fruits:                    # keys by default
    print(f"  {key}: {fruits[key]}")

for key, val in fruits.items():       # .items() → (key, value) pairs like C# foreach
    print(f"  {key.title()} x{val}")

# ─── Check if key exists ────────────────────────────────────
# C#: if (dict.ContainsKey("apple")) ...
if "apple" in fruits:
    print(f"\nHas apple ✓  (in is the idiomatic way)")

# ─── Practical example ───────────────────────────────────────
# C#: var lookup = users.ToDictionary(u => u.Id);
users_lookup = {
    "karim":  {"role": "dev", "years": 8},
    "maria":  {"role": "architect", "years": 12},
    "ahmed":  {"role": "manager", "years": 6},
}

user = users_lookup.get("karim")
print(f"\nKarim: {user}")
print(f"Role:  {user['role']}")
