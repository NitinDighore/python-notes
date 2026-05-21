temperature = 40

while temperature < 100:
    print(f"Current temperature: {temperature}") # Output: Current temperature: 40, then 55, then 70, then 85
    # temperature = temperature + 15
    temperature += 15

print("Tea is ready to boil") # Output: Tea is ready to boil

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The 'while-else' loop
print("\n1. The while-else construct:")
# The else block executes ONLY if the loop finishes naturally (condition becomes False), NOT if interrupted by a 'break'.
count = 0
while count < 3:
    count += 1
else:
    print("Loop finished naturally without a break statement.") # Output: Loop finished naturally without a break statement.

# Trick 2: Emulating a 'do-while' loop
print("\n2. Emulating do-while:")
# Python doesn't have a built-in do-while (which guarantees at least one run). We emulate it using `while True:` and checking the exit condition at the end.
while True:
    print("This will execute exactly once!") # Output: This will execute exactly once!
    break # Exit immediately, representing a condition being met

# Trick 3: Draining a collection using truthiness
print("\n3. Draining a list with pop():")
teas = ["Green", "Black", "Oolong"]
# An empty list evaluates to False. pop() removes items one by one until empty.
while teas:
    print(f"Brewing {teas.pop()}") # Output: Brewing Oolong, then Brewing Black, then Brewing Green

# Trick 4: The Walrus Operator (:=) in while loops
print("\n4. Walrus operator for compact loops:")
# Introduced in Python 3.8, it combines assignment and evaluation in one step.
n = 5
while (n := n - 1) > 0:
    print(f"Countdown: {n}") # Output: Countdown: 4, then 3, then 2, then 1

"""
--- NOTES: `while` Loops in Python ---

1. What is a `while` loop?
   - A `while` loop repeatedly executes a target block of code as long as a given boolean condition evaluates to `True`.
   - Unlike `for` loops, which iterate over a fixed sequence, `while` loops are used for indefinite iteration (when you don't know exactly how many times the loop needs to run in advance).

2. State Management:
   - The condition is evaluated *before* the loop body executes.
   - It is critical to update the state or counter variables inside the loop (like `temperature += 15`). If the state isn't updated, the condition will never become `False`, resulting in an "infinite loop" that crashes your program.

3. Latest Python Features:
   - **The Walrus Operator `:=` (Python 3.8+)**: As shown in Trick 4, this operator revolutionized `while` loops by allowing you to read data (e.g., from a file or network) and evaluate it on the exact same line, drastically reducing code duplication.
   - **Adaptive Specialization (Python 3.11+)**: Like `for` loops, `while` loops also benefited from PEP 659. The interpreter recognizes type-stable variable assignments happening inside a `while` loop (e.g., constantly adding integer 15 to `temperature`) and dynamically switches out generic bytecode for specialized, faster integer C-level instructions.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: When should you use a `while` loop instead of a `for` loop?
A1: You should use a `for` loop when you know the number of iterations in advance (like iterating through a list of items). You should use a `while` loop for indefinite iterations, where the loop relies on a condition that changes dynamically over time (like waiting for user input, tracking a temperature, or reading chunks of a file until the end is reached).

Q2: Does Python support `do-while` loops?
A2: No, Python does not have native `do-while` loops. However, you can achieve the exact same behavior by creating an infinite loop `while True:`, putting your logic at the top, and conditionally using the `break` keyword at the bottom of the loop block.

Q3: What causes an infinite `while` loop?
A3: An infinite loop occurs when the loop's condition expression is continuously evaluated as `True`. This usually happens because the developer forgot to update the loop control variable inside the block, or the logic for updating it was flawed.
"""