for batch in range(1, 5):
    print(f"Preparing chai for batch #{batch}") # Output: Preparing chai for batch #1, then #2, then #3, then #4

"""
--- NOTES: `for` loops and the `range()` Function ---

1. Loop Boundaries with `range()`:
   - The `range(start, stop)` function generates numbers beginning at `start` and ending just before `stop`. 
   - In this code, `range(1, 5)` includes 1, 2, 3, and 4. It explicitly excludes the upper boundary (5).

2. Iterable vs. Iterator:
   - The `range()` object is an **iterable**, not an iterator. 
   - This means you can loop over a `range()` object multiple times without it becoming "exhausted". (If it were a pure iterator, it would be consumed after the first pass).
   - Under the hood, Python's `for` loop automatically calls the `iter()` function on the iterable to get an iterator, and then calls `next()` on it until a `StopIteration` exception is raised.

3. Latest Python Enhancements (Python 3.11 & 3.12):
   - **Faster Loops**: Python 3.11 introduced "Zero-cost exceptions". Because `for` loops in Python terminate by catching a `StopIteration` exception silently, this architectural change made `for` loops notably faster than in Python 3.10 and below.
   - **Adaptive Interpreter**: Python 3.11+ actively specializes bytecode during runtime. If a `for` loop is repeatedly iterating over the same type (like integers in a `range`), Python optimizes the underlying C code for that specific data type, resulting in up to a 10-60% overall speedup.
   - **`strict=True` in `zip()` (Python 3.10+)**: While not shown in this snippet, when looping over multiple iterables simultaneously using `zip()`, Python 3.10 added a `strict=True` parameter to throw an error if the iterables are of unequal length, which catches a lot of common loop bugs.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Is `range()` an iterator or an iterable? How can you prove it?
A1: `range()` returns an iterable, not an iterator. You can prove this by creating a range object (e.g., `r = range(5)`) and iterating over it twice. It will work both times. Furthermore, calling `next(r)` raises a `TypeError: 'range' object is not an iterator`.

Q2: How would you make this loop iterate backwards from 5 down to 1?
A2: You can provide a negative step value to the `range()` function. The syntax would be `range(5, 0, -1)`. Note that the `stop` boundary is still exclusive, meaning it will stop at 1, not 0.

Q3: What happens if you run `for i in range(5, 1):` (where start is greater than stop without a step)?
A3: The loop will not execute at all. `range(5, 1)` yields an empty range object because the default step is `+1`. Since it cannot reach 1 by adding 1 to 5, it immediately stops without raising an error.

Q4: Can you access elements in a `range` object via indexing without converting it to a list?
A4: Yes! `range` objects support indexing and slicing. You can safely do `r = range(10, 20)` and access `r[0]` to get `10`, or `r[-1]` to get `19`, because `range` implements the sequence protocol in Python.
"""