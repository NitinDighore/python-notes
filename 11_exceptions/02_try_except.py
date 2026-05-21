chai_menu = {"masala": 30, "ginger": 40}

try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are tying to access does not exists") # Output: The key that you are tying to access does not exists


print("Hello chai code") # Output: Hello chai code (Notice the script didn't crash!)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Aliasing the exception object
print("\n1. Accessing the Exception Object (as e):")
try:
    chai_menu["mint"]
except KeyError as e:
    # 'e' contains the actual error object, which often holds the problematic value
    print(f"Missing Key: {e}") # Output: Missing Key: 'mint'

# Trick 2: Catching multiple exceptions in one block
print("\n2. Catching Multiple Exceptions simultaneously:")
def process_order(tea, quantity):
    try:
        total = chai_menu[tea] * int(quantity)
        print(f"Total: {total}")
    except (KeyError, ValueError) as e: # Use a tuple for multiple exception types!
        print(f"Order failed due to invalid input. Error: {type(e).__name__}")

process_order("masala", "two") # Output: Order failed due to invalid input. Error: ValueError

# Trick 3: Multiple Except Blocks (Order Matters!)
print("\n3. Order of Except Blocks:")
# Python checks 'except' blocks top-to-bottom. Always put specific exceptions FIRST!
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Caught specifically: Cannot divide by zero!") # Output: Caught specifically: Cannot divide by zero!
except Exception:
    print("Caught generally: Something went wrong.") # This won't run because the block above caught it first.

# Trick 4: Exception Chaining (raise ... from)
print("\n4. Exception Chaining:")
try:
    try:
        chai_menu["oolong"]
    except KeyError as e:
        # 'from None' hides the original KeyError and only shows the new ValueError to the user
        raise ValueError("Oolong is permanently out of stock!") from None
except ValueError as ve:
    print(f"Chained Error: {ve}") # Output: Chained Error: Oolong is permanently out of stock!

"""
--- NOTES: `try-except` Blocks ---

1. The Purpose of `try-except`:
   - Wrapping code in a `try` block tells Python: "Attempt to execute this code. If it crashes, don't stop the program. Instead, jump immediately to the matching `except` block."
   - As shown in the main code, printing "Hello chai code" succeeds because the `KeyError` was cleanly caught and handled, allowing the rest of the script to continue normally.

2. Hierarchy and Catch-Alls:
   - It is highly recommended to catch *specific* exceptions (like `KeyError`).
   - If you must catch anything, use `except Exception as e:`. Do NOT use a bare `except:`, as that catches system-exiting events like `KeyboardInterrupt` (when a user presses Ctrl+C).

3. Latest Python Features (Python 3.11+):
   - **Adding Notes to Exceptions**: In Python 3.11, the `add_note()` method was added to the `BaseException` class. You can now dynamically attach contextual information to an exception before it propagates upwards: `e.add_note("Failed during database transaction")`.
   - **Zero-Cost `try` Blocks**: Python 3.11 made `try` blocks practically free. Previously, entering a `try` block incurred a small performance penalty. Now, if no exception is raised, the `try` block executes just as fast as normal code.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if an exception is raised in a `try` block but there is no matching `except` block for that specific exception type?
A1: The exception will propagate up to the next enclosing `try-except` block (if one exists). If it is never caught, it reaches the top level, crashes the program, and prints a traceback to the console.

Q2: Does the order of multiple `except` blocks matter?
A2: Yes, absolutely. Python evaluates them from top to bottom. You must always place specific subclasses (like `KeyError`) before their broader parent classes (like `LookupError` or `Exception`). If `Exception` is placed first, it will catch everything, rendering the specific blocks below it unreachable.

Q3: How do you handle a situation where you want to execute the same error-handling logic for both a `TypeError` and a `ValueError`?
A3: You can catch them both in a single `except` statement by passing them as a tuple: `except (TypeError, ValueError):`.

Q4: What does the `as e` do in `except KeyError as e:`?
A4: It binds the raised exception instance object to the variable `e`. You can then inspect `e` to get the error message, the problematic value, or its arguments (e.g., `e.args`).
"""