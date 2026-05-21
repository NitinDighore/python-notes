cup = input("Choose your cup size (small/medium/large): ").lower()

if cup == "small":
    print("Price is 10 rupees") # Output: Price is 10 rupees (if input is 'small')
elif cup == "medium":
    print("Price is 15 rupees") # Output: Price is 15 rupees (if input is 'medium')
elif cup == "large":
    print("price is 20 rupees") # Output: price is 20 rupees (if input is 'large')
else:
    print("Unknown cup size") # Output: Unknown cup size (for any other input)

"""
--- NOTES: Conditional Statements (if-elif-else) in Python ---

1. What are Conditional Statements?
   - `if`, `elif`, and `else` statements allow a program to execute certain pieces of code based on specific conditions (boolean expressions).
   - Python evaluates the condition. If it is `True`, the indented block under it runs. If `False`, it moves to the next `elif` or `else` block.
   - You can have zero or more `elif` blocks, and an optional `else` block at the exact end of the chain.

2. How Different Data Types Work with Conditionals (Truthiness):
   - In Python, any object can be tested for truth value. This concept is called "Truthiness".
   - Falsy values (evaluate to False): `0`, `0.0`, `""` (empty string), `[]` (empty list), `{}` (empty dict), `()` (empty tuple), `set()`, `None`, and `False`.
   - Truthy values (evaluate to True): Everything else (e.g., non-zero numbers, non-empty sequences, `True`).
   
   * Coding Examples by Data Type:
     - Integers/Floats:
       if 0: print("Won't print") 
       if -5: print("Will print because it's non-zero")
     - Strings:
       if "": print("Won't print")
       if "chai": print("Will print because it's non-empty")
     - Lists/Dictionaries/Tuples/Sets:
       my_list = []
       if my_list: print("Won't print")
       my_list.append("tea")
       if my_list: print("Will print because list has items")
     - NoneType:
       if None: print("Won't print")

3. New Changes in Modern Python:
   - The Walrus Operator `:=` (Python 3.8+): Allows you to assign and evaluate a variable in the same conditional expression.
     Example: `if (n := len(cup)) > 4: print(f"Word length is {n}")`
   - Structural Pattern Matching `match-case` (Python 3.10+): A cleaner, powerful alternative to long `if-elif-else` chains (similar to switch/case in other languages). 
     Example:
     match cup:
         case "small": print("10 rupees")
         case "medium": print("15 rupees")
         case _: print("Unknown size")

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Can you have an `else` statement without an `if` statement?
A1: No, an `else` block for conditional flows must always be preceded by an `if` (or `elif`) block. (Note: `for` and `while` loops, as well as `try/except` blocks, can also have an `else` clause in Python, but a standalone `else` is a syntax error).

Q2: How does Python evaluate a condition like `if x:` when `x` is a dictionary?
A2: Python evaluates the "truthiness" of the dictionary. If the dictionary is empty (`{}`), it evaluates to `False`. If it contains one or more key-value pairs, it evaluates to `True`.

Q3: Is there a ternary operator in Python? How does it work?
A3: Yes, Python supports conditional expressions (the ternary operator) using the syntax: `value_if_true if condition else value_if_false`. Example: `price = 10 if cup == "small" else 20`.

Q4: What is the difference between an `if-elif-else` chain and multiple independent `if` statements?
A4: In an `if-elif-else` chain, Python stops evaluating conditions as soon as it finds one that is `True`. With multiple independent `if` statements, Python evaluates every single `if` condition, even if previous ones were already `True`.

Q5: Explain the `match-case` statement introduced in Python 3.10. Why use it over `if-elif`?
A5: `match-case` provides structural pattern matching. It is cleaner and more readable than long `if-elif` chains for comparing a single variable against multiple exact values. It also safely unpacks data structures (like dictionaries, lists, or custom objects) directly into variables if a structural pattern is matched.
"""