users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F10"},
    {"id": 3, "total": 80, "coupon": "P50"},
]

discounts = {
    "P20": (0.2, 0),
    "F10": (0.5, 0),
    "P50": (0, 10),
}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(f"{user["id"]} paid {user["total"]} and got discount for next visit of rupees {discount}")
    # Output: 
    # 1 paid 100 and got discount for next visit of rupees 20.0
    # 2 paid 150 and got discount for next visit of rupees 75.0
    # 3 paid 80 and got discount for next visit of rupees 10

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Dictionary Comprehension from a List of Dicts
print("\n1. Dictionary Comprehension to map User IDs to Totals:")
# Quickly transform a list of dictionaries into a single lookup dictionary mapping ID to Total
id_to_total = {u["id"]: u["total"] for u in users}
print(f"ID to Total Map: {id_to_total}") # Output: {1: 100, 2: 150, 3: 80}

# Trick 2: Grouping items using setdefault()
print("\n2. Grouping with setdefault():")
# A clean way to group items without writing an explicit if/else to check if the key already exists
grouped = {}
for u in users:
    category = "High Spend" if u["total"] > 90 else "Low Spend"
    grouped.setdefault(category, []).append(u["id"])
print(f"Grouped Users: {grouped}") # Output: {'High Spend': [1, 2], 'Low Spend': [3]}

# Trick 3: Using itemgetter to unpack multiple dictionary values
print("\n3. Fast multi-key extraction using itemgetter:")
from operator import itemgetter
# Extremely fast C-level unpacking of specific keys from dictionaries
extract_info = itemgetter("id", "coupon")
for u in users:
    uid, cp = extract_info(u)
    print(f"User {uid} used coupon {cp}") # Output: User 1 used coupon P20 ...

# Trick 4: The Walrus Operator in Dictionary Lookups
print("\n4. Using the walrus operator for dict lookups:")
bonus_points = {"P20": 50, "P50": 100}
for u in users:
    # Evaluate and assign in one step, ensuring we only print if a bonus actually exists
    if (bonus := bonus_points.get(u["coupon"])) is not None:
        print(f"User {u['id']} got {bonus} bonus points!") # Output: User 1 got 50 bonus points! ...

# Trick 5: Dictionary merging (Python 3.9+) inside a loop
print("\n5. Python 3.9+ Dictionary Merge (|):")
# Update dictionary records cleanly using the merge operator, which leaves the original unchanged
updated_users = [u | {"status": "processed"} for u in users]
print(f"First updated user: {updated_users[0]}") # Output: {'id': 1, 'total': 100, 'coupon': 'P20', 'status': 'processed'}

"""
--- NOTES: Dictionary Retrieval inside Loops ---

1. Safe Lookups (`dict.get`):
   - When iterating over data and doing dictionary lookups, it is common to encounter missing keys.
   - Instead of wrapping `dict[key]` in a `try-except` block, using `dict.get(key, default_value)` is much safer and more concise.
   - In this code, `discounts.get(..., (0, 0))` guarantees a fallback tuple is returned even if a user inputs an invalid coupon.

2. Latest Python Features:
   - **F-String Quote Reuse (Python 3.12+)**: Notice the print statement uses `user["id"]` directly inside an f-string wrapped in double quotes: `f"{user["id"]}"`. Prior to Python 3.12, this would raise a `SyntaxError` (you had to alternate quotes, like `f"{user['id']}"`). Python 3.12 relaxed this rule, making f-strings much easier to write!
   - **Dictionary Merge Operators (Python 3.9+)**: The union operators `|` and `|=` make it effortless to combine dictionaries or update keys inline.
   - **Structural Pattern Matching (Python 3.10+)**: You can now match dictionary structures directly. `case {"id": uid, "total": t}:` easily extracts items based on the dictionary's shape.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if you try to modify the size of a dictionary while iterating over its keys (`for key in my_dict:`)?
A1: Python will raise a `RuntimeError: dictionary changed size during iteration`. If you need to add or remove keys dynamically, you should iterate over a static list copy of the keys (`for key in list(my_dict):`).

Q2: Why use `discounts.get(user["coupon"], (0, 0))` instead of `discounts[user["coupon"]]`?
A2: If `user["coupon"]` is missing from the `discounts` dictionary, bracket access `[]` will throw a `KeyError` and crash the program. The `.get()` method safely handles missing keys by returning the fallback default value.

Q3: What is the time complexity of searching for a key in a dictionary inside a loop?
A3: The average time complexity for dictionary key lookups is O(1). This is incredibly efficient compared to searching lists (O(n)), because dictionaries are implemented as hash tables.

Q4: Explain how `dict.setdefault(key, default)` works compared to `dict.get(key, default)`.
A4: `get()` only *returns* the default value if the key is missing; it does not modify the dictionary. `setdefault()` returns the value if the key exists, but if it doesn't, it actually *inserts* the key with the default value into the dictionary and then returns it.
"""