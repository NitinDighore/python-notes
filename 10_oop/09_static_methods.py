class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
    

raw = " water , milk , ginger , honey "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned) # Output: ['water', 'milk', 'ginger', 'honey']

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Calling a static method via an instance
print("\n1. Calling via an instance:")
utils_obj = ChaiUtils()
# You can call a static method from an object instance, not just the Class name!
print(f"From instance: {utils_obj.clean_ingredients('a , b ')}") # Output: From instance: ['a', 'b']

# Trick 2: Bypassing the class completely (Unbound assignment)
print("\n2. Assigning static method to a variable:")
# Because it takes no implicit 'self' or 'cls', it can be passed around just like a regular function.
cleaner_func = ChaiUtils.clean_ingredients
print(f"Direct call: {cleaner_func(' x , y ')}") # Output: Direct call: ['x', 'y']

# Trick 3: Static methods in Inheritance
print("\n3. Inheritance with static methods:")
class AdvancedChaiUtils(ChaiUtils):
    pass
# Child classes inherit static methods seamlessly
print(f"Inherited call: {AdvancedChaiUtils.clean_ingredients(' chai , latte ')}") # Output: Inherited call: ['chai', 'latte']

# Trick 4: The alternative to Static Methods
print("\n4. Namespace Grouping:")
# We could have just defined `def clean_ingredients(text):` globally outside any class.
# The @staticmethod decorator is purely for organizational purposes, keeping utility functions safely isolated inside the `ChaiUtils` namespace.

"""
--- NOTES: Static Methods (`@staticmethod`) ---

1. What is a Static Method?
   - A static method is a method defined inside a class that does NOT receive an implicit first argument (neither `self` for the instance, nor `cls` for the class).
   - It behaves exactly like a standard, standalone Python function, but it is housed inside the class's namespace.

2. When to use `@staticmethod`:
   - Use it when a function performs a task that is logically related to the class, but does not need to access or modify any class state or instance state.
   - It is an excellent tool for organization, grouping, and encapsulation (like formatting data, mathematical calculations, or input validation).

3. Latest Python Features:
   - **Callable Static Methods (Python 3.10+)**: Prior to Python 3.10, if you tried to extract and call a static method directly from the raw class dictionary (e.g., `ChaiUtils.__dict__'clean_ingredients'`), it would raise an error because it was an uncallable descriptor object. Python 3.10 updated the `staticmethod` object to make it directly callable, simplifying metaprogramming and decorator combinations.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the main difference between `@staticmethod` and `@classmethod`?
A1: A `@classmethod` automatically receives the class itself as its first implicit argument (usually named `cls`), allowing it to access and modify class-level state or act as an alternative constructor. A `@staticmethod` receives no implicit first argument, acting purely as a regular function that happens to reside in the class's namespace.

Q2: Can a static method access an instance variable (like `self.flavor`)?
A2: No. Because a static method does not receive the `self` parameter, it has absolutely no knowledge of any specific object instances or their attributes.

Q3: Why use `@staticmethod` instead of simply defining a regular function outside the class at the module level?
A3: It's purely about code organization and namespace management. If a utility function is only ever used in the context of `ChaiUtils`, putting it inside the class as a static method keeps the global module namespace uncluttered and clearly signals to other developers that the function belongs conceptually to that class.

Q4: Can you override a static method in a child class?
A4: Yes! Just like any other method, you can define a method with the same name in a subclass. Python's MRO (Method Resolution Order) will cleanly resolve the call to the child's overridden static method instead of the parent's.
"""