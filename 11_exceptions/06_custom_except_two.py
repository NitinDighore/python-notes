class OutOfIngredientsError(Exception):
    pass

def make_chai(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Missing milk or sugar")
    print("chai is ready...")


try:
    make_chai(0, 1)
except OutOfIngredientsError as e:
    print(f"Error caught: {e}") # Output: Error caught: Missing milk or sugar

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Accessing Exception arguments directly
print("\n1. Accessing the args tuple:")
try:
    # You can pass as many arguments as you want to a default Exception
    raise OutOfIngredientsError("Milk", "Sugar", "Water")
except OutOfIngredientsError as e:
    # They are automatically stored in the 'args' tuple attribute
    print(f"Missing items stored in args: {e.args}") # Output: Missing items stored in args: ('Milk', 'Sugar', 'Water')

# Trick 2: Overriding __str__ for dynamic error messages
print("\n2. Overriding __str__ in a custom exception:")
class TemperatureError(Exception):
    def __init__(self, current_temp, required_temp):
        self.current_temp = current_temp
        self.required_temp = required_temp
        
    def __str__(self):
        # This controls exactly what prints when someone does `print(e)`
        return f"Temp is {self.current_temp}°C, but needs to be {self.required_temp}°C!"

try:
    raise TemperatureError(40, 100)
except TemperatureError as e:
    print(f"Formatted Error: {e}") # Output: Formatted Error: Temp is 40°C, but needs to be 100°C!

# Trick 3: Exception Chaining (Wrapping low-level errors)
print("\n3. Chaining with 'raise ... from':")
class DatabaseError(Exception): pass

try:
    try:
        int("not_a_number") # Raises built-in ValueError
    except ValueError as ve:
        # Wrap the low-level ValueError into our high-level domain DatabaseError
        raise DatabaseError("Failed to parse database record") from ve
except DatabaseError as e:
    print(f"High-level error: {e}") # Output: High-level error: Failed to parse database record
    print(f"Original cause: {e.__cause__}") # Output: Original cause: invalid literal for int() with base 10: 'not_a_number'

"""
--- NOTES: Custom Exceptions (Initialization and Formatting) ---

1. The `args` Tuple:
   - When you raise an exception and pass arguments to it (like `raise MyError("Msg", 404)`), Python automatically stores those arguments in a tuple called `args` on the exception object.
   - If you don't override `__init__`, calling `print(e)` will automatically print the contents of `e.args`.

2. Custom `__init__` and `__str__`:
   - To create rich exception objects that hold state (like the specific temperature that failed in Trick 2), you should override `__init__`.
   - Overriding `__str__` allows you to control exactly how the exception looks when it is converted to a string, printed, or logged.

3. Latest Python Features (Python 3.11+):
   - **Enriched Tracebacks**: Tracebacks in Python 3.11+ point to the exact column/expression that caused the error. If a custom exception is deeply nested, the squiggly lines `^^^^` will highlight exactly where the `raise` keyword or the failing operation was invoked, making custom exception debugging much faster.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the `e.args` attribute on an exception object?
A1: `args` is a tuple built into all standard Python exceptions. It contains all the positional arguments passed to the exception's constructor when it was raised.

Q2: When creating a custom exception with a custom `__init__`, do you have to call `super().__init__()`?
A2: It is highly recommended to call `super().__init__(*args)` if you want the exception to behave perfectly like standard Python exceptions (e.g., automatically populating the `args` tuple and formatting the default string representation). However, if you explicitly override `__str__`, you can technically bypass it without crashing.

Q3: What does `raise CustomError("msg") from e` do?
A3: It performs "Exception Chaining" (introduced in PEP 3134). It raises `CustomError` but cleanly attaches the original exception `e` to its `__cause__` attribute. When the traceback is printed, Python will display both errors, clearly stating "The above exception was the direct cause of the following exception".
"""