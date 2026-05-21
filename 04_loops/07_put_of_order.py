flavours = ["Ginger", "Out of Stock", "Lemon", "Discontinued", "Tulsi"]


for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        print(f"{flavour} item found") # Output: Discontinued item found (and then exits the loop entirely)
        break
    print(f"{flavour} item found") # Output: Ginger item found, then Lemon item found
    
print(f"Out side of loop") # Output: Out side of loop

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The 'for-else' connection with 'break'
print("\n1. How break affects for-else:")
# The else block in a loop executes ONLY if the loop finishes naturally. If 'break' is triggered, 'else' is skipped.
for item in ["A", "B", "C"]:
    if item == "B":
        break
else:
    print("This will NOT print because of the break statement.")

# Trick 2: 'continue' vs 'pass'
print("\n2. Difference between continue and pass:")
for num in [1, 2, 3]:
    if num == 2:
        pass # 'pass' does nothing, just acts as a placeholder. Execution continues to the next line.
        # print("Pass executed")
    if num == 3:
        continue # 'continue' immediately skips the rest of the block and goes to the next iteration.
    print(f"Processing number: {num}") # Output: Processing number: 1, Processing number: 2

# Trick 3: Breaking out of nested loops
print("\n3. Breaking out of nested loops:")
# A single 'break' only exits the innermost loop. 
for outer in [1, 2]:
    for inner in ["A", "B"]:
        if inner == "A":
            break # This only breaks the 'inner' loop. The 'outer' loop continues.
    print(f"Outer loop completed for: {outer}") # Output: Outer loop completed for: 1, then 2

# Trick 4: Simulating multi-level break using exceptions (Hack)
print("\n4. Breaking multiple loops using exceptions:")
# Since Python lacks labeled breaks (like Java/JavaScript), exceptions can be used to break out of deep nesting.
class BreakLoop(Exception): pass

try:
    for x in range(5):
        for y in range(5):
            if x == 1 and y == 1:
                raise BreakLoop
except BreakLoop:
    print(f"Successfully broke out of both loops at x={x}, y={y}") # Output: Successfully broke out of both loops at x=1, y=1

"""
--- NOTES: Loop Control Statements (`break`, `continue`, `pass`) ---

1. Control Flow Tools:
   - `break`: Completely exits the current loop, skipping any remaining iterations and the `else` block (if present).
   - `continue`: Skips the rest of the code inside the current iteration and jumps directly to the evaluation of the next iteration of the loop.
   - `pass`: A null operation that does absolutely nothing. It is used as a syntactic placeholder when a statement is required syntactically but you don't want any command or code to execute.

2. Behavior in Nested Loops:
   - `break` and `continue` only ever apply to the nearest (innermost) enclosing loop. They do not break out of outer loops.

3. Latest Python Features:
   - **Performance Improvements (Python 3.11+)**: While `break` and `continue` syntactically remain unchanged in modern Python, Python 3.11's Adaptive Interpreter handles loop control flows much more efficiently. Furthermore, "Zero-cost exceptions" in Python 3.11+ mean that using exceptions to simulate deep multi-level loop breaks (as shown in Trick 4) is practically cost-free in terms of overhead until the exception is actually raised.
   - **No Labeled Breaks**: Unlike JavaScript or Java, Python continues to deliberately omit "labeled breaks" (e.g., `break outerLoop`). PEP 3136 proposed this but was rejected by Guido van Rossum to maintain language simplicity.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the main difference between `pass` and `continue`?
A1: `pass` does nothing and lets execution continue to the immediate next line of code inside the loop. `continue` immediately halts the current iteration, ignores the remaining lines in the loop block, and jumps to the next item in the iterable.

Q2: Does `break` exit all nested loops?
A2: No. `break` only exits the innermost loop in which it is executed. To exit multiple nested loops, you must use flag variables, return early from a function, or raise a custom exception.

Q3: How does the `break` statement affect a `for...else` or `while...else` loop?
A3: If a `break` statement is executed, the `else` block belonging to the loop is completely skipped. The `else` block only runs if the loop exhausts its iterable naturally (or the `while` condition evaluates to `False`).

Q4: Can you use `break` or `continue` outside of a loop?
A4: No, `break` and `continue` can only be used inside `for` or `while` loop blocks. Using them outside a loop will result in a `SyntaxError`.
"""