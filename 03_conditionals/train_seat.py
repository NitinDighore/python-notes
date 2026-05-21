seat_type = input("Enter seat type (sleeper/AC/general/luxury)").lower()


match seat_type:
    case "sleeper":
        print("Sleeper - No AC, beds available") # Output: Sleeper - No AC, beds available (if input is 'sleeper')
    case "ac":
        print("AC - Air conditioned, comfy ride") # Output: AC - Air conditioned, comfy ride (if input is 'ac')
    case "general":
        print("General - Cheapest option, no reservation") # Output: General - Cheapest option, no reservation (if input is 'general')
    case "luxury":
        print("Luxury - Premium seats with meals") # Output: Luxury - Premium seats with meals (if input is 'luxury')
    case _:
        print("Invalid seat type") # Output: Invalid seat type (for any other input)

"""
--- NOTES: Structural Pattern Matching (match-case) ---

1. What is Structural Pattern Matching?
   - Introduced in Python 3.10, the `match-case` statement is Python's version of a "switch-case" statement found in other languages (like C, Java, or JavaScript), but it is significantly more powerful.
   - It takes a variable or expression (after the `match` keyword) and compares its structure and value against several patterns (the `case` statements).

2. The Wildcard Case (`_`):
   - The `case _:` acts as the default or fallback pattern. 
   - It will match everything. If none of the patterns above it match, this block executes. It is the equivalent of the `else` block in an `if-elif-else` chain.

3. Beyond Simple Values (Advanced Features):
   - While used here for simple string matching, `match-case` can unpack sequences, match dictionary structures, and evaluate data types.
   - Example of sequence unpacking: `case ["ac", num_seats]:`
   - Example of guards: You can add an `if` condition to a pattern, like `case "ac" if budget > 1000:`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Which version of Python introduced the `match-case` syntax?
A1: It was introduced in Python 3.10.

Q2: What happens if none of the cases match and you forgot to include a `case _:` block?
A2: If no pattern matches and there is no default `case _:`, the `match` block simply finishes silently without throwing an error (exactly like an `if-elif` chain without an `else` at the end).

Q3: Is `match-case` just a syntactic sugar for `if-elif-else`?
A3: For simple value comparisons (like the code above), yes, it operates similarly to `if-elif`. However, its true power lies in "Structural Pattern Matching" – the ability to automatically unpack sequences and dictionaries, match object types, and capture variables, which is much more cumbersome to do with `if-elif` chains.

Q4: Do you need to include a `break` statement at the end of each `case` in Python?
A4: No. Unlike languages like C or JavaScript, Python's `match-case` does NOT suffer from "fall-through". Once a matched case's block finishes executing, Python exits the entire `match` statement.
"""