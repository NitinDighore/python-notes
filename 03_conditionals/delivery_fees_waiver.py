order_amount = int(input("Enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is : {delivery_fees}") # Output: Delivery fees is : 0 (if amount > 300) or 30 (if amount <= 300)

"""
--- NOTES: Conditional Expressions (Ternary Operator) in Python ---

1. What is the Ternary Operator in Python?
   - Unlike C, Java, or JavaScript which use the `condition ? true_value : false_value` syntax, Python uses a more readable, English-like syntax called a "Conditional Expression".
   - Syntax: `value_if_true if condition else value_if_false`
   - It evaluates the `condition` first. If it's True, it evaluates and returns `value_if_true`; otherwise, it evaluates and returns `value_if_false`.
   - This is heavily used to assign a variable on a single line based on a condition, as seen in the code above.

2. One-line `if-elif-else` (Nested Ternary Operators):
   - You can chain conditional expressions to simulate an `if-elif-else` block in a single line.
   - Syntax: `value1 if condition1 else value2 if condition2 else value3`
   - Example:
     ```python
     # Traditional if-elif-else
     if order_amount > 500:
         status = "Premium"
     elif order_amount > 300:
         status = "Standard"
     else:
         status = "Basic"
         
     # One-line equivalent
     status = "Premium" if order_amount > 500 else "Standard" if order_amount > 300 else "Basic"
     ```
   - Note: While possible, chaining too many conditions on one line is generally discouraged in Python as it violates the PEP 8 principle of readability.
   
--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Does Python have a `? :` ternary operator like JavaScript or C++?
A1: No, Python does not use the `? :` syntax. Instead, it uses the `value_if_true if condition else value_if_false` syntax, which was introduced in Python 2.5 to improve code readability.

Q2: How would you write an `if-elif-else` block in a single line?
A2: You can write it by nesting conditional expressions. For example: `x = "Positive" if n > 0 else "Zero" if n == 0 else "Negative"`. 

Q3: Why might you choose NOT to use a nested one-line conditional expression?
A3: Readability. The Zen of Python states "Readability counts". Deeply nested ternary operators can be very difficult to read and maintain compared to a standard multi-line `if-elif-else` block.

Q4: What is short-circuit evaluation, and does the ternary operator use it?
A4: Short-circuit evaluation means that only the necessary parts of an expression are evaluated. Yes, the ternary operator uses it. In `x if C else y`, Python evaluates `C`. If `C` is True, `x` is evaluated and `y` is completely ignored (and vice versa). This is important if `x` or `y` are function calls that have side effects.
"""