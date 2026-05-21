chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Order for {customer_name} : {chai_type} please !") # Output: Order for Priya : Ginger chai please !

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}") # Output: First word: Aromatic
print(f"Last word: {chai_description[12:]}") # Output: Last word:  Bold
print(f"Last word: {chai_description[::-1]}") # Output: Last word: dloB dna citamorA

label_text = "Chai Spécial"
ecoded_label = label_text.encode("utf-8")
print(f"Non Encoded label: {label_text}") # Output: Non Encoded label: Chai Spécial
print(f"Encoded label: {ecoded_label}") # Output: Encoded label: b'Chai Sp\xc3\xa9cial'
decoded_label = ecoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}") # Output: Decoded label: Chai Spécial

# --- STRING SLICING EXAMPLES ---
word = "PythonProgramming"

# Syntax: string[start:stop:step]
print(f"\nOriginal word: {word}") # Output: Original word: PythonProgramming

# 1. Basic Slicing (start to stop-1)
print(f"Slice [0:6] (First 6 chars): {word[0:6]}") # Outputs: Python

# 2. Omitting start or stop
print(f"Slice [:6] (Omit start, defaults to 0): {word[:6]}") # Outputs: Python
print(f"Slice [6:] (Omit stop, goes to end): {word[6:]}")    # Outputs: Programming

# 3. Using steps
print(f"Slice [::2] (Every second character): {word[::2]}")  # Outputs: PtoPormig

# 4. Negative Indices (Counting from the end)
print(f"Slice [-11:-4] (Negative indices): {word[-11:-4]}")  # Outputs: Program

# 5. Reversing a string using negative step
print(f"Slice [::-1] (Reverse string): {word[::-1]}")        # Outputs: gnimmargorPnohtyP

# --- TRICK QUESTION EXAMPLE ---
print("\n--- Slicing Trick Question ---") # Output: --- Slicing Trick Question ---
trick_word = "DataScience"
# Trick: What happens if start > stop with a default positive step?
result = trick_word[5:2] 
print(f"trick_word[5:2] returns: '{result}' (An empty string! It does NOT throw an error)") # Output: trick_word[5:2] returns: '' (An empty string! It does NOT throw an error)

# To go backwards, you MUST provide a negative step:
result_backwards = trick_word[5:2:-1]
print(f"trick_word[5:2:-1] returns: '{result_backwards}'") # Output: trick_word[5:2:-1] returns: 'cSa'

"""
--- NOTES: Strings and String Methods in Python ---

1. What are Strings (`str`)?
   - Strings in Python are an immutable sequence of Unicode characters.
   - Because they are immutable, any method that seems to modify a string actually returns a completely NEW string object. The original string remains unchanged.
   - The code above demonstrates string slicing (`[:8]`, `[::-1]` for reversing) and encoding/decoding (`utf-8`).

2. Comprehensive List of Common String Methods:
   Note: Since `len()` is a built-in function and not a method, you call it as `len(string)` rather than `string.len()`.
   
   - **Length & Slicing**
     * `len(s)`: Returns the total number of characters in the string.
     * `s[start:stop:step]`: Slices the string (e.g., `s[::-1]` reverses it).
   
   - **Case Changing**
     * `s.lower()`: Returns a copy of the string converted to lowercase.
     * `s.upper()`: Returns a copy of the string converted to uppercase.
     * `s.title()`: Returns a title-cased version (first letter of every word capitalized).
     * `s.capitalize()`: Capitalizes only the first character of the string.
     * `s.swapcase()`: Swaps uppercase letters to lowercase and vice-versa.

   - **Searching & Counting**
     * `s.find(substring)`: Returns the lowest index where the substring is found. Returns `-1` if not found.
     * `s.index(substring)`: Similar to `find()`, but raises a `ValueError` if the substring is not found.
     * `s.count(substring)`: Returns the number of non-overlapping occurrences of a substring.
     * `s.startswith(prefix)`: Returns `True` if the string starts with the specified prefix.
     * `s.endswith(suffix)`: Returns `True` if the string ends with the specified suffix.

   - **Modifying & Formatting (Returns New Strings)**
     * `s.strip([chars])`: Removes leading and trailing whitespace (or specified characters).
     * `s.lstrip()` / `s.rstrip()`: Removes leading (left) or trailing (right) whitespace.
     * `s.replace(old, new, [count])`: Replaces occurrences of `old` with `new`.
     * `s.split(delimiter)`: Splits the string by the delimiter and returns a list of strings (defaults to splitting by whitespace).
     * `"delimiter".join(iterable)`: Joins elements of an iterable (like a list) into a single string, separated by the string it's called on. Example: `"-".join(["A", "B"])` -> `"A-B"`.

   - **Validation Methods (Returns Boolean)**
     * `s.isalpha()`: `True` if all characters are alphabetic letters.
     * `s.isdigit()`: `True` if all characters are digits.
     * `s.isalnum()`: `True` if all characters are alphanumeric (letters or numbers).
     * `s.isspace()`: `True` if the string contains only whitespace characters.

3. Latest Version Highlights (Python 3.8 - 3.12+):
   - `.removeprefix(prefix)` & `.removesuffix(suffix)` (Python 3.9+): A much safer alternative to `lstrip()` and `rstrip()` when you specifically want to remove a prefix/suffix substring, rather than a set of characters.
   - Enhanced f-strings (Python 3.12+): You can now reuse the same quote type inside an f-string expression. Example: `f"Result: {my_dict['key']}"` (Using single quotes inside an f-string formatted with double quotes used to be restricted or require escaping, now it's much more flexible).
   - Multi-line f-strings (Python 3.12+): Comments and backslashes are now fully supported directly inside f-string expressions.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Are strings mutable or immutable in Python? What does that mean for operations like `replace()`?
A1: Strings are immutable, meaning they cannot be changed in place. Operations like `s.replace("a", "b")` do not modify the original string `s`; instead, they create and return a brand new string object with the replacements made.

Q2: What is the difference between `s.find('x')` and `s.index('x')`?
A2: Both methods search for the substring `'x'`. However, if `'x'` is not found, `find()` returns `-1`, whereas `index()` raises a `ValueError`. Use `index()` when the substring MUST be present, and `find()` when its absence is handled by logic without exceptions.

Q3: What is the most efficient way to concatenate a large list of strings in Python?
A3: Using the `"".join(list_of_strings)` method is the most efficient way. Using the `+` operator inside a loop is highly inefficient because, since strings are immutable, it creates a new string object in memory during every iteration.

Q4: How do you reverse a string in Python?
A4: The most Pythonic and efficient way is to use slicing with a negative step: `reversed_s = s[::-1]`.

Q5: In Python 3.9, `.removeprefix()` was added. Why not just use the existing `.lstrip()`?
A5: `.lstrip("pre")` removes any combination of the characters 'p', 'r', and 'e' from the beginning of the string, which can cause unexpected bugs (e.g., `"prepare".lstrip("pre")` returns `"pare"`). `.removeprefix("pre")` strictly removes the exact substring `"pre"` only if it appears at the start.
"""
