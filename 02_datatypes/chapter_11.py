import arrow

brewing_time = arrow.utcnow()
print(f"Brewing time UTC: {brewing_time}") # Output example: Brewing time UTC: 2026-05-21T04:27:00.000000+00:00

rome_time = brewing_time.to("Europe/Rome")
print(f"Brewing time in Rome: {rome_time}") # Output example: Brewing time in Rome: 2026-05-21T06:27:00.000000+02:00

from collections import namedtuple
chaiProfile = namedtuple("chaiProfile", ["flavor", "aroma"])

my_chai = chaiProfile(flavor="spicy", aroma="cardamom")
print(f"My chai profile: {my_chai}") # Output: My chai profile: chaiProfile(flavor='spicy', aroma='cardamom')
print(f"Flavor: {my_chai.flavor}") # Output: Flavor: spicy
print(f"Aroma: {my_chai[1]}") # Output: Aroma: cardamom

"""
--- NOTES: Third-Party Libraries (Arrow) and namedtuple ---

1. Third-Party Library: `arrow`
   - `arrow` is a popular third-party Python library for creating, manipulating, formatting, and converting dates, times, and timestamps.
   - It is designed to be much simpler and more human-friendly than Python's built-in `datetime` module.
   - Key features include timezone conversions (like `.to("Europe/Rome")`), relative time formatting (e.g., "an hour ago"), and easy parsing.
   - Note: Since `arrow` is a third-party package, it must be installed via `pip install arrow` before use.

2. Built-in `collections.namedtuple`
   - `namedtuple` is a factory function from Python's built-in `collections` module that creates subclasses of `tuple`.
   - It allows you to access elements using named attributes (e.g., `my_chai.flavor`) as well as standard integer indices (e.g., `my_chai[1]`), making the code much more readable.
   - Like standard tuples, namedtuples are immutable.

3. Methods used with `namedtuple`:
   - Instantiation: `obj = ClassName(field1=val1, field2=val2)`
   - Attribute Access: `obj.field1` or `obj[0]`
   - `obj._make(iterable)`: A class method that makes a new instance from an existing sequence or iterable.
   - `obj._asdict()`: Returns a new `dict` mapping field names to their corresponding values.
   - `obj._replace(**kwargs)`: Returns a new instance of the named tuple replacing specified fields with new values (since tuples are immutable, it doesn't modify the original).
   - `obj._fields`: A tuple of strings listing the field names.
   
--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why would you use a `namedtuple` instead of a regular dictionary or a custom class?
A1: A `namedtuple` is more memory-efficient than a standard dictionary (it doesn't have a per-instance `__dict__`). Compared to a custom class, it requires significantly less boilerplate code. It also retains the immutability and sequence behavior of a regular tuple while adding the readability of named fields.

Q2: Since a `namedtuple` is immutable, how can you change one of its values?
A2: Because it is immutable, you cannot change a value in place (e.g., `my_chai.flavor = "sweet"` will raise an `AttributeError`). Instead, you must create a new instance with the updated value. The `_replace()` method is specifically designed for this: `updated_chai = my_chai._replace(flavor="sweet")`.

Q3: What does the leading underscore in methods like `_asdict()` or `_replace()` mean in a `namedtuple`?
A3: In standard Python convention, a leading underscore usually indicates a "private" or "internal" method. However, for `namedtuple`, the underscores are used to prevent naming conflicts with user-defined field names. They are part of the public API and are meant to be used safely.

Q4: Are `namedtuple` instances hashable?
A4: Yes, just like regular tuples, `namedtuple` instances are hashable as long as all of their field values are also hashable. This means they can be used as keys in a dictionary or added to a set.
"""