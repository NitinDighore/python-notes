import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49

print(f"Ideal temp { ideal_temp }") # Output: Ideal temp 95.5
print(f"Current temp { current_temp }") # Output: Current temp 95.49
print(f"Difference temp { ideal_temp - current_temp }") # Output: Difference temp 0.010000000000005116
print(sys.float_info) # Output: sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

"""
--- NOTES: Floating-Point Numbers, Decimals, and Fractions in Python ---

1. Floating-Point Numbers (`float`)
   - Floats represent real numbers with a fractional component. Python's `float` is typically implemented using C's `double`, following the IEEE 754 standard for 64-bit floating-point arithmetic.
   - Precision Issues: Because floats are represented in binary (base-2) fractions, most decimal (base-10) fractions cannot be represented exactly. This leads to small rounding errors. For example, `95.5 - 95.49` might yield `0.010000000000005116` instead of exactly `0.01`.

2. High-Precision Alternatives Demonstrated via Imports:
   - `decimal.Decimal`: Provides exact decimal arithmetic. It is essential for financial applications or anywhere exact decimal representation is required. Decimals avoid the base-2 rounding issues of standard floats.
   - `fractions.Fraction`: Provides support for rational number arithmetic. It stores numbers as a numerator and denominator, avoiding precision loss from division (e.g., `Fraction(1, 3)` instead of `0.3333...`).

3. `sys.float_info`:
   - This provides a struct sequence containing information about the float type for the current architecture, such as maximum and minimum values, precision (epsilon), and radix.

4. Latest Version Highlights & Best Practices (Modern Python):
   - `math.isclose()` (Python 3.5+): Because of precision errors, you should almost never use `==` to compare two floats. Instead, use `math.isclose(a, b)` to check if they are "close enough" within a certain tolerance.
   - Enhanced f-string formatting (Python 3.6+): You can cleanly format float precision for display without altering the underlying value, e.g., `f"{value:.2f}"` rounds the display to 2 decimal places.
   - New Math Functions (Python 3.12+): Python 3.12 introduced `math.sumprod()` for computing the sum of products (dot product) which is highly optimized and more accurate for floats than doing it manually.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why does `0.1 + 0.2 == 0.3` evaluate to `False` in Python?
A1: This happens due to floating-point representation limitations under the IEEE 754 standard. `0.1` and `0.2` cannot be represented exactly in binary, so they are stored with slight approximations. When added, the approximations compound, resulting in a value like `0.30000000000000004`, which is not exactly equal to `0.3`.

Q2: How should you properly check for equality between two floating-point numbers?
A2: You should check if the absolute difference between the numbers is smaller than a very small threshold (epsilon). The standard and most readable way in modern Python is to use the `math.isclose(a, b)` function.

Q3: When would you choose to use `decimal.Decimal` over the standard `float` type?
A3: `Decimal` should be used when exact decimal precision is required, most notably in financial calculations, currency representation, or scientific applications where rounding errors inherent in binary floating-point arithmetic are unacceptable.

Q4: What is the main drawback of using `decimal.Decimal` or `fractions.Fraction` compared to standard `float`?
A4: Performance and memory. Standard `float` operations are heavily optimized at the hardware level and are very fast. `Decimal` and `Fraction` objects are software-implemented and therefore significantly slower and consume more memory.

Q5: Explain what `sys.float_info.epsilon` represents.
A5: Epsilon represents the difference between 1.0 and the least value greater than 1.0 that is representable as a float. It effectively indicates the machine's precision limit for floating-point calculations and the magnitude of rounding errors.
"""
