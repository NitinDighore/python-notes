class ChaiOrder:
    
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai"
    
order = ChaiOrder("Masala", 200)
print(order.summary()) # Output: 200ml of Masala chai

order_two = ChaiOrder("Ginger", 220)
print(order_two.summary()) # Output: 220ml of Ginger chai

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: __new__ vs __init__ (The true constructor)
print("\n1. __new__ vs __init__:")
class MagicCup:
    def __new__(cls, *args, **kwargs):
        print("1. __new__ is called to CREATE the object in memory")
        instance = super().__new__(cls)
        return instance
        
    def __init__(self, type_):
        print("2. __init__ is called to INITIALIZE the object's state")
        self.type = type_

magic = MagicCup("Elixir") # Output: 1. __new__ is called... then 2. __init__ is called...

# Trick 2: Alternative Constructors using @classmethod
print("\n2. Alternative Constructors:")
class CustomChai:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size
        
    @classmethod
    def from_string(cls, data_string):
        # Allows creating an object from a string format like "Matcha-300"
        t, s = data_string.split("-")
        return cls(t, int(s))

custom = CustomChai.from_string("Matcha-300")
print(f"Created from string: {custom.type}, {custom.size}ml") # Output: Created from string: Matcha, 300ml

# Trick 3: Using @dataclass to auto-generate __init__
print("\n3. Modern Python with @dataclass:")
from dataclasses import dataclass

@dataclass
class ModernChai:
    type_: str
    size: int

modern = ModernChai("Oolong", 250)
print(f"Dataclass Chai: {modern}") # Output: Dataclass Chai: ModernChai(type_='Oolong', size=250)

"""
--- NOTES: Constructors (`__init__`) and Object Instantiation ---

1. The `__init__` Method:
   - `__init__` is often called the "constructor" in Python, but it's technically the "initializer".
   - It is automatically called immediately after the object has been created in memory.
   - Its primary job is to set up the initial state of the object by assigning arguments to `self` attributes.
   - It MUST return `None`. Returning any other value will raise a `TypeError`.

2. The True Constructor (`__new__`):
   - `__new__(cls)` is the actual constructor. It allocates memory and creates the empty object.
   - It is a static method (even without the decorator) that returns a new instance of the class. Once returned, Python passes that instance to `__init__`.

3. Latest Python Features (Python 3.10+):
   - **Dataclasses (`@dataclass`)**: As shown in Trick 3, writing `__init__` manually is becoming less common for simple data-holding classes. Python 3.10 added powerful features to dataclasses like `kw_only=True` (forcing keyword arguments during instantiation) and `slots=True` (drastically reducing memory usage).

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between `__new__` and `__init__`?
A1: `__new__` is a class-level method responsible for *creating* and returning a new, empty instance of a class. `__init__` is an instance-level method responsible for *initializing* the state of that newly created instance.

Q2: Can `__init__` return a value?
A2: No. `__init__` is strictly an initializer. It must implicitly return `None`. If you try to write `return True` inside `__init__`, Python will raise a `TypeError: __init__() should return None`.

Q3: How do you handle multiple ways to instantiate a class (e.g., from individual parameters OR from a JSON string)?
A3: Python does not support method overloading (having multiple `__init__` functions with different signatures). The standard, Pythonic way is to use `@classmethod` to create "Alternative Constructors" (as demonstrated in Trick 2).
"""