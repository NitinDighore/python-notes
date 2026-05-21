from pydantic import BaseModel, field_validator, model_validator, ValidationError, Field
from datetime import datetime
from typing import Annotated, Any

class Person(BaseModel):
    first_name: str
    last_name : str

    @field_validator('first_name', 'last_name')
    def names_must_be_capitalize(cls, v):
        if not v.istitle():
            raise ValueError('Names must be capitilized')
        return v
    

class User(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, v):
        return v.lower().strip()
    


class Product(BaseModel):
    price: str # $4.44

    @field_validator('price', mode='before')
    def parse_price(cls, v):
        if isinstance(v, str):
            return float(v.replace('$', ''))
        return v
    
class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime


    @model_validator(mode="after")
    def validate_date_range(cls, values):
        if values.start_date >= values.end_date:
            raise ValueError('end_date must be after start_date')
        return values


# --- Added Instantiations and Prints ---

try:
    person = Person(first_name="hitesh", last_name="choudhary")
except ValidationError as e:
    print(e) 
    # Output:
    # 2 validation errors for Person
    # first_name
    #   Value error, Names must be capitilized [type=value_error, input_value='hitesh', input_type=str]
    # last_name
    #   Value error, Names must be capitilized [type=value_error, input_value='choudhary', input_type=str]

user = User(email="  MyEmail@Example.com  ")
print(f"Normalized Email: {user.email}") # Output: Normalized Email: myemail@example.com

product = Product(price="$99.99")
print(f"Parsed Price: {product.price}") # Output: Parsed Price: 99.99

try:
    date_range = DateRange(start_date="2025-01-02", end_date="2025-01-01")
except ValidationError as e:
    print(e)
    # Output:
    # 1 validation error for DateRange
    #   Value error, end_date must be after start_date [type=value_error, input_value={'start_date': datetime.dat...0, 0), 'end_date': ...}, input_type=dict]

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Reusable Validators (Pydantic V2 + Annotated)
print("\n1. Reusable Validators:")
from pydantic.functional_validators import AfterValidator

# Define a simple, reusable validation function
def must_be_capitalized(v: str) -> str:
    if not v.istitle():
        raise ValueError(f"'{v}' must be capitalized.")
    return v

# Use `Annotated` to apply the validator declaratively!
CapitalizedStr = Annotated[str, AfterValidator(must_be_capitalized)]

class ReusablePerson(BaseModel):
    first_name: CapitalizedStr
    last_name: CapitalizedStr

p = ReusablePerson(first_name="Hitesh", last_name="Choudhary")
print(f"Reusable validation passed for: {p.first_name}") # Output: Reusable validation passed for: Hitesh

# Trick 2: Applying a validator to ALL fields
print("\n2. Applying validator to all fields with '*':")
class CleanStrings(BaseModel):
    a: str
    b: str

    @field_validator('*', mode='before')
    def strip_all_strings(cls, v: Any):
        if isinstance(v, str):
            return v.strip()
        return v

cleaned = CleanStrings(a="  leading", b="trailing  ")
print(f"Cleaned strings: a='{cleaned.a}', b='{cleaned.b}'") # Output: Cleaned strings: a='leading', b='trailing'

"""
--- NOTES: Pydantic Field and Model Validators ---

1. What are Validators?
   - The filename `advance_validators.py` highlights Pydantic's core strength: data validation.
   - `@field_validator`: A decorator that runs a function to check, clean, or transform a specific field's data during model instantiation.
   - `@model_validator`: A decorator that runs after all individual field validators. It is used for "cross-field" validation, where the validity of one field depends on the value of another (like `start_date` vs `end_date`).

2. Validator Modes:
   - `mode='after'` (default): The validator runs *after* Pydantic has parsed the input into its expected Python type.
   - `mode='before'`: The validator runs *before* Pydantic does any parsing. This is useful for cleaning raw input data, like stripping the `$` from a price string before it's converted to a float.

3. Latest Python & Pydantic Features (Pydantic V2):
   - **Complete Rewrite**: Pydantic V2 was rewritten from the ground up in Rust, making it 5-50x faster than V1.
   - **New Validator Syntax**: The `@validator` and `@root_validator` decorators from V1 have been replaced by the more explicit and powerful `@field_validator` and `@model_validator`.
   - **`Annotated` Validators**: As shown in Trick 1, Pydantic V2 heavily encourages using `typing.Annotated` to apply validation rules declaratively, making models cleaner and validators more reusable.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between a `@field_validator` and a `@model_validator`?
A1: A `@field_validator` is bound to one or more specific fields and runs on their individual values. A `@model_validator` runs on the entire model (or a dictionary of its values) and is used to enforce rules that involve relationships between multiple fields.

Q2: In a `@field_validator`, what does the `cls` argument represent?
A2: The `cls` argument represents the class itself (e.g., `Person`). It is passed implicitly, similar to a `@classmethod`. While not always used, it allows the validator to access class-level variables if needed.

Q3: How would you ensure a `password` field and a `confirm_password` field are identical?
A3: You would use a `@model_validator(mode='after')`. This allows you to access the already-validated values for both fields from the `values` object and compare them.

Q4: What does `mode='before'` signify in a `@field_validator`?
A4: It tells Pydantic to run the validation function on the raw input data *before* any type coercion or parsing occurs. This is ideal for cleaning up data formats, like removing currency symbols or standardizing date strings, before Pydantic tries to convert them to `float` or `datetime` objects.
"""