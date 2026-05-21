kettle_boiled = False

if kettle_boiled:
    print("Kellle Done! time to make Chai") # Output: (No output because kettle_boiled is False)

"""
--- NOTES: Basic `if` Statements and Boolean Flags ---

1. The Basic `if` Statement:
   - The `if` statement is the most fundamental control flow tool in Python.
   - It evaluates a single condition. If that condition is `True` (or "truthy"), the indented block of code immediately beneath it is executed.
   - If the condition is `False` (or "falsy") and there is no `else` or `elif` block provided, Python simply skips the indented block and continues executing the rest of the script.

2. Boolean Flags:
   - Variables like `kettle_boiled` are often referred to as "flags" or "state variables". 
   - They are heavily used in programming to track whether a specific event has occurred or a specific state has been reached (e.g., `is_logged_in = True`, `has_errors = False`).

3. PEP 8 Best Practices for Booleans:
   - When checking a boolean variable in an `if` statement, you should evaluate the variable directly: `if kettle_boiled:` or `if not kettle_boiled:`.
   - It is considered un-Pythonic and against PEP 8 style guidelines to compare a boolean to `True` or `False` using the equality operator (e.g., `if kettle_boiled == True:` is frowned upon).

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if an `if` statement evaluates to `False` and there is no `else` block?
A1: Python simply skips the indented code block under the `if` statement and proceeds to execute the next unindented line of code in the program. No error is raised.

Q2: Why is it recommended to write `if flag:` instead of `if flag == True:`?
A2: Writing `if flag:` is considered more readable, idiomatic Python. More importantly, it relies on Python's concept of "truthiness", which safely evaluates the condition without forcing a strict type comparison against the `True` singleton.

Q3: If we changed `kettle_boiled = None`, would the `print` statement execute? Why or why not?
A3: It would not execute. `None` is a "falsy" value in Python. When Python evaluates `if None:`, it treats it as `False`, so the block is skipped.
"""