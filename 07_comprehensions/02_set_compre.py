favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais }
print(unique_chai) # Output: {'Masala Chai', 'Green Tea', 'Lemon Tea', 'Elaichi Chai'} (Order may vary)


recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices) # Output: {'ginger', 'cardamom', 'clove', 'milk', 'black pepper'} (Order may vary)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Filtering and standardizing data simultaneously
print("\n1. Standardizing text to ensure uniqueness:")
# Often, dirty data has capitalization or spacing issues that prevent normal sets from deduplicating them.
dirty_data = ["  Masala ", "masala", "MASALA  ", "ginger"]
clean_set = {chai.strip().lower() for chai in dirty_data}
print(f"Cleaned unique set: {clean_set}") # Output: {'ginger', 'masala'}

# Trick 2: Set comprehension from a String
print("\n2. Unique characters from a string:")
# Set comprehensions iterate over ANY iterable, making them perfect for finding unique letters (like vowels)
sentence = "chaicode is awesome"
unique_vowels = {char for char in sentence if char in "aeiou"}
print(f"Unique vowels used: {unique_vowels}") # Output: {'e', 'o', 'a', 'i'}

# Trick 3: Cartesian Product in a Set Comprehension
print("\n3. Cartesian product of two iterables:")
# Just like list comprehensions, you can use multiple 'for' loops to create combinations
sizes = ["Small", "Large"]
teas = ["Green", "Black"]
combos = {f"{s} {t}" for s in sizes for t in teas}
print(f"Combinations: {combos}") # Output: {'Large Black', 'Small Black', 'Large Green', 'Small Green'}

# Trick 4: The Walrus Operator (:=) in set comprehensions
print("\n4. Using the Walrus operator (:=):")
numbers = [10, 15, 21, 33, 40]
def math_logic(n): return n % 7
# We only want unique, non-zero remainders, evaluating the function only once per loop
valid_remainders = {(res := math_logic(n)) for n in numbers if (res := math_logic(n)) > 0}
print(f"Valid remainders: {valid_remainders}") # Output: {1, 3, 5}

"""
--- NOTES: Set Comprehensions ---

1. What are Set Comprehensions?
   - Introduced in Python 2.7, Set Comprehensions provide a concise way to create sets.
   - Syntax: `{expression for item in iterable if condition}`
   - Because they output a `set`, they automatically filter out duplicate values during creation.
   - Similar to standard sets, every evaluated expression (the items being added) MUST be hashable (immutable), otherwise a `TypeError` is raised.

2. Latest Python Features (Python 3.12 Enhancements):
   - **Comprehension Inlining (PEP 709)**: Just like list comprehensions, Python 3.12+ inlines set comprehensions directly into the executing scope instead of compiling them as hidden nested functions. 
   - **Impact**: This removes the overhead of creating a new function frame, making set comprehensions noticeably faster in Python 3.12 compared to older versions.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: How does Python know the difference between a Set Comprehension and a Dictionary Comprehension since both use `{}`?
A1: Python determines the type based on the expression before the `for` keyword. If it is a single value (e.g., `{x for x in data}`), it creates a set. If it is a key-value pair separated by a colon (e.g., `{k: v for k, v in data}`), it creates a dictionary.

Q2: Is it better to use `set(my_list)` or `{x for x in my_list}` to remove duplicates from a list?
A2: If you are simply converting an existing list directly to a set without any filtering or transformations, using the built-in `set(my_list)` is slightly faster and more readable. You should use a set comprehension when you need to map (transform) the items or filter them conditionally while deduplicating.

Q3: Why doesn't the output of a set comprehension match the order of the original list?
A3: Sets are implemented using hash tables under the hood. They are inherently unordered collections. The order of elements is determined by their hash values and the history of insertions, not by the order they were processed in the comprehension.

Q4: What happens if you try to do `{[1, 2] for x in range(3)}`?
A4: It will raise a `TypeError: unhashable type: 'list'`. You cannot store mutable data types (like lists or dictionaries) inside a set. You would need to convert the inner list to a tuple: `{(1, 2) for x in range(3)}`.
"""