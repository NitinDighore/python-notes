from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Before function runs")
        func()
        print("After function runs")
    return wrapper

@my_decorator
def greet():
    print("Hello from decorators class from chaicode")


greet() 
# Output:
# Before function runs
# Hello from decorators class from chaicode
# After function runs

print(greet.__name__) # Output: greet

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Decorator Stacking (Multiple Decorators)
print("\n1. Stacking Decorators:")
def bold(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper

# Decorators are applied bottom to top (inside out)
@bold
@italic
def format_text(text):
    return text

print(format_text("Chai")) # Output: <b><i>Chai</i></b>

# Trick 2: Decorators with Arguments
print("\n2. Decorators accepting arguments:")
# Requires an extra layer of nesting to capture the decorator's arguments
def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice") 
# Output:
# Hello, Alice!
# Hello, Alice!
# Hello, Alice!

# Trick 3: Class-based Decorators
print("\n3. Class-based Decorators:")
# Useful for maintaining state (like a call counter)
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0
        wraps(func)(self) # Preserves metadata

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"Call {self.num_calls} of {self.func.__name__!r}")
        return self.func(*args, **kwargs)

@CountCalls
def brew():
    print("Brewing...")

brew() # Output: Call 1 of 'brew' \n Brewing...
brew() # Output: Call 2 of 'brew' \n Brewing...

"""
--- NOTES: Decorators in Python ---

1. What is a Decorator?
   - The folder `09_decorators` introduces one of Python's most powerful metaprogramming features.
   - A decorator is a function that takes another function (or class) as an argument, extends or alters its behavior, and returns a new function, all without explicitly modifying the original function's source code.
   - It heavily relies on functions being "first-class objects" and the concept of closures.
   - The `@decorator_name` syntax is just syntactic sugar for `func = decorator_name(func)`.

2. The importance of `@functools.wraps`:
   - When you wrap a function, the new wrapper function replaces the original. This means the original function loses its identity (its `__name__`, `__doc__`, etc., become that of the wrapper).
   - `@wraps(func)` is a utility decorator that copies the metadata from the original function to the wrapper function, preserving its identity for introspection and debugging.

3. Latest Python Features:
   - **Relaxed Decorator Syntax (Python 3.9+)**: Prior to Python 3.9, the `@` symbol could only be followed by a single named identifier or a function call. Python 3.9 relaxed this grammar (PEP 614), allowing ANY valid Python expression that evaluates to a callable to be used as a decorator. For example, you can now do things like `@buttons[0].clicked.connect` or `@(lambda f: f)`.
   - **Type Hinting Decorators (Python 3.10+)**: Providing correct type hints for decorators used to be incredibly difficult. Python 3.10 introduced `ParamSpec` (PEP 612), which allows static type checkers to accurately forward the argument types and return types of the wrapped function through the decorator.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Explain how decorators are applied when multiple are stacked on a single function.
A1: Decorators are applied from the bottom up (closest to the function definition first). For example:
    @decorator1
    @decorator2
    def func(): pass
    This is evaluated as: `func = decorator1(decorator2(func))`.

Q2: Why do we write `*args, **kwargs` inside the wrapper function of a decorator?
A2: By using `*args` and `**kwargs`, the wrapper function can accept any arbitrary number of positional and keyword arguments. This makes the decorator completely generic and reusable for any function, regardless of its specific signature.

Q3: What happens if you forget to return the `wrapper` function at the end of your decorator?
A3: When Python evaluates the `@decorator` syntax, it replaces the target function with whatever the decorator returns. If the decorator doesn't return anything (i.e., returns `None`), the original function is replaced by `None`. Trying to call it later will result in a `TypeError: 'NoneType' object is not callable`.

Q4: Can you decorate a Class instead of a function?
A4: Yes! Class decorators work exactly like function decorators. They take a class as an argument, modify it (e.g., add new methods, properties, or register it in a system), and return the modified class or a new class. Examples include `@dataclass` or `@staticmethod` (which technically decorates a method).
"""