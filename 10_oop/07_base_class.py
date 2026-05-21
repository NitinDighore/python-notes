class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         self.type = type_
#         self.strength = strength
#         self.spice_level = spice_level
        

# class GingerChai(Chai):
#     def __init__(self, type_, strength, spice_level):
#         Chai.__init__(self, type_, strength)
#         self.spice_level = spice_level


class GingerChai(Chai):
    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength)
        self.spice_level = spice_level


my_chai = GingerChai("Ginger", "Strong", "High")
print(f"Type: {my_chai.type}") # Output: Type: Ginger
print(f"Strength: {my_chai.strength}") # Output: Strength: Strong
print(f"Spice Level: {my_chai.spice_level}") # Output: Spice Level: High

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Using super() outside of __init__
print("\n1. Using super() to extend regular methods:")
class AdvancedChai(Chai):
    def brew(self):
        return "Brewing base chai"
        
class FancyAdvancedChai(AdvancedChai):
    def brew(self):
        # You can call the parent's method and append your own behavior!
        base_brew = super().brew()
        return f"{base_brew} with fancy techniques!"
        
fancy_cup = FancyAdvancedChai("Fancy", "Mild")
print(fancy_cup.brew()) # Output: Brewing base chai with fancy techniques!

# Trick 2: The danger of forgetting super()
print("\n2. Forgetting to call super():")
class BrokenChai(Chai):
    def __init__(self, type_, strength, spice_level):
        # We deliberately forget to call super().__init__(type_, strength) here!
        self.spice_level = spice_level

broken = BrokenChai("Broken", "Weak", "None")
try:
    print(broken.type)
except AttributeError as e:
    print(f"Error caught: {e}") # Output: Error caught: 'BrokenChai' object has no attribute 'type'

# Trick 3: super() and Multiple Inheritance (Cooperative Multiple Inheritance)
print("\n3. super() auto-resolves Multiple Inheritance (MRO Preview):")
class A:
    def ping(self): print("Ping A")
class B(A):
    def ping(self): 
        print("Ping B")
        super().ping()
class C(A):
    def ping(self):
        print("Ping C")
        super().ping()
class D(B, C):
    def ping(self):
        print("Ping D")
        super().ping()

d = D()
d.ping() 
# Output:
# Ping D
# Ping B
# Ping C
# Ping A

"""
--- NOTES: Base Classes and `super()` ---

1. The `super()` Function:
   - `super()` returns a proxy (temporary) object that allows you to refer to the parent class (the Base Class).
   - It is predominantly used inside `__init__` to ensure that the parent class is properly initialized before the child class adds its own specific attributes, honoring the DRY (Don't Repeat Yourself) principle.

2. Why not use `Chai.__init__(self, ...)`?
   - As shown in the commented-out code, you *can* explicitly name the parent class. However, `super()` is vastly superior.
   - If the name of the Base Class changes in the future, `super()` dynamically adapts. Hardcoding `Chai.__init__` would require manual updates across the entire codebase.
   - Most importantly, `super()` is required for Multiple Inheritance to work correctly without calling the same ancestor class multiple times.

3. Latest Python Features:
   - **Zero-Argument `super()`**: In Python 2, you had to write `super(GingerChai, self).__init__()`. Python 3 introduced compiler magic that implicitly injects the class and instance, making `super().__init__()` valid and clean.
   - **Super Call Inlining (Python 3.12)**: Python 3.12 heavily optimized `super()`. Under the hood, calls to `super()` are now often inlined by the compiler. This drastically reduces the overhead of looking up parent methods, making class inheritance much faster.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if a child class defines an `__init__` method but forgets to call `super().__init__()`?
A1: The child object will be created, but the initialization logic from the parent class will never execute. Any attributes (like `self.type` in this example) defined in the parent's `__init__` will be missing, leading to an `AttributeError` if accessed.

Q2: Can you use `super()` in methods other than `__init__`?
A2: Yes. `super()` can be used in any instance method to call a method of the same name defined in the parent class. This is extremely useful for "extending" behavior rather than completely "overwriting" it.

Q3: Why is `super()` essential for multiple inheritance?
A3: `super()` leverages Python's Method Resolution Order (MRO) algorithm. It dynamically determines the next logical class in the inheritance chain. If you used hardcoded class names (like `B.__init__` and `C.__init__`), a grandparent class might be initialized twice. `super()` guarantees every ancestor is called exactly once.
"""