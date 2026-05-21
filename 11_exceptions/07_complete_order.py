class InvalidChaiError(Exception): pass

def bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        if flavor not in menu:
            raise InvalidChaiError("that chai is not available")
        if not isinstance(cups, int):
            raise TypeError("Number of cups must be an integer")
        total = menu[flavor] * cups
        print(f"Your bill for {cups} cups of {flavor} chai: rupees {total}")
    except Exception as e:
        print("Error: ", e)
    finally:
        print("Thank you for visiting chaicode!")


bill("mint", 2) 
# Output: 
# Error:  that chai is not available
# Thank you for visiting chaicode!

bill("masala", "three")
# Output:
# Error:  Number of cups must be an integer
# Thank you for visiting chaicode!

bill("ginger", 3)
# Output:
# Your bill for 3 cups of ginger chai: rupees 120
# Thank you for visiting chaicode!

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: EAFP (Easier to Ask for Forgiveness than Permission)
print("\n1. EAFP vs LBYL:")
# The original bill() function uses LBYL (Look Before You Leap) with `if flavor not in menu:`.
# Python strictly prefers EAFP: Just try the operation and catch the exact error if it fails!
def eafp_bill(flavor, cups):
    menu = {"masala": 20, "ginger": 40}
    try:
        # We don't check. We just do the math. If flavor is missing, it raises KeyError.
        # If cups is a string like "two", int() raises ValueError.
        total = menu[flavor] * int(cups)
        print(f"EAFP Bill: rupees {total}")
    except KeyError:
        print(f"EAFP Error: {flavor} is not available.")
    except ValueError:
        print("EAFP Error: Number of cups must be a valid number.")

eafp_bill("mint", 2) # Output: EAFP Error: mint is not available.
eafp_bill("ginger", "two") # Output: EAFP Error: Number of cups must be a valid number.

# Trick 2: The Retry Pattern
print("\n2. The Exception Retry Pattern:")
# Very common in real-world apps (like retrying a failed database connection or API request)
import random
def unreliable_network():
    if random.random() < 0.7: # 70% chance to fail
        raise ConnectionError("Network timeout!")
    return "Payment Successful!"

for attempt in range(3):
    try:
        print(f"Attempt {attempt + 1}...")
        result = unreliable_network()
        print(result)
        break # Success! Exit the loop.
    except ConnectionError as e:
        print(f"Failed: {e}")
else:
    # This runs ONLY if the loop never hit 'break' (i.e., all 3 attempts failed)
    print("Transaction aborted after 3 failed attempts.")

# Trick 3: Global Exception Hook
print("\n3. Global Exception Hook (sys.excepthook):")
import sys
# You can intercept uncaught exceptions globally before they crash your program!
# This is how tools like Sentry or Datadog log crashes in production apps.
def custom_crash_handler(exc_type, exc_value, exc_traceback):
    print(f"💥 CRITICAL CRASH INTERCEPTED: {exc_type.__name__} - {exc_value}")

# Uncomment the lines below to see it in action:
# sys.excepthook = custom_crash_handler
# raise RuntimeError("The server is on fire!")

"""
--- NOTES: Complete Real-World Exception Handling ---

1. Broad Exception Catching (`except Exception as e`):
   - In the `bill()` function, we catch `Exception`. While catching broad exceptions is generally an anti-pattern deep inside your business logic, it is acceptable at the "top level" of an application (like an endpoint route or the final orchestrator function) to gracefully handle errors and display them to the user instead of crashing the server.

2. LBYL vs EAFP:
   - **LBYL (Look Before You Leap)**: Check conditions before executing (e.g., `if type(cups) != int`). Common in Java/C++.
   - **EAFP (Easier to Ask for Forgiveness than Permission)**: Just run the code inside a `try` block and catch the error if it fails (Trick 1). This is the highly favored "Pythonic" approach because it is generally faster and avoids race conditions (TOCTOU - Time of Check to Time of Use).

3. Latest Python Features (Python 3.11+):
   - **Collecting Multiple Validation Errors**: In a real app, if a user submits an order with both a bad flavor AND a bad cup count, you'd want to tell them *both* errors at once, not just the first one. Python 3.11's `ExceptionGroup` makes this natively possible by aggregating multiple exceptions inside a single block and raising them together!

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What does "Easier to Ask for Forgiveness than Permission" (EAFP) mean in Python?
A1: It is a programming style where you assume the valid data or keys exist and attempt the operation directly inside a `try` block, catching the resulting exception if your assumption was wrong. It contrasts with "Look Before You Leap" (LBYL), which uses numerous `if` statements to check for preconditions before executing the code.

Q2: Is it okay to use `except Exception as e:`?
A2: Generally, no. You should catch specific exceptions (like `KeyError` or `ValueError`) to avoid masking unrelated bugs (like `NameError` from a typo). However, at the absolute top boundary of an application (like a main event loop or web server router), it is acceptable to catch `Exception` simply to log the crash and return a friendly 500 Error to the user without killing the entire process.

Q3: How would you implement a mechanism to retry a piece of code 5 times if it throws an exception?
A3: By wrapping a `try-except` block inside a `for` loop that runs 5 times. If the `try` block succeeds, you use the `break` keyword to exit the loop. If it fails, the `except` block handles the error, and the loop continues to the next iteration. You can attach a `for-else` block to handle the scenario where all 5 attempts fail.
"""