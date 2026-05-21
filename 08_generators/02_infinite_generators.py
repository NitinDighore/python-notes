def infinite_chai():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_chai()
user2 = infinite_chai()

for _ in range(5):
    print(next(refill)) # Output: Refil #1, Refil #2, Refil #3, Refil #4, Refil #5

for _ in range(6):
    print(next(user2)) # Output: Refil #1, Refil #2, Refil #3, Refil #4, Refil #5, Refil #6 (user2 has its own isolated state!)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Safely grabbing a chunk from an infinite generator using itertools.islice
print("\n1. Slicing Infinite Generators:")
import itertools
# islice allows you to slice an iterator just like a list, stopping it from evaluating infinitely!
first_three = list(itertools.islice(infinite_chai(), 3))
print(f"First 3 refills: {first_three}") # Output: ['Refil #1', 'Refil #2', 'Refil #3']

# Trick 2: The built-in infinite generator (itertools.count)
print("\n2. itertools.count():")
# Python has its own highly optimized C-level infinite generator inside the itertools module!
counter = itertools.count(start=10, step=5)
print(f"Count: {next(counter)}, {next(counter)}, {next(counter)}") # Output: Count: 10, 15, 20

# Trick 3: Conditionally stopping an infinite stream using itertools.takewhile
print("\n3. Stopping with takewhile:")
# takewhile consumes the infinite generator ONLY while a condition remains True
evens = (x for x in itertools.count(2, 2)) # Infinite generator of even numbers
under_ten = list(itertools.takewhile(lambda x: x < 10, evens))
print(f"Evens under 10: {under_ten}") # Output: [2, 4, 6, 8]

# Trick 4: Pipelining Infinite Generators
print("\n4. Pipelining Infinite Streams:")
# You can map transformations over an infinite generator. They evaluate lazily!
raw_stream = infinite_chai()
uppercase_stream = (cup.upper() for cup in raw_stream) # This is a new infinite, lazy generator
print(f"Piped: {next(uppercase_stream)}, {next(uppercase_stream)}") # Output: Piped: REFIL #1, REFIL #2

"""
--- NOTES: Infinite Generators ---

1. What are Infinite Generators?
   - An infinite generator is a generator function containing a loop that never terminates (like `while True:`).
   - Because generators evaluate lazily (one step at a time via `yield`), they can model infinite sequences (like counting to infinity, reading a continuous live data stream, or generating infinite random numbers) without ever crashing the system's memory.

2. Isolated State:
   - As shown with `refill` and `user2`, every time you call a generator function, it returns a brand-new, completely independent generator object. The `count` variable in `user2` does not interfere with the `count` variable in `refill`.

3. Latest Python Features:
   - **`itertools.batched` (Python 3.12+)**: Itertools continues to get powerful upgrades for working with iterators. `batched()` allows you to safely grab chunks of an infinite stream. For example, `next(itertools.batched(infinite_chai(), 5))` will instantly yield the first 5 elements as a tuple, making continuous stream processing incredibly elegant.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why doesn't an infinite generator cause a `MemoryError` in Python?
A1: Because it relies on lazy evaluation. It doesn't attempt to generate and store all infinite values in memory at once. It only stores its local state and computes the single next value exactly when `next()` is called. 

Q2: What happens if you run `list(infinite_chai())`?
A2: It will cause an infinite loop and eventually crash your program. The `list()` constructor tries to consume the entire iterator until a `StopIteration` exception is raised. Since `infinite_chai()` never raises `StopIteration`, `list()` will continuously append items until it consumes all available system RAM, throwing a `MemoryError`.

Q3: If you can't use `list()` or standard `for` loops blindly on an infinite generator, how do you consume them safely?
A3: You can consume them safely by:
    1) Manually calling `next(gen)` a fixed number of times.
    2) Using a `for` loop but ensuring there is a conditional `break` statement inside the loop block.
    3) Using tools from the `itertools` library like `islice()` to grab a specific chunk or `takewhile()` to stop dynamically.

Q4: Can you use functions like `sum()`, `max()`, or `min()` on an infinite generator?
A4: No. Just like the `list()` constructor, mathematical aggregators require iterating through the entire sequence to find the final total or maximum value. Passing an infinite generator to `sum()` will result in an infinite loop.
"""