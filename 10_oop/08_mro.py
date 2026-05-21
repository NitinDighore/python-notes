class A:
    label = "A: Base class"

class B(A):
    label = "B: Masala blend"

class C(A):
    label = "C: Herbal blend"

class D(C, B):
    pass

cup = D()
print(cup.label) # Output: C: Herbal blend
print(D.__mro__) # Output: (<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: mro() method vs __mro__ attribute
print("\n1. mro() method:")
# You can also use the .mro() method which returns a List instead of a Tuple.
print(f"MRO List: {D.mro()}") # Output: [<class '__main__.D'>, <class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]

# Trick 2: Deliberately breaking the MRO (Inconsistent Hierarchy)
print("\n2. Inconsistent MRO Error:")
# B inherits from A. Therefore, B MUST be resolved before A.
# If we try to define `class BadClass(A, B):`, Python will crash because we are asking it to resolve A before B!
try:
    class BadClass(A, B): 
        pass
except TypeError as e:
    print(f"MRO crashed gracefully: {e}") # Output: MRO crashed gracefully: Cannot create a consistent method resolution order (MRO) for bases A, B

# Trick 3: Cooperative super() across the MRO
print("\n3. Using super() to travel the MRO:")
# super() doesn't just call the "parent". It calls the *NEXT* class in the MRO!
class X:
    def brew(self): print("Brewing X")
class Y(X):
    def brew(self): 
        print("Brewing Y")
        super().brew()
class Z(X):
    def brew(self): 
        print("Brewing Z")
        super().brew()
class MegaBlend(Y, Z):
    def brew(self):
        print("Brewing MegaBlend")
        super().brew()

mega = MegaBlend()
mega.brew() 
# Output: 
# Brewing MegaBlend (Next is Y)
# Brewing Y (Next is Z, NOT X! Because MRO is MegaBlend -> Y -> Z -> X)
# Brewing Z (Next is X)
# Brewing X

"""
--- NOTES: Method Resolution Order (MRO) ---

1. What is MRO?
   - MRO stands for Method Resolution Order. It is the exact order in which Python searches for base classes when executing a method or accessing an attribute.
   - In single inheritance, it's simple: look in the Child, then Parent, then Grandparent, then `object`.
   - In multiple inheritance (like `class D(C, B):`), it resolves left-to-right (`C` before `B`), whilst ensuring that a parent class (`A`) is never searched before any of its children (`B` or `C`).

2. C3 Linearization (The Diamond Problem):
   - Python resolves the "Diamond Problem" (where multiple parent classes share the same grandparent) using an algorithm called C3 Linearization.
   - C3 guarantees: 
     1) Children precede their parents.
     2) If a class inherits from multiple classes, they are kept in the order specified in the base list (left-to-right).
   - If C3 cannot satisfy both conditions simultaneously, Python raises a `TypeError` (as shown in Trick 2).

3. Latest Python Features:
   - **MRO remains stable**: Python adopted C3 Linearization in Python 2.3, and it remains the bedrock of Python 3's class system.
   - **Zero-argument `super()` (Python 3+)**: The `super()` keyword was specifically overhauled in Python 3 to seamlessly read the `__mro__` under the hood. It dynamically determines the *current* class executing the method and delegates to the *next* class in the MRO array, making multiple inheritance incredibly powerful and cooperative.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the "Diamond Problem" in multiple inheritance?
A1: The Diamond Problem occurs when a class inherits from two parent classes that both inherit from the same grandparent class. The ambiguity arises over which path to traverse first. Python cleanly solves this using the C3 Linearization MRO algorithm to guarantee a consistent order.

Q2: What is the difference between `__mro__` and `mro()`?
A2: `__mro__` is a read-only class attribute that stores a Tuple of the method resolution order. `mro()` is a method on the class (belonging to the `type` metaclass) that returns a List of the method resolution order. Custom metaclasses can override `mro()` to change inheritance behavior, but this is highly advanced and rare.

Q3: If `class Child(Parent1, Parent2):` is defined, and both parents have a method named `start()`, which one gets executed when `child.start()` is called?
A3: `Parent1.start()` gets executed. Because Python evaluates multiple inheritance from left to right, `Parent1` precedes `Parent2` in the MRO.

Q4: Will `super()` always call the direct parent of a class?
A4: No! In multiple inheritance, `super()` delegates to the *next class in the MRO*. As shown in Trick 3, inside `Y.brew()`, `super().brew()` actually calls `Z.brew()`, not `X.brew()`, because `Z` is the next class in `MegaBlend`'s MRO array. This is called "Cooperative Multiple Inheritance".
"""