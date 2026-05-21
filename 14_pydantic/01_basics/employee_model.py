from typing import Optional
from pydantic import BaseModel, Field, ValidationError
import re

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee Name",
        examples=["Hitesh Choudhary"] # Pydantic V2 expects examples to be a list
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000
    )


class User(BaseModel):
    # In Pydantic V2, 'regex' is renamed to 'pattern'. Added basic regex patterns to avoid errors.
    email: str = Field(..., pattern=r'^[\w\.-]+@[\w\.-]+\.\w+$')
    phone: str = Field(..., pattern=r'^\+?[1-9]\d{1,14}$')
    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years",
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )


# --- Added Instantiations and Prints ---

emp = Employee(id=1, name="Hitesh", salary=50000)
print(f"Valid Employee: {emp}")
# Output: Valid Employee: id=1 name='Hitesh' department='General' salary=50000.0

try:
    # Fails because salary is less than 10000 and name is less than 3 chars
    bad_emp = Employee(id=2, name="Jo", salary=5000)
except ValidationError as e:
    print(f"Employee Validation Failed: {e.error_count()} errors found.")
    # Output: Employee Validation Failed: 2 errors found.

valid_user = User(email="test@example.com", phone="+1234567890", age=25, discount=10.5)
print(f"Valid User Email: {valid_user.email}")
# Output: Valid User Email: test@example.com

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Dynamic Defaults using default_factory
print("\n1. Dynamic Defaults (default_factory):")
from datetime import datetime
class Event(BaseModel):
    name: str
    # If we used default=datetime.now(), it would lock the time to when the script started!
    # default_factory evaluates the function every single time a new object is created.
    created_at: datetime = Field(default_factory=datetime.now)

e1 = Event(name="Login")
import time; time.sleep(0.1)
e2 = Event(name="Logout")
print(f"E1 time: {e1.created_at.time()}")
print(f"E2 time: {e2.created_at.time()} (Notice they are different!)")

# Trick 2: Field Aliases (Mapping JSON keys to Python snake_case)
print("\n2. Field Aliases:")
class APIResponse(BaseModel):
    # JSON often uses camelCase or reserved words, Python uses snake_case
    user_id: int = Field(alias="userId")
    class_name: str = Field(alias="class")

# We instantiate using the JSON aliases
resp = APIResponse(**{"userId": 99, "class": "Premium"})
# But access them using nice Python variable names!
print(f"Mapped user_id: {resp.user_id}, class_name: {resp.class_name}") 
# Output: Mapped user_id: 99, class_name: Premium

# Trick 3: Hiding sensitive fields from repr and dumps
print("\n3. Hiding Sensitive Fields:")
class SecretConfig(BaseModel):
    username: str
    # exclude=True prevents it from appearing in model_dump()
    # repr=False prevents it from appearing when printing the object
    password: str = Field(..., exclude=True, repr=False)

config = SecretConfig(username="admin", password="super_secret_password")
print(f"Object repr: {config}") # Output: Object repr: username='admin'
print(f"Dumped dict: {config.model_dump()}") # Output: Dumped dict: {'username': 'admin'}

"""
--- NOTES: Pydantic Field Validation ---

1. The `Field` Function:
   - `Field` is used to customize and add rich metadata/constraints to specific model attributes.
   - Common constraints include `min_length` & `max_length` (for strings), and `ge` (greater-than-or-equal), `gt`, `le`, `lt` (for numbers).

2. The Ellipsis (`...`):
   - When you see `Field(..., ge=10000)`, the `...` (Ellipsis) specifically tells Pydantic: "This field is strictly required, there is no default value."
   - If the field were optional with a default, it would look like `Field(default=5000, ge=1000)`.

3. Latest Python & Pydantic Features (Pydantic V2):
   - **`regex` -> `pattern`**: In Pydantic V1, regular expressions were passed to `Field` using `regex=r'...'`. In Pydantic V2, this keyword was officially renamed to `pattern=r'...'` to perfectly align with JSON Schema standard specifications.
   - **Strict Mode**: Pydantic V2 introduced a `strict=True` argument for fields and models. When enabled, it disables data coercion (e.g., passing the string `"25"` to an `int` field will fail, rather than automatically converting it to an integer).

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What does the `...` (Ellipsis) mean inside a `Field()` function?
A1: It indicates that the field is mandatory (required). It acts as a placeholder for the `default` argument when you want to supply extra validation constraints but do not want to supply a default value.

Q2: If you want a timestamp field to automatically record the exact time the object was created, why should you use `default_factory=datetime.now` instead of `default=datetime.now()`?
A2: If you use `default=datetime.now()`, the function is evaluated exactly once when the class is initially defined in memory. Every single object created thereafter will share that exact same timestamp. `default_factory` accepts a callable and evaluates it dynamically every time a new instance is created.

Q3: How do you handle mapping a JSON payload containing the key `"user-id"` to a Python class attribute named `user_id`?
A3: You use the `alias` parameter inside the Field: `user_id: int = Field(alias="user-id")`. Pydantic will read `"user-id"` from the incoming dictionary and map it cleanly to `user_id` in Python.

Q4: How can you prevent a user's password from being exposed when someone runs `print(user.model_dump())`?
A4: You can define the field as `password: str = Field(..., exclude=True)`. This ensures that whenever the model is serialized to a dictionary or JSON, the password field is entirely stripped out.
"""
