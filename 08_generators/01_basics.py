def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

stall = serve_chai()

# for cup in stall:
#     print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

# generator function
def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

chai = get_chai_gen()
print(next(chai)) # Output: Cup 1
print(next(chai)) # Output: Cup 2
print(next(chai)) # Output: Cup 3
# print(next(chai)) # gives error (StopIteration)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Proving Memory Efficiency
print("\n1. Memory Efficiency (List vs Generator):")
import sys
# A list allocates memory for all elements immediately. A generator only allocates memory for its state.
list_data = [x for x in range(100000)]
gen_data = (x for x in range(100000))
print(f"List size: {sys.getsizeof(list_data)} bytes") # Output: ~800000+ bytes
print(f"Generator size: {sys.getsizeof(gen_data)} bytes") # Output: ~200 bytes (Constant small size!)

# Trick 2: Retaining state inside a loop
print("\n2. Yielding inside a loop:")
# Generators remember local variables and execution state between next() calls
def countdown(n):
    while n > 0:
        yield n
        n -= 1
# You can instantly consume a finite generator into a list
print(f"Countdown from 3: {list(countdown(3))}") # Output: Countdown from 3: [3, 2, 1]

# Trick 3: Returning a value from a generator
print("\n3. Return values in generators:")
# In Python 3.3+, generators can `return` a value. This value gets attached to the StopIteration exception!
def gen_with_return():
    yield "Processing..."
    return "Operation Complete!"

g = gen_with_return()
print(next(g)) # Output: Processing...
try:
    next(g)
except StopIteration as e:
    print(f"Generator finished with: {e.value}") # Output: Generator finished with: Operation Complete!

# Trick 4: Unpacking a generator directly
print("\n4. Unpacking a generator into variables:")
# As long as the number of variables matches the exact number of yields, you can unpack them directly!
def get_two_teas():
    yield "Matcha"
    yield "Oolong"

tea1, tea2 = get_two_teas()
print(f"Tea 1: {tea1}, Tea 2: {tea2}") # Output: Tea 1: Matcha, Tea 2: Oolong

"""
--- NOTES: Generators and the `yield` Keyword ---

1. What is a Generator?
   - A generator is a special type of function in Python that returns a lazy iterator.
   - Instead of computing an entire result set at once and returning it (like `get_chai_list`), a generator yields one result at a time, pausing its execution and retaining its local state until the next item is requested.

2. The `yield` Keyword:
   - When Python encounters `yield`, it pauses the function, saves all its local variables and execution state, and returns the yielded value to the caller.
   - When `next()` is called again on the generator object, the function resumes execution immediately *after* the last `yield` statement.

3. Latest Python Features (Python 3.11+):
   - **Zero-Cost Exceptions**: Generators terminate by raising a `StopIteration` exception. In older Python versions, raising and catching exceptions carried a heavy performance penalty. Python 3.11 introduced "zero-cost exceptions", drastically speeding up the completion phase of `for` loops that rely on generators under the hood.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the main difference between `yield` and `return`?
A1: `return` completely terminates the function and destroys its local state. `yield` simply pauses the function, returning a value but keeping the local variables and state intact in memory so the function can resume exactly where it left off on the next call.

Q2: What happens when you call a generator function like `stall = serve_chai()`? Does the code inside the function execute immediately?
A2: No. Calling a generator function does NOT execute its body. It simply returns a generator object. The code inside the function only begins to execute when you explicitly call `next(stall)` or iterate over it using a `for` loop.

Q3: How do you reset a generator once it has been exhausted?
A3: You cannot reset or rewind a generator. Once it raises `StopIteration`, it is permanently exhausted. To iterate over the sequence again, you must call the original generator function to instantiate a brand-new generator object.

Q4: Why are generators considered highly memory efficient?
A4: Because they do not load the entire dataset into memory at once. If you need to process a 5-gigabyte text file line by line, a list would crash your RAM by trying to load all 5GB. A generator will load exactly one line, yield it, and discard it, using a tiny, constant amount of memory regardless of the file's size.
"""