# Interger

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is {total_grams}") # Output: Total grams of base tea is 17

remaing_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is {remaing_tea}") # Output: Total grams of remaining tea is 11

milk_litres = 7
servings = 4
milk_per_serving = milk_litres / servings
print(f"Milk per serving is {milk_per_serving}") # Output: Milk per serving is 1.75

total_tea_bags = 7
pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}") # Output: While tea bags per pot: 1

total_cadamom_pods = 10
pods_per_cup = 3
leftover_pods = total_cadamom_pods % pods_per_cup
print(f"Leftover C pods {leftover_pods}") # Output: Leftover C pods 1

base_flavor_strength = 2
scale_factor = 3
powerful_falvour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strenght {powerful_falvour}") # Output: Scaled flavour strenght 8
# 2 * 2 * 2

total_tea_leaves_harvested = 1_000_000_000
print(f"tea leaves: {total_tea_leaves_harvested}") # Output: tea leaves: 1000000000

"""
--- NOTES: Integers and Arithmetic Operations in Python ---

1. Integer Data Type (`int`)
   - Integers are whole numbers without a fractional component. They can be positive, negative, or zero.
   - In Python 3, integers have arbitrary precision, meaning there is no fixed limit to their size; they are limited only by the available memory.

2. Arithmetic Operators Demonstrated:
   - Addition (`+`), Subtraction (`-`)
   - True Division (`/`): Always returns a float, even if the numbers divide evenly (e.g., `7 / 4 = 1.75`).
   - Floor Division (`//`): Returns an integer, rounding down to the nearest whole number (e.g., `7 // 4 = 1`).
   - Modulo (`%`): Returns the remainder of a division operation (e.g., `10 % 3 = 1`).
   - Exponentiation (`**`): Raises the first number to the power of the second (e.g., `2 ** 3 = 8`).

3. Readability Features:
   - Underscores in Numeric Literals: As seen in `1_000_000_000`, Python allows underscores to group digits for better readability. These underscores are ignored by the Python interpreter (introduced in Python 3.6).

4. Latest Version Highlights (Python 3.8 - 3.11+):
   - Debugging f-strings (Python 3.8+): The `=` specifier in f-strings makes debugging easier. E.g., `print(f"{total_grams=}")` prints `total_grams=17`.
   - `.bit_count()` (Python 3.10+): The `int` type now has a `bit_count()` method that returns the number of ones in the binary representation of the absolute value of the integer (e.g., `(5).bit_count()` -> 2).
   - DoS Protection (Python 3.11+): Python introduced a limit on integer-to-string conversions (default 4300 digits) to prevent Denial of Service attacks when converting massive strings to ints. This can be configured via `sys.set_int_max_str_digits()`.
   - Math Optimizations (Python 3.11+): Integer math operations have been significantly optimized at the C level, making basic arithmetic faster.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between `/` and `//` in Python?
A1: `/` performs "true division" and always returns a floating-point number (e.g., `10 / 2 = 5.0`). `//` performs "floor division", returning an integer that is the mathematical floor of the quotient (e.g., `10 // 3 = 3`, and `-10 // 3 = -4`).

Q2: Is there a maximum limit to the size of an integer in Python?
A2: In Python 3, the `int` type has arbitrary precision, so there is no architectural maximum limit like `INT_MAX` found in C or Java (e.g., 2^31-1). The only limit is the amount of RAM available on your system. (Note: Since Python 3.11, there is a limit for string-to-int conversion to prevent DoS, but the integer value itself is memory-bound).

Q3: How would you make a very large number like one billion readable in Python code without turning it into a string?
A3: You can use underscores as visual separators. For example, `1_000_000_000`. Python ignores the underscores when parsing the integer.

Q4: In Python 3.10+, if you need to count the number of set bits (1s) in the binary representation of an integer, what built-in method would you use?
A4: You can use the `int.bit_count()` method. For example, the binary representation of 5 is '101', so `(5).bit_count()` returns 2.

Q5: In modern Python (3.8+), what is the quickest way to print a variable's name alongside its value using f-strings?
A5: You can append an `=` sign to the variable name inside the f-string curly braces. For example, `print(f"{bags_per_pot=}")` will output `bags_per_pot=1`.
"""
