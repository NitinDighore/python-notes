from pydantic import BaseModel, computed_field, Field


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
    
booking = Booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_night=100.0
)

print(booking.total_amount) # Output: 300.0
print(booking.model_dump()) 
# Output: {'user_id': 123, 'room_id': 456, 'nights': 3, 'rate_per_night': 100.0, 'total_amount': 300.0}

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Computed fields with Caching (Python 3.8+ / Pydantic V2)
print("\n1. Memoizing expensive properties using @cached_property:")
from functools import cached_property
import time

class HeavyAnalytics(BaseModel):
    dataset: list[int]

    @computed_field
    @cached_property # Replaces standard @property to cache the result!
    def sum_data(self) -> int:
        print("Doing expensive math...")
        time.sleep(0.5)
        return sum(self.dataset)

analytics = HeavyAnalytics(dataset=[10, 20, 30])
print(f"First call: {analytics.sum_data}") # Output: Doing expensive math... \n First call: 60
print(f"Second call: {analytics.sum_data}") # Output: Second call: 60 (Instantly from cache!)
print(f"Dumped with cache: {analytics.model_dump()}") # Output: {'dataset': [10, 20, 30], 'sum_data': 60}

# Trick 2: Customizing the serialization of Computed Fields
print("\n2. Aliases and hiding computed fields:")
class Invoice(BaseModel):
    amount: float
    tax_rate: float

    # We can rename how it appears in JSON outputs using 'alias'
    # We can also hide it from print(repr(obj)) using 'repr=False'
    @computed_field(alias="taxAmount", repr=False)
    @property
    def tax(self) -> float:
        return self.amount * self.tax_rate

inv = Invoice(amount=100.0, tax_rate=0.05)
print(f"Repr (tax hidden): {inv}") # Output: Repr (tax hidden): amount=100.0 tax_rate=0.05
print(f"Dumped (with alias): {inv.model_dump(by_alias=True)}") # Output: Dumped (with alias): {'amount': 100.0, 'tax_rate': 0.05, 'taxAmount': 5.0}

# Trick 3: Chaining Computed Properties
print("\n3. Chaining computed fields:")
class Box(BaseModel):
    length: float
    width: float
    height: float

    @computed_field
    @property
    def base_area(self) -> float:
        return self.length * self.width

    @computed_field
    @property
    def volume(self) -> float:
        # Computed fields can safely rely on other computed fields
        return self.base_area * self.height

box = Box(length=2, width=3, height=4)
print(f"Box volume: {box.volume}") # Output: Box volume: 24.0

"""
--- NOTES: Computed Properties in Pydantic ---

1. The Purpose of `@computed_field`:
   - In standard Python, defining a `@property` allows you to compute a value on the fly when it is accessed.
   - However, in older Pydantic versions (V1), standard properties were completely ignored by `.dict()` and JSON schema generation. They were invisible to serialization.
   - Pydantic V2 introduced the `@computed_field` decorator. When stacked on top of a `@property`, it tells Pydantic: "Treat this dynamically calculated value as a formal field when dumping data to a dictionary or JSON."

2. Read-Only by Default:
   - Computed fields act purely as read-only serialized data. If you attempt to explicitly pass `total_amount=300.0` when instantiating the `Booking` model, Pydantic will raise a validation error, because computed fields are derived, not set by the user.

3. Latest Python & Pydantic Features:
   - **Pydantic V2 Rust Core**: Because Pydantic V2 is written in Rust, generating dumps containing multiple complex computed fields is incredibly fast.
   - **Integration with `cached_property`**: As seen in Trick 1, Pydantic V2 allows `@computed_field` to seamlessly wrap Python's built-in `@cached_property` (introduced in 3.8). This ensures that heavy calculations are executed exactly once, then securely cached inside the model instance for all future serializations.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why do we need the `@computed_field` decorator? Isn't `@property` enough?
A1: Standard `@property` methods work for instance access (e.g., `booking.total_amount`), but they are ignored when serializing the model using `model_dump()` or `model_dump_json()`. The `@computed_field` decorator strictly registers the property into Pydantic's core schema, guaranteeing it gets serialized along with the standard fields.

Q2: Can I provide a value for a `@computed_field` during model initialization? Example: `Booking(nights=3, rate_per_night=100, total_amount=300)`?
A2: No. Pydantic will raise a `ValidationError` stating that an unexpected keyword argument was provided. Computed fields evaluate dynamically after instantiation; they are not initialized via user input.

Q3: Can a `@computed_field` return a complex type, like a custom class or list?
A3: Yes! Just like regular fields, you simply type-hint the return value of the property (e.g., `def my_list(self) -> List[str]:`). Pydantic will automatically validate and serialize the returned data structure into standard dictionary/JSON formats during a `model_dump()`.
"""