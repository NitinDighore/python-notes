# file = open("order.txt", "w")
# try:
#     file.write("Masala chai - 2 cups")
# finally:
#     file.close()


with open("order.txt", "w") as file:
    file.write("ginger tea - 4 cups")

# Let's read it back to verify
with open("order.txt", "r") as file:
    print(file.read()) # Output: ginger tea - 4 cups

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Modern File Handling with pathlib
print("\n1. Modern File Handling (pathlib):")
from pathlib import Path
# Pathlib is the modern, Object-Oriented way to handle file paths. It handles OS-specific slashes automatically!
file_path = Path("modern_order.txt")
file_path.write_text("Matcha - 1 cup") # Opens, writes, and closes the file in one clean line!
print(file_path.read_text()) # Output: Matcha - 1 cup

# Trick 2: Appending to a file ('a' mode)
print("\n2. Appending to a file:")
with open("order.txt", "a") as file:
    file.write("\nLemon tea - 2 cups")
with open("order.txt", "r") as file:
    print(repr(file.read())) # Output: 'ginger tea - 4 cups\nLemon tea - 2 cups'

# Trick 3: Multiple Context Managers simultaneously
print("\n3. Multiple Context Managers:")
# You can open a source file for reading and a destination file for writing at the exact same time
with open("order.txt", "r") as source, open("copy.txt", "w") as dest:
    dest.write(source.read())
print("Copied contents from order.txt to copy.txt successfully.")

# Trick 4: Creating a Custom Context Manager (Class-based)
print("\n4. Custom Context Manager (Class):")
class TimerContext:
    # __enter__ runs right at the start of the 'with' block
    def __enter__(self):
        import time
        self.start = time.perf_counter()
        return self # This is bound to the variable after 'as'

    # __exit__ runs when the block finishes (or crashes)
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        end = time.perf_counter()
        print(f"Block executed in {end - self.start:.6f} seconds")
        # If we returned True here, it would swallow any exceptions raised inside the block!

with TimerContext():
    sum(range(1000000)) # Output: Block executed in 0.01XXXX seconds

# Trick 5: Custom Context Manager (Generator/Decorator-based)
print("\n5. Custom Context Manager (Decorator):")
from contextlib import contextmanager

@contextmanager
def open_and_log(filename, mode):
    print(f"Opening {filename}...")
    f = open(filename, mode)
    try:
        yield f # Execution pauses here and yields the file object to the 'with' block
    finally:
        print(f"Closing {filename}...")
        f.close()

with open_and_log("temp.txt", "w") as f:
    f.write("test data")
# Output:
# Opening temp.txt...
# Closing temp.txt...

"""
--- NOTES: File Handling and Context Managers ---

1. The `with` Statement (Context Managers):
   - The commented-out code at the top shows how we used to handle files: wrapping them in a `try...finally` block to guarantee the `file.close()` method was called even if an error occurred while writing.
   - The `with` statement abstracts all of this setup and teardown logic. It automatically calls `__enter__()` to set up the resource, and absolutely guarantees that `__exit__()` is called (which closes the file) when the block terminates.

2. Common File Modes:
   - `"r"`: Read (default). Raises `FileNotFoundError` if the file doesn't exist.
   - `"w"`: Write. Truncates (overwrites completely) the file if it exists, or creates it if it doesn't.
   - `"a"`: Append. Writes data to the absolute end of the file without overwriting existing data.
   - `"b"`: Binary mode. Used for non-text files like images or PDFs (e.g., `"rb"` or `"wb"`).

3. Latest Python Features (Python 3.10+):
   - **Parenthesized Context Managers**: Python 3.10 updated the parser to allow you to group multiple context managers across multiple lines using parentheses. This prevents overly long, unreadable lines.
     ```python
     with (
         open("file1.txt", "r") as f1,
         open("file2.txt", "w") as f2
     ):
         f2.write(f1.read())
     ```

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why is it heavily recommended to use `with open("file.txt") as f:` instead of `f = open("file.txt")`?
A1: If you open a file without a `with` block and an exception occurs before you call `f.close()`, the file handle remains open, potentially causing memory leaks or locking the file at the OS level. The `with` statement guarantees the file is safely closed regardless of exceptions.

Q2: What happens if you open a file in `"w"` mode that already contains data?
A2: Opening a file in `"w"` (write) mode immediately truncates the file to zero length, permanently erasing all existing data in it. If you want to keep the existing data and add to it, you must use `"a"` (append) mode.

Q3: How do you create a custom Context Manager?
A3: You can create a class that implements the `__enter__` and `__exit__` dunder methods. Alternatively, you can write a generator function, decorate it with `@contextlib.contextmanager`, use `yield` to pass the resource to the block, and wrap the `yield` in a `try-finally` block for cleanup.

Q4: In an `__exit__` method, what happens if it returns `True`?
A4: If the `__exit__` method of a context manager returns `True`, it tells Python to gracefully swallow (suppress) any exception that was raised inside the `with` block, and execution will continue normally after the block.
"""