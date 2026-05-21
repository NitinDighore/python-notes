masala_spices = ("cardamom", "cloves", "cinnamon")

(spice1, spice2, spice3) = masala_spices

print(f"Main masala spices: {spice1}, {spice2}, {spice3}") # Output: Main masala spices: cardamom, cloves, cinnamon

ginger_ratio, cadramom_ratio = 2, 1
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}") # Output: Ratio is G :2 and C: 1
ginger_ratio, cadramom_ratio = cadramom_ratio, ginger_ratio
print(f"Ratio is G :{ginger_ratio} and C: {cadramom_ratio}") # Output: Ratio is G :1 and C: 2

# membership testing

print(f"Is cinnamon in masala spices ? {'cinnamon' in masala_spices}") # Output: Is cinnamon in masala spices ? True

"""
--- NOTES: Tuples in Python ---

1. What are Tuples?
   - Tuples are ordered, immutable collections of items in Python.
   - They are defined using parentheses `()`, e.g., `(1, 2, 3)`, though the parentheses are often optional when defining them (this is called tuple packing).
   - Because they are immutable, once a tuple is created, its elements cannot be changed, added, or removed.

2. Key Operations Demonstrated:
   - Tuple Unpacking: Assigning the elements of a tuple to individual variables, e.g., `(spice1, spice2, spice3) = masala_spices`. The number of variables must match the number of items in the tuple.
   - Multiple Assignment & Swapping: Python allows multiple variables to be assigned at once using tuples. This is commonly used for swapping variables without needing a temporary variable: `a, b = b, a`.
   - Membership Testing: The `in` operator checks if an item exists within the tuple (returns `True` or `False`).

3. Why use Tuples over Lists?
   - Performance: Tuples are slightly faster and use less memory than lists because of their immutability.
   - Safety: They provide a form of write-protection. If data shouldn't change throughout the program lifecycle, using a tuple guarantees it remains constant.
   - Dictionary Keys: Because tuples are immutable (and therefore hashable), they can be used as keys in a dictionary, whereas lists cannot.

4. Built-in Functions and Methods for Tuples:
   Because tuples are immutable, they only have two specific methods. However, many built-in Python functions work with tuples.
   
   - Tuple Specific Methods:
     * `t.count(value)`: Returns the number of times a specified value occurs in a tuple.
     * `t.index(value, [start, [stop]])`: Searches the tuple for a specified value and returns the index of the first match. Raises a ValueError if not found.
   
   - Built-in Functions commonly used with Tuples:
     * `len(t)`: Returns the total number of items in the tuple.
     * `max(t)` / `min(t)`: Returns the highest or lowest value in the tuple (elements must be comparable, like all numbers).
     * `sum(t)`: Sums all items in the tuple (elements must be numeric).
     * `any(t)`: Returns True if ANY item in the tuple is truthy.
     * `all(t)`: Returns True if ALL items in the tuple are truthy.
     * `sorted(t)`: Takes a tuple and returns a new sorted LIST (does not modify or return a tuple).
     * `tuple(iterable)`: Converts an iterable (like a list or string) into a tuple.
     * `enumerate(t)`: Returns an enumerate object yielding pairs of (index, value) for the tuple.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the main difference between a List and a Tuple in Python?
A1: The primary difference is mutability. Lists are mutable (you can change, add, or remove items after creation), while tuples are immutable (their contents cannot be modified after creation). Syntactically, lists use square brackets `[]` and tuples use parentheses `()`.

Q2: How do you create a tuple with a single element?
A2: To create a single-element tuple, you must include a trailing comma. For example, `single_tuple = (5,)` or `single_tuple = 5,`. Without the comma, Python evaluates `(5)` simply as the integer `5` in parentheses.

Q3: Can a tuple contain mutable objects? If so, can you change them?
A3: Yes, a tuple can contain mutable objects like lists or dictionaries. While the tuple itself is immutable (you cannot change *which* objects the tuple holds), the mutable objects *inside* the tuple can still be modified. For example, if `t = ([1, 2], 3)`, you can do `t[0].append(3)`, resulting in `t` becoming `([1, 2, 3], 3)`.

Q4: Explain the concept of "Tuple Unpacking".
A4: Tuple unpacking allows you to assign each item of a tuple to a corresponding variable in a single statement. For instance, `a, b, c = (1, 2, 3)` assigns `1` to `a`, `2` to `b`, and `3` to `c`. You can also use the `*` operator to unpack remaining elements into a list: `first, *rest = (1, 2, 3, 4)`.

Q5: Why would you use a tuple as a dictionary key instead of a list?
A5: Dictionary keys must be hashable, which implies they must be immutable. Since tuples are immutable (provided they contain only immutable elements), they are hashable and can be used as dictionary keys. Lists are mutable and therefore unhashable, so they cannot be used as keys.
"""