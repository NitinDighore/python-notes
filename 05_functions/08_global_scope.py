chai_type = "Plain"

def front_desk():
    def kitchen():
        global chai_type
        chai_type = "Irnai"
    kitchen()


front_desk()
print("Final global chai: ", chai_type) # Output: Final global chai:  Irnai

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Reading vs. Modifying Global Variables
print("\n1. Reading vs Modifying:")
global_counter = 10
def read_only():
    # You DO NOT need the 'global' keyword if you are strictly *reading* the variable!
    print(f"Reading global counter: {global_counter}") # Output: Reading global counter: 10
read_only() 

# Trick 2: Shadowing a Global Variable (Forgetting the global keyword)
print("\n2. Shadowing (Local override):")
message = "Hello Global"
def shadow_variable():
    message = "Hello Local" # This creates a brand new local variable, it does NOT touch the global one
    print(f"Inside function: {message}") # Output: Inside function: Hello Local
shadow_variable()
print(f"Outside function: {message}") # Output: Outside function: Hello Global

# Trick 3: Using 'global' to create a variable dynamically
print("\n3. Creating globals from inside a function:")
def inject_global():
    global new_secret_var # This variable doesn't exist anywhere yet!
    new_secret_var = "I was born inside a function!"
inject_global()
print(f"Injected global: {new_secret_var}") # Output: Injected global: I was born inside a function!

# Trick 4: Modifying globals using the built-in globals() dictionary
print("\n4. The globals() dictionary hack:")
def manipulate_globals_dict():
    # globals() returns a dictionary representing the current global symbol table
    globals()["dynamic_chai"] = "Matcha"
manipulate_globals_dict()
print(f"Dynamically created via globals(): {dynamic_chai}") # Output: Dynamically created via globals(): Matcha

"""
--- NOTES: Global Scope and the `global` Keyword ---

1. The `global` Keyword:
   - By default, if you assign a value to a variable inside a function, Python assumes it is a local variable.
   - The `global` keyword explicitly tells Python: "Do not create a local variable. Instead, bind this name to the variable in the top-level module (global) scope."
   - As shown in Trick 3, you can even use `global` to declare a variable that hasn't been created yet, injecting it into the global namespace.

2. Why Globals are generally frowned upon (Best Practices):
   - **Hidden State / Side Effects**: Functions that modify global variables are no longer "pure". Their behavior depends on the state of the system, making them incredibly hard to test and debug in large applications.
   - **Concurrency Issues**: In multi-threaded environments, global variables can lead to race conditions if multiple threads try to modify them simultaneously.
   - **Alternative**: It is almost always better to pass data into a function via arguments and return the modified data, maintaining a functional programming approach.

3. Latest Python Features (Performance Optimizations):
   - **Faster Global Lookups (Python 3.11+)**: Historically, accessing a global variable was notably slower than accessing a local one because Python had to look up the global dictionary on every access. With the introduction of the Specializing Adaptive Interpreter (PEP 659) in Python 3.11, the `LOAD_GLOBAL` bytecode instruction now specializes dynamically. It caches the dictionary keys if they remain stable, making global variable lookups almost as fast as local ones.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Do you need to use the `global` keyword if you just want to print or read a global variable inside a function?
A1: No. Python's LEGB scope resolution rule will automatically look for the variable in the global scope if it isn't found locally. You only need the `global` keyword if you intend to *reassign* or *modify* the variable.

Q2: What happens if you try to print a global variable inside a function, and then assign a new value to it on the next line without using the `global` keyword?
A2: This will raise an `UnboundLocalError`. Because Python sees an assignment further down in the function body, it assumes the variable is local for the *entire* function block. When it tries to execute the `print()` statement, it realizes the local variable hasn't been bound yet and throws an error.

Q3: Can the `global` keyword be used to modify a variable in an enclosing (parent) function?
A3: No. The `global` keyword specifically targets the top-level module namespace. To modify a variable in an enclosing function, you must use the `nonlocal` keyword instead.

Q4: What does the `globals()` function do?
A4: `globals()` is a built-in Python function that returns a dictionary representing the current global symbol table. You can use it to read global variables or even modify/create them dynamically by adding keys to the dictionary.
"""