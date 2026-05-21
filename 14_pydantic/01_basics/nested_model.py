from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address


address = Address(
    street="123 something",
    city="Jaipur",
    postal_code="100001"
)

user = User(
    id=1,
    name="Hitesh",
    address=address,
)


user_data = {
    "id": 1,
    "name": "Hitesh",
    "address": {
        "street": "321 something",
        "city": "Paris",
        "postal_code": "20002"
    }
}

user = User(**user_data)
print(user) 
# Output: id=1 name='Hitesh' address=Address(street='321 something', city='Paris', postal_code='20002')

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Accessing nested attributes
print("\n1. Accessing Nested Data:")
# You can use standard dot-notation to drill down into nested models
print(f"User's City: {user.address.city}") # Output: User's City: Paris

# Trick 2: Safe Optional Nesting
print("\n2. Optional Nested Models:")
class Profile(BaseModel):
    bio: str

class FlexibleUser(BaseModel):
    name: str
    # If the user doesn't provide a profile dictionary, it safely defaults to None
    profile: Optional[Profile] = None

f_user = FlexibleUser(name="Alice")
print(f"Flexible User without profile: {f_user}") # Output: Flexible User without profile: name='Alice' profile=None

# Trick 3: Deep Copying and Updating (Pydantic V2)
print("\n3. Updating Nested Models (model_copy):")
# Pydantic models are meant to be somewhat immutable. To change a nested value, you should copy and update.
# model_copy() replaces the old .copy() from Pydantic V1
updated_user = user.model_copy(update={"name": "Hitesh Pro", "address": Address(street="New St", city="London", postal_code="99999")})
print(f"Updated User City: {updated_user.address.city}") # Output: Updated User City: London

# Trick 4: Fine-grained Exclusion on Dumps
print("\n4. Excluding Nested Fields during Export:")
# You can explicitly target nested fields to hide them when dumping to a dictionary
safe_dump = user.model_dump(exclude={"address": {"postal_code": True}})
print(f"Dump without postal code: {safe_dump}") 
# Output: Dump without postal code: {'id': 1, 'name': 'Hitesh', 'address': {'street': '321 something', 'city': 'Paris'}}

"""
--- NOTES: Nested Models in Pydantic ---

1. Automatic Recursive Parsing:
   - Pydantic shines at handling complex, nested JSON data (like responses from Web APIs or NoSQL databases).
   - When you define a field as another Pydantic `BaseModel` (e.g., `address: Address`), and you pass a raw nested dictionary (like `user_data`), Pydantic will automatically traverse the dictionary and instantiate the nested `Address` model for you.

2. Validation Error Bubbling:
   - If the nested dictionary is missing a required field (e.g., `"city"` is missing from the `"address"` dict), Pydantic will raise a `ValidationError` and precisely point out the location of the error using a "loc" path (e.g., `loc=('address', 'city')`).

3. Latest Python & Pydantic Features (Pydantic V2):
   - **Rust Core Performance**: In Pydantic V2, the core validation engine is written in Rust (`pydantic-core`). This means traversing and validating deeply nested dictionaries is exponentially faster than in V1.
   - **New Methods**: As shown in the tricks, V2 prefixes its core methods with `model_` to prevent clashes. `.dict()` is now `model_dump()`, and `.copy()` is now `model_copy()`.
   - **Python 3.10 Union Syntax**: Instead of `Optional[Address]`, modern Python allows you to write `address: Address | None = None`, keeping nested schemas incredibly clean.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: How do you define a one-to-many nested relationship in Pydantic?
A1: You use the `List` type hint (or `list[]` in Python 3.9+) combined with your nested model. For example: `addresses: List[Address]`. If a user passes a list of dictionaries, Pydantic will iterate through them and create a list of `Address` instances.

Q2: What happens if I pass a pre-instantiated `Address` object instead of a dictionary when creating a `User`?
A2: It works perfectly! Pydantic is flexible. As shown in the original code, `User(id=1, name="H", address=address)` works exactly the same as unpacking `user_data`. Pydantic accepts both raw dictionaries and fully formed model instances for nested fields.

Q3: How do you extract just the nested dictionary back out of the parent model?
A3: You can call `model_dump()` on the parent, which recursively dumps all children into dictionaries. Alternatively, if you only want the nested data, you can directly access the child model and dump it: `user.address.model_dump()`.

Q4: If I update `user.address.city = "New City"`, does it pass validation?
A4: While Python technically allows you to mutate the attribute after instantiation, Pydantic does *not* re-validate the model upon attribute assignment by default. To strictly enforce validation on assignment, you must configure the model with `model_config = {'validate_assignment': True}`. Otherwise, it's safer to use `model_copy(update=...)`.
"""