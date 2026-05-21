ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")
print(f"Ingredients are: {ingredients}") # Output: Ingredients are: ['water', 'milk', 'black tea', 'sugar']
ingredients.remove("water")
print(f"Ingredients are: {ingredients}") # Output: Ingredients are: ['milk', 'black tea', 'sugar']

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai: {chai_ingredients}") # Output: chai: ['water', 'milk', 'ginger', 'cardamom']
chai_ingredients.insert(2, "black tea")
print(f"chai: {chai_ingredients}") # Output: chai: ['water', 'milk', 'black tea', 'ginger', 'cardamom']

last_added = chai_ingredients.pop()
print(f"{last_added}") # Output: cardamom
print(f"chai: {chai_ingredients}") # Output: chai: ['water', 'milk', 'black tea', 'ginger']
chai_ingredients.reverse()
print(f"chai: {chai_ingredients}") # Output: chai: ['ginger', 'black tea', 'milk', 'water']
chai_ingredients.sort()
print(f"chai: {chai_ingredients}") # Output: chai: ['black tea', 'ginger', 'milk', 'water']

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar level: {max(sugar_levels)}") # Output: Maximum sugar level: 5
print(f"Minimum sugar level: {min(sugar_levels)}") # Output: Minimum sugar level: 1

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
print(f"Liquid mix: {full_liquid_mix}") # Output: Liquid mix: ['water', 'milk', 'ginger']

strong_brew = ["black tea", "water"] * 3
print(f"String brew: {strong_brew}") # Output: String brew: ['black tea', 'water', 'black tea', 'water', 'black tea', 'water']

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA", b"CARD")
print(f"Bytes: {raw_spice_data}") # Output: Bytes: bytearray(b'CARDMON')

"""
--- NOTES: Lists in Python ---

1. What are Lists?
   - Lists are ordered, mutable collections of items in Python.
   - They are defined using square brackets `[]` and can contain mixed data types.
   - Because they are mutable, lists can be modified in place (items can be added, removed, or changed) without creating a new object.

2. Built-in Functions used with Lists:
   - `len(lst)`: Returns the total number of items in the list.
   - `max(lst)`: Returns the largest item in the list (items must be comparable).
   - `min(lst)`: Returns the smallest item in the list (items must be comparable).
   - `sum(lst)`: Sums the items of an iterable from left to right and returns the total (items must be numeric).
   - `sorted(lst, key=None, reverse=False)`: Returns a new sorted list from the items in iterable.
   - `any(lst)`: Returns True if any item of the iterable is true. If the iterable is empty, returns False.
   - `all(lst)`: Returns True if all items of the iterable are true (or if the iterable is empty).
   - `enumerate(lst, start=0)`: Returns an enumerate object. Yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument.
   - `zip(*iterables)`: Returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the argument sequences or iterables.

3. List Specific Methods:
   - Adding Elements:
     * `lst.append(x)`: Adds an item to the end of the list.
     * `lst.extend(iterable)`: Extends the list by appending all the items from the iterable.
     * `lst.insert(i, x)`: Inserts an item at a given position. The first argument is the index of the element before which to insert.
   
   - Removing Elements:
     * `lst.remove(x)`: Removes the first item from the list whose value is equal to x. Raises a ValueError if there is no such item.
     * `lst.pop([i])`: Removes the item at the given position in the list, and returns it. If no index is specified, `a.pop()` removes and returns the last item in the list.
     * `lst.clear()`: Removes all items from the list. Equivalent to `del lst[:]`.
   
   - Searching and Reorganizing:
     * `lst.index(x, [start, [stop]])`: Returns zero-based index in the list of the first item whose value is equal to x. Raises a ValueError if there is no such item.
     * `lst.count(x)`: Returns the number of times x appears in the list.
     * `lst.sort(key=None, reverse=False)`: Sorts the items of the list in place.
     * `lst.reverse()`: Reverses the elements of the list in place.
     * `lst.copy()`: Returns a shallow copy of the list. Equivalent to `lst[:]`.

4. Other Operations:
   - Concatenation (`+`): Combines two lists to create a new list (e.g., `list1 + list2`).
   - Multiplication (`*`): Repeats a list a specified number of times to create a new list (e.g., `list * 3`).
   - `bytearray` (Bonus in code): A mutable sequence of integers in the range 0 <= x < 256. Useful for dealing with raw binary data or manipulating strings at a byte level efficiently.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between `append()` and `extend()`?
A1: `append()` adds its argument as a single element to the end of a list. The length of the list will increase by 1. `extend()` iterates over its argument adding each element to the list, extending the list. The length of the list will increase by however many elements were in the iterable argument. For example, if `lst = [1, 2]`, `lst.append([3, 4])` results in `[1, 2, [3, 4]]`, while `lst.extend([3, 4])` results in `[1, 2, 3, 4]`.

Q2: Is a list mutable or immutable? What does that mean for operations like `sort()` vs `sorted()`?
A2: Lists are mutable, meaning their contents can be modified in place. The method `sort()` modifies the original list in place and returns `None`. The built-in function `sorted()` takes an iterable, leaves the original iterable unchanged, and returns a new sorted list.

Q3: Explain what `list.pop()` does when called without arguments vs with an argument.
A3: When called without arguments, `list.pop()` removes and returns the last item of the list. When called with an index argument, `list.pop(i)` removes and returns the item at index `i`.

Q4: What is the time complexity of `list.insert(0, value)` and why?
A4: The time complexity is O(N). Because lists in Python are implemented as dynamic arrays, inserting an element at the beginning requires shifting all existing elements one position to the right in memory.

Q5: What is the difference between a shallow copy (using `lst.copy()` or `lst[:]`) and a deep copy (using `copy.deepcopy(lst)`)?
A5: A shallow copy creates a new list object but populates it with references to the child objects found in the original. If the list contains mutable objects (like other lists), modifying those nested objects will affect both copies. A deep copy creates a new list object and recursively copies all child objects, meaning no references are shared; modifications to nested objects in the deep copy will not affect the original.
"""