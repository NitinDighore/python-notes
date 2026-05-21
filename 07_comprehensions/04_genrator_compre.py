daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(sale for sale in daily_sales if sale > 5)

print(total_cups) # Output: 61

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Finding the first match instantly (Short-circuiting)
print("\n1. Short-circuiting with next():")
# Unlike a list comprehension which processes the entire list, next() on a generator stops the exact millisecond it finds a match!
first_huge_sale = next((sale for sale in daily_sales if sale > 10), "No huge sales")
print(f"First huge sale: {first_huge_sale}") # Output: First huge sale: 12

# Trick 2: Memory efficient boolean checks
print("\n2. any() and all() with generators:")
# Just like next(), any() and all() evaluate lazily, saving massive amounts of time on large datasets
has_single_digit = any(sale < 10 for sale in daily_sales)
all_positive = all(sale > 0 for sale in daily_sales)
print(f"Has single digit: {has_single_digit}, All positive: {all_positive}") # Output: Has single digit: True, All positive: True

# Trick 3: Generator Exhaustion (The "One-Time Use" Trap)
print("\n3. The Generator Exhaustion Trap:")
gen = (sale for sale in daily_sales if sale == 15)
print(f"First iteration list: {list(gen)}") # Output: First iteration list: [15]
print(f"Second iteration list: {list(gen)}") # Output: Second iteration list: [] (It's empty! Generators can only be consumed ONCE)

# Trick 4: Chaining Generators (Pipelines)
print("\n4. Chaining Generators for pipelines:")
# You can chain multiple generators together without creating intermediate lists in memory
squared_sales = (sale ** 2 for sale in daily_sales)
str_sales = (f"Sale: {sq}" for sq in squared_sales if sq > 100)
print(f"Chained output: {next(str_sales)}") # Output: Chained output: Sale: 144

# Trick 5: Formatting Strings from iterables
print("\n5. Joining strings lazily:")
names = ["Aman", "Zane", "Raj"]
# str.join() takes an iterable. Using a generator expression prevents allocating a temporary list
joined_names = ", ".join(name.upper() for name in names)
print(f"Joined Names: {joined_names}") # Output: Joined Names: AMAN, ZANE, RAJ

"""
--- NOTES: Generator Expressions ---

1. What are Generator Expressions?
   - They are a high-performance, memory-efficient alternative to list comprehensions.
   - Syntax: `(expression for item in iterable if condition)` (Notice the parentheses `()` instead of brackets `[]`).
   - **Lazy Evaluation**: Instead of evaluating the entire iterable and building a full list in memory, a generator expression creates a generator object that yields one item at a time only when explicitly requested (e.g., via `next()` or a `for` loop).

2. Syntactic Sugar in Functions:
   - When passing a generator expression as the *only* argument to a function (like `sum()`, `any()`, or `max()`), you don't need double parentheses. Python allows `sum(x for x in data)` instead of `sum((x for x in data))`.

3. Latest Python Features:
   - **Exception Handling Speedups (Python 3.11+)**: Generators rely heavily on the `StopIteration` exception to know when to finish yielding values. Python 3.11 introduced "zero-cost exceptions", meaning the internal mechanism that handles this `StopIteration` is now significantly faster, directly speeding up generator consumption.
   - **Note on PEP 709 (Python 3.12)**: While list/dict/set comprehensions were "inlined" in Python 3.12 for a speed boost, Generator Expressions were specifically *excluded* from this PEP. Generators inherently require a separate execution frame to save their state across multiple `next()` calls, so they still compile as separate frames.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the primary difference between a list comprehension `[...]` and a generator expression `(...)`?
A1: A list comprehension evaluates the entire sequence immediately and stores all items in memory as a fully populated list. A generator expression returns an iterator object and evaluates items lazily (one by one) on demand, which uses almost no memory regardless of how huge the dataset is.

Q2: What happens if you try to iterate over a generator twice?
A2: A generator is exhausted after its first complete iteration. If you try to iterate over it a second time, it will silently yield nothing (an empty sequence). If you need to iterate over data multiple times, you must either recreate the generator or cast it to a list first.

Q3: How does the `sum()` function work with a generator expression?
A3: `sum()` continuously calls `next()` on the generator object passed into it, maintaining a running total until the generator raises a `StopIteration` exception (meaning it has run out of items).

Q4: Would you use a list comprehension or a generator expression to find a specific user in a database of 1 million users?
A4: A generator expression combined with `next()`. For example: `next(u for u in users if u.id == 5)`. This will stop searching the exact moment it finds the user. A list comprehension would needlessly process and load all 1 million users into memory first.
"""