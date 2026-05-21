class Chai:
    temperature = "hot"
    strength = "Strong"


cutting = Chai()
print(cutting.temperature) # Output: hot

cutting.temperature = "Mild"
cutting.cup = "small"
print("After changing ",cutting.temperature) # Output: After changing  Mild
print("cup size is  ",cutting.cup) # Output: cup size is   small
print("Direct look into the class ", Chai.temperature) # Output: Direct look into the class  hot

del cutting.temperature
del cutting.cup
print(cutting.temperature) # Output: hot

# Wrapped in a try-except block because deleting the cup attribute makes the next line crash!
try:
    print(cutting.cup)
except AttributeError as e:
    print(f"Error: {e}") # Output: Error: 'Chai' object has no attribute 'cup'

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Dynamic Attribute Manipulation using built-ins
print("\n1. getattr(), setattr(), hasattr(), delattr():")
# These built-in functions allow you to manipulate attributes dynamically using strings
setattr(cutting, "price", 10)
print(f"Has price? {hasattr(cutting, 'price')}") # Output: Has price? True
print(f"Price is: {getattr(cutting, 'price')}") # Output: Price is: 10
delattr(cutting, "price")

# Trick 2: Preventing Attribute Shadowing with __slots__
print("\n2. Preventing dynamic attributes with __slots__:")
class StrictChai:
    __slots__ = ['temperature'] # Only allows 'temperature' to be set
    def __init__(self):
        self.temperature = "hot"

strict_cup = StrictChai()
# strict_cup.cup_size = "small" # Uncommenting this raises AttributeError: 'StrictChai' object has no attribute 'cup_size'
print("strict_cup.cup_size assignment prevented by __slots__!")

# Trick 3: Intercepting missing attributes with __getattr__
print("\n3. Catching missing attributes dynamically:")
class ForgivingChai:
    def __getattr__(self, name):
        # This is ONLY called if the attribute is NOT found via normal lookup
        return f"Attribute '{name}' doesn't exist, but here's a default!"

magic_cup = ForgivingChai()
print(magic_cup.sugar_level) # Output: Attribute 'sugar_level' doesn't exist, but here's a default!

"""
--- NOTES: Attribute Shadowing ---

1. What is Attribute Shadowing?
   - Attribute shadowing occurs when an instance attribute has the exact same name as a class attribute.
   - Because Python looks in the instance's namespace (`__dict__`) before looking in the class's namespace, the instance attribute "shadows" or hides the class attribute.
   - When we do `cutting.temperature = "Mild"`, we aren't changing `Chai.temperature`. We are creating a brand new instance attribute that intercepts the lookup.

2. `del` behavior:
   - When you `del cutting.temperature`, it deletes the instance attribute. 
   - The next time you call `cutting.temperature`, Python doesn't find it in the instance, so it gracefully falls back to the class attribute, returning `"hot"`.
   - `cutting.cup` was never a class attribute. It only existed on the instance. So when it's deleted, attempting to access it immediately raises an `AttributeError`.

3. Latest Python Features (Python 3.11+):
   - **PEP 659 (Specializing Adaptive Interpreter)**: Python 3.11+ massively sped up attribute lookups (`LOAD_ATTR` and `STORE_ATTR` instructions). The interpreter caches the memory offsets of attributes dynamically during execution, making instance and class attribute access nearly as fast as looking up a local variable.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens when you delete an instance variable that has the same name as a class variable?
A1: The instance variable is removed from the object's `__dict__`. Subsequent access to that attribute via the instance will fall back to the class variable, effectively "un-shadowing" it.

Q2: How can you access the class attribute when it has been shadowed by an instance attribute?
A2: You can access it directly through the class name (e.g., `Chai.temperature`) or by explicitly looking at the instance's class via `cutting.__class__.temperature`.

Q3: How do you prevent users from adding random attributes (like `cutting.cup = "small"`) to an instance?
A3: You can define `__slots__ = ['temperature', 'strength']` inside the class. This disables the creation of the dynamic `__dict__` for instances, restricting them to only the explicitly allowed attributes, which saves memory and prevents dynamic shadowing.

Q4: What is the difference between `__getattr__` and `__getattribute__`?
A4: `__getattribute__` is called unconditionally every time ANY attribute is accessed on an object. `__getattr__` is only called as a fallback if the attribute cannot be found through the normal lookup process (i.e., it doesn't exist in the instance namespace or class namespace).
"""