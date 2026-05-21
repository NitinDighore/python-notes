def chai_flavor(flavor="masala"):
    """Return the flavor of chai."""
    chai="ginger"
    return flavor


print(chai_flavor.__doc__) # Output: Return the flavor of chai.
print(chai_flavor.__name__) # Output: chai_flavor

help(len) # Output: Help on built-in function len in module builtins: ... (shows len docstring)

def generate_bill(chai=0, samosa=0):
    """
    Calculate the total bill for chai and samosa

    :param chai: Number of chai cups (10 rupees each)
    :param samosa: NUmber of samosa (15 rupees each)
    : return: (total amount, thank you message as string)
    """
    total = chai*10 + samosa*15
    return total, "Thank you for visiting chaicode.com"

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Accessing function defaults and local variables
print("\n1. Introspecting variables and defaults:")
# __code__ contains the compiled bytecode and metadata, like the names of all local variables
print(f"Local variables in chai_flavor: {chai_flavor.__code__.co_varnames}") # Output: Local variables in chai_flavor: ('flavor', 'chai')
print(f"Default arguments in generate_bill: {generate_bill.__defaults__}") # Output: Default arguments in generate_bill: (0, 0)

# Trick 2: Dynamically modifying Dunder Attributes
print("\n2. Modifying __name__ and __doc__ at runtime:")
# Function attributes are not strictly read-only! You can dynamically change them.
chai_flavor.__name__ = "super_chai_flavor"
chai_flavor.__doc__ = "Returns the ultimate chai flavor."
print(f"New name: {chai_flavor.__name__}") # Output: New name: super_chai_flavor
print(f"New doc: {chai_flavor.__doc__}") # Output: New doc: Returns the ultimate chai flavor.

# Trick 3: Using the 'dir()' built-in
print("\n3. Exploring all properties of an object using dir():")
# dir() returns a list of all attributes and methods (including dunders) available on the object
print(f"Some attributes of generate_bill: {dir(generate_bill)[:5]}") # Output: Some attributes of generate_bill: ['__annotations__', '__builtins__', '__call__', '__class__', '__closure__']

# Trick 4: Accessing Type Annotations programmatically
print("\n4. Accessing __annotations__:")
def typed_chai(cups: int) -> str:
    return f"{cups} cups of chai"
# Type hints are stored in a special dunder dictionary at runtime
print(f"Annotations: {typed_chai.__annotations__}") # Output: Annotations: {'cups': <class 'int'>, 'return': <class 'str'>}

# Trick 5: Advanced Introspection using the `inspect` module
print("\n5. Using the inspect module:")
import inspect
# The standard library's inspect module provides powerful formatting for these built-in properties
sig = inspect.signature(generate_bill)
print(f"Signature of generate_bill: {sig}") # Output: Signature of generate_bill: (chai=0, samosa=0)

"""
--- NOTES: Built-in Function Attributes and Introspection ---

1. Dunder Properties:
   - The filename `12_built_in.py` hints at exploring Python's built-in tools and attributes.
   - Attributes surrounded by double underscores (like `__name__` and `__doc__`) are affectionately called "dunder" (double underscore) or "magic" attributes.
   - `__doc__`: Stores the docstring (the first unassigned string in a function/class body), used for documentation.
   - `__name__`: Stores the original name of the function as a string.

2. Introspection Tools:
   - Python is highly introspective, meaning a program can examine its own structure at runtime.
   - `help(obj)`: Invokes the built-in help system to display the docstring and signature of an object.
   - `dir(obj)`: Returns a list of all valid attributes attached to that object.

3. Latest Python Features:
   - **Docstring dedenting (Python 3.13)**: The Python 3.13 compiler now automatically strips leading indentation from docstrings when creating the `__doc__` attribute. This significantly reduces memory usage across large applications and makes runtime parsing cleaner.
   - **`inspect.get_annotations()` (Python 3.10+)**: Safely retrieves annotations, properly handling the delayed evaluation of type hints (PEP 563) which is heavily used in modern Python development.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What are "dunder" methods or attributes?
A1: "Dunder" stands for "double underscore". They are special, reserved attributes and methods in Python (like `__doc__`, `__init__`, `__str__`) that give objects built-in capabilities or store metadata. They are not meant to be named manually by developers to avoid shadowing core language features.

Q2: How does the `help()` function know what to print?
A2: The `help()` function inspects the object passed to it and primarily reads its `__doc__` attribute. It also looks at the function's signature (`__code__` or using `inspect`) to generate a readable manual page.

Q3: Can you change a function's name while the program is running?
A3: Yes! Functions are first-class objects, and many of their dunder attributes are writable. You can dynamically assign a new string to `func.__name__`. This is routinely done by decorators using `@functools.wraps` to preserve the wrapped function's original identity.

Q4: What is the `__code__` attribute on a function?
A4: The `__code__` attribute contains the compiled bytecode of the function and several read-only metadata properties about it, such as `co_varnames` (a tuple of local variable names) and `co_argcount` (the number of positional arguments).
"""