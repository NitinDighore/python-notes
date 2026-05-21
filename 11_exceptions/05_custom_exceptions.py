def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "elaichai"]:
        raise ValueError("Unsupported chai flavor...")
    print(f"brewing {flavor} chai...")


try:
    brew_chai("mint")
except ValueError as e:
    print(f"Caught error: {e}") # Output: Caught error: Unsupported chai flavor...

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Defining a True Custom Exception
print("\n1. Creating a basic custom exception:")
# You create a custom exception by simply inheriting from the built-in `Exception` class
class ChaiFlavorError(Exception):
    """Custom exception raised when an invalid tea flavor is requested."""
    pass

def strict_brew(flavor):
    if flavor == "coffee":
        raise ChaiFlavorError("We don't serve coffee here!")
    print(f"Brewing {flavor}...")

try:
    strict_brew("coffee")
except ChaiFlavorError as e:
    print(f"Custom Error Caught: {e}") # Output: Custom Error Caught: We don't serve coffee here!

# Trick 2: Custom Exceptions with Extra Attributes
print("\n2. Exceptions with custom data payloads:")
class OutOfStockError(Exception):
    def __init__(self, item, alternatives):
        # Initialize the parent Exception with a default message
        super().__init__(f"Sorry, {item} is out of stock.")
        self.item = item
        self.alternatives = alternatives # Store custom data on the error object

try:
    raise OutOfStockError("Oolong", ["Green", "Black"])
except OutOfStockError as e:
    print(f"{e} Try these instead: {e.alternatives}") 
    # Output: Sorry, Oolong is out of stock. Try these instead: ['Green', 'Black']

# Trick 3: Adding Context Notes (Python 3.11+)
print("\n3. Using add_note() dynamically:")
try:
    err = ChaiFlavorError("Temperature too low!")
    err.add_note("This occurred during the secondary heating phase.")
    raise err
except ChaiFlavorError as e:
    print(f"Error: {e} | Notes: {e.__notes__}") 
    # Output: Error: Temperature too low! | Notes: ['This occurred during the secondary heating phase.']

"""
--- NOTES: Custom Exceptions ---

1. Why create Custom Exceptions?
   - Built-in exceptions like `ValueError` or `TypeError` are very broad. If a complex application raises a `ValueError`, it could be from a bad database ID, an invalid user input, or a math calculation error.
   - Defining custom exceptions (like `InsufficientFundsError` or `InvalidChaiFlavorError`) makes your application's domain logic extremely clear. It allows calling code to catch and handle specific business-logic errors cleanly without accidentally catching unrelated system errors.

2. Best Practices:
   - Always inherit from `Exception`, not `BaseException`.
   - Give your custom exception classes descriptive names ending in `...Error`.

3. Latest Python Features (Python 3.11+):
   - **`.add_note()` Method**: As shown in Trick 3, Python 3.11 added the `.add_note()` method to exceptions. Instead of having to create a highly complex custom exception class just to store extra debugging context, you can simply append notes dynamically before the exception propagates up the stack.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: How do you create a custom exception in Python?
A1: You define a new class that inherits from the built-in `Exception` class (or one of its subclasses like `ValueError`). Even an empty class with just `pass` is sufficient to act as a unique error type.

Q2: Why should you inherit from `Exception` and not `BaseException`?
A2: `BaseException` is the absolute root of the exception hierarchy. System-level exiting events like `SystemExit` and `KeyboardInterrupt` inherit directly from `BaseException`. If you inherit your custom business logic errors from `BaseException`, developers using `except Exception:` won't catch your error, leading to unexpected application crashes.

Q3: If I create `class MyError(ValueError):`, can it be caught by `except ValueError:`?
A3: Yes! Because of inheritance, catching a parent exception class will automatically catch all of its subclasses. This is useful if your error is fundamentally a value issue, but you want to provide a specific domain name for it.
"""