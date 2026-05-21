menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_tea = [my_tea for my_tea in menu if "Iced" in my_tea]

print(iced_tea) # Output: ['Iced Lemon Tea', 'Iced Peach Tea']

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: If-Else Transformation (Ternary inside Comprehension)
print("\n1. If-Else inside List Comprehension:")
# If you want an 'else', the conditional moves to the FRONT of the 'for' keyword.
standardized_menu = [tea if "Iced" in tea else f"Hot {tea}" for tea in menu]
print(f"Standardized Menu: {standardized_menu}") 
# Output: ['Hot Masala Chai', 'Iced Lemon Tea', 'Hot Green Tea', 'Iced Peach Tea', 'Hot Ginger chai']

# Trick 2: Flattening a 2D List (Nested Loops)
print("\n2. Flattening a Matrix:")
# You can use multiple 'for' clauses. They evaluate from left to right!
tea_batches = [["Green", "Black"], ["Oolong", "White"]]
flat_teas = [tea for batch in tea_batches for tea in batch]
print(f"Flattened Teas: {flat_teas}") # Output: ['Green', 'Black', 'Oolong', 'White']

# Trick 3: Multiple If Conditions
print("\n3. Multiple Conditions:")
# You can chain multiple 'if' conditions at the end (acts like an implicit 'and')
complex_filter = [tea for tea in menu if "Tea" in tea if "Iced" not in tea]
print(f"Hot 'Tea's only: {complex_filter}") # Output: ['Green Tea']

# Trick 4: The Walrus Operator in Comprehensions
print("\n4. Using the Walrus Operator (:=):")
# Compute an expensive transformation once, assign it, and filter by it simultaneously.
loud_menu = [loud_tea for tea in menu if (loud_tea := tea.upper()).startswith("M")]
print(f"Starts with M: {loud_menu}") # Output: ['MASALA CHAI']

# Trick 5: Creating a list of functions/lambdas
print("\n5. List of Lambdas (Watch out for Late Binding!):")
# Advanced: Creating multipliers. Note the `m=i` default argument to avoid the late-binding closure bug.
multipliers = [lambda x, m=i: x * m for i in range(3)]
print(f"Multiplier results for 5: {[func(5) for func in multipliers]}") # Output: [0, 5, 10]

"""
--- NOTES: List Comprehensions ---

1. What are Comprehensions?
   - List comprehensions provide a concise, readable, and "Pythonic" way to create lists.
   - Syntax: `[expression for item in iterable if condition]`
   - They are generally faster than using traditional `for` loops with `.append()` because they are highly optimized at the C-level under the hood.

2. When to avoid them:
   - Do not use list comprehensions purely for their side effects (like `[print(x) for x in data]`). Use a standard `for` loop instead.
   - If the comprehension spans multiple lines and involves deeply nested loops or complex logic, a standard `for` loop is preferred for readability. The Zen of Python states: "Readability counts."

3. Latest Python Features (Python 3.12 Enhancements):
   - **Comprehension Inlining (PEP 709)**: Prior to Python 3.12, comprehensions (list, dict, and set) were compiled as separate, nested functions under the hood. This incurred a frame-creation overhead. In Python 3.12, comprehensions are officially "inlined" directly into the surrounding scope. 
   - **Impact**: This makes comprehensions up to 11% faster in Python 3.12+ and resolves several obscure bugs related to variable scoping (`locals()` behavior) inside comprehensions.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between a list comprehension and a generator expression?
A1: A list comprehension uses square brackets `[]` and evaluates the entire list in memory immediately. A generator expression uses parentheses `()` and returns an iterator that yields items one by one. For huge datasets, generator expressions are vastly more memory-efficient.

Q2: How do you write an `if-else` statement in a list comprehension?
A2: The `if-else` block must be placed *before* the `for` keyword as a conditional expression. Example: `[x if x > 0 else 0 for x in data]`. If you only have an `if` statement (for filtering), it goes *after* the `for` loop: `[x for x in data if x > 0]`.

Q3: Can you have nested `for` loops in a list comprehension?
A3: Yes. You can chain them sequentially. The order is identical to how you would write nested `for` loops normally (outer loop first, inner loop second). Example: `[item for sublist in matrix for item in sublist]`.
"""