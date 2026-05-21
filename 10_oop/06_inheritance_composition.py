class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} chai....")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamom, ginger, cloves.")


class ChaiShop:
    chai_cls = BaseChai

    def __init__(self):
        self.chai = self.chai_cls("Regular")

    def serve(self):
        print(f"Serving {self.chai.type} chai in the shop")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai


shop = ChaiShop()
fancy = FancyChaiShop()

shop.serve() 
# Output: 
# Serving Regular chai in the shop
# Preparing Regular chai....

fancy.serve() 
# Output: 
# Serving Regular chai in the shop
# Preparing Regular chai....

fancy.chai.add_spices() # Output: Adding cardamom, ginger, cloves.

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Dependency Injection (Better Composition)
print("\n1. Dependency Injection:")
# Instead of hardcoding the class inside the shop, pass the instantiated object in!
# This makes the shop highly testable and loosely coupled.
class ModernShop:
    def __init__(self, chai_instance):
        self.chai = chai_instance # HAS-A relationship (Composition)

my_custom_chai = MasalaChai("Super Spicy")
modern_shop = ModernShop(my_custom_chai)
modern_shop.chai.prepare() # Output: Preparing Super Spicy chai....

# Trick 2: Dynamic Delegation (__getattr__)
print("\n2. Dynamic Delegation (Composition acting like Inheritance):")
# You can make a composed object seamlessly route missing methods to its internal component
class SmartShop:
    def __init__(self):
        self._internal_chai = MasalaChai("Smart")
        
    def __getattr__(self, name):
        # If SmartShop doesn't have a method, automatically pass the call to _internal_chai!
        return getattr(self._internal_chai, name)

smart = SmartShop()
smart.add_spices() # Output: Adding cardamom, ginger, cloves. (Routed automatically!)

# Trick 3: isinstance vs issubclass
print("\n3. isinstance() vs issubclass():")
print(f"Is MasalaChai a subclass of BaseChai? {issubclass(MasalaChai, BaseChai)}") # Output: True
print(f"Is fancy a ChaiShop? {isinstance(fancy, ChaiShop)}") # Output: True
print(f"Is fancy a BaseChai? {isinstance(fancy, BaseChai)}") # Output: False (It HAS a BaseChai, but it IS NOT a BaseChai)

"""
--- NOTES: Inheritance vs Composition ---

1. Inheritance (The "IS-A" Relationship):
   - `MasalaChai` inherits from `BaseChai`. Therefore, MasalaChai IS-A BaseChai.
   - It automatically receives all methods (`prepare`) and attributes of the parent class.
   - Best used when objects share core functionality and belong to the exact same taxonomic family.

2. Composition (The "HAS-A" Relationship):
   - `ChaiShop` does NOT inherit from `BaseChai`. Instead, it instantiates `BaseChai` inside its `__init__` and saves it to `self.chai`.
   - Therefore, ChaiShop HAS-A Chai. 
   - It delegates the work to its internal component (`self.chai.prepare()`).

3. "Favor Composition over Inheritance":
   - A famous design principle from the "Gang of Four" design patterns book.
   - Deep inheritance trees make code incredibly fragile (the "Fragile Base Class" problem). If you change the parent, it can break dozens of children.
   - Composition is loosely coupled. You can swap out the internal parts dynamically at runtime (like we did with `chai_cls = MasalaChai`) without altering the `ChaiShop` structure.

4. Latest Python Features (Python 3.8+):
   - **`typing.Protocol` (Duck Typing/Structural Subtyping)**: Modern Python highly favors composition and loose coupling. By using `Protocol`, you can define an "Interface" (e.g., any object that has a `prepare()` method). Your `ChaiShop` can accept ANY object that matches the Protocol, regardless of whether it inherits from `BaseChai` or not!

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between Inheritance and Composition?
A1: Inheritance implies an "IS-A" relationship (a Car IS-A Vehicle) where the child tightly binds to the parent's implementation. Composition implies a "HAS-A" relationship (a Car HAS-A Engine) where a class contains objects of other classes to delegate work, promoting loose coupling.

Q2: How did `FancyChaiShop` change the type of chai served without rewriting the `__init__` method?
A2: `ChaiShop` was designed using a Factory pattern approach. It uses the class attribute `chai_cls` to instantiate the tea in `__init__`. `FancyChaiShop` simply overrides `chai_cls` to point to `MasalaChai`. When `FancyChaiShop` calls `super().__init__()` (implicitly done here since it has no `__init__`), it uses the overridden class attribute!

Q3: Why is Composition often preferred over Inheritance?
A3: Because it is more flexible and less fragile. You can change the behavior of a composed class at runtime by swapping its internal components. With inheritance, behaviors are hardcoded at compile time. Furthermore, deep inheritance trees often lead to the "Diamond Problem" (multiple inheritance conflicts).
"""