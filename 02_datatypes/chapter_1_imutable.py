sugar_amount = 2
print(f"Initial sugar: {sugar_amount}") # Output: Initial sugar: 2

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}") # Output: Second Initial sugar: 12

print(f"ID of 2: {id(2)}") # Output example: ID of 2: 140732812404584 (Value will vary by run)
print(f"ID of 12: {id(12)}") # Output example: ID of 12: 140732812404904 (Value will vary by run)

"""
--- NOTES: Immutable Data Types in Python ---

1. What are Immutable Data Types?
   - Immutable data types are types whose state or value cannot be modified after they are created.
   - Examples of immutable data types in Python: Integers (int), Floats (float), Strings (str), Tuples (tuple), Booleans (bool), Frozensets (frozenset).

2. Concept Demonstrated in the Code:
   - When we assign `sugar_amount = 2`, an integer object with the value `2` is created in memory, and the variable name `sugar_amount` refers to it.
   - When we reassign `sugar_amount = 12`, Python does NOT modify the existing integer object `2` into `12`.
   - Instead, it creates a NEW integer object `12` in memory (or reuses a cached one) and updates the variable `sugar_amount` to point to this new object.
   - This behavior is verified using the `id()` function, which returns the memory address of an object. The IDs of `2` and `12` are different, proving that reassignment creates/references a new object rather than modifying the original one.

3. Why is Immutability Important?
   - Thread safety: Immutable objects are inherently thread-safe in concurrent programs since their state cannot be changed.
   - Dictionary Keys & Sets: Only hashable objects can be used as dictionary keys or stored in sets. Immutable types like integers, strings, and tuples (if they only contain immutable elements) are hashable.
   - Memory Efficiency: Python caches small integers (-5 to 256) and short strings (string interning). Since they are immutable, multiple variables can safely reference the same object without the risk of one variable modifying the value for others.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between mutable and immutable data types in Python? Give examples.
A1: Mutable types can be modified in-place after creation (e.g., Lists, Dictionaries, Sets). Modifying them does not change their memory address. Immutable types cannot be changed after creation (e.g., Integers, Strings, Tuples). Any operation that seems to modify an immutable object actually creates a completely new object.

Q2: If strings are immutable, how are we able to do operations like `s = s + "a"`?
A2: When you do `s = s + "a"`, Python does not modify the original string `s` in memory. It evaluates the expression, creates a completely new string object with the concatenated result, and then reassigns the variable `s` to point to this new object.

Q3: Can a tuple (which is immutable) contain a mutable object, like a list? If so, can you modify that list?
A3: Yes, a tuple can contain mutable objects. While you cannot modify the tuple itself (e.g., you can't replace the list with another object or change the tuple's size), you CAN modify the contents of the mutable list inside it. The tuple only holds a reference to the list, and that reference doesn't change when the list's contents change.

Q4: What will be the output of `x = 10; y = 10; print(x is y)`? Why?
A4: The output will be `True`. This is because of Python's "integer caching" (or interning). Python caches integer objects in the range of -5 to 256 for performance optimization. Therefore, both `x` and `y` reference the exact same object in memory.

Q5: Explain the purpose of the `id()` function as used in the code snippet.
A5: The `id()` function returns a unique integer identifying the object (in CPython, it's the memory address). In this context, it is used to demonstrate immutability by proving that the objects `2` and `12` are completely different objects residing at different memory locations, confirming that the value of `2` wasn't mutated into `12`.
"""
