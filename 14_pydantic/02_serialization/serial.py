from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime


class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )


user = User(
    id=1,
    name="Hitesh",
    email="h@hitesh.ai",
    createdAt=datetime(2024, 3, 15, 14, 30,),
    address=Address(
        street="Something",
        city="Jaipur",
        zip_code="009988"
    ),
    is_active=False,
    tags=["premium", "subscriber"]
)

python_dict = user.model_dump()
print(user) 
# Output: id=1 name='Hitesh' email='h@hitesh.ai' is_active=False createdAt=datetime.datetime(2024, 3, 15, 14, 30) address=Address(street='Something', city='Jaipur', zip_code='009988') tags=['premium', 'subscriber']

print("="*30)
print(python_dict) 
# Output: {'id': 1, 'name': 'Hitesh', 'email': 'h@hitesh.ai', 'is_active': False, 'createdAt': datetime.datetime(2024, 3, 15, 14, 30), 'address': {'street': 'Something', 'city': 'Jaipur', 'zip_code': '009988'}, 'tags': ['premium', 'subscriber']}

json_str = user.model_dump_json()
print("="*30)
print(json_str) 
# Output: {"id":1,"name":"Hitesh","email":"h@hitesh.ai","is_active":false,"createdAt":"15-03-2024 14:30:00","address":{"street":"Something","city":"Jaipur","zip_code":"009988"},"tags":["premium","subscriber"]}

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The Pydantic V2 Way (@field_serializer)
print("\n1. Custom Serialization (@field_serializer):")
from pydantic import field_serializer

class ModernUser(BaseModel):
    name: str
    joined_at: datetime

    # json_encoders is deprecated in V2! The modern way is @field_serializer
    @field_serializer('joined_at')
    def serialize_dt(self, dt: datetime, _info):
        return dt.strftime('%Y/%m/%d')

m_user = ModernUser(name="Alice", joined_at=datetime(2024, 5, 20))
print(f"V2 Serialized: {m_user.model_dump_json()}") # Output: {"name":"Alice","joined_at":"2024/05/20"}

# Trick 2: Serializing the Entire Model (@model_serializer)
print("\n2. Customizing the entire model dump (@model_serializer):")
from pydantic import model_serializer

class SecretData(BaseModel):
    public_id: int
    secret_code: str

    @model_serializer
    def serialize_model(self):
        # You can completely hijack the dump process to return whatever you want!
        return {"id": self.public_id, "data": "REDACTED"}

secret = SecretData(public_id=99, secret_code="XYZ123")
print(f"Model Serialized: {secret.model_dump()}") # Output: {'id': 99, 'data': 'REDACTED'}

# Trick 3: Excluding Unset Defaults
print("\n3. Exclude Unset values during dump:")
class Settings(BaseModel):
    theme: str = "dark"
    notifications: bool = True
    custom_status: str | None = None

user_settings = Settings(custom_status="Away")
# By default, model_dump() includes EVERYTHING. 
# exclude_unset=True only dumps fields the user EXPLICITLY set, ignoring defaults!
print(f"Exclude Unset: {user_settings.model_dump(exclude_unset=True)}") 
# Output: Exclude Unset: {'custom_status': 'Away'}

# Trick 4: Serializing with Aliases
print("\n4. Serializing by Alias:")
from pydantic import Field
class DBRecord(BaseModel):
    # Python uses snake_case, but our database wants camelCase
    user_name: str = Field(alias="userName")

record = DBRecord(userName="Bob")
print(f"Standard Dump: {record.model_dump()}") # Output: {'user_name': 'Bob'}
print(f"Alias Dump: {record.model_dump(by_alias=True)}") # Output: {'userName': 'Bob'}

"""
--- NOTES: Pydantic Serialization ---

1. What is Serialization?
   - Serialization is the process of converting a complex Python object (like a Pydantic `BaseModel`) into a standard format that can be easily stored or transmitted (like a Python `dict` or a JSON `string`).
   - `model_dump()` converts the model to a Python dictionary.
   - `model_dump_json()` converts the model directly to a JSON string.

2. Controlling the Output:
   - Pydantic provides massive control over what gets serialized. You can use arguments like `include`, `exclude`, `exclude_unset`, `exclude_defaults`, and `exclude_none` directly inside the `model_dump()` method to fine-tune the resulting data payload.

3. Latest Python Features (Pydantic V2):
   - **Deprecation of `json_encoders`**: In Pydantic V1, `json_encoders` inside the `Config` class was the standard way to format dates, UUIDs, or custom objects. In Pydantic V2, this is officially deprecated. The Rust core engine (pydantic-core) now handles serialization. To customize it, you must use the `@field_serializer` or `@model_serializer` decorators (shown in Tricks 1 & 2).
   - **Serialization Modes (`mode='json'`)**: In Pydantic V2, `model_dump()` returns Python objects by default (e.g., a `datetime` object stays a `datetime` object in the dictionary). If you want the dictionary to contain JSON-compatible types (e.g., turning the `datetime` into an ISO-8601 string), you use `model_dump(mode='json')`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between `model_dump()` and `model_dump_json()`?
A1: `model_dump()` serializes the model into a standard Python dictionary, leaving objects like `datetime` or `UUID` intact as Python objects. `model_dump_json()` serializes the model into a raw JSON-formatted string, converting all Python objects into their JSON-compatible string equivalents.

Q2: How do you prevent a field (like a password) from being included when you call `model_dump()`?
A2: You can define the field with `exclude=True` in the model definition (e.g., `password: str = Field(exclude=True)`). Alternatively, you can exclude it dynamically at runtime by passing the `exclude` argument to the dump method: `user.model_dump(exclude={'password'})`.

Q3: Why is `json_encoders` deprecated in Pydantic V2, and what should be used instead?
A3: `json_encoders` was deprecated because Pydantic V2 moved the core validation and serialization logic to Rust for performance reasons. The `Config` approach was incompatible with the new architecture. Instead, developers should use the `@field_serializer` decorator to cleanly define custom serialization logic directly on the fields.

Q4: What does `exclude_unset=True` do?
A4: It tells the serializer to only include fields that were explicitly provided with a value when the model was instantiated. Any fields that fell back to their default values will be omitted from the output. This is heavily used in API PATCH requests where you only want to send the fields that actually changed.
"""