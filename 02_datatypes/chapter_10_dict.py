chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}") # Output: Chai order: {'type': 'Masala Chai', 'size': 'Large', 'sugar': 2}

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}") # Output: Recipe base: black tea
print(f"Recipe: {chai_recipe}") # Output: Recipe: {'base': 'black tea', 'liquid': 'milk'}
del chai_recipe["liquid"]
print(f"Recipe: {chai_recipe}") # Output: Recipe: {'base': 'black tea'}

print(f"Is sugar in the order? {'sugar' in chai_order}") # Output: Is sugar in the order? True

chai_order = {"type": "Ginger Chai", "size": "Medium", "sugar": 1}

# print(f"Order details (keys): {chai_order.keys()}") # Output: Order details (keys): dict_keys(['type', 'size', 'sugar'])
# print(f"Order details (values): {chai_order.values()}") # Output: Order details (values): dict_values(['Ginger Chai', 'Medium', 1])
# print(f"Order details (items): {chai_order.items()}") # Output: Order details (items): dict_items([('type', 'Ginger Chai'), ('size', 'Medium'), ('sugar', 1)])

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}") # Output: Removed last item: ('sugar', 1)

extra_spices = {"cardamom": "crushed", "ginger": "sliced"}
chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}") # Output: Updated chai recipe: {'base': 'black tea', 'cardamom': 'crushed', 'ginger': 'sliced'}

customer_note = chai_order.get("size", "NO Note")
print(f"customer_note is: {customer_note}") # Output: customer_note is: Medium

"""
--- NOTES: Dictionaries in Python ---

1. What are Dictionaries?
   - Dictionaries are mutable, ordered (as of Python 3.7+) collections of key-value pairs.
   - They are defined using curly braces `{}` with `key: value` pairs or using the `dict()` constructor.
   - Keys must be of an immutable (hashable) type, such as strings, numbers, or tuples.
   - Values can be of any data type and can be duplicated, but keys must be unique.
   - They are highly optimized for data retrieval, insertion, and deletion.

2. Built-in Functions used with Dictionaries:
   - `len(d)`: Returns the number of key-value items in the dictionary.
   - `all(d)`: Returns True if all keys of the dictionary are truthy (or if the dict is empty).
   - `any(d)`: Returns True if any key of the dictionary is truthy.
   - `sum(d)`: Sums the keys of the dictionary (keys must be numeric types).
   - `max(d)`: Returns the maximum key in the dictionary.
   - `min(d)`: Returns the minimum key in the dictionary.
   - `sorted(d)`: Returns a new sorted list of the dictionary's keys.
   - `iter(d)`: Returns an iterator over the keys of the dictionary.

3. Dictionary Specific Methods:
   - `d.clear()`: Removes all items from the dictionary.
   - `d.copy()`: Returns a shallow copy of the dictionary.
   - `d.fromkeys(iterable, value=None)`: Creates a new dictionary with keys from iterable and values set to `value`.
   - `d.get(key, default=None)`: Returns the value for `key` if `key` is in the dictionary, otherwise returns `default`.
   - `d.items()`: Returns a view object displaying a list of a dictionary's (key, value) tuple pairs.
   - `d.keys()`: Returns a view object displaying a list of all the keys in the dictionary.
   - `d.values()`: Returns a view object displaying a list of all the values in the dictionary.
   - `d.pop(key, default)`: Removes specified `key` and returns the corresponding value. If the key is not found, `default` is returned if given; otherwise, it raises a `KeyError`.
   - `d.popitem()`: Removes and returns a (key, value) pair as a tuple. Since Python 3.7, pairs are returned in LIFO (Last In, First Out) order.
   - `d.setdefault(key, default=None)`: If `key` is in the dictionary, return its value. If not, insert `key` with a value of `default` and return `default`.
   - `d.update([other])`: Updates the dictionary with the key/value pairs from `other`, overwriting existing keys.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Are dictionaries ordered or unordered in Python?
A1: In Python 3.6, dictionaries became ordered as an implementation detail of CPython. Starting from Python 3.7, it is an official language feature that dictionaries maintain their insertion order.

Q2: What is the difference between accessing a value using `d[key]` versus `d.get(key)`?
A2: If the key does not exist, `d[key]` will raise a `KeyError`, which interrupts your program if not handled. On the other hand, `d.get(key)` will safely return `None` (or a specified default value) without raising an error.

Q3: What are the requirements for a dictionary key in Python?
A3: A dictionary key must be hashable, meaning it must be of an immutable type. Valid types include strings, integers, floats, and tuples (provided the tuple only contains immutable elements). Lists and sets are mutable and therefore unhashable, so they cannot be used as dictionary keys.

Q4: How do you merge two dictionaries in modern Python?
A4: In Python 3.9+, you can use the union operator `|`. For example, `merged = dict1 | dict2`. If there are overlapping keys, the values from the right-hand dictionary (`dict2`) will overwrite those from the left-hand one. Before 3.9, you would commonly use the unpack operator: `merged = {**dict1, **dict2}` or the `update()` method.

Q5: What is the average time complexity for looking up, inserting, or deleting a key-value pair in a dictionary?
A5: The average time complexity is O(1) for all of these operations. This is because Python dictionaries are implemented under the hood as hash tables.

Q6: What does the `popitem()` method do and in what order?
A6: `popitem()` removes and returns a key-value pair from the dictionary as a tuple. In Python 3.7+, it follows LIFO (Last In, First Out) order, meaning it will always remove and return the most recently inserted pair.
"""