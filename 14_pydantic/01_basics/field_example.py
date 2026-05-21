from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


cart_data = {
    "user_id": 123,
    "items": ["Laptop", "Mouse", "Keyboard"],
    "quantities": {"laptop": 1, "mouse": 2, "keyboard": 3}
}

cart = Cart(**cart_data)
print(cart) 
# Output: user_id=123 items=['Laptop', 'Mouse', 'Keyboard'] quantities={'laptop': 1, 'mouse': 2, 'keyboard': 3}

# BlogPost with the Optional field left blank
post = BlogPost(title="Pydantic Basics", content="Learning about fields.")
print(post) 
# Output: title='Pydantic Basics' content='Learning about fields.' image_url=None

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Modern Type Hinting (Python 3.9+ & 3.10+)
print("\n1. Modern Python Type Hinting (No 'typing' module needed):")
class ModernCart(BaseModel):
    user_id: int
    items: list[str] # Built-in list instead of typing.List (Python 3.9+)
    quantities: dict[str, int] # Built-in dict instead of typing.Dict (Python 3.9+)
    tags: str | None = None # Pipe operator instead of Optional[str] (Python 3.10+)

m_cart = ModernCart(user_id=456, items=["Pen"], quantities={"Pen": 5})
print(f"Modern Cart: {m_cart}") 
# Output: Modern Cart: user_id=456 items=['Pen'] quantities={'Pen': 5} tags=None

# Trick 2: Pydantic Automatic Type Coercion
print("\n2. Automatic Type Coercion:")
# Pydantic is smart enough to convert tuples to lists, or string numbers to ints!
coerced_cart = Cart(
    user_id="789", # Passed a string, Pydantic coerces to an int
    items=("Monitor", "Cable"), # Passed a tuple, Pydantic coerces to a list
    quantities={"monitor": "2", "cable": "1"} # Passed string values, Pydantic coerces to ints
)
print(f"Coerced Types: id={type(coerced_cart.user_id)}, items={type(coerced_cart.items)}")
# Output: Coerced Types: id=<class 'int'>, items=<class 'list'>

# Trick 3: Defaulting mutable collections safely
print("\n3. Safe Mutable Defaults with Field(default_factory=...):")
from pydantic import Field
class SafeCart(BaseModel):
    user_id: int
    # While standard Python suffers from the "mutable default trap" for `items: list = []`,
    # Pydantic safely handles it. However, `default_factory` is the strict best practice!
    items: list[str] = Field(default_factory=list)

safe = SafeCart(user_id=999)
print(f"Safe Cart Items: {safe.items}") # Output: Safe Cart Items: []

"""
--- NOTES: Complex Type Fields in Pydantic ---

1. Complex Types (`List`, `Dict`, `Optional`):
   - The filename `field_example.py` showcases how Pydantic handles standard Python data structures.
   - `List[str]`: Ensures every item in the list is validated and coerced into a string.
   - `Dict[str, int]`: Ensures all keys are strings and all values are integers.
   - `Optional[str]`: A type hint meaning the value can be either a `str` or `None`.

2. Pydantic Type Coercion:
   - Pydantic prioritizes *parsing* over strict validation. If a field expects a `List` but you pass a `tuple` or `set`, it will automatically convert it to a `list` rather than throwing an error. If it expects an `int` and you pass `"123"`, it parses it into an integer.

3. Latest Python Features (Python 3.9 & 3.10+):
   - **Standard Collection Generics (PEP 585 / Python 3.9)**: You no longer need to import `List` or `Dict` from the `typing` module. You can use the lowercase built-in types directly (e.g., `list[str]`, `dict[str, int]`).
   - **Union Operator `|` (PEP 604 / Python 3.10)**: You no longer need to import `Optional` or `Union`. You can write `str | None` instead of `Optional[str]`. This makes Pydantic models significantly cleaner and more readable.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between `image_url: Optional[str]` and `image_url: str = None`?
A1: `Optional[str]` is purely a type hint indicating the value *can* be None. However, it does not actually provide a default value; without `= None`, Pydantic will still strictly require you to pass `image_url` when instantiating the model (even if you explicitly pass `image_url=None`). Setting `= None` actually provides the default value, making the field truly optional during instantiation.

Q2: Is `items: list[str] = []` safe in Pydantic, considering Python's mutable default argument trap?
A2: In standard Python classes or functions, `items = []` is dangerous because the list is instantiated once and shared across all instances. However, Pydantic is incredibly smart and automatically deep-copies default lists and dictionaries during model instantiation, so it is actually safe! Still, many developers prefer `Field(default_factory=list)` to be completely explicit and align with standard Python `@dataclass` practices.

Q3: What happens if I pass `quantities={"laptop": "one"}` to the `Cart` model?
A3: Pydantic will raise a `ValidationError`. While it enthusiastically attempts type coercion (converting the string `"1"` to an integer `1`), it cannot coerce the English alphabet word `"one"` into a valid integer.
"""