# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


value = 13

if remainder := value % 5:
    print(f"Not divisible, remainder is {remainder}") # Output: Not divisible, remainder is 3


# available_sizes = ["small", "medium", "large"]

# if (requested_size := input("Enter your chai cup size: ")) in available_sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")



flavors = ["masala", "ginger", "lemon", "mint"]

print("Available flavors: ", flavors) # Output: Available flavors:  ['masala', 'ginger', 'lemon', 'mint']

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available") # Output: Sorry, [user input] is not available (if not in list)

print(f"You choose {flavor} chai") # Output: You choose [user input] chai (when a valid flavor is entered)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: List Comprehension Optimization
print("\n1. List Comprehensions:")
# Without walrus, you often call an expensive function twice: once to filter, once to store.
# With walrus, you evaluate it once, filter it, and store it.
numbers = [2, 8, 1, 9, 3]
def expensive_func(n): return n ** 2
results = [res for n in numbers if (res := expensive_func(n)) > 20]
print(f"Results > 20: {results}") # Output: Results > 20: [64, 81]

# Trick 2: Capturing Regex Matches
print("\n2. Capturing Regex Matches:")
import re
text = "Order id: 54321"
# Captures the regex object and checks if it matched in a single clean line
if match := re.search(r"id: (\d+)", text):
    print(f"Found ID: {match.group(1)}") # Output: Found ID: 54321

# Trick 3: any() / all() with capture
print("\n3. any() with capture:")
# any() short-circuits. The walrus operator captures the EXACT item that caused it to evaluate to True!
values = [0, False, '', "Chai", 0.0]
if any((truthy_val := v) for v in values):
    print(f"First truthy value found: {truthy_val}") # Output: First truthy value found: Chai

# Trick 4: Chunk processing / Iterator depletion
print("\n4. Draining an iterator/list:")
data = [10, 20, 30]
# Often used for files: `while chunk := file.read(1024):`. Here we emulate it with list popping.
while data and (item := data.pop(0)):
    print(f"Processed: {item}") # Output: Processed: 10, then 20, then 30

"""
--- NOTES: Assignment Expressions (The Walrus Operator `:=`) ---

1. What is the Walrus Operator?
   - Introduced in Python 3.8 (PEP 572), the assignment expression operator `:=` (affectionately called the walrus operator because it looks like a walrus on its side) allows you to assign a value to a variable and return that value in the same expression.
   - Its primary purpose is to reduce code duplication, tighten scope, and improve readability in `while` loops, `if` statements, and comprehensions.

2. Why not just use `=`?
   - Python strictly separates statements (like `x = 5`) and expressions (like `x == 5`). This prevents a very common bug found in C or JavaScript where a developer types `if (x = 5)` meaning to type `if (x == 5)`. 
   - By creating a distinctly new operator (`:=`), Python allows assignments inside expressions safely, making the developer's intent explicit.

3. Latest Python Features:
   - **Pattern Matching Integration (Python 3.10+)**: The walrus operator pairs extremely well with the new structural pattern matching `match-case` blocks. You can use it inside a "guard" clause. 
     Example: `case _ if (m := re.match(pattern, text)): print(m.group())`
   - **Exception Group Catching (Python 3.11+)**: You can use the walrus operator to capture and act on specific grouped exceptions in a single step using the new `except*` syntax.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What version of Python introduced the `:=` operator, and what is its formal name?
A1: It was introduced in Python 3.8 and is formally known as the "Assignment Expression" operator.

Q2: Can you use the walrus operator for a standalone assignment? Example: `x := 5`.
A2: No. Standalone assignment using the walrus operator without parentheses is a `SyntaxError`. It is designed specifically to be used *inside* other expressions. If you want to force it standalone, you must wrap it in parentheses: `(x := 5)`, though this is heavily discouraged over standard `x = 5`.

Q3: How does the walrus operator optimize list comprehensions?
A3: If you have a comprehension like `[func(x) for x in data if func(x) > 10]`, Python executes `func(x)` twice for every element that passes the condition. Using the walrus operator: `[y for x in data if (y := func(x)) > 10]` stores the result during the conditional check and reuses it for the output, cutting the function calls in half.

Q4: Is there any difference in variable scope when using the walrus operator in comprehensions?
A4: Yes! Variables assigned via `=` inside a list comprehension (which is technically not possible directly) would be tightly bound. However, the variable created by the walrus operator `:=` inside a list or dict comprehension "leaks" out into the enclosing scope, remaining accessible after the comprehension finishes.
"""