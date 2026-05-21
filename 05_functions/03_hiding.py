def get_input():
    print("Getting user input") # Output: Getting user input

def validate_input():
    print("Validating the user info") # Output: Validating the user info

def save_to_db():
    print("saving to database") # Output: saving to database

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print("User registration complete") # Output: User registration complete


register_user()

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: True Information Hiding via Nested Functions (Local Scope)
print("\n1. Hiding functions inside another function:")
def secure_registration():
    # These functions only exist inside secure_registration. 
    # They are completely hidden from the global scope and cannot be called from outside!
    def _fetch():
        print("Fetching securely...")
    def _save():
        print("Saving securely...")
        
    _fetch()
    _save()
    print("Secure registration complete.")

secure_registration()
# _fetch() # Uncommenting this would raise a NameError! It is successfully hidden.

# Trick 2: Module-Level Hiding using __all__
print("\n2. Hiding exports with __all__:")
# By defining __all__, you explicitly control what gets exported if someone runs `from 03_hiding import *`
# In this case, `get_input`, `validate_input`, etc., will be hidden from the wildcard import.
__all__ = ['register_user', 'secure_registration']
print(f"Functions available for wildcard export: {__all__}")

# Trick 3: The Convention of the Single Underscore
print("\n3. Hiding by Convention:")
def _internal_helper():
    # The single leading underscore is a universally accepted Python convention.
    # It tells other developers: "This is an internal implementation detail, do not use it directly."
    print("This is meant to be hidden/private.")
_internal_helper()

"""
--- NOTES: Abstraction and Information Hiding ---

1. Abstraction (Hiding Complexity):
   - The primary theme of `03_hiding.py` is Abstraction. 
   - The caller of `register_user()` doesn't need to know *how* to get input, validate it, or connect to the database. They just want to register a user.
   - By wrapping complex sequential logic behind a single, simple interface (`register_user()`), you "hide" the complexity of the underlying operations.

2. Information Hiding (Encapsulation):
   - While `register_user` abstracts the workflow, `get_input` and `save_to_db` are currently still exposed in the global scope (meaning anyone can call them directly, which might be dangerous or lead to bad data states).
   - As shown in Trick 1, you can physically hide helper logic by defining functions *inside* of other functions (Nested Functions/Closures). 

3. Latest Python Features:
   - **Type Hinting & Static Analysis (Python 3.9+)**: Modern Python heavily relies on tools like `mypy` for static analysis. If you prefix a function with an underscore (e.g., `def _save_to_db():`), strict type checkers will flag an error if an external script tries to import and use it, enforcing information hiding without needing strict language-level runtime blocks.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Does Python have true "private" methods or variables like Java or C++?
A1: No, Python does not have access modifiers like `public`, `private`, or `protected`. Instead, Python relies heavily on convention. A single leading underscore (`_func()`) indicates a protected/internal variable, while a double leading underscore (`__func()`) in classes invokes "name mangling" to make it harder to access from outside, but it is never truly strictly restricted. "We are all consenting adults here" is a famous Python motto regarding this.

Q2: What is the purpose of the `__all__` list in a Python file?
A2: The `__all__` list is used for module-level information hiding. It defines the explicit list of strings representing the names of variables, functions, and classes that will be exported when a developer uses `from module import *`. Anything not in `__all__` is kept "hidden" from the wildcard import.

Q3: If I define a helper function inside another function, can I access it globally?
A3: No. Nested functions live exclusively in the local scope of their parent function. Once the parent function finishes executing, the nested function is garbage collected (unless it was returned as a closure). Trying to call it globally will result in a `NameError`.
"""