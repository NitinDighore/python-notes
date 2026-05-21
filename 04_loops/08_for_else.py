staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff") # Output: Amit is eligible to manage the staff
        break
else:
    print(f"No one is eligible to manage the staff") # Output: (Skipped in this case because of break)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The 'for-else' executing naturally
print("\n1. Naturally exhausting the loop:")
# If the break statement is never reached, the else block will execute.
for name, age in staff:
    if age > 20: # Condition is never met
        print(f"{name} is over 20.")
        break
else:
    print("No staff member is over 20.") # Output: No staff member is over 20.

# Trick 2: 'while-else' construct
print("\n2. The while-else construct:")
# The 'else' block works identically with while loops!
count = 3
while count > 0:
    count -= 1
else:
    print("While loop finished naturally.") # Output: While loop finished naturally.

# Trick 3: Empty iterables and the else block
print("\n3. Empty iterable behavior:")
# If the list is empty, the loop instantly finishes without breaking, so the else block triggers immediately.
empty_list = []
for item in empty_list:
    break
else:
    print("Loop ran on empty list, else executes immediately!") # Output: Loop ran on empty list, else executes immediately!

# Trick 4: Replacing flag variables with for-else
print("\n4. Replacing boolean flags:")
# In other languages, you need a 'found = False' flag to check if a search failed. In Python, you just use 'else'.
search_id = 99
for current_id in [1, 2, 3]:
    if current_id == search_id:
        print("Found!")
        break
else:
    print("Not found, without needing a flag variable.") # Output: Not found, without needing a flag variable.

"""
--- NOTES: The `for...else` Construct ---

1. What is `for...else`?
   - Python has a unique construct where loops (`for` and `while`) can have an `else` block attached to them.
   - The code inside the `else` block executes **ONLY IF** the loop completes its iterations naturally (i.e., it exhausts the iterable).
   - If the loop is terminated prematurely using a `break` statement, the `else` block is completely skipped.
   - A helpful way to mentally read `else` in this context is to read it as `nobreak`.

2. Primary Use Case:
   - It is primarily used for search operations. Instead of setting a boolean flag (e.g., `is_found = False`) before a loop and checking it after the loop, you can simply use the `else` block to handle the "item not found" scenario.

3. Latest Python Features:
   - **Adaptive Specialization (Python 3.11+)**: While the syntactical behavior of `for...else` hasn't changed in recent versions, the underlying execution is much faster. Python 3.11's specializing adaptive interpreter (PEP 659) heavily optimizes type-stable loops. Furthermore, changes to how exceptions are handled ("Zero-cost exceptions") mean that terminating a loop (which implicitly catches `StopIteration`) has practically zero overhead now compared to older Python 3.x versions.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: When exactly does the `else` block attached to a `for` loop execute?
A1: It executes only when the loop terminates naturally. "Naturally" means the iterable was completely exhausted without the loop ever encountering a `break` statement.

Q2: What happens if you use `continue` inside a `for...else` loop? Will the `else` block still execute?
A2: Yes, it will still execute. The `continue` statement only skips the current iteration and moves to the next one. It does not terminate the loop entirely. As long as `break` is not executed, the loop finishes naturally and the `else` block runs.

Q3: What happens if the list you are iterating over is entirely empty?
A3: If the iterable is empty, the loop body never executes. Because a `break` statement was never encountered, the `else` block will execute immediately.

Q4: Is it considered good practice to use `for...else`?
A4: Yes, it is considered highly "Pythonic", especially for search loops, because it removes the need for tracking state with boolean flag variables. However, because it's a unique feature to Python, it can sometimes confuse developers coming from languages like Java or C++, so adding a brief comment is often helpful.
"""