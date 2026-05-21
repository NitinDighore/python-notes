is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f"Total actions: {total_actions}") # Output: Total actions: 6

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_present)}") # Output: Is there milk? False

water_hot = True
tea_added = True

can_server = water_hot and tea_added
print(f"Can serve chai? {can_server}") # Output: Can serve chai? True

"""
--- NOTES: Booleans and Logical Operations in Python ---

1. Boolean Data Type (`bool`)
   - Booleans represent truth values and can only be `True` or `False`.
   - In Python, `bool` is actually a subclass of `int`. This means `True` behaves like the integer `1`, and `False` behaves like the integer `0`.

2. Concepts Demonstrated in the Code:
   - Upcasting / Implicit Conversion: When a boolean is used in an arithmetic operation (e.g., `stri_count + is_boiling`), Python automatically "upcasts" the boolean to an integer. `True` becomes `1`, making `5 + 1 = 6`.
   - Truthiness & `bool()` casting: The `bool()` function evaluates the "truthiness" of a value. In Python, zero (`0`), empty sequences (`""`, `[]`, `()`), empty dictionaries (`{}`), and `None` evaluate to `False`. Non-zero numbers and non-empty sequences evaluate to `True`.
   - Logical Operators: Python uses english words for logical operations (`and`, `or`, `not`). The `and` operator returns `True` only if both operands evaluate to `True`.

3. Latest Version Highlights (Python 3.8 - 3.11+):
   - The Walrus Operator `:=` (Python 3.8+): Often used in boolean contexts, it allows you to assign a value to a variable as part of a larger expression (e.g., inside an `if` or `while` statement: `if (n := len(a)) > 10:`).
   - Pattern Matching (Python 3.10+): You can use boolean conditions (guards) in `match/case` statements using the `if` keyword to refine matches (e.g., `case x if x > 0:`).

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: In Python, is `bool` a subclass of `int`? Prove it.
A1: Yes, `bool` is a subclass of `int`. You can prove this programmatically using `issubclass(bool, int)` which returns `True`. Because of this, `True + True` equals `2`.

Q2: Explain the concept of "Truthiness" in Python. Give examples of "falsy" values.
A2: Truthiness refers to how Python evaluates non-boolean values in a boolean context (like an `if` statement). Values that evaluate to `False` are called "falsy", and everything else is "truthy". Falsy values include: `0`, `0.0`, `""` (empty string), `[]` (empty list), `{}` (empty dict), `()` (empty tuple), `None`, and `False`.

Q3: What does the term "Short-circuit evaluation" mean in the context of `and` and `or` operators?
A3: Short-circuit evaluation means Python stops evaluating logical expressions as soon as the final outcome is determined. 
   - For `A and B`, if `A` is `False`, Python immediately returns `A` (or `False`) without evaluating `B` (since the whole expression can never be true).
   - For `A or B`, if `A` is `True`, Python immediately returns `A` (or `True`) without evaluating `B`.

Q4: If `total_actions = 5 + True` results in `6`, what is the type of `total_actions`?
A4: The type of `total_actions` is `int`. Even though one operand is a boolean, Python implicitly converts the boolean to an integer (upcasting) during arithmetic operations, resulting in an integer output.

Q5: In modern Python, how does the walrus operator (`:=`) improve boolean conditional loops?
A5: It allows you to simultaneously assign a value and check its truthiness in a single line, reducing code duplication. For example, instead of assigning a variable and then checking it in a `while` loop, you can do: `while (line := file.readline()): print(line)`.
"""
