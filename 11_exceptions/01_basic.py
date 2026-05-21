orders = ["masala", "ginger"]

try:
    print(orders[2])
except IndexError as e:
    print(f"Error: {e}") # Output: Error: list index out of range

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Catching Base Classes (LookupError)
print("\n1. Catching Base Exceptions:")
# LookupError is the parent class for both IndexError (lists) and KeyError (dictionaries).
# Catching it allows you to handle both data structure lookup failures with one block.
try:
    print(orders[5])
except LookupError as e:
    print(f"Lookup failed: {e}") # Output: Lookup failed: list index out of range

# Trick 2: Silently ignoring exceptions with contextlib.suppress
print("\n2. Silently ignoring exceptions:")
from contextlib import suppress
# Sometimes you don't care if an operation fails. Instead of writing a try-except block with a 'pass',
# suppress() makes the intent incredibly explicit and clean.
with suppress(IndexError):
    print(orders[10]) # This silently fails and continues execution
print("Program continued normally.") # Output: Program continued normally.

# Trick 3: Exception Groups (Python 3.11+)
print("\n3. Exception Groups (Python 3.11+):")
# ExceptionGroups allow you to raise and handle MULTIPLE unrelated exceptions at the exact same time.
try:
    raise ExceptionGroup("Task Failures", [
        ValueError("Invalid chai temperature"),
        TypeError("Expected a string")
    ])
# The new `except*` (except-star) syntax acts as a filter, catching only the specific exceptions out of the group!
except* ValueError as e:
    print(f"Caught ValueErrors: {e.exceptions}") # Output: Caught ValueErrors: (ValueError('Invalid chai temperature'),)
except* TypeError as e:
    print(f"Caught TypeErrors: {e.exceptions}") # Output: Caught TypeErrors: (TypeError('Expected a string'),)

"""
--- NOTES: Exceptions and Error Handling Basics ---

1. What are Exceptions?
   - Exceptions are events that disrupt the normal flow of a program's execution (runtime errors).
   - When Python encounters an error (like dividing by zero, or accessing an index that doesn't exist), it stops executing and "raises" an Exception object.
   - If the exception is not "caught" (handled) by a `try-except` block, the program crashes and prints a Traceback.

2. Latest Python Features (Python 3.11+):
   - **ExceptionGroups and `except*`**: Python 3.11 introduced `ExceptionGroup` (PEP 654), allowing multiple exceptions to be raised and handled simultaneously. This is especially crucial for modern asynchronous programming (`asyncio`), where multiple concurrent tasks can fail at the same time.
   - **Fine-grained Error Locations**: Tracebacks in Python 3.11+ now point to the exact expression that caused the error using squiggly lines (`^^^^^^`), rather than just pointing to the line number. This makes debugging deeply nested dictionaries or math equations significantly easier.
   - **Zero-Cost Exceptions**: In Python 3.11, the `try` block was optimized so that it has virtually zero performance overhead if an exception is NOT raised. Exception handling is now extremely fast.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between a SyntaxError and an Exception?
A1: A `SyntaxError` occurs during the parsing stage (compile-time) because the code doesn't follow Python's grammatical rules (like missing a colon). An `Exception` occurs during execution (run-time) when syntactically correct code attempts an illegal operation (like accessing an out-of-bounds list index).

Q2: What is the difference between `IndexError` and `KeyError`?
A2: `IndexError` is raised when you try to access a sequence (like a list or tuple) using an integer index that is out of bounds (e.g., index 2 on a 2-item list). `KeyError` is raised when you try to access a dictionary using a key that does not exist in the dictionary. Both inherit from `LookupError`.

Q3: Why shouldn't you use a bare `except:` block to catch errors?
A3: A bare `except:` catches *everything*, including `BaseException` classes like `KeyboardInterrupt` (Ctrl+C) and `SystemExit`. This means a user cannot easily kill your program. It also hides unexpected bugs. You should always catch specific exceptions (like `except IndexError:`) or, at the very broadest, `except Exception:`.
"""