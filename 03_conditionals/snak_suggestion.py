snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great Choice! We'll serve you {snack}") # Output: Great Choice! We'll serve you cookies (if input is 'cookies' or 'samosa')
else:
    print("Sorry, we only serve cookies or samosa with tea") # Output: Sorry, we only serve cookies or samosa with tea (for any other input)

"""
--- NOTES: Logical Operators (`or`) and Short-Circuit Evaluation ---

1. The Logical `or` Operator:
   - Used to combine multiple conditional statements.
   - The `or` operator returns `True` if at least ONE of the conditions is `True`.
   - It only returns `False` if ALL conditions evaluate to `False`.

2. Short-Circuit Evaluation:
   - Python optimizes conditional checks by stopping early as soon as the final result is known.
   - In an `A or B` statement, if `A` evaluates to `True`, Python immediately returns `True` and completely ignores `B` (it doesn't even execute it). This is known as short-circuiting.

3. A Common Beginner Pitfall:
   - A frequent mistake is writing code like: `if snack == "cookies" or "samosa":`
   - Python evaluates this as `(snack == "cookies") or ("samosa")`. Because `"samosa"` is a non-empty string, it evaluates to `True` (Truthiness). This means the entire statement will *always* evaluate to `True`, regardless of what `snack` is.
   - The correct way is to explicitly compare the variable each time: `if snack == "cookies" or snack == "samosa":`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: How does short-circuit evaluation work with the `or` operator?
A1: In Python, `or` evaluates expressions from left to right. If the first expression is `True`, the overall expression is guaranteed to be `True`, so Python short-circuits and skips evaluating the remaining expressions.

Q2: Why does `if x == "A" or "B":` always execute the `if` block, even if `x` is `"C"`?
A2: Because of operator precedence and truthiness. It is evaluated as `(x == "A") or ("B")`. While `x == "A"` evaluates to `False`, `"B"` is a non-empty string which evaluates to `True`. `False or True` resolves to `True`.

Q3: If you have a long list of items to check, e.g., `if x == a or x == b or x == c or x == d:`, how can you make this more Pythonic?
A3: You should use the `in` operator combined with a tuple, list, or set. For example: `if x in ("a", "b", "c", "d"):`. This is much cleaner, more readable, and conceptually evaluates membership rather than multiple equalities.
"""