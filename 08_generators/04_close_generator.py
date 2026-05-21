def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha"
    yield "Oolong"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai) # Output: Masala Chai, then Ginger Chai, then Matcha, then Oolong


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, No more chai") # Output (triggered by .close()): Stall closed, No more chai


stall = chai_stall()
print(next(stall)) # Output: Waiting for chai order
stall.close() #cleanup

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: 'yield from' with standard iterables
print("\n1. yield from with standard iterables:")
def flatten_list():
    yield from ["Tea", "Coffee"]
    yield from "Cup" # Strings are iterables too!

print(list(flatten_list())) # Output: ['Tea', 'Coffee', 'C', 'u', 'p']

# Trick 2: Proper GeneratorExit handling
print("\n2. Catching GeneratorExit explicitly:")
def proper_cleanup_stall():
    try:
        yield "Open for business"
    except GeneratorExit:
        # This is the explicit exception raised by .close()
        print("Gracefully closing the stall. Cleaning up resources.")

stall2 = proper_cleanup_stall()
next(stall2)
stall2.close() # Output: Gracefully closing the stall. Cleaning up resources.

# Trick 3: Catching return values from subgenerators
print("\n3. Catching return values with yield from:")
def sub_generator():
    yield "Brewing..."
    return "Done!"

def main_generator():
    result = yield from sub_generator() # Captures the 'return' value from the subgenerator
    print(f"Subgenerator returned: {result}")
    yield "Serving!"

list(main_generator()) # Output: Subgenerator returned: Done!

# Trick 4: Auto-closing generators using contextlib
print("\n4. Context Manager for Generators:")
from contextlib import closing

def temporary_stall():
    try:
        yield "Quick tea"
    except GeneratorExit:
        print("Temporary stall dismantled.")

with closing(temporary_stall()) as ts:
    print(next(ts)) # Output: Quick tea
# ts.close() is called automatically upon exiting the 'with' block! Output: Temporary stall dismantled.

"""
--- NOTES: `yield from` and Generator Cleanup ---

1. Delegating to Subgenerators (`yield from`):
   - Introduced in Python 3.3 (PEP 380), `yield from iterable` is a powerful shortcut. 
   - It is functionally equivalent to `for item in iterable: yield item`, but it does much more. It establishes a transparent, two-way communication channel between the caller and the subgenerator, automatically passing `.send()`, `.throw()`, and `.close()` calls directly to the inner generator.

2. Generator Cleanup (`.close()`):
   - The `.close()` method is used to gracefully terminate a generator.
   - When called, it raises a `GeneratorExit` exception inside the generator at the exact point where it is currently paused.
   - This allows the generator to run `try...finally` or `except GeneratorExit` blocks to release resources (like closing open files, network sockets, or database connections).

3. Latest Python Features (Python 3.11+):
   - **Zero-Cost Exceptions**: Because `.close()` explicitly relies on throwing a `GeneratorExit` exception, the introduction of zero-cost exceptions in Python 3.11 made shutting down generators and cleaning up resources significantly faster under the hood.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the benefit of `yield from gen` over `for x in gen: yield x`?
A1: While both output the same sequence, `yield from` automatically handles the complex edge cases of bidirectional communication. If the caller uses `.send()` or `.throw()`, `yield from` routes them directly to the subgenerator. Doing that manually with a `for` loop requires heavily nested `try/except` boilerplate code.

Q2: Why is it considered bad practice to use a bare `except:` to handle `.close()`, as seen in the original `chai_stall()` function?
A2: A bare `except:` catches `BaseException`, which includes system-level events like `KeyboardInterrupt` (Ctrl+C). It is always safer and more explicit to catch `GeneratorExit` directly, or even better, use a `try...finally` block to guarantee cleanup happens regardless of how the generator terminates.

Q3: What happens if a generator catches `GeneratorExit`, ignores it, and tries to `yield` another value?
A3: Python will raise a `RuntimeError: generator ignored GeneratorExit`. Once `.close()` is called on a generator, it is strictly forbidden from yielding any more values. It must terminate immediately.

Q4: Can `yield from` be used with regular lists or strings?
A4: Yes! `yield from` works with ANY iterable object in Python, not just other generators. It will simply iterate over the collection and yield its elements one by one.
"""