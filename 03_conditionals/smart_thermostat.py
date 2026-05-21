device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!") # Output: High temperature alert!
    else:
        print("Temperature is normal") # Output: Temperature is normal (if temp <= 35)
else:
    print("Device is offline") # Output: Device is offline (if status != 'active')

"""
--- NOTES: Nested `if` Statements and Logical Grouping ---

1. What are Nested `if` Statements?
   - A nested `if` statement is simply an `if` statement placed inside another `if`, `elif`, or `else` block.
   - They are useful when you need to check for a condition only after a previous condition has already been evaluated as `True` (hierarchical checking).
   - In this code, it makes sense to only evaluate the temperature if the device is currently online/active.

2. Flattening Nested Conditions (Logical Grouping):
   - While nesting is powerful, excessive nesting makes code difficult to read (sometimes referred to as the "Arrow Anti-Pattern").
   - The Zen of Python states: "Flat is better than nested."
   - Often, you can combine conditions using logical operators (`and`). 
     Example: `if device_status == "active" and temperature > 35:`
   - Note: In this specific script, nesting is appropriate because we want to provide granular feedback for each individual failure state (e.g., printing "Device is offline" vs "Temperature is normal").

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is a nested `if` statement?
A1: It's an `if` statement that exists inside the block of another `if`, `elif`, or `else` statement. It allows for multi-level, dependent decision making.

Q2: How does Python know which `if` statement an `else` block belongs to in a nested structure?
A2: Python relies entirely on indentation. An `else` statement is paired with the nearest preceding `if` statement that exists at the exact same indentation level.

Q3: How can you avoid deeply nested `if` statements to improve code readability?
A3: You can use logical operators (`and`, `or`) to combine conditions. When working inside functions, you can also use "guard clauses" (early returns) to exit the function immediately if a preliminary condition fails, preventing the rest of the code from needing to be nested.
"""