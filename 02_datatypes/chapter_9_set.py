essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}") # Output: All spices: {'cloves', 'cardamom', 'black pepper', 'cinnamon', 'ginger'}

common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}") # Output: common spices: {'ginger'}

only_in_essential = essential_spices - optional_spices
print(f"Only in essential spices: {only_in_essential}") # Output: Only in essential spices: {'cardamom', 'cinnamon'}

print(f"Is 'cloves' in optional spices? {'cloves' in optional_spices}") # Output: Is 'cloves' in optional spices? True

"""
--- NOTES: Sets in Python ---

1. What are Sets?
   - Sets are unordered, mutable collections of unique elements.
   - They are defined using curly braces `{}` or the built-in `set()` function.
   - Note: An empty set must be created using `set()`, not `{}` (which creates an empty dictionary).
   - Because they are unordered, sets do not support indexing or slicing.
   - Sets are highly optimized for fast membership testing (using `in` operator) and eliminating duplicate entries.

2. Set Operations Demonstrated:
   - Union (`|`): Combines elements from both sets (no duplicates).
   - Intersection (`&`): Returns elements that are common to both sets.
   - Difference (`-`): Returns elements that are in the first set but not in the second.

3. Built-in Functions used with Sets:
   - `len(s)`: Returns the number of items in the set.
   - `max(s)`: Returns the largest item in the set (items must be comparable).
   - `min(s)`: Returns the smallest item in the set (items must be comparable).
   - `sum(s)`: Sums the items of the set (items must be numeric).
   - `sorted(s)`: Returns a new sorted list from the elements in the set.
   - `any(s)`: Returns True if any element in the set is truthy.
   - `all(s)`: Returns True if all elements in the set are truthy.
   - `enumerate(s)`: Returns an enumerate object yielding (index, value) pairs.

4. Set Specific Methods:
   - Modifying Sets:
     * `s.add(elem)`: Adds a single element to the set.
     * `s.update(*others)`: Updates the set, adding elements from all other iterables provided. Equivalent to `|=`.
     * `s.remove(elem)`: Removes an element from the set. Raises `KeyError` if the element is not found.
     * `s.discard(elem)`: Removes an element from the set if it is present. Does not raise an error if not found.
     * `s.pop()`: Removes and returns an arbitrary element from the set. Raises `KeyError` if empty.
     * `s.clear()`: Removes all elements from the set.

   - Set Mathematical Operations:
     * `s.union(*others)`: Returns a new set with elements from the set and all others. Equivalent to `|`.
     * `s.intersection(*others)`: Returns a new set with elements common to the set and all others. Equivalent to `&`.
     * `s.difference(*others)`: Returns a new set with elements in the set that are not in the others. Equivalent to `-`.
     * `s.symmetric_difference(other)`: Returns a new set with elements in either the set or other but not both. Equivalent to `^`.
     * `s.intersection_update(*others)`: Updates the set, keeping only elements found in it and all others. Equivalent to `&=`.
     * `s.difference_update(*others)`: Updates the set, removing elements found in others. Equivalent to `-=`.
     * `s.symmetric_difference_update(other)`: Updates the set, keeping only elements found in either set, but not in both. Equivalent to `^=`.

   - Boolean Queries:
     * `s.isdisjoint(other)`: Returns True if the set has no elements in common with other.
     * `s.issubset(other)`: Returns True if every element in the set is in other. Equivalent to `<=`.
     * `s.issuperset(other)`: Returns True if every element in other is in the set. Equivalent to `>=`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: How do you create an empty set? Why can't you use `{}`?
A1: You create an empty set using `set()`. You cannot use `{}` because that syntax is reserved for creating an empty dictionary, as dictionaries were introduced in Python before sets.

Q2: What is the time complexity of checking if an item exists in a set vs a list?
A2: Checking membership (`item in collection`) in a set has an average time complexity of O(1) because sets are implemented using hash tables. In a list, it takes O(N) time because it requires a linear scan.

Q3: What is the difference between `remove()` and `discard()` in a set?
A3: Both remove an element from a set. However, if the element is not present, `remove()` will raise a `KeyError`, whereas `discard()` will do nothing and silently pass.

Q4: Can you add a list or dictionary as an element of a set? Why or why not?
A4: No, you cannot add mutable types like lists, dictionaries, or other sets into a set. A set's elements must be hashable, which requires them to be immutable (e.g., integers, strings, tuples). 

Q5: Explain the difference between `s.difference(other)` and `s.difference_update(other)`.
A5: `s.difference(other)` creates and returns a brand new set containing the difference, leaving the original set `s` unchanged. `s.difference_update(other)` modifies the original set `s` in place by removing the elements found in `other`, and returns `None`.
"""

