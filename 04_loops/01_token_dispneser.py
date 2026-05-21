for token in range(1, 11):
    print(f"Serving chai to Token #{token}") # Output: Serving chai to Token #1, Token #2 ... up to Token #10

"""
--- NOTES: `for` loops and `range()` ---

1. What is a `for` loop in Python?
   - Unlike traditional C-style `for` loops (e.g., `for(int i=0; i<10; i++)`), Python's `for` loops act as iterators. They iterate over elements of a sequence (like a list, tuple, or string) or any other iterable object in the order they appear.
   
2. The `range()` Function:
   - `range(start, stop, step)` generates a sequence of numbers.
   - `start` (optional, defaults to 0): The starting value.
   - `stop` (required): The loop stops *before* reaching this value. So `range(1, 11)` goes from 1 to 10.
   - `step` (optional, defaults to 1): The increment size (can be negative for counting down).
   - `range()` creates a "lazy" iterable object. It doesn't generate all the numbers in memory at once; it generates them on the fly, which makes it extremely memory efficient regardless of the size.

3. Latest Python Features Related to Loops:
   - **Performance (Python 3.11+)**: Python 3.11 introduced the "Specializing Adaptive Interpreter" (PEP 659). Under the hood, this significantly speeds up `for` loops and overall execution by adapting instructions dynamically during runtime to optimize for the specific data types being processed.
   - **`itertools.pairwise` (Python 3.10+)**: A fantastic new addition to the `itertools` standard library that allows you to easily iterate over sliding windows of pairs in a loop (e.g., `for a, b in pairwise(iterable):`).

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What does `range(1, 11)` actually return? Does it return a list?
A1: No, it does not return a list. It returns a `range` object, which is a specialized immutable sequence type. It generates the numbers on demand during iteration rather than storing them all in memory.

Q2: How does a `for` loop work under the hood in Python?
A2: Python's `for` loop implicitly calls the `iter()` function on the iterable object to obtain an iterator. It then repeatedly calls the `next()` function on that iterator to get the next element until a `StopIteration` exception is raised, at which point the loop cleanly terminates.

Q3: What is the difference between `range()` in Python 3 and `xrange()` in Python 2?
A3: In Python 2, `range()` returned a fully populated list in memory, which was very inefficient for large loops, while `xrange()` returned a memory-efficient generator-like object. In Python 3, `xrange()` was simply renamed to `range()` and the old list-generating `range()` was completely removed. 

Q4: Can you modify the loop variable (e.g., `token`) inside a Python `for` loop to skip iterations or control flow?
A4: You can assign a new value to the loop variable inside the block, but it won't affect the loop's overall iteration process. The `for` loop will simply overwrite your change on the next iteration with the next value fetched from the iterable. To control loop flow, you must use statements like `continue` or `break`.
"""