from pydantic import BaseModel, field_validator, model_validator, ValidationError
from typing import Any


class User(BaseModel):
    username: str

    @field_validator('username')
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v
    

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password do not match")
        return values


# --- Added Instantiations and Prints ---

try:
    bad_user = User(username="bob")
except ValidationError as e:
    print("User Error:", e.errors()[0]['msg']) 
    # Output: User Error: Value error, Username must be at least 4 characters

good_user = User(username="alice")
print(f"Valid User: {good_user.username}") # Output: Valid User: alice

try:
    bad_signup = SignupData(password="secret123", confirm_password="password321")
except ValidationError as e:
    print("Signup Error:", e.errors()[0]['msg'])
    # Output: Signup Error: Value error, Password do not match

good_signup = SignupData(password="secret123", confirm_password="secret123")
print("Signup successful!") # Output: Signup successful!

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Accessing ValidationInfo in field_validator
print("\n1. Using ValidationInfo for contextual validation:")
from pydantic import ValidationInfo

class Profile(BaseModel):
    is_admin: bool
    access_level: int

    @field_validator('access_level')
    def check_admin_level(cls, v: int, info: ValidationInfo):
        # info.data contains the already-validated fields that were defined BEFORE this field!
        is_admin = info.data.get('is_admin', False)
        if not is_admin and v > 5:
            raise ValueError("Non-admins cannot have an access level greater than 5")
        return v

try:
    Profile(is_admin=False, access_level=10)
except ValidationError as e:
    print("Profile Error:", e.errors()[0]['msg']) 
    # Output: Profile Error: Value error, Non-admins cannot have an access level greater than 5

# Trick 2: Model Validator (mode='before')
print("\n2. Model Validator (mode='before'):")
# Sometimes you need to validate or manipulate the RAW input dictionary before Pydantic parses it
class RawData(BaseModel):
    full_name: str

    @model_validator(mode='before')
    @classmethod
    def split_names(cls, data: Any) -> Any:
        # If the user passed first_name and last_name separately, combine them!
        if isinstance(data, dict) and 'first_name' in data and 'last_name' in data:
            data['full_name'] = f"{data['first_name']} {data['last_name']}"
        return data

raw = RawData.model_validate({"first_name": "John", "last_name": "Doe"})
print(f"Computed Full Name: {raw.full_name}") # Output: Computed Full Name: John Doe

# Trick 3: Multiple fields in one field_validator
print("\n3. Validating multiple fields with one function:")
class PasswordCheck(BaseModel):
    pin1: str
    pin2: str

    @field_validator('pin1', 'pin2')
    @classmethod
    def must_be_numeric(cls, v: str):
        if not v.isnumeric():
            raise ValueError("PIN must be purely numeric")
        return v

try:
    PasswordCheck(pin1="1234", pin2="12a4")
except ValidationError as e:
    print("PIN Error:", e.errors()[0]['msg']) # Output: PIN Error: Value error, PIN must be purely numeric

"""
--- NOTES: Field and Model Validation ---

1. `@field_validator`:
   - Used to apply custom validation logic to specific individual fields.
   - Pydantic executes field validators in the exact order the fields are defined in the class (top-to-bottom).

2. `@model_validator`:
   - Used to apply custom validation logic across multiple fields or the entire model.
   - `mode='after'` (default): Runs after all fields have been individually validated and coerced. It receives the fully constructed model instance (which is why `values.password` works as object attribute access).
   - `mode='before'`: Runs before any field validation occurs. It receives the raw input dictionary.

3. Latest Pydantic Features (V2):
   - **`ValidationInfo`**: Replaces the old `values` dictionary parameter from V1's `@validator`. It safely provides access to the validation context and previously validated fields without confusing type signatures.
   - **Classmethod requirement**: In Pydantic V2, `@model_validator(mode='before')` and `@field_validator` implicitly act as class methods under the hood, but explicitly adding the `@classmethod` decorator is considered best practice and is required by some strict static type checkers.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: If `access_level` was defined *before* `is_admin` in the `Profile` class (Trick 1), would `info.data.get('is_admin')` work?
A1: No. Pydantic validates fields strictly from top to bottom. If `access_level` is validated first, `is_admin` has not been validated yet, so it will not exist in the `info.data` dictionary.

Q2: When should you use `@model_validator(mode='before')` instead of `mode='after'`?
A2: You use `mode='before'` when you need to manipulate or check the raw dictionary input *before* Pydantic tries to coerce the types or fails due to missing required fields. For example, consolidating legacy API fields into a new field structure before validation begins.

Q3: Can a validator modify the value of a field?
A3: Yes! A validator must always `return` a value. If you return a modified or cleaned value (like stripping whitespace, capitalizing, or replacing characters), that modified value will be permanently stored in the model.
"""