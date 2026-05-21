from typing import List, Optional
from pydantic import BaseModel

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None

Comment.model_rebuild()


comment = Comment(
    id= 1,
    content="First comment",
    replies=[
        Comment(id=2, content="reply 1"),
        Comment(id=3, content="reply 2", replies=[
            Comment(id=4, content="nested reply")
        ])
    ]
)

print(f"Root comment: {comment.content}") # Output: Root comment: First comment
print(f"Deeply nested reply: {comment.replies[1].replies[0].content}") # Output: Deeply nested reply: nested reply

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Circular Dependencies (Multiple Models)
print("\n1. Circular Dependencies (Mutually Referencing Models):")
# When two models refer to each other, you MUST use string forward references for the one defined first.
class Team(BaseModel):
    name: str
    members: List['Employee'] = [] # Forward reference to Employee

class Employee(BaseModel):
    name: str
    # Team is already defined above, so we don't strictly need quotes here, 
    # but it is good practice in circular structures.
    team: Optional[Team] = None 

# Resolves the 'Employee' string reference inside Team now that Employee exists
Team.model_rebuild() 

eng_team = Team(name="Engineering")
emp1 = Employee(name="Alice", team=eng_team)
eng_team.members.append(emp1)
print(f"Team has {len(eng_team.members)} member: {eng_team.members[0].name}") # Output: Team has 1 member: Alice

# Trick 2: Parsing deeply nested self-referencing dictionaries
print("\n2. Parsing Deeply Nested Dictionaries:")
tree_data = {
    "id": 10,
    "content": "Root",
    "replies": [
        {"id": 11, "content": "Child 1"},
        {"id": 12, "content": "Child 2", "replies": [{"id": 13, "content": "Grandchild"}]}
    ]
}
# Pydantic recursively instantiates the Comment objects all the way down the tree!
tree = Comment.model_validate(tree_data)
print(f"Parsed Grandchild: {tree.replies[1].replies[0].content}") # Output: Parsed Grandchild: Grandchild

# Trick 3: from __future__ import annotations (Python 3.7+)
print("\n3. Dropping quotes with __future__ annotations:")
# If you place `from __future__ import annotations` at the absolute top of your file,
# you can write `replies: Optional[List[Comment]] = None` WITHOUT string quotes ('Comment'),
# even before the class is fully evaluated! Python treats all annotations as strings automatically.
print("Use `from __future__ import annotations` to avoid string quotes in self-references!")

"""
--- NOTES: Self-Referencing Models and Circular Dependencies ---

1. What are Forward References?
   - In Python, code is executed from top to bottom. If a class refers to itself inside its own body (like `Comment` referring to `Comment`), Python usually throws a `NameError` because the class isn't fully constructed in memory yet.
   - To fix this, we use a "Forward Reference" by wrapping the class name in a string (`'Comment'`).

2. `model_rebuild()` in Pydantic V2:
   - In Pydantic V1, this method was called `update_forward_refs()`. 
   - Pydantic needs to build its core validation schemas. When it sees a string like `'Comment'`, it doesn't know what that is initially. Calling `Comment.model_rebuild()` tells Pydantic to scan the local namespace, find the fully constructed `Comment` class, and replace the string references with the actual class type so validation can execute properly.

3. Latest Python Features (Python 3.10+ & PEP 563):
   - **`from __future__ import annotations`**: This feature (introduced in Python 3.7 and heavily used in modern codebases) changes how Python parses type hints. It automatically evaluates all type hints as strings under the hood. This means you never have to manually wrap your self-referencing classes in quotes again. Pydantic fully supports this, making schemas much cleaner.
   - **Modern Union Syntax**: Instead of `Optional[List['Comment']]`, Python 3.10+ allows the highly readable `list['Comment'] | None`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why do we have to put `'Comment'` in string quotes inside the `Comment` class definition?
A1: Because at the exact moment Python parses that line of code, the `Comment` class has not finished being created yet. If you omit the quotes, Python raises a `NameError`. The quotes tell Python it's a string literal to be evaluated later (a Forward Reference).

Q2: What is the exact purpose of `Comment.model_rebuild()`?
A2: It instructs Pydantic to traverse the model's fields, look for any forward string references (like `'Comment'`), and resolve them against the current global namespace into actual Python types, thus completing the internal Rust validation schema.

Q3: If Model A contains a List of Model B, and Model B contains an instance of Model A, how do you resolve this circular dependency in Pydantic?
A3: You define Model A first with a string forward reference to `'Model B'`. Then you define Model B, which can reference `Model A` directly (since A is already fully defined). Finally, you explicitly call `ModelA.model_rebuild()` so it resolves the string reference to the now-existing `Model B`.
"""