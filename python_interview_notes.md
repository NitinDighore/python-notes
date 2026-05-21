# Comprehensive Python Interview Notes

This guide is synthesized from your complete Python codebase and supplemented with interview-focused explanations, tips, and best practices. Use this to review concepts before a Python interview.

## 1. Data Types & Structures (`02_datatypes`)

Python has dynamically typed variables. The core built-in structures are highly optimized.

*   **Basic Types**: `int`, `float`, `str`, `bool`, `NoneType`.
*   **Complex/Collection Types**:
    *   **List (`[]`)**: Ordered, mutable, allows duplicates.
    *   **Tuple (`()`)**: Ordered, **immutable**, allows duplicates. Faster and more memory-efficient than lists.
    *   **Set (`{}`)**: Unordered, mutable, **no duplicates**. Uses hash tables (O(1) lookups).
    *   **Dictionary (`{k: v}`)**: Ordered (since Python 3.7), mutable, key-value pairs. Keys must be immutable/hashable.

> **Interview Tip:** Always know the difference between Mutability and Immutability. Strings and Tuples are immutable; if you "modify" them, you are actually creating a new object in memory. Know the time complexities (Big-O) of common operations (e.g., checking `if x in list` is O(n), but `if x in set` is O(1)).

## 2. Conditionals & Control Flow (`03_conditionals`)

*   **Standard structures**: `if`, `elif`, `else`.
*   **Truthy & Falsy**: Empty lists `[]`, dictionaries `{}`, sets `set()`, strings `""`, `0`, `0.0`, and `None` evaluate to `False`. Everything else is generally `True`.
*   **Ternary Operator**: `x = a if condition else b`
*   **Match-Case** (Python 3.10+): Structural pattern matching, similar to `switch/case` in other languages but more powerful (can unpack sequences and dictionaries).

## 3. Loops & Iteration (`04_loops`)

*   **`for` and `while` loops**: Used for iteration. `break` exits the loop, `continue` skips the current iteration, `pass` is a null operation placeholder.
*   **`for-else` / `while-else`**: A unique Python feature. The `else` block executes *only if* the loop completes naturally (i.e., it was NOT terminated by a `break` statement).
*   **Walrus Operator (`:=`)** (Python 3.8+): Assignment expression. Assigns and returns a variable in the same expression.
    ```python
    if (n := len(my_list)) > 10:
        print(f"List is too long ({n} elements)")
    ```

> **Interview Tip:** The `for-else` construct is a common trivia question. Remember: `else` means "no break".

## 4. Functions & Scope (`05_functions`)

*   **Parameters & Arguments**:
    *   Positional vs. Keyword arguments.
    *   `*args` (Tuple of positional arguments) and `**kwargs` (Dictionary of keyword arguments).
*   **Scope & LEGB Rule**: Python resolves variables in this order: **L**ocal -> **E**nclosing -> **G**lobal -> **B**uilt-in.
*   **`global` and `nonlocal`**:
    *   `global`: Used inside a function to modify a global variable.
    *   `nonlocal`: Used inside nested functions to modify a variable in the enclosing (non-global) scope.
*   **Closures**: A nested function that remembers the state of its enclosing environment even if the outer function has finished executing.

## 5. Comprehensions (`07_comprehensions`)

Comprehensions provide a concise way to create collections. They are often faster than using `for` loops and `append()`.

*   **List Comprehension**: `[x**2 for x in range(10) if x % 2 == 0]`
*   **Set Comprehension**: `{x for x in data}`
*   **Dict Comprehension**: `{k: v for k, v in data.items()}`
*   **Generator Expression**: `(x**2 for x in range(10))` -> *Does not create a tuple, creates a generator object.*

> **Interview Tip:** When dealing with large datasets, prefer generator expressions over list comprehensions to save memory (lazy evaluation).

## 6. Generators (`08_generators`)

*   Generators are functions that use the `yield` keyword instead of `return`.
*   They return a generator iterator, pausing execution and saving local state when `yield` is hit, and resuming when `next()` is called.
*   **Benefits**: Extremely memory-efficient. Great for infinite sequences or reading massive files line-by-line.
*   **Advanced**: You can send data *into* a generator using `gen.send(value)`, close it with `gen.close()`, or throw exceptions inside it with `gen.throw()`.

## 7. Decorators (`09_decorators`)

*   A decorator is a function that takes another function and extends its behavior without explicitly modifying it. (Based on closures and higher-order functions).
*   Common use cases: Logging, timing, authentication/authorization, caching (`functools.lru_cache`).
*   **Syntax**: `@decorator_name` above the function definition.
*   **`functools.wraps`**: Always use `@wraps(func)` inside your decorator to preserve the original function's metadata (like `__name__` and `__doc__`).

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Before execution")
        result = func(*args, **kwargs)
        print("After execution")
        return result
    return wrapper
```

## 8. Object-Oriented Programming (OOP) (`10_oop`)

*   **Classes and Instances**: `__init__` is the initializer, not strictly the constructor (`__new__` is the constructor). `self` refers to the instance.
*   **Inheritance**: Subclassing another class. Python supports Multiple Inheritance.
*   **MRO (Method Resolution Order)**: The order Python looks for a method in a hierarchy of classes (C3 Linearization algorithm). Accessible via `ClassName.mro()` or `ClassName.__mro__`.
*   **Magic/Dunder Methods**: E.g., `__str__` (readable string for users), `__repr__` (unambiguous string for developers), `__len__`, `__eq__`.
*   **Decorators in OOP**:
    *   `@staticmethod`: Doesn't take `self` or `cls`. Just a normal function attached to the class namespace.
    *   `@classmethod`: Takes `cls` as the first argument. Often used as alternative constructors.
    *   `@property`: Turns a method into a read-only attribute ("getter"). Can be paired with `@property_name.setter`.
*   **Attribute Shadowing**: Instance attributes take precedence over class attributes with the same name.

## 9. Exception Handling (`11_exceptions`)

*   **Structure**: `try`, `except`, `else`, `finally`.
    *   `else`: Runs only if *no* exception was raised in the `try` block.
    *   `finally`: Runs *always*, useful for resource cleanup (closing files, DB connections).
*   **Custom Exceptions**: Create by inheriting from the base `Exception` class.

> **Interview Tip:** Never use a bare `except:`. Always catch specific exceptions (e.g., `except ValueError:`) to avoid swallowing expected system errors like `KeyboardInterrupt`.

## 10. Concurrency & Threads (`12_threads_concurrency`)

*   **GIL (Global Interpreter Lock)**: A mutex in CPython that allows only one thread to execute Python bytecodes at a time. This means multi-threading in Python does NOT run concurrently for CPU-bound tasks.
*   **Threading**: Best for **I/O-bound tasks** (network requests, file reading/writing), where threads spend time waiting.
*   **Multiprocessing**: Bypasses the GIL by creating entirely new processes (each with its own Python interpreter and memory). Best for **CPU-bound tasks** (heavy math, data processing).
*   **Synchronization Primitives**: Locks, Queues, Semaphores (to prevent Race Conditions and Deadlocks).

> **Interview Tip:** The GIL is one of the most frequently asked Python interview topics. Be ready to explain it and how to bypass it (multiprocessing, C extensions, or using `asyncio` for concurrent I/O).

## 11. Asynchronous Python (`13_async_python`)

*   Uses `async def` and `await`.
*   Built on the concept of an **Event Loop**.
*   **Coroutines**: Functions defined with `async def`. They don't run until awaited or scheduled as a task.
*   **Async vs. Threading**: Async is often lighter and faster for massive concurrent I/O operations (like thousands of websocket connections) because it handles switching at the application level rather than the OS level (context switching overhead).
*   Concurrency hazards (Race Conditions, Deadlocks) still exist in async code if awaiting improperly or sharing state without async primitives.

## 12. Pydantic (`14_pydantic`)

Pydantic provides data validation and settings management using Python type hints. Heavily used in modern frameworks like FastAPI.

*   **BaseModel**: Core class to inherit from.
*   **Validation**: It guarantees that the types and constraints you define are strictly enforced. (e.g., if you specify an `int` and pass `"123"`, it coerces it to `123`; if you pass `"abc"`, it raises a Validation error).
*   **Nested Models**: You can use Pydantic models as types inside other Pydantic models.
*   **Serialization**: Easy conversion to and from JSON (`model_dump()`, `model_validate_json()`).

## General Best Practices & Interview Advice

1.  **Readability Counts**: Follow PEP 8 (Python's style guide). Use meaningful variable names.
2.  **Built-in Functions**: Be familiar with `enumerate()`, `zip()`, `map()`, `filter()`, `all()`, `any()`.
3.  **Context Managers (`with` statement)**: Used for resource management. Implementing custom ones requires defining `__enter__` and `__exit__` dunder methods.
4.  **Copying**: Understand the difference between `copy` (Shallow copy) and `deepcopy` (Deep copy) in the `copy` module.
5.  **Memory Management**: Python uses Reference Counting and a Garbage Collector (to detect reference cycles).

---
*Good luck with your interview preparation! Review the code examples in your workspace to see these concepts in action.*