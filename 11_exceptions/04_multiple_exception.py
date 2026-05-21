def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"total cost is {cost}")
    except KeyError:
        print("Sorry that chai is not on menu")
    except TypeError:
        print("Quantity must be in number")

process_order("ginger", 2) # Output: Sorry that chai is not on menu
process_order("masala", "two") # Output: total cost is twotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwotwo

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The Sequence Repetition Trap (Why didn't the code above raise a TypeError?)
print("\n1. The String Multiplication Trap:")
# In Python, int * str does NOT raise an error; it repeats the string!
# To truly trigger the TypeError block, we must perform an operation Python can't resolve, like division or string concatenation with an int.
try:
    price = 20
    cost = price / "two" 
except TypeError as e:
    print(f"Caught TypeError: {e}") # Output: Caught TypeError: unsupported operand type(s) for /: 'int' and 'str'

# Trick 2: Grouping Multiple Exceptions
print("\n2. Catching Multiple Exceptions Identically:")
# You can handle different exceptions with the exact same logic using a tuple.
try:
    result = {"masala": 20}["ginger"] / 0
except (KeyError, ZeroDivisionError) as e:
    print(f"Caught an expected failure: {type(e).__name__}") # Output: Caught an expected failure: KeyError

# Trick 3: Exception Hierarchy (Order Matters!)
print("\n3. Hierarchy ordering (Specific before General):")
try:
    raise KeyError("Missing chai")
except LookupError: # LookupError is the PARENT class of KeyError
    print("Caught by LookupError (Parent)") # Output: Caught by LookupError (Parent)
except KeyError:
    # This block will NEVER run because the broader parent exception above caught it first!
    print("Caught by KeyError (Child)") 

# Trick 4: Exception Groups and except* (Python 3.11+)
print("\n4. Handling Multiple Concurrent Exceptions:")
# Modern Python allows raising multiple unrelated errors at the exact same time.
try:
    raise ExceptionGroup("Setup Failures", [KeyError("No cups"), TypeError("Bad milk")])
except* KeyError as e:
    print(f"Handled the KeyErrors: {e.exceptions}") # Output: Handled the KeyErrors: (KeyError('No cups'),)
except* TypeError as e:
    print(f"Handled the TypeErrors: {e.exceptions}") # Output: Handled the TypeErrors: (TypeError('Bad milk'),)

"""
--- NOTES: Multiple Exceptions and Hierarchies ---

1. Multiple `except` Blocks:
   - A single `try` block can have multiple `except` blocks. Python will check them from top to bottom.
   - As soon as Python finds a matching exception type, it executes that block and ignores the rest.

2. Exception Hierarchy:
   - Exceptions in Python are organized into a class hierarchy. For example, `KeyError` and `IndexError` both inherit from `LookupError`, which inherits from `Exception`, which inherits from `BaseException`.
   - Because Python matches top-to-bottom, you MUST put specific/child exceptions (like `KeyError`) BEFORE broad/parent exceptions (like `Exception`). Otherwise, the parent block will catch everything, masking your specific error handlers.

3. Latest Python Features (Python 3.11+):
   - **`ExceptionGroup` and `except*`**: Prior to Python 3.11, an application could only raise and handle one exception at a time. The new `ExceptionGroup` allows multiple exceptions to be bundled together. The `except*` (except-star) syntax allows a single `try` block to match and process *multiple* `except*` blocks if the group contains errors of those types.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why didn't `process_order("masala", "two")` raise a `TypeError`?
A1: Because Python allows multiplying an integer by a string. This operation implies "sequence repetition". `20 * "two"` evaluates to the string `"two"` repeated 20 times. It never raises an error, so the `except TypeError:` block is bypassed.

Q2: What happens if an exception is raised that doesn't match any of your `except` blocks?
A2: The exception propagates upwards to the next enclosing `try-except` block. If it reaches the main execution thread and remains uncaught, the program crashes and prints a traceback.

Q3: Is it better to write multiple `except` blocks or one `except Exception:` block with `if/elif` statements inside?
A3: It is vastly better to use multiple `except` blocks. It is more readable, significantly faster, and follows the Pythonic philosophy of letting the language's native exception-handling mechanisms do the routing for you.

Q4: If `KeyError` is a subclass of `LookupError`, what happens if you put `except LookupError:` before `except KeyError:`?
A4: The `except LookupError:` block will catch the `KeyError`, and the `except KeyError:` block will become "dead code" (unreachable). Specific exceptions must always be ordered before their parent exceptions.
"""