# def make_chai():
#     # return "Here is your masal chai"
#     print("Here is your masala chai")

# return_value = make_chai()

# print(return_value)

def idle_chaiwala():
    pass

print(idle_chaiwala()) # Output: None

def sold_cups():
    return 120

total = sold_cups()
print(total) # Output: 120

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai over"
    return "Chai is ready"
    print("chai") # This is "dead code" and will never execute because of the return above it

print(chai_status(0)) # Output: Sorry, chai over
print(chai_status(5)) # Output: Chai is ready


def chai_report():
    return 100, 20, 10 # sold, remaining

sold, remaining, not_paid = chai_report()
print("Sold: ", sold) # Output: Sold:  100
print("Remaining: ", remaining) # Output: Remaining:  20

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Ignoring specific returned values
print("\n1. Ignoring specific return values with '_':")
def get_user_info():
    return "Alice", "alice@email.com", "127.0.0.1", "Admin"
# We only care about name and role, so we use '_' for the rest
name, _, _, role = get_user_info()
print(f"Name: {name}, Role: {role}") # Output: Name: Alice, Role: Admin

# Trick 2: Returning Multiple Values using '*' (Unpacking)
print("\n2. Star unpacking for multiple returns:")
first, *rest = get_user_info()
print(f"First: {first}, Rest: {rest}") # Output: First: Alice, Rest: ['alice@email.com', '127.0.0.1', 'Admin']

# Trick 3: Conditional Returns (Ternary Return)
print("\n3. Conditional Returns:")
def is_even(n):
    return True if n % 2 == 0 else False
print(f"Is 4 even? {is_even(4)}") # Output: Is 4 even? True

# Trick 4: Early Returns (Guard Clauses)
print("\n4. Guard Clauses (Early Returns):")
# Instead of deeply nested if-else statements, return early to keep code flat
def process_refund(status):
    if status != "eligible":
        return "Refund Denied" # Exits immediately
    # Process refund logic here...
    return "Refund Approved"
print(process_refund("pending")) # Output: Refund Denied

# Trick 5: Returning a Function (Closures)
print("\n5. Returning Functions:")
def greeting_maker(greeting):
    def greeter(user_name):
        return f"{greeting}, {user_name}!"
    return greeter # Notice there are no parentheses, we return the function itself
say_hello = greeting_maker("Hello")
print(say_hello("World")) # Output: Hello, World!

"""
--- NOTES: Function Returns ---

1. The `return` Keyword:
   - The `return` statement is used to exit a function and pass a calculated value back to the caller.
   - A function immediately terminates when it hits a `return` statement. Any code written beneath it inside the same block is called "dead code" (or unreachable code) and will never execute.
   - If a function has no explicit `return` statement, Python implicitly returns `None`.

2. Returning Multiple Values:
   - Python is unique because it makes returning multiple values look effortless (e.g., `return 1, 2, 3`).
   - Under the hood, Python is actually packing these values into a single Tuple `(1, 2, 3)` and returning that tuple. The caller can then unpack the tuple into multiple variables.

3. Latest Python Features (Type Hinting for Returns):
   - **Python 3.9+**: You can directly use standard collections for type hinting return values (e.g., `def func() -> tuple[int, str]:`).
   - **Python 3.10+**: `TypeAlias` and `|` pipe syntax makes hint declarations for multiple/dynamic returns incredibly readable: `def process() -> int | None:`.
   - **Python 3.11+**: `typing.Unpack` allows you to strictly define the types of a dynamic sequence of return values if returning `*args`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What does a Python function return if it doesn't have a `return` statement, like `idle_chaiwala()`?
A1: It implicitly returns `None`.

Q2: How does Python support returning multiple values? Does it actually return multiple objects?
A2: Technically, it only returns a *single* object. When you write `return a, b`, Python packs `a` and `b` into a single Tuple `(a, b)` and returns that Tuple. The syntax just makes it look like multiple distinct values.

Q3: In the `chai_status` function, why does `print("chai")` never execute?
A3: Because the function hits the `return "Chai is ready"` statement first. A `return` immediately halts the function's execution and exits. The code below it is considered "unreachable" or "dead code".

Q4: How do you handle a function that returns 5 values, but you only need the first and last one?
A4: You can use the underscore `_` as a throwaway variable to catch the unwanted values: `first, _, _, _, last = my_func()`. Alternatively, you can use the star unpacking operator: `first, *_, last = my_func()`.
"""