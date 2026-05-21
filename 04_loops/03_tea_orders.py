orders = ["hitesh", "Aman", "Becky", "Carlos"]

for name in orders:
    print(f"Order ready for {name}") # Output: Order ready for hitesh, then Aman, then Becky, then Carlos

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The 'for...else' loop. 
# The else block executes ONLY if the loop completes normally (no 'break' encountered).
print("\n1. The for-else construct:")
for name in orders:
    if name == "Zane":
        print("Found Zane!")
        break
else:
    print("Zane was not found in the orders.") # Output: Zane was not found in the orders.

# Trick 2: The dangerous way to modify a list while iterating (Classic Bug)
print("\n2. The danger of removing without a copy (skipping items):")
buggy_orders = ["A", "B", "C", "D"]
for item in buggy_orders:
    buggy_orders.remove(item) # Removes the current item, causing the next item to slide into the current index!
print(f"Buggy orders left over: {buggy_orders}") # Output: ['B', 'D'] (Notice it skipped elements)

# Trick 3: Safe removal of items by iterating over a shallow copy
print("\n3. Safely modifying a list while iterating:")
safe_orders = ["A", "B", "C", "D"]
for item in safe_orders[:]: # `[:]` creates a shallow copy of the list specifically for the loop to track
    safe_orders.remove(item)
print(f"Safe orders left over: {safe_orders}") # Output: [] (Successfully removed all items)

# Trick 4: Iterating backwards using `reversed()` or slicing `[::-1]`
print("\n4. Iterating backwards:")
for name in reversed(orders):
    print(f"Backwards: {name}")

# Trick 5: "One-liner" loop using list comprehension for side effects (Trick/Hack)
print("\n5. List comprehension for side-effects:")
# Often discouraged in production code, but evaluates the loop and executes functions in a single line
_ = [print(f"Long name alert: {n}") for n in orders if len(n) > 4]

"""
--- NOTES: Iterating over Lists with `for` loops ---

1. Pythonic Iteration:
   - Unlike languages like C or Java where you might use a loop counter (e.g., `for i=0; i<len; i++`), Python `for` loops iterate over the items of any sequence (like a list, tuple, or string) directly.
   - This is considered much more readable and "Pythonic".

2. Modifying Collections during Iteration:
   - It is generally a bad practice to add or remove items from a list while you are actively iterating over it. 
   - Because Python tracks iteration via indices internally, changing the list size mid-loop causes elements to shift, leading to skipped items or infinite loops.

3. Latest Python Features:
   - **Adaptive Specialization (Python 3.11+)**: Python aggressively optimizes "type-stable" loops at runtime. Because the `orders` list contains only strings, the interpreter adapts the bytecode specifically for string operations, making the loop significantly faster under the hood.
   - **`itertools.batched` (Python 3.12+)**: A new function added to the `itertools` standard library that allows you to easily iterate over a list in chunks (e.g., processing 2 orders at a time: `for batch in batched(orders, 2):`), which removes the need to write complex index-slicing logic.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: If you wanted to print the order number along with the name, how would you change the loop?
A1: You should use the built-in `enumerate()` function. 
    Example: `for index, name in enumerate(orders, start=1): print(f"Order #{index}: {name}")`.

Q2: Is it better to use `for name in orders:` or `for i in range(len(orders)):`? Why?
A2: It is almost always better to use `for name in orders:`. It is more concise, easier to read, and avoids the unnecessary overhead of indexing `orders[i]` inside the loop block. You only need `range(len())` if you absolutely have to overwrite the original list elements by their index.

Q3: What specifically happens if you remove an item from `orders` inside this `for` loop?
A3: It will skip the immediate next item in the list. When an element is removed, all subsequent elements shift one index to the left. However, the loop's internal iterator will still blindly move to the *next* index position, thereby stepping right over the item that just shifted left.

Q4: If you need to filter or remove items from a list during a loop, what is the best approach?
A4: The best approach is to avoid mutating the original list while looping. Instead, you can iterate over a shallow copy of the list (e.g., `for name in orders[:]:`) and modify the original, OR simply build a new list using a list comprehension (e.g., `orders = [name for name in orders if name != "Becky"]`).
"""