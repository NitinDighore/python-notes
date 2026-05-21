class Chai:
    origin = "India"

print(Chai.origin) # Output: India

Chai.is_hot = True
print(Chai.is_hot) # Output: True

# creating objects from class Chai

masala = Chai()
print(f"Masala {masala.origin}") # Output: Masala India
print(f"Masala {masala.is_hot}") # Output: Masala True
masala.is_hot = False

print("Class: ", Chai.is_hot) # Output: Class:  True
print(f"Masala {masala.is_hot}") # Output: Masala False
masala.flavor = "Masala"
print(masala.flavor) # Output: Masala

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Visualizing Namespaces with __dict__
print("\n1. Looking directly into namespaces:")
# Python objects store their unique attributes in a dictionary called __dict__
print(f"Masala instance namespace: {masala.__dict__}") # Output: {'is_hot': False, 'flavor': 'Masala'}
# Notice that 'origin' is NOT in the instance namespace. It belongs to the class namespace!
print(f"Chai class namespace contains 'origin': {'origin' in Chai.__dict__}") # Output: True

# Trick 2: The Mutable Class Attribute Trap
print("\n2. The Mutable Class Variable Trap:")
class TrickyChai:
    spices = [] # This list is shared across ALL instances!

cup1 = TrickyChai()
cup2 = TrickyChai()
cup1.spices.append("Ginger") # Modifying the shared list via cup1

print(f"Cup 2 spices: {cup2.spices}") # Output: Cup 2 spices: ['Ginger'] (It leaked from cup1 to cup2!)
# Lesson: Never use mutable defaults as class variables unless you explicitly want them shared globally!

# Trick 3: Shadowing and Un-shadowing
print("\n3. Deleting instance attributes to fallback to class attributes:")
# When we did `masala.is_hot = False` earlier, it "shadowed" the class variable for this specific instance.
print(f"Before delete: {masala.is_hot}") # Output: False (Instance variable)
del masala.is_hot # Delete the instance variable
print(f"After delete: {masala.is_hot}") # Output: True (Fell back to reading the Class variable!)

"""
--- NOTES: Namespaces, Class vs Instance Variables ---

1. What is a Namespace?
   - A namespace is essentially a dictionary mapping variable names (keys) to their corresponding objects (values).
   - In OOP, the Class has its own namespace, and every single Instance created from that class has its own separate namespace.

2. Class Attributes vs Instance Attributes:
   - **Class Attributes** (like `origin = "India"`): Belong to the class itself. They are shared across all instances of the class. They save memory when multiple objects need the exact same value.
   - **Instance Attributes** (like `masala.flavor`): Belong exclusively to the specific object/instance. They define the unique state of that specific object.

3. Attribute Resolution Order:
   - When you access `masala.is_hot`, Python searches in this exact order:
     1. The Instance namespace (`masala.__dict__`).
     2. The Class namespace (`Chai.__dict__`).
     3. The Base Classes (Parent classes) if inheritance is used.
   - If it doesn't find the attribute anywhere, it throws an `AttributeError`.

4. Latest Python Features (Python 3.11+):
   - **Adaptive Specialization (PEP 659)**: Python 3.11 dramatically sped up attribute access. Under the hood, Python caches the exact memory offset of object attributes dynamically during runtime, effectively bypassing the `__dict__` dictionary lookup overhead for "type-stable" code. This makes reading/writing `masala.flavor` significantly faster in modern Python.
   - **`__slots__` usage**: For massive scaling, modern Python code heavily utilizes `__slots__ = ('flavor', 'is_hot')` in classes. This entirely disables the `__dict__` for instances, saving massive amounts of memory and enforcing strict attribute constraints.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if I modify a class attribute using the class name (e.g., `Chai.origin = "China"`)?
A1: The change will immediately reflect across ALL existing and future instances of `Chai` that do not have their own explicitly set `origin` instance attribute, because they all reference the same class dictionary.

Q2: What happens if I modify a class attribute using an instance (e.g., `masala.origin = "China"`)?
A2: It does NOT modify the class attribute. Instead, Python creates a brand-new instance attribute called `origin` specifically inside the `masala` object's namespace. This new local attribute "shadows" (hides) the class attribute for that specific instance.

Q3: Why did `cup2.spices` show "Ginger" in the trick example?
A3: Because `spices = []` was defined at the class level, so it is a single list object stored in memory and shared by all instances. When `cup1.spices.append()` was called, it mutated that shared list. To give each cup its own list, it must be initialized inside the `__init__` method.

Q4: What is `__dict__`?
A4: `__dict__` is a built-in dictionary attribute present on most Python objects and classes. It stores all the writable, dynamic attributes for that specific namespace.
"""