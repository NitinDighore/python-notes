menu = ["Green", "Lemon", "Spiced", "Mint"]

for idx, item in enumerate(menu, start=1):
    print(f"{idx} : {item} chai") # Output: 1 : Green chai, then 2 : Lemon chai, then 3 : Spiced chai, then 4 : Mint chai

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Creating a dictionary from a list using enumerate
print("\n1. List to Dictionary using enumerate:")
# By casting enumerate directly to a dict, you instantly map index numbers to list items
menu_dict = dict(enumerate(menu, start=100))
print(f"Menu Dict: {menu_dict}") # Output: {100: 'Green', 101: 'Lemon', 102: 'Spiced', 103: 'Mint'}

# Trick 2: Modifying a list in-place using enumerate
print("\n2. In-place modification of list:")
# enumerate gives you the exact index needed to overwrite elements in the original list
for idx, item in enumerate(menu):
    menu[idx] = item.upper()
print(f"Uppercase Menu: {menu}") # Output: ['GREEN', 'LEMON', 'SPICED', 'MINT']

# Trick 3: Iterating backwards while keeping forward indexing
print("\n3. Iterating backwards with enumerate:")
# Notice that enumerate's counter still counts 0, 1, 2... but the items are pulled backwards
for idx, item in enumerate(reversed(menu)):
    print(f"Index {idx}: {item}") # Output: Index 0: MINT, Index 1: SPICED, etc.

# Trick 4: Skipping elements based on their index
print("\n4. Skipping elements based on index:")
# enumerate is perfect when you need to act only on even or odd positions in a sequence
for idx, item in enumerate(menu):
    if idx % 2 == 0: # Targets indices 0, 2
        print(f"Even index {idx}: {item}") # Output: Even index 0: GREEN, Even index 2: SPICED

# Trick 5: Unpacking complex nested iterables with enumerate
print("\n5. Unpacking nested items:")
# You can unpack the index AND the inner tuple in one clean line
nested_menu = [("Green", 50), ("Lemon", 60)]
for idx, (name, price) in enumerate(nested_menu, start=1):
    print(f"#{idx} - {name} costs {price}") # Output: #1 - Green costs 50, #2 - Lemon costs 60

"""
--- NOTES: The `enumerate()` Function ---

1. What is `enumerate()`?
   - `enumerate(iterable, start=0)` is a built-in Python function that adds a counter to an iterable and returns it as an enumerate object.
   - It yields pairs containing a count (starting from `start`) and a value yielded by the iterable.
   - It is the highly recommended, "Pythonic" alternative to using `for i in range(len(collection)):`.

2. Latest Python Features:
   - **Performance Boosts (Python 3.11+)**: Python's specializing adaptive interpreter makes looping with `enumerate()` and unpacking tuples significantly faster under the hood by dynamically optimizing the C-level bytecode during execution.
   - **Strict `zip()` (Python 3.10+)**: Developers sometimes use `enumerate` when they actually want to iterate over two lists simultaneously based on index. Python 3.10 added `zip(list1, list2, strict=True)` to throw a `ValueError` if the lists are of unequal lengths, providing a safer, native alternative to manual index-based iteration.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What does the `enumerate()` function actually return?
A1: It returns an `enumerate` object, which is an iterator. It does NOT return a list of tuples unless you explicitly cast it using `list(enumerate(iterable))`. Being an iterator makes it memory efficient, yielding one tuple at a time instead of storing them all in memory.

Q2: Can `enumerate()` be used with sets and dictionaries?
A2: Yes! It works with any iterable. However, since sets are unordered, the indices assigned will be arbitrary. For dictionaries, iterating normally yields its keys, so `enumerate(my_dict)` will yield `(index, key)` pairs.

Q3: Is it better to use `range(len(list))` or `enumerate(list)`? Why?
A3: `enumerate` is heavily preferred in Python. `range(len(list))` forces you to manually look up the item via `list[i]` inside the loop block, which is less readable and slightly less efficient. `enumerate` neatly unpacks the index and the item simultaneously.
"""