class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2
    
    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Tea leaf age must be between 1 and 5 years")
        
leaf = TeaLeaf(2)
print(leaf.age) # Output: 4 (because 2 + 2)

try:
    leaf.age = 6
except ValueError as e:
    print(f"Error: {e}") # Output: Error: Tea leaf age must be between 1 and 5 years
    
print(leaf.age) # Output: 4 (remains unchanged due to the validation failure)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Read-Only Properties
print("\n1. Read-Only Properties:")
class SecureChai:
    def __init__(self):
        self._secret_recipe = "Top Secret Blend"
        
    @property
    def recipe(self):
        return self._secret_recipe
        # Notice there is no @recipe.setter! This makes it read-only.

secure = SecureChai()
print(f"Recipe: {secure.recipe}") # Output: Recipe: Top Secret Blend
# secure.recipe = "New Blend" # This would raise an AttributeError!

# Trick 2: Computed Properties
print("\n2. Computed Properties (No extra memory used):")
class Order:
    def __init__(self, price, quantity):
        self.price = price
        self.quantity = quantity
        
    @property
    def total(self):
        # Computes dynamically instead of storing a 'total' variable in memory
        return self.price * self.quantity

my_order = Order(50, 3)
print(f"Total Bill: {my_order.total}") # Output: Total Bill: 150

# Trick 3: The Deleter Decorator
print("\n3. Using the @property.deleter:")
class ManageableChai:
    def __init__(self):
        self._status = "Available"
        
    @property
    def status(self):
        return self._status
        
    @status.deleter
    def status(self):
        print("Deleting status securely...")
        self._status = "Deleted"

manageable = ManageableChai()
del manageable.status # Output: Deleting status securely...
print(f"New Status: {manageable.status}") # Output: New Status: Deleted

# Trick 4: Cached Properties (Python 3.8+)
print("\n4. functools.cached_property:")
from functools import cached_property
import time

class ExpensiveCalculation:
    @cached_property
    def complex_data(self):
        print("Running expensive computation...")
        time.sleep(0.5) # Simulating a 0.5-second process
        return 42

calc = ExpensiveCalculation()
print(f"First call: {calc.complex_data}") # Output: Running expensive computation... \n First call: 42
print(f"Second call: {calc.complex_data}") # Output: Second call: 42 (Instant! Computation bypassed)

"""
--- NOTES: Property Decorators and Encapsulation ---

1. What is Encapsulation?
   - Encapsulation is an OOP principle of hiding the internal state of an object and requiring all interaction to be performed through an object's methods.
   - In Python, we prefix variables with a single underscore (`self._age`) to indicate they are "protected" or "internal" (by convention).

2. The `@property` Decorator:
   - In languages like Java, developers write `getAge()` and `setAge(val)` methods to encapsulate data. This leads to verbose code like `obj.setAge(obj.getAge() + 1)`.
   - Python's `@property` decorator allows you to define methods but access them exactly like standard attributes (e.g., `leaf.age`). 
   - When you access `leaf.age`, Python automatically calls the getter method. When you write `leaf.age = 5`, Python automatically calls the setter method.

3. Latest Python Features:
   - **`functools.cached_property` (Python 3.8+)**: A fantastic addition for computed properties. If a property is expensive to calculate (like querying a database or doing complex math), `@cached_property` computes it once on the first access, stores the result in the instance's dictionary, and instantly returns the cached value on all subsequent accesses.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: How do you make an attribute read-only in a Python class?
A1: You make the underlying variable "protected" (e.g., `_attribute`) and only define a `@property` getter method for it, deliberately omitting the `@attribute.setter` method.

Q2: Can I just bypass the property and modify `leaf._age` directly?
A2: Yes. Because Python does not have strict access modifiers (like `private` in C++), a developer can technically still do `leaf._age = 100`, bypassing your validation logic. The underscore is a strong convention, relying on the philosophy that "we are all consenting adults here."

Q3: Why would you use a `@property` instead of just a regular attribute?
A3: Properties allow you to add validation logic (like ensuring `age` is between 1 and 5) without changing the class's public interface. If you start with a normal attribute and later realize you need validation, you can easily convert it to a `@property` without breaking any external code that uses `obj.attribute`.
"""
