from functools import wraps

def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"🚀 Calling: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"✅ Finished: {func.__name__}")
        return result
    return wrapper

@log_activity
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status {milk}")

brew_chai("Masala") 
# Output:
# 🚀 Calling: brew_chai
# Brewing Masala chai and milk status no
# ✅ Finished: brew_chai

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Capturing and logging arguments and return values
print("\n1. Capturing Args and Return Values:")
def log_details(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # *args and **kwargs hold the exact inputs passed to the function!
        print(f"[LOG] Executing {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} returned: {result}")
        return result
    return wrapper

@log_details
def add_sugar(cups, spoons=2):
    return f"Added {cups * spoons} spoons of sugar."

add_sugar(3, spoons=1)
# Output:
# [LOG] Executing add_sugar with args=(3,), kwargs={'spoons': 1}
# [LOG] add_sugar returned: Added 3 spoons of sugar.

# Trick 2: Performance Timing Decorator
print("\n2. Performance Logging (Timing execution):")
import time
def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter() # Highly precise timer
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️ {func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@time_it
def slow_brew():
    time.sleep(0.1) # Simulating a delay
    return "Done"

slow_brew() # Output: ⏱️ slow_brew took 0.10XXXX seconds

# Trick 3: Integrating with the built-in logging module
print("\n3. Professional Logging Integration:")
import logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def professional_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"System execution -> {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@professional_logger
def serve():
    pass

serve() # Output: INFO: System execution -> serve

"""
--- NOTES: Decorators for Logging and Monitoring ---

1. Aspect-Oriented Programming (AOP):
   - The filename `02_logging_decorator.py` demonstrates using decorators to separate "cross-cutting concerns." 
   - Logging, timing, and security checks are operations needed across many functions. Instead of copying and pasting `print("starting")` inside every single function body, a decorator extracts this logic to a reusable wrapper, keeping your core business logic clean.

2. Capturing Flow (`func()` vs `return func()`):
   - In `log_activity`, notice we store `result = func(*args, **kwargs)`.
   - If we just wrote `return func(*args, **kwargs)`, the function would end immediately, and we wouldn't be able to run our "✅ Finished" print statement! Capturing the result allows us to execute "post-function" logic before finally handing the result back to the caller.

3. Latest Python Features:
   - **`typing.ParamSpec` (Python 3.10+)**: When writing logging decorators, type hinting the `*args` and `**kwargs` used to lose the original function's signature. With `ParamSpec`, static type checkers can now perfectly pass the arguments and return types through the decorator, retaining full IDE autocompletion for decorated functions!
   - **`sys.monitoring` (Python 3.12+)**: For extremely low-level performance tracking, Python 3.12 introduced the `sys.monitoring` API. For enterprise profiling tools, this is heavily replacing manual timing decorators because it operates with near-zero overhead.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: How do you log the exact arguments a user passed into a decorated function?
A1: Inside the decorator's inner `wrapper` function, you can inspect the `*args` (which is a tuple of positional arguments) and `**kwargs` (which is a dictionary of keyword arguments) directly.

Q2: Why do we assign `result = func(*args, **kwargs)` and return `result` at the end of the wrapper? Why not just return `func(*args, **kwargs)` immediately?
A2: If we return immediately, the `wrapper` function terminates at that exact line. By capturing the output in a `result` variable, we pause the return process, allowing us to execute teardown logic (like logging "Finished", closing database connections, or stopping a timer) before finally sending the result back to the original caller.

Q3: Is it a good idea to use decorators for logging in production applications?
A3: Yes, it is considered a best practice. It strictly adheres to the Single Responsibility Principle (SRP) by keeping logging code completely separate from the core business logic.
"""