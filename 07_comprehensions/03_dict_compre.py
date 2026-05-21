tea_prices_inr = {
    "Masala Chai": 40,
    "Green Tea": 50,
    "Lemon Tea": 200
}

tea_prices_usd = {tea:price / 80 for tea, price in tea_prices_inr.items()}
print(tea_prices_usd) # Output: {'Masala Chai': 0.5, 'Green Tea': 0.625, 'Lemon Tea': 2.5}

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Filtering items (If condition)
print("\n1. Filtering items:")
# Keep only teas that cost more than 45 INR. The condition goes at the end.
premium_teas = {tea: price for tea, price in tea_prices_inr.items() if price > 45}
print(f"Premium Teas: {premium_teas}") # Output: {'Green Tea': 50, 'Lemon Tea': 200}

# Trick 2: If-Else condition on the Value
print("\n2. If-Else on Values:")
# Note: If-Else goes BEFORE the 'for' keyword, acting on the value expression.
tea_labels = {tea: ("Expensive" if price > 100 else "Cheap") for tea, price in tea_prices_inr.items()}
print(f"Tea Labels: {tea_labels}") # Output: {'Masala Chai': 'Cheap', 'Green Tea': 'Cheap', 'Lemon Tea': 'Expensive'}

# Trick 3: Swapping Keys and Values (Dictionary Inversion)
print("\n3. Inverting a Dictionary:")
# Warning: If you have duplicate values in the original, the last evaluated key will overwrite previous ones!
inverted_dict = {price: tea for tea, price in tea_prices_inr.items()}
print(f"Inverted Dict: {inverted_dict}") # Output: {40: 'Masala Chai', 50: 'Green Tea', 200: 'Lemon Tea'}

# Trick 4: Creating a Dict from two lists with transformations
print("\n4. Zipping lists with a transformation:")
keys = ["Black", "White", "Oolong"]
values = [30, 45, 60]
# While dict(zip(keys, values)) is great, comprehensions allow on-the-fly math/logic during the zip
discounted_menu = {k: v * 0.9 for k, v in zip(keys, values)}
print(f"Discounted Menu: {discounted_menu}") # Output: {'Black': 27.0, 'White': 40.5, 'Oolong': 54.0}

# Trick 5: Dictionary Comprehension with enumerate()
print("\n5. Using enumerate() to create ID mappings:")
teas_list = ["Masala", "Ginger", "Lemon"]
# Quickly generate a dictionary mapping values to unique IDs
id_mapping = {tea: index for index, tea in enumerate(teas_list, start=1)}
print(f"ID Mapping: {id_mapping}") # Output: {'Masala': 1, 'Ginger': 2, 'Lemon': 3}

"""
--- NOTES: Dictionary Comprehensions ---

1. What are Dictionary Comprehensions?
   - They provide a concise way to create dictionaries from any iterable.
   - Syntax: `{key_expression: value_expression for item in iterable if condition}`
   - Very heavily used for extracting subsets of dictionaries, changing keys/values on the fly, or quickly inverting dictionaries.

2. Latest Python Features (Python 3.12 Enhancements):
   - **Comprehension Inlining (PEP 709)**: Similar to list and set comprehensions, dictionary comprehensions are now inlined by the compiler directly into the local scope. 
   - **Impact**: Before Python 3.12, the interpreter created a hidden temporary function to evaluate the dictionary comprehension, which had noticeable overhead. Inlining removes this frame overhead, making dictionary comprehensions up to 11% faster in Python 3.12+.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: How do you invert a dictionary (swap its keys and values) in Python?
A1: The most Pythonic way is using a dictionary comprehension: `{v: k for k, v in original_dict.items()}`.

Q2: What happens during a dictionary inversion if the original dictionary has duplicate values?
A2: Since dictionary keys must be unique, any duplicate value (which becomes the new key) will overwrite previous entries. The last key-value pair processed in the iteration will "win" and be the one retained.

Q3: Why would you use `{k: v for k, v in zip(list1, list2)}` instead of just `dict(zip(list1, list2))`?
A3: If you are directly converting the zipped lists into a dictionary, `dict(zip(list1, list2))` is cleaner and slightly faster. You only *need* to use a dictionary comprehension if you want to apply some transformation or logic to the keys or values during creation (e.g., `{k.upper(): v * 2 for k, v in zip(list1, list2)}`) or filter items using an `if` clause.

Q4: Can a dictionary comprehension return a set?
A4: No. While both use curly braces `{}`, if you include a colon `:` separating a key and value, Python strictly evaluates it as a dictionary comprehension. If you omit the colon, Python evaluates it as a set comprehension.
"""