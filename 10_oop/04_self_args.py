class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe()) # Output: A 150ml chai cup
print(Chaicup.describe(cup)) # Output: A 150ml chai cup

cup_two = Chaicup()
cup_two.size = 100
print(Chaicup.describe(cup_two)) # Output: A 100ml chai cup

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Bound Methods vs Functions
print("\n1. Bound Methods:")
# When accessed via an instance, it's a "bound method" (it remembers the instance)
print(f"cup.describe is: {cup.describe}") # Output: <bound method Chaicup.describe of ...>
# When accessed via the Class, it's just a standard function!
print(f"Chaicup.describe is: {Chaicup.describe}") # Output: <function Chaicup.describe at ...>

# Trick 2: 'self' is NOT a keyword!
print("\n2. 'self' is just a convention:")
class RebelCup:
    size = 200
    # You can name the first parameter ANYTHING. 'this_object' works perfectly fine.
    def describe(this_object):
        return f"Rebel cup is {this_object.size}ml"

rc = RebelCup()
print(rc.describe()) # Output: Rebel cup is 200ml

# Trick 3: Duck Typing with explicit class method calls
print("\n3. Duck Typing:")
class FakeCup:
    size = 500 # It just needs to have the 'size' attribute

fake = FakeCup()
# We can pass a completely unrelated object into Chaicup.describe as long as it quacks like a cup!
print(Chaicup.describe(fake)) # Output: A 500ml chai cup

"""
--- NOTES: The `self` Parameter ---

1. What is `self`?
   - In Python, `self` represents the instance of the class. It binds the attributes with the given arguments.
   - When you call a method like `cup.describe()`, Python implicitly translates it behind the scenes to `Chaicup.describe(cup)`.
   - This is why every instance method in a Python class must take `self` (or some equivalent name) as its very first parameter.

2. Bound vs Unbound:
   - A "Bound Method" is a function that has its first argument (`self`) already locked into a specific instance.
   - In Python 3, calling a method directly on the class (`Chaicup.describe`) returns a standard, unbound function, which requires you to manually provide the instance as the first argument.

3. Latest Python Features (Python 3.11+):
   - **`typing.Self` (PEP 673)**: Introduced in Python 3.11, the `Self` type hint makes it incredibly easy to annotate methods that return an instance of their own class (like builder patterns or factory methods). 
     Example: 
     ```python
     from typing import Self
     class Chai:
         def brew(self) -> Self:
             return self
     ```

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Is `self` a reserved keyword in Python?
A1: No, `self` is not a keyword. It is simply a very strong PEP 8 naming convention. You could technically name the first parameter `this`, `me`, or `obj`, and Python would execute it perfectly fine. However, using anything other than `self` is heavily frowned upon.

Q2: What error do you get if you forget to include `self` in an instance method definition?
A2: You will get a `TypeError`. For example, if you define `def describe():` and then call `cup.describe()`, Python translates it to `Chaicup.describe(cup)`. It will raise an error stating: `describe() takes 0 positional arguments but 1 was given`.

Q3: If `cup.describe()` and `Chaicup.describe(cup)` do the exact same thing, which one should I use?
A3: You should virtually always use `cup.describe()`. It is the idiomatic, Object-Oriented way to invoke a method in Python. Explicitly calling the class and passing the instance is mostly used when working with `super()` or multiple inheritance.
"""