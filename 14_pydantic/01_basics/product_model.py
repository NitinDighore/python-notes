from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True


product_one = Product(id=1, name="Laptop", price=999.99, in_stock=True)
print(product_one) # Output: id=1 name='Laptop' price=999.99 in_stock=True

product_two = Product(id=2, name="Mouse", price=24.33)
print(product_two) # Output: id=2 name='Mouse' price=24.33 in_stock=True

try:
    # This will fail because 'id' and 'price' do not have default values and are required!
    product_three = Product(name="keyboard")
except ValidationError as e:
    print(f"Validation Error caught: {e.error_count()} missing fields!")
    # Output: Validation Error caught: 2 missing fields!

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Immutability (Frozen Models)
print("\n1. Frozen Models (Immutable):")
class FrozenProduct(BaseModel):
    # In Pydantic V2, configuration is handled via the model_config dictionary
    model_config = {'frozen': True}
    id: int
    name: str

frozen_item = FrozenProduct(id=10, name="Tablet")
try:
    frozen_item.name = "iPad" # Fails because the model is frozen!
except ValidationError as e:
    print(f"Frozen Error: {e.errors()[0]['msg']}") # Output: Frozen Error: Instance is frozen

# Trick 2: Validating Assignments dynamically
print("\n2. Validate Assignment:")
class DynamicProduct(BaseModel):
    # Normally, Pydantic only validates upon creation. This forces validation upon EVERY assignment!
    model_config = {'validate_assignment': True} 
    price: float

dynamic_item = DynamicProduct(price=50.0)
try:
    dynamic_item.price = "Not a number" # This string assignment will be caught!
except ValidationError as e:
    print(f"Assignment Error: {e.errors()[0]['msg']}") # Output: Assignment Error: Input should be a valid number...

# Trick 3: Parsing from Dictionaries 
print("\n3. Dictionary Unpacking vs model_validate:")
data = {"id": 99, "name": "Headphones", "price": 45.0}
# Method A: Standard Python kwargs unpacking
prod_a = Product(**data)
# Method B: Pydantic's built-in dictionary validator (cleaner for complex data)
prod_b = Product.model_validate(data)
print(f"Parsed Product via model_validate: {prod_b.name}") # Output: Parsed Product via model_validate: Headphones

"""
--- NOTES: Pydantic Data Models ---

1. Required vs Optional Fields:
   - In Pydantic, if a field is type-hinted but does NOT have a default value (like `id` and `price`), it is strictly required. Omitting it raises a `ValidationError`.
   - If a field is assigned a default value (like `in_stock: bool = True`), it becomes optional during object instantiation.

2. Pydantic vs `@dataclass`:
   - Python has a built-in `@dataclass` decorator that heavily reduces boilerplate code for classes. 
   - The key difference: Standard `dataclass` does NOT validate data at runtime. If you pass a string `"Hello"` into an `int` field in a standard dataclass, Python happily accepts it. Pydantic `BaseModel` strictly enforces types and validates data dynamically during runtime.

3. Latest Python & Pydantic Features (Pydantic V2):
   - **`model_config` Dict**: In Pydantic V1, model configuration was done using an inner `class Config:`. In Pydantic V2, this was deprecated in favor of a class-level dictionary named `model_config = {...}` (as seen in the trick examples), which is much more performant and IDE-friendly.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if I forget to provide the `id` field when creating a `Product`?
A1: Because `id` has no default value assigned in the class definition, Pydantic treats it as a required field. Instantiating the object without it will immediately raise a `pydantic.ValidationError`.

Q2: Can I change the value of `product_one.price` after it has been created? Does Pydantic validate the new value?
A2: Yes, you can change it (e.g., `product_one.price = 50`). By default, Pydantic does *not* validate data upon reassignment for performance reasons. If you assign a string to it, it will accept it. To force validation on reassignment, you must set `model_config = {'validate_assignment': True}`.

Q3: How do you make a Pydantic model immutable so its fields cannot be changed after creation?
A3: You set `'frozen': True` in the `model_config` dictionary. Any attempt to modify an attribute after instantiation will raise a `ValidationError`.

Q4: What is the difference between `Product(**data)` and `Product.model_validate(data)`?
A4: Functionally, they both parse a dictionary into a Pydantic model. However, `**data` uses Python's standard keyword unpacking, which can fail or act weirdly if the dictionary contains keys that aren't valid Python identifiers (like `"user-id"`). `model_validate` is Pydantic's native method designed to safely handle raw data structures and aliases directly.
"""