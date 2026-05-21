class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai)) # Output: <class 'type'>

ginger_tea = Chai()
print(type(ginger_tea)) # Output: <class '__main__.Chai'>
print(type(ginger_tea) is Chai) # Output: True
print(type(ginger_tea) is ChaiTime) # Output: False

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Checking types with isinstance() (The Best Practice)
print("\n1. type() vs isinstance():")
# While type(obj) is Class works, isinstance() is the heavily preferred Pythonic way because it supports inheritance.
print(f"Is ginger_tea a Chai? {isinstance(ginger_tea, Chai)}") # Output: True

# Trick 2: Dynamic Class Creation (Metaprogramming)
print("\n2. Creating a class dynamically using type():")
# type() isn't just for checking types. With 3 arguments (name, bases, dict), it dynamically CREATES a new class!
DynamicChai = type("DynamicChai", (object,), {"flavor": "Spicy", "size": "Large"})
dynamic_cup = DynamicChai()
print(f"Dynamic Chai flavor: {dynamic_cup.flavor}") # Output: Spicy

# Trick 3: "Monkey Patching" empty objects
print("\n3. Attaching attributes to an empty object on the fly:")
# Even if a class has just 'pass', you can dynamically assign attributes to its instances!
empty_cup = Chai()
empty_cup.price = 50
empty_cup.rating = "5 Stars"
print(f"Empty cup now has a price: {empty_cup.price} and rating: {empty_cup.rating}") # Output: Empty cup now has a price: 50 and rating: 5 Stars

# Trick 4: Accessing the class from the instance directly
print("\n4. The __class__ dunder attribute:")
# You can find out what class an object belongs to without the type() function using the __class__ attribute.
print(f"ginger_tea's class is: {ginger_tea.__class__}") # Output: <class '__main__.Chai'>

"""
--- NOTES: Object-Oriented Programming (OOP) & Simple Classes ---

1. What is OOP?
   - Object-Oriented Programming is a programming paradigm based on the concept of "objects", which can contain data (attributes/properties) and code (methods/functions).
   - `01_simple_class.py` demonstrates the most basic building block of OOP: the `class` keyword.
   - A Class is a blueprint (or template). An Object (or Instance) is a concrete realization of that blueprint (like `ginger_tea`).

2. The `pass` Keyword:
   - `pass` is a null statement in Python. It does absolutely nothing.
   - It is required here because Python expects an indented block of code after the `class Chai:` declaration. `pass` prevents an `IndentationError` while you leave the class empty for future development.

3. Latest Python Features (Classes):
   - **Dataclasses (Python 3.7+ / Enhanced in 3.10+)**: Modern Python heavily uses the `@dataclass` decorator to automatically write boilerplate class code (like `__init__`, `__repr__`, etc.). Python 3.10 added the `kw_only` and `slots` parameters to dataclasses to make them incredibly fast and memory-efficient.
   - **Performance (Python 3.11+)**: Python 3.11 optimized the creation of objects (instantiation) and attribute access under the hood. Objects now take up less memory, and creating instances of classes is significantly faster.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why does `print(type(Chai))` output `<class 'type'>`?
A1: In Python, everything is an object, including classes themselves! Classes are instances of a "Metaclass". The default metaclass in Python is called `type`. So, the class `Chai` is an object of type `type`.

Q2: Why is it highly recommended to use `isinstance(obj, Class)` instead of `type(obj) is Class`?
A2: `type(obj) is Class` strictly checks if the object is exactly that specific class. `isinstance(obj, Class)` checks if the object is that class OR any subclass of that class. In OOP, inheritance is everywhere, so `isinstance` is much safer and more flexible.

Q3: Can you add attributes to an object if its class is completely empty (just has `pass`)?
A3: Yes! Python objects are highly dynamic. Unless restricted by `__slots__`, every object has an internal `__dict__` where you can assign arbitrary new attributes on the fly (known as Monkey Patching).
"""