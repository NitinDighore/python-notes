def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup


my_bill = calculate_bill(3, 15)
print(my_bill) # Output: 45

print("Order for table 2: ", calculate_bill(2, 50)) # Output: Order for table 2:  100

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Keyword Arguments for Immediate Readability
print("\n1. Keyword Arguments:")
# calculate_bill(3, 15) is vague (what is 3? what is 15?). 
# Naming the arguments at the call site makes it instantly understandable!
clear_bill = calculate_bill(cups=4, price_per_cup=20)
print(f"Clear bill: {clear_bill}") # Output: Clear bill: 80

# Trick 2: Modern Python Readability (Type Hints + Docstrings)
print("\n2. Type Hints and Docstrings:")
def calculate_taxed_bill(cups: int, price_per_cup: float, tax_rate: float = 0.05) -> float:
    """
    Calculates the total bill including tax.

    Args:
        cups (int): Number of cups ordered.
        price_per_cup (float): Price of a single cup.
        tax_rate (float): Tax rate to apply (default is 5%).
        
    Returns:
        float: The final calculated amount.
    """
    base = cups * price_per_cup
    return base + (base * tax_rate)

print(f"Taxed bill: {calculate_taxed_bill(2, 20.0)}") # Output: Taxed bill: 42.0

# Trick 3: Forcing Keyword-Only Arguments
print("\n3. Forcing Keyword Arguments:")
# Using a bare asterisk (*) in the parameter list forces all subsequent arguments to be passed by keyword, preventing ambiguous positional calls.
def secure_transaction(*, amount: float, user_id: int):
    print(f"Processing {amount} for user {user_id}")

# secure_transaction(100.0, 5) # Uncommenting this would raise a TypeError!
secure_transaction(amount=100.0, user_id=5) # Output: Processing 100.0 for user 5

"""
--- NOTES: Code Readability ---

1. The Philosophy of Readability:
   - The creator of Python, Guido van Rossum, famously said: "Code is read much more often than it is written."
   - `04_readability.py` focuses on making your function signatures clear. Descriptive variable names like `calculate_bill`, `cups`, and `price_per_cup` act as self-documenting code.
   - Following PEP 8 (Python's official style guide) ensures your code is readable by the broader Python community.

2. Tools for Readability:
   - **Docstrings**: Multi-line strings (`\"\"\"...\"\"\"`) placed immediately inside a function definition to explain what the function does.
   - **Type Hinting**: Introduced in Python 3.5 (PEP 484), type hints explicitly state what data types a function expects and returns (e.g., `def foo(age: int) -> bool:`).

3. Latest Python Features (Type Hinting Enhancements):
   - **Python 3.9+**: Built-in generic types (`list[int]` instead of `typing.List[int]`).
   - **Python 3.10+**: Introduced the pipe `|` operator for cleaner union types (e.g., `def parse(data: int | str):`).
   - **Python 3.12+**: Introduced the `type` keyword for type aliases. You can drastically improve readability for complex types by assigning them a name: `type UserDict = dict[str, str | int]`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: If Python is a dynamically typed language, what is the point of adding type hints?
A1: While type hints are ignored by the Python runtime (they don't enforce types at execution), they drastically improve readability, enable powerful IDE autocompletion/linting, and allow static analysis tools (like `mypy`) to catch type-related bugs before the code is even run.

Q2: What is a docstring, and how do you access it programmatically?
A2: A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition, used for documentation. You can access it at runtime using the `__doc__` special attribute of the object (e.g., `print(calculate_taxed_bill.__doc__)`) or by using the built-in `help()` function.

Q3: What does the `*` do in a function signature like `def func(a, b, *, c, d):`?
A3: It marks the end of positional arguments. Any arguments defined after the bare `*` must be passed strictly as keyword arguments. In this example, `c` and `d` must be explicitly named when calling the function (e.g., `func(1, 2, c=3, d=4)`), forcing the caller to write readable code.
"""