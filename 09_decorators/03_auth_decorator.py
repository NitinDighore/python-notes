from functools import wraps

def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only")
            return None
        else:
            return func(user_role)
    return wrapper

@require_admin
def acess_tea_inventory(role):
    print("Access granted to tea inventory")

acess_tea_inventory("user") # Output: Access denied: Admins only
acess_tea_inventory("admin") # Output: Access granted to tea inventory

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Parameterized Auth Decorators
print("\n1. Parameterized Auth (Dynamic Roles):")
# To pass arguments to a decorator itself, you need 3 levels of nested functions!
def require_permission(required_role):
    def decorator(func):
        @wraps(func)
        def wrapper(user_role, *args, **kwargs):
            if user_role != required_role:
                print(f"🚫 Denied: Requires '{required_role}' role.")
                return None
            return func(user_role, *args, **kwargs)
        return wrapper
    return decorator

@require_permission("manager")
def delete_records(role):
    print("✅ Records deleted.")

delete_records("user")    # Output: 🚫 Denied: Requires 'manager' role.
delete_records("manager") # Output: ✅ Records deleted.

# Trick 2: State-based Auth (Session Checking)
print("\n2. Session-based Auth (Hidden state):")
# In real apps, you rarely pass the role directly. The decorator checks a session/token.
current_session = {"user": "Alice", "is_authenticated": False}

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not current_session.get("is_authenticated"):
            print("🔒 Please log in first!")
            return
        return func(*args, **kwargs)
    return wrapper

@login_required
def view_dashboard():
    print(f"Welcome to your dashboard, {current_session['user']}!")

view_dashboard() # Output: 🔒 Please log in first!
current_session["is_authenticated"] = True # Simulate user logging in
view_dashboard() # Output: Welcome to your dashboard, Alice!

# Trick 3: Stacking Auth and Logging
print("\n3. Stacking Auth to log security events:")
def log_security(func):
    @wraps(func)
    def wrapper(user_role, *args, **kwargs):
        print(f"[SECURITY] User with role '{user_role}' attempting to execute '{func.__name__}'")
        return func(user_role, *args, **kwargs)
    return wrapper

# Order matters! Security log wraps the auth check, so it logs BEFORE the auth check denies access.
@log_security
@require_admin
def view_secrets(role):
    print("Viewing top secret tea recipes...")

view_secrets("user") 
# Output: 
# [SECURITY] User with role 'user' attempting to execute 'view_secrets'
# Access denied: Admins only

"""
--- NOTES: Authorization and State Decorators ---

1. Separation of Concerns (Security):
   - The filename `03_auth_decorator.py` highlights using decorators as "Guards".
   - Security checks (Authentication = "Are you logged in?", Authorization = "Do you have permission?") clutter up business logic if placed directly inside every function.
   - Decorators extract this security logic. If you ever need to change how permissions are validated, you only update the single `@require_admin` decorator, and every protected endpoint in your app is instantly updated.

2. Latest Python Features:
   - **`typing.ParamSpec` (Python 3.10+)**: When creating complex parameterized decorators (like Trick 1), statically hinting them so IDEs know the decorated function's exact signature used to be nearly impossible. `ParamSpec` allows you to explicitly map the `*args` and `**kwargs` types from the `wrapper` back to the original `func`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why do you need 3 levels of nested functions to make a decorator that accepts arguments (like `@require_permission("manager")`)?
A1: Because the `@` syntax immediately invokes the decorator with the argument provided (e.g., `"manager"`). The outermost function is just a "factory" that receives this argument and returns the *actual* decorator. The middle function is the actual decorator that receives the target function. The innermost function is the wrapper that executes the logic.

Q2: What happens if I stack decorators in the wrong order, for example: `@require_admin` on top of `@log_security`?
A2: Decorators execute from the bottom up (inside-out). If `@require_admin` is on top, it wraps the logger. When a "user" calls the function, `@require_admin` triggers first, prints "Access denied", and returns `None`. The inner `@log_security` decorator will NEVER be executed. This is a common bug where unauthorized access attempts fail to be logged.

Q3: How do frameworks like Flask or FastAPI know who is currently logged in if we don't pass the `user_role` as an argument to the function?
A3: They use "Context Variables" (like Flask's `request` or `session` objects) which are globally accessible proxies bound to the current execution thread or async context. The decorator imports and checks this context object directly, similar to how Trick 2 checks the `current_session` dictionary.
"""