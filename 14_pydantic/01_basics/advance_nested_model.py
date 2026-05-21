from pydantic import BaseModel
from typing import Optional, List, Union


class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class Company(BaseModel):
    name: str
    address: Optional[Address] = None

class Employee(BaseModel):
    name: str
    company: Optional[Company] = None


class TextConent(BaseModel):
    type: str = "text"
    content: str

class ImageContent(BaseModel):
    type: str = "Image"
    url: str
    alt_text: str

class Article(BaseModel):
    title: str
    sections: List[Union[TextConent, ImageContent]]


class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class Organization(BaseModel):
    name: str
    head_quarter: Address
    branches: List[Address]=[]


# --- Added Instantiations and Prints ---

article_data = {
    "title": "Pydantic V2 is Here",
    "sections": [
        {"type": "text", "content": "Pydantic V2 is written in Rust."},
        {"type": "Image", "url": "http://example.com/logo.png", "alt_text": "Pydantic Logo"}
    ]
}

article = Article(**article_data)
print(article) 
# Output: title='Pydantic V2 is Here' sections=[TextConent(type='text', content='Pydantic V2 is written in Rust.'), ImageContent(type='Image', url='http://example.com/logo.png', alt_text='Pydantic Logo')]

org_data = {
    "name": "Tech Corp",
    "head_quarter": {
        "street": "123 Innovation Drive",
        "city": {
            "name": "San Francisco",
            "state": {
                "name": "California",
                "country": {
                    "name": "United States",
                    "code": "US"
                }
            }
        },
        "postal_code": "94105"
    }
}

org = Organization(**org_data)
print(f"HQ Country: {org.head_quarter.city.state.country.name}") # Output: HQ Country: United States

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Pydantic V2 Discriminated Unions
print("\n1. Discriminated Unions (Faster and Safer):")
from pydantic import Field
from typing import Literal

# Using Literal is the modern way to define the discriminator key
class VideoContent(BaseModel):
    type: Literal["video"]
    length: int

class AudioContent(BaseModel):
    type: Literal["audio"]
    bitrate: int

class MediaArticle(BaseModel):
    title: str
    # Discriminator explicitly tells Pydantic to look at 'type' to decide which model to parse.
    # This is much faster than standard Union, which tries every model sequentially!
    media: List[Union[VideoContent, AudioContent]] = Field(discriminator='type')

media_data = {"title": "Podcast", "media": [{"type": "audio", "bitrate": 128}]}
media_article = MediaArticle(**media_data)
print(f"Parsed media type: {type(media_article.media[0]).__name__}") # Output: Parsed media type: AudioContent

# Trick 2: Excluding specific nested fields during dump
print("\n2. Dumping Deeply Nested Models:")
# model_dump allows fine-grained dictionary control over what to exclude deeply within nested models!
dumped = org.model_dump(exclude={"head_quarter": {"city": {"state": {"country": {"code": True}}}}})
print(f"Dumped Country (No Code): {dumped['head_quarter']['city']['state']['country']}") 
# Output: Dumped Country (No Code): {'name': 'United States'}

# Trick 3: Forward References (Self-referencing or interdependent models)
print("\n3. Postponed Annotations (String references):")
# If models refer to each other cyclically, use strings as type hints and rebuild the model later.
class TreeNode(BaseModel):
    value: int
    left: Optional['TreeNode'] = None
    right: Optional['TreeNode'] = None

# In Pydantic V2, you must explicitly call model_rebuild() after the class is defined
# so Pydantic can resolve the string annotations.
TreeNode.model_rebuild()

tree = TreeNode(value=1, left={"value": 2})
print(f"Tree root: {tree.value}, Left child: {tree.left.value}") # Output: Tree root: 1, Left child: 2

"""
--- NOTES: Advanced Nested Models and Unions ---

1. Deeply Nested Models:
   - The filename `advance_nested_model.py` highlights complex data structures (like Organization -> Address -> City -> State -> Country).
   - Pydantic handles this seamlessly. If you pass a heavily nested JSON dictionary, Pydantic recursively instantiates every nested model automatically.
   - **Warning**: In the original file, `Address` is defined twice. In Python, the second definition shadows (overwrites) the first. Be careful with naming!

2. Union Types:
   - `Union[TextConent, ImageContent]` means the section could be *either* text or an image.
   - Pydantic attempts to match the provided data against the models from left to right. Whichever model successfully validates the data first is the one chosen.

3. Latest Python & Pydantic Features (Pydantic V2 / Python 3.10+):
   - **`|` Pipe Syntax (Python 3.10+)**: You can replace `Union[TextConent, ImageContent]` with `TextConent | ImageContent` for much cleaner, modern syntax.
   - **Discriminated Unions (Pydantic V2)**: As shown in Trick 1, if you have a massive `Union` of 20 different models, Pydantic V2 trying to validate them sequentially is slow. Adding a `discriminator` field (like `type: Literal['audio']`) tells the Rust core engine exactly which model to use instantly, making parsing extremely fast and deterministic.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if a dictionary passed to a `Union[TextConent, ImageContent]` has fields that match both models?
A1: If standard `Union` is used, Pydantic checks them from left to right. The first model that successfully validates without raising an error is instantiated, even if the second model was a "better" or more exact match. This is why "Discriminated Unions" (Trick 1) are strongly preferred.

Q2: How do you handle circular dependencies in Pydantic models (e.g., `Employee` has a `Company`, and `Company` has a list of `Employee`s)?
A2: You use Forward References. Instead of referencing the class directly, you reference it as a string (e.g., `company: 'Company'`). After both classes are defined, you must call `Employee.model_rebuild()` to allow Pydantic to resolve the string references into actual class types.

Q3: How do you access a specific field in a deeply nested Pydantic model?
A3: You use standard Python dot-notation, effectively chaining the attributes. For example: `org.head_quarter.city.state.name`.

Q4: Can I convert a deeply nested Pydantic model back into a JSON-compatible dictionary?
A4: Yes, using the `model_dump()` method (Pydantic V2) or `.dict()` (Pydantic V1). It recursively converts all nested models into standard Python dictionaries.
"""