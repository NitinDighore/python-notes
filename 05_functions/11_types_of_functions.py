def pure_chai(cups):
    return cups * 10

total_chai = 0

# not recommended
def impure_chai(cups):
    global total_chai
    total_chai += cups


def pour_chai(n):
    print(n)
    if n == 0:
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(3))
# Output:
# 3
# 2
# 1
# 0
# All cups poured


chai_types = ["light", "kadak", "ginger", "kadak"]


strong_chai = list(filter(lambda chai: chai!="kadak", chai_types))

print(strong_chai) # Output: ['light', 'ginger']

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Recursive Memoization
print("\n1. Recursive Memoization with functools.cache:")
import functools
@functools.cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(f"100th Fibonacci: {fibonacci(100)}") # Output: 100th Fibonacci: 354224848179261915075 (Calculated instantly!)

# Trick 2: Immediately Invoked Function Expression (IIFE) with Lambdas
print("\n2. IIFE (Immediately Invoked Function Expression):")
# You can define and execute a lambda function in a single line
greeting = (lambda name: f"Hello, {name}!")("Alice")
print(greeting) # Output: Hello, Alice!

# Trick 3: Lambda with map and reduce
print("\n3. Lambda with map() and reduce():")
from functools import reduce
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, nums))
product = reduce(lambda x, y: x * y, nums)
print(f"Squared: {squared}, Product: {product}") # Output: Squared: [1, 4, 9, 16], Product: 24

# Trick 4: Sorting using a lambda key
print("\n4. Custom sorting with lambda:")
users = [{"name": "Aman", "age": 25}, {"name": "Zane", "age": 20}, {"name": "Meera", "age": 30}]
users.sort(key=lambda u: u["age"])
print(f"Sorted by age: {users}") # Output: Sorted by age: [{'name': 'Zane', 'age': 20}, {'name': 'Aman', 'age': 25}, {'name': 'Meera', 'age': 30}]

"""
--- NOTES: Types of Functions ---

1. Pure vs Impure Functions:
   - **Pure Functions**: Always return the same output for the same input and have no side effects (they don't modify global variables, write to files, etc.). `pure_chai` is a pure function.
   - **Impure Functions**: Rely on or modify state outside their local scope (side effects). `impure_chai` changes the global `total_chai` variable, making it impure. Pure functions are strongly preferred for testability and predictable behavior.

2. Recursive Functions:
   - A function that calls itself to solve smaller instances of the same problem.
   - Crucial Rule: Every recursive function must have a "Base Case" (e.g., `if n == 0:`), otherwise it will run infinitely until it hits Python's maximum recursion depth (causing a `RecursionError`).

3. Lambda Functions (Anonymous Functions):
   - Created using the `lambda` keyword.
   - Syntax: `lambda arguments: expression`
   - They are restricted to a single expression. They cannot contain assignments or multiple statements.
   - Most commonly used as short throwaway functions for `filter()`, `map()`, or custom `sort()` keys.

4. Latest Python Features:
   - **`functools.cache` (Python 3.9+)**: A simpler, faster alternative to `lru_cache(maxsize=None)`. It is incredibly useful for recursive functions, turning exponential time complexity (like raw Fibonacci) into linear time complexity by memorizing previously computed results.
   - **No Tail Call Optimization (TCO)**: Unlike functional languages (like Haskell or Scheme), Python deliberately does *not* optimize tail-recursive functions. Guido van Rossum chose to keep the stack trace intact for better debugging. If you recurse too deeply (default usually 1000 calls), Python will crash.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is a Pure Function, and why is it beneficial?
A1: A pure function is a function where the return value is only determined by its input values, without observable side effects. This makes them highly predictable, extremely easy to unit test, and safe for parallel execution.

Q2: What causes a `RecursionError` in Python?
A2: It is caused when a recursive function fails to hit its base case and continuously calls itself until it exceeds Python's maximum recursion depth limit (typically 1000). You can increase this limit via `sys.setrecursionlimit()`, but hitting the limit usually indicates a logical bug.

Q3: Can a lambda function contain multiple expressions or a `return` statement?
A3: No. A lambda function can only contain a single expression. It implicitly returns the evaluated result of that expression, so writing the `return` keyword explicitly inside a lambda will cause a `SyntaxError`.

Q4: What is memoization?
A4: Memoization is an optimization technique used primarily to speed up computer programs by storing the results of expensive function calls and returning the cached result when the same inputs occur again. It's heavily used in recursive algorithms (like dynamic programming).
"""