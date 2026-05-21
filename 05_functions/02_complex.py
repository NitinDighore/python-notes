def fetch_sales():
    print("Fetching the sales data") # Output: Fetching the sales data


def filter_valid_sales():
    print("Filtering valid sales data") # Output: Filtering valid sales data

def summarize_data():
    print("Summarizing sales data") # Output: Summarizing sales data


def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_data()
    print("Report is ready") # Output: Report is ready


generate_report()

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Storing functions in a list to execute sequentially (Pipeline)
print("\n1. Executing a pipeline of functions from a list:")
# Functions are objects, so they can be stored in a list without calling them (no parentheses).
pipeline = [fetch_sales, filter_valid_sales, summarize_data]
for step in pipeline:
    step() # Calls each function in the list one by one

# Trick 2: Returning functions (Higher-Order Functions)
print("\n2. Returning a function from a function:")
def get_report_generator():
    # Returns the function object itself, doesn't call it
    return generate_report

runner = get_report_generator()
runner() # Now calling the returned function

# Trick 3: Passing functions as arguments (Callbacks)
print("\n3. Passing functions as arguments:")
def execute_step(func):
    print(f"Executing: {func.__name__}")
    func()

execute_step(fetch_sales) # Passes the function reference

"""
--- NOTES: Function Composition and Managing Complexity ---

1. Abstraction and Orchestration:
   - The filename `02_complex.py` implies dealing with complex tasks. 
   - A great way to manage complexity is to break down a large monolithic task into smaller, highly focused, single-responsibility functions (e.g., `fetch_sales`, `filter_valid_sales`).
   - `generate_report` acts as an "orchestrator" or "coordinator" function. It doesn't do the low-level work itself; instead, it calls the specialized functions in the correct order. This is a core software design pattern.

2. Functions are First-Class Citizens:
   - In Python, functions are "first-class objects". This means they can be assigned to variables, stored in data structures (like lists or dictionaries), passed as arguments to other functions, and returned from other functions (as shown in the Trick Examples).

3. Latest Python Features:
   - **Type Hinting for Callables (Python 3.9+)**: When passing functions as arguments, you can type hint them using `collections.abc.Callable` (preferred over `typing.Callable` in modern Python). For example, `def execute_step(func: Callable[[], None]):` indicates a function that takes no arguments and returns `None`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What does it mean that functions are "first-class citizens" in Python?
A1: It means that functions are treated just like any other object (like integers or strings). You can assign them to variables, pass them as arguments to other functions (callbacks), return them from functions, and store them in data structures.

Q2: Why is it better to have an orchestrator function like `generate_report` instead of putting all the code into one giant function?
A2: It promotes the Single Responsibility Principle (SRP) and abstraction. Smaller functions are easier to read, test, and debug. If you need to change how data is fetched, you only modify `fetch_sales`, without touching the reporting logic or filtering logic.

Q3: How do you pass a function without calling it?
A3: You simply reference the function's name without parentheses (e.g., `my_var = fetch_sales`). Adding parentheses (e.g., `fetch_sales()`) immediately executes the function and evaluates to its return value.

Q4: What is a Higher-Order Function?
A4: A higher-order function is a function that either takes one or more functions as arguments, or returns a function as its result.
"""