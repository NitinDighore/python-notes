spice_mix = set()
print(f"Initial spice mix id: {id(spice_mix)}") # Output example: Initial spice mix id: 140732812404584 (Value will vary by run)
print(f"Initial spice mix id: {spice_mix}") # Output: Initial spice mix id: set()
spice_mix.add("Ginger")
spice_mix.add("cardamom")
spice_mix.add("lemon")
print(f"Initial spice mix id: {spice_mix}") # Output example: Initial spice mix id: {'lemon', 'Ginger', 'cardamom'} (Order may vary)
print(f"After spice mix id: {id(spice_mix)}") # Output example: After spice mix id: 140732812404584 (Will match the initial ID)

"""
--- NOTES: Mutable Data Types in Python ---

1. What are Mutable Data Types?
   - Mutable data types are types whose state or contents can be modified after they are created in memory.
   - Examples of mutable data types in Python: Lists (list), Dictionaries (dict), Sets (set), Byte Arrays (bytearray).

2. Concept Demonstrated in the Code:
   - We initialize an empty set `spice_mix` and print its unique memory identifier using `id()`.
   - We then modify the set by adding elements ("Ginger", "cardamom", "lemon") using the `.add()` method.
   - When we print the `id()` again after the additions, we see that the memory address remains EXACTLY the same.
   - This proves that sets are mutable. Python modifies the existing object in-place rather than destroying it and creating a new one (which is what happens with immutable types like integers or strings).

3. Why is Mutability Important?
   - In-place Operations: Mutating objects is generally memory efficient and faster for collections of data because it avoids the overhead of copying the entire collection every time an item is added, removed, or changed.
   - Call by Object Reference: When you pass a mutable object (like a list or set) to a function, any modifications made to that object inside the function will affect the original object outside the function.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why does the `id()` of the `spice_mix` remain the same after adding items to it?
A1: Because `set` is a mutable data type in Python. When we use the `.add()` method, it modifies the data structure in its existing memory location (in-place) without needing to create a new set object.

Q2: What would happen if we tried to add a list (e.g., `["cloves", "pepper"]`) to our `spice_mix` set?
A2: It would raise a `TypeError: unhashable type: 'list'`. Sets themselves are mutable, but the elements inside a set MUST be immutable (hashable). Since a list is mutable, it cannot be added as an element of a set. You would use a tuple instead if you needed an iterable element inside a set.

Q3: Explain what happens when you pass a mutable object to a function and alter it.
A3: Since Python passes variables by "object reference," passing a mutable object to a function passes a reference to the same memory location. If the function alters the object (e.g., appends to a list or adds to a set), the original object outside the function is also altered.

Q4: If mutable types are so memory efficient for updates, why does Python have immutable equivalents like `frozenset` or `tuple`?
A4: Immutable types provide safety from accidental modification, are inherently thread-safe in multi-threaded programs, and most importantly, can be hashed. Because they can be hashed, they can be used as dictionary keys or as elements inside a set, whereas mutable types cannot. 

Q5: Can you copy a mutable object like a set to prevent it from being modified by reference?
A5: Yes. You can create a shallow copy using the `.copy()` method (e.g., `new_mix = spice_mix.copy()`) or by using the `set()` constructor (e.g., `new_mix = set(spice_mix)`). For complex nested mutable objects (like a list of lists), you might need `copy.deepcopy()` from the `copy` module.
"""
