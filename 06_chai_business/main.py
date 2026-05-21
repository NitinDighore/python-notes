import recipes.flavors

print(recipes.flavors.ginger_chai()) # Output: (e.g., 'Ginger chai is ready!')

from recipes.flavors import elachai_chai, ginger_chai

print(ginger_chai()) # Output: (e.g., 'Ginger chai is ready!')

print("\n--- TRICK CODING EXAMPLES (MODULES & PACKAGES) ---")

# Trick 1: Aliasing modules for cleaner code
print("\n1. Aliasing Imports:")
# import recipes.flavors as rf
# print(rf.ginger_chai())

# Trick 2: Handling Circular Imports (Conceptual)
print("\n2. Conditional/Local Imports (Avoiding Circular Dependency):")
def get_complex_flavor():
    # Importing inside the function delays the import until the function is actually called.
    # This is a common hack to bypass circular import errors where Module A and Module B import each other.
    # from recipes.advanced_flavors import secret_chai
    # return secret_chai()
    pass

# Trick 3: Differentiating between running as script vs importing
print("\n3. Execution Guard (__name__ == '__main__'):")
# This block ONLY runs if you execute `python main.py` directly from the terminal.
# It will NOT run if another file does `import main`.
if __name__ == "__main__":
    print("This script (main.py) is being run directly!")
else:
    print("This script is being imported into another file!")

"""
--- NOTES: Python Modules and Packages Summary ---

1. Topic Summary (`06_chai_business` structure):
   - This folder represents a standard Python project architecture.
   - A **Module** is simply a single Python file (e.g., `flavors.py`) containing related functions, classes, and variables.
   - A **Package** is a directory (e.g., `recipes/`) containing multiple modules. Historically, it required an `__init__.py` file to be recognized as a package.
   - `main.py` acts as the entry point of the application, orchestrating the logic by importing tools from the `recipes` package.

2. Import Variations:
   - `import module`: Imports the whole module. You must prefix calls with the module name (e.g., `module.func()`). Safe from naming collisions.
   - `from module import func`: Imports a specific function. You can call it directly (`func()`). Risks shadowing local variables with the same name.
   - `from module import *`: Imports everything. Highly discouraged as it pollutes the namespace and makes tracking function origins difficult.

3. Latest Python Features (Packaging & Imports):
   - **Implicit Namespace Packages (Python 3.3+)**: You no longer strictly need an `__init__.py` file inside a directory for Python to treat it as a package. However, including it is still standard practice to denote regular packages and execute initialization code.
   - **Lazy Imports / `importlib` Improvements (Python 3.12+)**: Modern Python environments and large frameworks are increasingly utilizing `importlib` and mechanisms to lazily load modules only when they are accessed, significantly speeding up application boot times and reducing memory overhead.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the purpose of the `__init__.py` file in a directory?
A1: Historically (pre-Python 3.3), it was strictly required to make Python treat the directory as a package. Today, it is used to execute initialization code for the package or to define the `__all__` list, which controls exactly what gets exported when a user does a wildcard import (`from package import *`).

Q2: What happens if you import the same module twice in a script?
A2: Python only loads and executes the module the *first* time it is imported. Subsequent imports are simply fetched from `sys.modules` (a dictionary that acts as a cache for loaded modules). Therefore, there is virtually no performance penalty for importing a module multiple times across different files.

Q3: How do you fix a "Circular Import" error?
A3: Circular imports occur when Module A imports Module B, and Module B simultaneously imports Module A. You can fix this by: 
    1) Refactoring the code to extract the shared dependency into a new Module C.
    2) Moving the import statement inside the specific function that needs it (local import, as shown in Trick 2).
    3) Importing the module itself (`import B`) rather than a specific attribute (`from B import func`).

Q4: Explain the `if __name__ == "__main__":` block.
A4: Every Python module has a built-in `__name__` attribute. If the file is being executed directly as the main program, Python sets `__name__` to `"__main__"`. If the file is imported into another module, `__name__` is set to the file's actual name. This block prevents testing or execution code from running when the file is simply being imported as a utility.
"""
