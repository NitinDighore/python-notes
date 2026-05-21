# chai = "Ginger chai"

# def prepare_chai(order):
#     print("Preparing ", order)


# prepare_chai(chai)
# print(chai)


chai = [1, 2, 3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai) # Output: [1, 42, 3]


def make_chai(tea, milk, sugar):
    print(tea, milk, sugar) 

make_chai("Darjeeling", "Yes", "Low") #positional -> Output: Darjeeling Yes Low
make_chai(tea="Green", sugar="Medium", milk="No") #keywords -> Output: Green No Medium


def special_chai(*ingredients, **extras):
    print("Ingredients", ingredients) 
    print("Extras", extras) 

special_chai("Cinnamon", "Cardmom", sweetener="Honey", foam="yes") 
# Output: 
# Ingredients ('Cinnamon', 'Cardmom')
# Extras {'sweetener': 'Honey', 'foam': 'yes'}

# def chai_order(order=[]):
#     order.append("Masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order) # Output: []

chai_order() # Output: []
chai_order() # Output: []

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The Mutable Default Trap (Demonstrated)
print("\n1. The Mutable Default Trap:")
# Showing why the commented-out chai_order() function above was dangerous
def dangerous_append(item, lst=[]):
    lst.append(item)
    return lst
print(f"Call 1: {dangerous_append(1)}") # Output: [1]
print(f"Call 2: {dangerous_append(2)}") # Output: [1, 2] (The list state persisted!)

# Trick 2: Positional-Only Arguments (Python 3.8+)
print("\n2. Positional-Only Arguments (/):")
# The '/' character forces all parameters before it to be strictly positional (no keywords allowed)
def fast_add(x, y, /):
    return x + y
print(f"Positional only add: {fast_add(10, 20)}") # Output: 30
# fast_add(x=10, y=20) # Uncommenting this would raise a TypeError!

# Trick 3: Unpacking Iterables and Dicts into Functions
print("\n3. Unpacking into Functions:")
def profile(name, age, city):
    print(f"{name} is {age} and lives in {city}")

data_list = ["Alice", 28, "Paris"]
data_dict = {"name": "Bob", "city": "Tokyo", "age": 35}

# Unpack a list as positional args, and a dict as keyword args
profile(*data_list) # Output: Alice is 28 and lives in Paris
profile(**data_dict) # Output: Bob is 35 and lives in Tokyo

# Trick 4: Combined Function Signature Order
print("\n4. The Ultimate Signature Order:")
# The mandatory order is: Positional/Standard -> *args -> Keyword-Only -> **kwargs
def ultimate_func(a, b=2, *args, c=3, **kwargs):
    print(f"a:{a}, b:{b}, args:{args}, c:{c}, kwargs:{kwargs}")

ultimate_func(1, 10, 100, 200, c=50, d=99)
# Output: a:1, b:10, args:(100, 200), c:50, kwargs:{'d': 99}

"""
--- NOTES: Input Parameters and Arguments ---

1. Parameter vs. Argument Types:
   - **Positional**: Bound based on the order they are passed (e.g., `make_chai("A", "B", "C")`).
   - **Keyword**: Bound based on the explicit parameter name, allowing you to pass them in any order (e.g., `make_chai(sugar="C", tea="A", milk="B")`).
   - **`*args`**: Collects arbitrary extra positional arguments into a Tuple.
   - **`**kwargs`**: Collects arbitrary extra keyword arguments into a Dictionary.

2. Call by Object Reference:
   - When you pass a mutable object (like the list `chai`) to `edit_chai(cup)`, the `cup` parameter points to the exact same list in memory. Altering `cup` alters the original `chai` list.

3. Latest Python Features:
   - **Positional-Only Arguments `/` (Python 3.8+)**: Allows developers to explicitly block keyword argument passing for certain parameters, which is useful for highly optimized C-like functions (like `len()` or `sum()`).
   - **Unpacking TypedDict (Python 3.12 - PEP 692)**: You can now provide strict type hints for `**kwargs` using `Unpack[MyTypedDict]`, giving you full autocompletion and type checking for dynamic keyword arguments.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Explain the "Mutable Default Argument" trap in Python.
A1: If you define a default argument as a mutable object (like a list `def func(lst=[])`), Python evaluates that list only ONCE when the function is defined, not every time it's called. This means all subsequent calls to the function share the exact same list. To avoid this, default arguments should be immutable (like `None`), and the mutable object should be instantiated inside the function body (`if lst is None: lst = []`).

Q2: What is the difference between `*args` and `**kwargs`?
A2: `*args` captures an arbitrary number of unnamed (positional) arguments passed to a function and stores them as a Tuple. `**kwargs` captures an arbitrary number of named (keyword) arguments and stores them as a Dictionary. (Note: the words 'args' and 'kwargs' are just conventions, the asterisks `*` and `**` are the operators doing the work).

Q3: In what exact order must you define parameters in a complex Python function signature?
A3: The strict order is:
    1. Standard Positional Arguments (or Positional-Only with `/`)
    2. Default Arguments
    3. `*args`
    4. Keyword-Only Arguments
    5. `**kwargs`

Q4: How do you force an argument to be keyword-only?
A4: You place it *after* `*args` or after a bare asterisk `*` in the function signature. For example: `def my_func(a, *, b):`. Here, `b` MUST be passed as a keyword argument (e.g., `my_func(1, b=2)`).
"""