
chai_type = "ginger"
def update_order():
    chai_type = "Elaichi"
    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar"
    kitchen()
    print("After kitchen update", chai_type) # Output: After kitchen update Kesar

update_order()

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: State accumulation in Closures using nonlocal
print("\n1. State Accumulator:")
# This is the most common use case for nonlocal. It allows a nested function to "remember" and modify state.
def make_accumulator():
    total = 0
    def add(amount):
        nonlocal total
        total += amount
        return total
    return add

acc = make_accumulator()
print(f"Added 10: {acc(10)}, Added 20: {acc(20)}") # Output: Added 10: 10, Added 20: 30

# Trick 2: nonlocal vs global side-by-side
print("\n2. nonlocal vs global:")
x = "Global"
def outer():
    x = "Enclosing"
    def inner_nonlocal():
        nonlocal x
        x = "Modified by nonlocal"
    def inner_global():
        global x
        x = "Modified by global"
    
    inner_nonlocal()
    print(f"Outer x after nonlocal: {x}") # Output: Outer x after nonlocal: Modified by nonlocal
    inner_global()
    print(f"Outer x after global: {x}") # Output: Outer x after global: Modified by nonlocal (Outer x is unchanged by global!)
outer()
print(f"Global x: {x}") # Output: Global x: Modified by global

# Trick 3: Multiple Nested Layers
print("\n3. Multiple Nested Layers:")
def level_1():
    var = "Level 1"
    def level_2():
        var = "Level 2" # This is the target
        def level_3():
            nonlocal var # Binds to the NEAREST enclosing scope (level_2), not level_1
            var = "Changed by Level 3"
        level_3()
        print(f"Level 2 var: {var}") # Output: Level 2 var: Changed by Level 3
    level_2()
    print(f"Level 1 var: {var}") # Output: Level 1 var: Level 1
level_1()

"""
--- NOTES: The `nonlocal` Keyword and Closures ---

1. What does `nonlocal` do?
   - The `nonlocal` keyword is used inside nested functions to declare that a variable refers to a previously bound variable in the nearest enclosing scope.
   - It allows you to *modify* a variable defined in an outer function from within an inner function. Without `nonlocal`, attempting to assign a value to `chai_type` would simply create a brand-new local variable in the inner function, leaving the outer one unchanged.

2. Constraints of `nonlocal`:
   - It ONLY searches enclosing function scopes. 
   - It will NEVER search the global (module) scope. 
   - The variable must already exist in the enclosing scope before you declare it `nonlocal`.

3. Latest Python Features:
   - **Python 3.12 Comprehension Inlining (PEP 709)**: In older Python versions, comprehensions created a hidden function scope, which sometimes led to confusing scoping behavior. With PEP 709, comprehensions are inlined. While you generally don't use `nonlocal` directly inside a comprehension itself, using `nonlocal` in a function that *contains* comprehensions is now slightly faster and more predictable due to the removal of the hidden frame overhead.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if you use `nonlocal` on a variable that doesn't exist in any enclosing function?
A1: Python will immediately raise a `SyntaxError: no binding for nonlocal 'variable_name' found`. The variable MUST already exist in an enclosing function's scope.

Q2: Can `nonlocal` be used to modify a global variable?
A2: No. If the variable is only defined at the global (top) level, using `nonlocal` will throw a `SyntaxError`. You must use the `global` keyword to modify top-level variables.

Q3: Why is `nonlocal` heavily used in decorators?
A3: Decorators often wrap a function and need to maintain some form of internal state (like caching a result, or counting how many times the function was called). `nonlocal` allows the inner wrapper function to update variables defined in the outer decorator function between successive calls, completely avoiding the use of messy global variables.
"""