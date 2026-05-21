def add_vat(price, vat_rate):
    return price * (100 + vat_rate)/100


orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}") 
    # Output:
    # Original: 100, Final with VAT: 110.0
    # Original: 150, Final with VAT: 165.0
    # Original: 200, Final with VAT: 220.0

print("\n--- TRICK CODING EXAMPLES (TRACING & DEBUGGING) ---")

# Trick 1: The f-string debug trick (Python 3.8+)
print("\n1. Quick tracing with f-string '=' specifier:")
# Adding an '=' inside an f-string prints both the variable name and its value, perfect for fast tracing!
sample_price = 450
print(f"{sample_price=} | {add_vat(sample_price, 5)=}") 
# Output: sample_price=450 | add_vat(sample_price, 5)=472.5

# Trick 2: Tracing function calls with a Decorator
print("\n2. Tracing execution using a Decorator:")
import functools

def trace_calls(func):
    """A decorator that prints the exact arguments and return values of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[TRACE] Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[TRACE] {func.__name__} returned {result}")
        return result
    return wrapper

@trace_calls
def multiply(a, b):
    return a * b

multiply(3, 4) 
# Output: 
# [TRACE] Calling multiply with args=(3, 4), kwargs={}
# [TRACE] multiply returned 12

# Trick 3: Using the built-in logging module instead of print()
print("\n3. Using logging for professional tracing:")
import logging
# Configuring logging to show DEBUG level messages and above
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')
logging.debug(f"Calculated VAT for 100: {add_vat(100, 10)}")
# Output: DEBUG: Calculated VAT for 100: 110.0

"""
--- NOTES: Tracing and Debugging Functions ---

1. What is Tracing?
   - The filename `05_trace.py` highlights the concept of tracking the execution flow and state of variables in a program.
   - Tracing helps identify logical errors (bugs) by letting you see exactly what data is passed into a function and what comes out.
   - While `print()` is the most common beginner tool for tracing, professional software relies on debuggers (like the built-in `pdb`), logging modules, or dedicated tracing decorators.

2. Latest Python Features (Tracing & Debugging):
   - **f-string debug specifier `=` (Python 3.8+)**: As shown in Trick 1, `f"{var=}"` makes quick print debugging incredibly efficient, saving you from writing `print(f"var: {var}")`.
   - **Fine-grained Error Tracebacks (Python 3.11+)**: When an error occurs, Python 3.11+ tracebacks point directly to the *exact* expression that caused the error (using squiggly lines `^^^^^`), not just the line number. This drastically reduces the need for manual `print` tracing to find where a bad value came from.
   - **Low Impact Monitoring - PEP 669 (Python 3.12+)**: Python 3.12 introduced `sys.monitoring`, an API for profilers and debuggers to trace execution with near-zero performance overhead, replacing the older, slower `sys.settrace()` backend.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why should you use the `logging` module instead of `print()` for tracing issues in a production application?
A1: `print()` outputs everything to standard output indiscriminately, which can severely clutter logs. The `logging` module allows you to set severity levels (DEBUG, INFO, WARNING, ERROR, CRITICAL), redirect output to specific files, format timestamps, and easily turn off debug messages in production without having to delete the underlying code.

Q2: What is the `pdb` module in Python and how do you trigger it?
A2: `pdb` is the built-in Python Debugger. It allows you to pause program execution at a specific line, step through code line by line, inspect variable states, and dynamically execute Python code in that exact frozen context. In modern Python (3.7+), you can trigger it simply by calling the built-in `breakpoint()` function anywhere in your code.

Q3: How does a decorator help with tracing function calls?
A3: A decorator acts as a wrapper around a function. By wrapping a function, you can automatically execute monitoring code (like printing the arguments or measuring the execution time) right before and right after the target function runs. This keeps your actual business logic completely clean and separates the debugging logic from the function itself.
"""