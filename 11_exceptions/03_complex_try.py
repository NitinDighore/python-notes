def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")
        if flavor == "unknown":
            raise ValueError("We don't know that flavor")
    except ValueError as e:
        print("Error: ", e)
    else:
        print(f"{flavor} chai is served")
    finally:
        print("Next customer please")

serve_chai("masala")
# Output: 
# Preparing masala chai...
# masala chai is served
# Next customer please

print("-" * 20)

serve_chai("unknown")
# Output:
# Preparing unknown chai...
# Error:  We don't know that flavor
# Next customer please

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The 'finally' block ALWAYS executes, even if you 'return' early!
print("\n1. finally vs return:")
def early_return():
    try:
        print("Executing try block...")
        return "Result from try"
    finally:
        print("Executing finally block... BEFORE the return happens!")

print(f"Function output: {early_return()}") 
# Output: 
# Executing try block...
# Executing finally block... BEFORE the return happens!
# Function output: Result from try

# Trick 2: The Exception Swallowing Trap (Anti-Pattern)
print("\n2. The Exception Swallowing Trap:")
def swallow_exception():
    try:
        1 / 0 # Raises ZeroDivisionError
    finally:
        # If you return a value inside finally, it CANCELS the active exception!
        # Note: Linters will flag this as an error ("A 'return' cannot be used
        # to exit a 'finally' block") because hiding errors is highly dangerous.
        # We have commented it out to avoid linter errors and bad practices.
        # return "The error completely vanished!"
        pass

try:
    print(f"Swallowed result: {swallow_exception()}")
except ZeroDivisionError as e:
    print(f"Since the return is commented out, the error naturally propagated: {repr(e)}")

# Trick 3: Why use 'else' instead of just putting everything in 'try'?
print("\n3. Why the 'else' block matters:")
# If we put all code in `try`, we might accidentally catch exceptions we didn't mean to catch.
try:
    menu = {"chai": 20}
    price = menu["chai"] # We expect a KeyError if "chai" is missing.
except KeyError:
    print("Chai not found on menu.")
else:
    # We only want to execute this if the menu lookup succeeded.
    # If THIS code raises a KeyError (e.g., empty dictionary popup), the `except` block ABOVE will NOT catch it!
    # This correctly isolates the error handling to only the intended operation.
    print(f"Success! Price is {price}") # Output: Success! Price is 20

"""
--- NOTES: Complex Try Blocks (`else` and `finally`) ---

1. The Complete `try` Flow:
   - **`try`**: Code that might cause an exception. Should be kept as short as possible.
   - **`except`**: Code that runs ONLY if an exception is raised in the `try` block.
   - **`else`**: Code that runs ONLY if the `try` block succeeds (i.e., no exceptions were raised). It does not catch exceptions raised within itself.
   - **`finally`**: Code that runs ALWAYS, regardless of whether an exception occurred, was handled, or if the function returned early. It is universally used for "teardown" or "cleanup" logic (like closing files, releasing network sockets, or closing database connections).

2. Latest Python Features (Python 3.11+):
   - **Zero-Cost Exceptions**: Python 3.11 optimized the `try` block overhead to practically zero. This encourages developers to use `try-except` blocks (EAFP - Easier to Ask for Forgiveness than Permission) more freely, rather than proactively checking conditions using `if-else` (LBYL - Look Before You Leap).

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if you have a `return` statement in the `try` block AND a `return` statement in the `finally` block?
A1: The `return` statement in the `finally` block will override the `return` statement in the `try` block. The function will evaluate the `try` block, hit the `finally` block before exiting, and the `finally` block's return value will be the final output.

Q2: Does `finally` execute if you call `sys.exit()` inside the `try` block?
A2: Yes! `sys.exit()` simply raises a `SystemExit` exception under the hood. The `finally` block intercepts this and executes its cleanup code before the program actually terminates. (Note: It will NOT run if the OS forcefully kills the process via SIGKILL or power loss).

Q3: Why shouldn't you write a `return` or `break` statement inside a `finally` block?
A3: As demonstrated in Trick 2, issuing a `return`, `break`, or `continue` inside a `finally` block silently discards any active exception that was propagating through the `try` block. This is a severe anti-pattern known as "exception swallowing" and hides critical bugs.

Q4: Why use the `else` block instead of just appending the success code directly inside the bottom of the `try` block?
A4: Separation of concerns and safety. The `try` block should strictly contain the exact line(s) of code expected to raise the error. If you put subsequent success logic inside the `try` block, and that success logic happens to raise the same error type (e.g., a `ValueError`), your `except` block will accidentally catch it, masking a completely different bug.
"""