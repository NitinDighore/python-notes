names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees") # Output: Hitesh paid 50 rupees, then Meera paid 70 rupees, then Sam paid 100 rupees, then Ali paid 55 rupees

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Creating a dictionary directly from two lists using zip
print("\n1. Two lists to Dictionary:")
# Passing a zipped object to dict() instantly maps the first list to keys and the second to values
order_dict = dict(zip(names, bills))
print(f"Order Dict: {order_dict}") # Output: {'Hitesh': 50, 'Meera': 70, 'Sam': 100, 'Ali': 55}

# Trick 2: Zipping more than two iterables
print("\n2. Zipping multiple iterables:")
tips = [5, 10, 15, 5]
# You can zip as many lists together as you want
for name, amount, tip in zip(names, bills, tips):
    print(f"{name} paid {amount} + {tip} tip")

# Trick 3: "Unzipping" a list of tuples using zip and the unpack operator (*)
print("\n3. Unzipping data:")
zipped_data = [("A", 1), ("B", 2), ("C", 3)]
# Using the * operator unpacks the list into positional arguments, effectively unzipping it
unzipped_letters, unzipped_nums = zip(*zipped_data)
print(f"Letters: {unzipped_letters}, Nums: {unzipped_nums}") # Output: Letters: ('A', 'B', 'C'), Nums: (1, 2, 3)

# Trick 4: Handling unequal lengths (Silent truncation vs Strict)
print("\n4. Unequal lengths (Default behavior):")
short_list = [1, 2]
# zip stops at the shortest iterable automatically, silently dropping the "C"
print(list(zip(["A", "B", "C"], short_list))) # Output: [('A', 1), ('B', 2)]

# Trick 5: Handling unequal lengths with padding (itertools.zip_longest)
print("\n5. Using zip_longest for unequal lists:")
from itertools import zip_longest
# Instead of dropping "C", it fills the missing paired value with a specified fillvalue
print(list(zip_longest(["A", "B", "C"], short_list, fillvalue="MISSING"))) # Output: [('A', 1), ('B', 2), ('C', 'MISSING')]

"""
--- NOTES: The `zip()` Function ---

1. What is `zip()`?
   - `zip(*iterables)` is a built-in Python function that takes two or more iterables and aggregates them into tuples, returning an iterator.
   - The `i`-th tuple contains the `i`-th element from each of the argument iterables.
   - By default, the iterator gracefully stops when the shortest input iterable is exhausted.

2. Latest Python Features:
   - **Strict Zipping (Python 3.10+)**: A common source of bugs with `zip()` was silently losing data if the iterables were of unequal lengths. Python 3.10 introduced the `strict` keyword argument. 
     Example: `zip(list1, list2, strict=True)`. If `list1` and `list2` are not the exact same length, this will explicitly raise a `ValueError`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Does `zip()` return a list?
A1: No, in modern Python (Python 3), `zip()` returns a `zip` object, which is an iterator. It yields tuples one by one on demand. If you need a list, you must explicitly cast it using `list(zip(a, b))`. (Note: In Python 2, it used to return a list, but it was changed to an iterator to improve memory efficiency).

Q2: What happens if the iterables passed to `zip()` have different lengths?
A2: By default, `zip()` stops generating tuples as soon as the shortest iterable is exhausted, silently ignoring any remaining items in the longer iterables. 

Q3: How do you prevent `zip()` from silently dropping data when lists are of unequal length?
A3: In Python 3.10+, you should use `zip(a, b, strict=True)` to raise a `ValueError` if they don't match. For earlier versions, or if you want to pad the missing values instead of raising an error, you should use `itertools.zip_longest(a, b, fillvalue=None)`.

Q4: Explain how "unzipping" works with `zip(*iterable)`.
A4: The `*` (unpacking) operator unpacks the sequence (e.g., a list of tuples) into separate positional arguments for the `zip` function. So `zip(*[(1, 2), (3, 4)])` is evaluated as `zip((1, 2), (3, 4))`. `zip` then takes the first items `(1, 3)` and puts them in a tuple, and the second items `(2, 4)` and puts them in a tuple, effectively unzipping them.
"""