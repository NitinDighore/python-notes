def serve_chai():
    chai_type = "Masala" # local scope
    print(f"Inside function {chai_type}") # Output: Inside function Masala


chai_type = "Lemon"
serve_chai()
print(f"Outside function: {chai_type}") # Output: Outside function: Lemon


def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "Ginger" # Creates a NEW local variable, doesn't modify the enclosing one
        print("Inner:", chai_order) # Output: Inner: Ginger
    print_order()
    print("Outer: ", chai_order) # Output: Outer:  lemon

chai_order = "Tulsi" # Global
chai_counter()
print("Global :", chai_order) # Output: Global : Tulsi

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The 'global' keyword
print("\n1. Modifying Global Scope:")
coffee_type = "Black"
def change_coffee():
    global coffee_type # Tells Python to use the globally defined coffee_type
    coffee_type = "Espresso"
change_coffee()
print(f"Global coffee is now: {coffee_type}") # Output: Global coffee is now: Espresso

# Trick 2: The 'nonlocal' keyword
print("\n2. Modifying Enclosing Scope (nonlocal):")
def outer_counter():
    count = 0
    def inner_counter():
        nonlocal count # Tells Python to use the 'count' from outer_counter
        count += 1
        return count
    return inner_counter # Returns the function itself (Closure)

my_counter = outer_counter()
print(f"Count: {my_counter()} then {my_counter()}") # Output: Count: 1 then 2

# Trick 3: Closures (Remembering Scope)
print("\n3. Closures:")
def multiplier(x):
    # The inner lambda function "remembers" the value of x from the enclosing scope
    return lambda y: x * y
double = multiplier(2)
print(f"Double of 5: {double(5)}") # Output: Double of 5: 10

# Trick 4: The UnboundLocalError Trap
print("\n4. The UnboundLocalError trap:")
trap_var = 10
def trap_func():
    # print(trap_var) # Uncommenting this raises UnboundLocalError!
    # Why? Because trap_var is assigned BELOW, Python considers it a LOCAL variable for the whole block.
    # It refuses to fall back to the global scope if it sees an assignment anywhere in the local scope.
    trap_var = 20 
    print(f"Trap var: {trap_var}") # Output: Trap var: 20
trap_func()

"""
--- NOTES: Variable Scopes and the LEGB Rule ---

1. The LEGB Rule:
   - Python resolves variable names using the LEGB rule, checking scopes in this exact order:
     1. **L**ocal: Names assigned in any way within a function (`def` or `lambda`), and not declared global in that function.
     2. **E**nclosing: Names in the local scope of any and all enclosing functions (`def` or `lambda`), from inner to outer.
     3. **G**lobal: Names assigned at the top-level of a module file, or declared global in a `def` within the file.
     4. **B**uilt-in: Names preassigned in the built-in names module (e.g., `print`, `len`, `Exception`).

2. Latest Python Features (Scope changes in Python 3.12):
   - **Comprehension Inlining (PEP 709)**: In Python 3.11 and older, list/dict/set comprehensions created a completely separate execution frame (like a hidden function) which had performance overhead. In Python 3.12, comprehensions are inlined into the local scope. This speeds them up by ~11%, though it introduces minor internal changes to how locals are managed.
   - **Type Parameter Scopes (PEP 695)**: Python 3.12 introduced a new, strict scope specifically for Type Parameters (e.g., `def funcT:`). The type variable `T` lives in its own isolated scope so it doesn't leak into or clash with local variables.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the LEGB rule in Python?
A1: It is the acronym for the order in which Python resolves variable names: Local, Enclosing, Global, and Built-in.

Q2: What is the difference between the `global` and `nonlocal` keywords?
A2: `global` is used to declare that a variable inside a function refers to the module's top-level global scope. `nonlocal` is used in nested functions to declare that a variable refers to a previously bound variable in the nearest enclosing function's scope (but NOT the global scope).

Q3: What is a Closure in Python?
A3: A closure is a nested function that captures and "remembers" the bindings of variables in its enclosing scope, even after the outer function has finished executing and returned. This is demonstrated in Trick 2 and 3 above.

Q4: Why does accessing a global variable before defining a local variable of the same name cause an `UnboundLocalError`?
A4: Because Python's scope resolution happens at compile-time (before execution). If Python sees an assignment to a variable anywhere inside a function body, it treats that variable as local for the *entire* function. If you try to print it before the assignment line, Python realizes the local variable hasn't been bound to a value yet and throws an error, rather than falling back to the global variable.
"""