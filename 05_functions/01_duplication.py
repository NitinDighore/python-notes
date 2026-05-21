def print_order(name, chai_type):
    print(f"{name} orderded {chai_type} chai!")


print_order("Aman", "masala") # Output: Aman orderded masala chai!
print_order("Hitesh", "Ginger") # Output: Hitesh orderded Ginger chai!
print_order("Jia", "Tulsi") # Output: Jia orderded Tulsi chai!

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Argument Unpacking (*args) with a Loop
print("\n1. Unpacking arguments in a loop:")
# Instead of repeating the function call manually, we iterate over a data structure and unpack the tuple.
bulk_orders = [("Alice", "Green"), ("Bob", "Oolong"), ("Charlie", "Black")]
for order in bulk_orders:
    print_order(*order) # Output: Alice orderded Green chai! ...

# Trick 2: Keyword Unpacking from a Dictionary (**kwargs)
print("\n2. Unpacking keyword arguments from a dict:")
# Dictionaries matching the exact parameter names can be unpacked straight into the function
dict_order = {"name": "Dave", "chai_type": "Matcha"}
print_order(**dict_order) # Output: Dave orderded Matcha chai!

# Trick 3: Using functools.partial to create a specialized function
print("\n3. Pre-filling arguments with functools.partial:")
from functools import partial
# If Hitesh is a regular customer, we can create a specific function for him that pre-fills the first argument
hitesh_order = partial(print_order, "Hitesh")
hitesh_order("Lemon") # Output: Hitesh orderded Lemon chai!

"""
--- NOTES: Functions and Code Duplication ---

1. The DRY Principle (Don't Repeat Yourself):
   - The filename `01_duplication.py` hints at one of the core tenets of software engineering: DRY.
   - Instead of writing `print(f"... orderded ... chai!")` multiple times manually, we abstract the repetitive logic into a single function.
   - Maintainability: If we ever need to fix a typo (like "orderded" to "ordered") or change the logic, we only have to update it in one place (inside the function body) instead of everywhere it was used.

2. What is a Function?
   - A function is a reusable block of code designed to perform a single, related action.
   - It allows you to pass data (known as parameters) into it, and optionally return data.

3. Latest Python Features (Type Hinting & Readability):
   - While not strictly functional changes, modern Python highly encourages Type Hinting to make functions self-documenting.
   - **Python 3.9+**: Built-in generic types (e.g., `list[str]` instead of `typing.List[str]`).
   - **Python 3.10+**: Introduced the pipe operator `|` for Union types. Example: `def print_order(name: str, chai_type: str | None = None):`.
   - **Python 3.12+**: Introduced the `type` keyword for type aliases, making complex function signatures much easier to read (e.g., `type Customer = tuple[str, str]`).

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the DRY principle and how do functions help achieve it?
A1: DRY stands for "Don't Repeat Yourself". It aims to reduce software pattern repetition. Functions help achieve this by encapsulating logic into a single block that can be invoked multiple times, preventing code duplication.

Q2: What is the difference between a parameter and an argument?
A2: A "parameter" is the variable defined in the function signature (e.g., `name` and `chai_type` in the definition). An "argument" is the actual concrete value passed to the function when it is invoked (e.g., `"Aman"`, `"masala"`).

Q3: What happens if you call `print_order("Aman")` without providing the second argument?
A3: Python will immediately raise a `TypeError: print_order() missing 1 required positional argument: 'chai_type'`, terminating the program.

Q4: Is Python "pass-by-value" or "pass-by-reference"?
A4: Python is technically "pass-by-object-reference" (or pass-by-assignment). If you pass an immutable object (like an int or string), it behaves like pass-by-value. If you pass a mutable object (like a list or dict), modifications to that object inside the function will reflect outside the function.
"""
