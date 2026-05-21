from pydantic import BaseModel, ValidationError

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id': '101a', 'name': "Chaicode", 'is_active': True}

try:
    user = User(**input_data)
    print(user)
except ValidationError as e:
    print(f"Error: {e.errors()[0]['msg']}") 
    # Output: Error: Input should be a valid integer, unable to parse string as an integer

# Valid input to show success and coercion
valid_data = {'id': '101', 'name': "Chaicode", 'is_active': "yes"}
valid_user = User(**valid_data)
print(valid_user) 
# Output: id=101 name='Chaicode' is_active=True

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Parsing JSON strings directly (Pydantic V2)
print("\n1. Parsing JSON strings directly:")
json_str = '{"id": 99, "name": "Alice", "is_active": false}'
# model_validate_json replaces the old parse_raw() from V1
user_from_json = User.model_validate_json(json_str)
print(f"From JSON: {user_from_json}") # Output: From JSON: id=99 name='Alice' is_active=False

# Trick 2: Exporting Models (Dump)
print("\n2. Exporting to Dictionary and JSON:")
# model_dump() replaces the old .dict(), and model_dump_json() replaces .json()
print(f"As Dict: {valid_user.model_dump()}") # Output: As Dict: {'id': 101, 'name': 'Chaicode', 'is_active': True}
print(f"As JSON: {valid_user.model_dump_json()}") # Output: As JSON: {"id":101,"name":"Chaicode","is_active":true}

# Trick 3: Strict Mode (No Coercion!)
print("\n3. Strict Mode Validation:")
class StrictUser(BaseModel):
    # This configuration prevents Pydantic from trying to convert "101" to 101
    model_config = {'strict': True}
    id: int
    name: str

try:
    StrictUser(id="50", name="Bob") # "50" is a string, which violates strict int rules
except ValidationError as e:
    print(f"Strict Error: {e.errors()[0]['msg']}") # Output: Strict Error: Input should be a valid integer

"""
--- NOTES: Pydantic Basics ---

1. What is Pydantic?
   - Pydantic is a data validation and settings management library for Python.
   - It relies heavily on Python's type hints (`id: int`).
   - If the data is valid, it creates a strongly-typed Python object. If it is invalid, it raises a very clear `ValidationError`.

2. Automatic Type Coercion:
   - Pydantic is incredibly forgiving by default. As shown in the `valid_data` example, passing the string `"101"` to an `int` field will automatically coerce it to the integer `101`. Passing `"yes"` to a `bool` field automatically coerces it to `True`.
   - However, if coercion is mathematically impossible (like `"101a"` to an integer), it will aggressively fail.

3. Latest Python & Pydantic Features (Pydantic V2):
   - **Pydantic V2 Core**: Pydantic was entirely rewritten in Rust. This makes validation 5x to 50x faster than Pydantic V1.
   - **Method Renames**: In Pydantic V2, the core methods were renamed with a `model_` prefix to prevent them from clashing with your own model fields.
     - `obj.dict()` -> `obj.model_dump()`
     - `obj.json()` -> `obj.model_dump_json()`
     - `Model.parse_raw()` -> `Model.model_validate_json()`
     - `Model.parse_obj()` -> `Model.model_validate()`

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if I pass `{'id': '101a'}` to the `User` model, where `id` is type-hinted as `int`?
A1: Pydantic will attempt to convert the string `'101a'` into an integer. When the underlying `int('101a')` operation fails, Pydantic intercepts the error and raises a `ValidationError`, providing detailed context about exactly which field failed and why.

Q2: Is Pydantic purely for type checking?
A2: No. Tools like `mypy` perform static type checking (before the code runs). Pydantic performs *runtime* data validation and parsing. It guarantees that the data entering your application conforms to the shapes you defined.

Q3: How do you prevent Pydantic from automatically coercing types (e.g., converting the string `"10"` to the int `10`)?
A3: You can enable "Strict Mode". In Pydantic V2, you can do this by setting `model_config = {'strict': True}` inside the class, or by instantiating the model using `User.model_validate(data, strict=True)`.

Q4: Why does Pydantic V2 use the `model_` prefix for all of its core methods?
A4: To prevent namespace collisions. If Pydantic used `.dump()` instead of `.model_dump()`, and you had a database table with a column named `dump`, your field name would conflict with Pydantic's internal method, causing massive headaches. The `model_` prefix ensures your data fields will rarely conflict with the library.
"""