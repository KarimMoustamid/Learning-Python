"""
Python Lists 📋
- Like List<T> in C#, but: heterogeneous, dynamic, and slicing works on them too
- Zero-indexed, mutable
- Can hold mixed types in the same list
"""

# ─── Creating lists ───────────────────────────────────────────
numbers = [10, 20, 30, 40, 50]                    # like new List<int> { 10, 20, ... }
mixed = [1, "hello", 3.14, True, None]            # C# would need List<object?>
empty = []                                        # or list()

print(f"numbers: {numbers}")
print(f"mixed:   {mixed}")
print(f"empty:   {empty}")

# ─── Indexing & Slicing (same syntax as strings!) ─────────────
print(f"\nFirst:        {numbers[0]}")            # 10
print(f"Last:         {numbers[-1]}")            # 50 (negative = from end)
print(f"First 3:      {numbers[:3]}")            # [10, 20, 30]
print(f"Last 3:       {numbers[-3:]}")           # [30, 40, 50]
print(f"Every other:  {numbers[::2]}")           # [10, 30, 50]

# ─── Mutating (adding / removing) ────────────────────────────
nums = [1, 2, 3]
nums.append(4)                          # like .Add() in C#
nums.insert(0, 0)                       # insert at position 0
print(f"\nAfter append/insert: {nums}")

nums.remove(2)                          # removes FIRST occurrence of value 2
popped = nums.pop()                     # removes and returns LAST element
print(f"After remove(2) & pop(): {nums}  (popped={popped})")

# ─── Sorting ─────────────────────────────────────────────────
scores = [88, 42, 99, 73, 61]
scores.sort()                           # in-place — modifies the list
print(f"\nSorted scores: {scores}")
print(f"Reversed:      {list(reversed(scores))}")  # reversed() returns an iterator

# ─── Comprehensions (C# .Select() equivalent) ────────────────
# C#: numbers.Select(x => x * x).ToList()
squares = [x * x for x in range(1, 6)]
print(f"\nSquares 1-5: {squares}")

# With a filter (C#: .Where(x => x % 2 == 0).Select(...).ToList())
evens = [x for x in range(10) if x % 2 == 0]
print(f"Evens 0-9:   {evens}")
