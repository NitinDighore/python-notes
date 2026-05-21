class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
    
    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")
        return cls(tea_type, sweetness, size)
    
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in ["Small", "Medium", "Large"]


print(ChaiUtils.is_valid_size("Medium")) # Output: True

order1 = ChaiOrder.from_dict({"tea_type": "masala", "sweetness": "medium", "size":"Large"})
order2 = ChaiOrder.from_string("Ginger-Low-Small")
order3 = ChaiOrder("Large", "Low", "Large")

print(order1.__dict__) # Output: {'tea_type': 'masala', 'sweetness': 'medium', 'size': 'Large'}
print(order2.__dict__) # Output: {'tea_type': 'Ginger', 'sweetness': 'Low', 'size': 'Small'}
print(order3.__dict__) # Output: {'tea_type': 'Large', 'sweetness': 'Low', 'size': 'Large'}

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Why we use 'cls' instead of hardcoding 'ChaiOrder'
print("\n1. Inheritance with Alternative Constructors:")
class SpecialChaiOrder(ChaiOrder):
    def __init__(self, tea_type, sweetness, size):
        super().__init__(tea_type, sweetness, size)
        self.is_special = True

# Because from_string uses `cls()`, calling it on the child class creates a CHILD object, not a parent object!
special_order = SpecialChaiOrder.from_string("Matcha-High-Large")
print(f"Is it a SpecialChaiOrder? {type(special_order).__name__}") # Output: Is it a SpecialChaiOrder? SpecialChaiOrder
print(f"Has is_special attribute? {hasattr(special_order, 'is_special')}") # Output: Has is_special attribute? True

# Trick 2: Tracking Class State (Object Registry)
print("\n2. Using classmethod to track state across all instances:")
class TrackedChai:
    _total_orders = 0 # Class variable
    
    def __init__(self):
        TrackedChai.increment_orders()
        
    @classmethod
    def increment_orders(cls):
        cls._total_orders += 1
        
    @classmethod
    def get_total_orders(cls):
        return f"Total cups ordered globally: {cls._total_orders}"

c1, c2 = TrackedChai(), TrackedChai()
print(TrackedChai.get_total_orders()) # Output: Total cups ordered globally: 2

# Trick 3: Modern Type Hinting for Alternative Constructors
print("\n3. Type Hinting with typing.Self (Python 3.11+):")
from typing import Self

class ModernOrder:
    def __init__(self, name: str):
        self.name = name
        
    @classmethod
    def create_default(cls) -> Self:
        # Self tells the IDE that this returns an instance of whatever class called it
        return cls("Standard Tea")

print(f"Modern Order: {ModernOrder.create_default().name}") # Output: Modern Order: Standard Tea

"""
--- NOTES: Class Methods (`@classmethod`) ---

1. What is a Class Method?
   - A `@classmethod` is a method that is bound to the class and not the object of the class.
   - It implicitly receives the class itself as its first argument (conventionally named `cls`), just like instance methods receive `self`.
   
2. Alternative Constructors (Overloading `__init__`):
   - Unlike languages like Java or C++, Python does not support standard constructor overloading (defining multiple `__init__` methods with different parameters).
   - The Pythonic way to handle multiple initialization paths (e.g., creating an order from individual strings vs creating it from a JSON dictionary) is to use `@classmethod` to create "Alternative Constructors" (like `from_dict` or `from_string`).

3. Latest Python Features:
   - **`typing.Self` (Python 3.11+)**: Historically, type hinting a method that returns an instance of its own class (like an alternative constructor) was awkward (you had to use string literals like `-> "ChaiOrder"` or messy `TypeVar`s). Python 3.11 introduced `typing.Self`, making this highly elegant and safe across inheritance trees.
   - **Deprecation of `@classmethod` + `@property` (Python 3.11+)**: Previously, developers occasionally stacked these two decorators to create class-level properties. This behavior was complex, buggy, and has been formally deprecated/removed in Python 3.11.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why do we write `return cls(...)` in an alternative constructor instead of `return ChaiOrder(...)`?
A1: If you hardcode the class name `ChaiOrder(...)`, the method will *always* return a `ChaiOrder` object, even if the method was inherited and called by a subclass (like `SpecialChaiOrder`). By using `return cls(...)`, it dynamically uses the specific class that invoked the method, ensuring subclasses construct their own type correctly.

Q2: What is the main difference between `@classmethod` and `@staticmethod`?
A2: A `@classmethod` takes the class itself as its implicit first argument (`cls`), allowing it to access or modify class state, and instantiate objects dynamically. A `@staticmethod` takes no implicit first argument; it behaves like a standard standalone function that just happens to be organized inside the class namespace.

Q3: How do you achieve constructor overloading in Python?
A3: Because Python does not allow multiple `__init__` definitions, constructor overloading is achieved by using `@classmethod` to define alternative builder methods (usually prefixed with `from_` or `create_`, e.g., `from_string` or `from_json`).
"""