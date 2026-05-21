def chai_customer():
    print("Welcome ! What chai would you like ?") # Output (on next(stall)): Welcome ! What chai would you like ?
    order = yield
    while True:
        print(f"Preparing: {order}") 
        order = yield

stall = chai_customer()
next(stall) # start the generator (primes it to the first yield)

stall.send("Masala Chai") # Output: Preparing: Masala Chai
stall.send("Lemon Chai") # Output: Preparing: Lemon Chai

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Auto-priming Coroutine Decorator
print("\n1. Auto-priming Decorator:")
# Generators used as coroutines always need next() called once before you can send() data.
def coroutine(func):
    def wrapper(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen) # Prime the generator automatically!
        return gen
    return wrapper

@coroutine
def auto_primed_customer():
    print("Ready for orders!") # Output: Ready for orders!
    while True:
        order = yield
        print(f"Got order: {order}")

fast_stall = auto_primed_customer()
fast_stall.send("Green Tea") # Output: Got order: Green Tea

# Trick 2: Yielding and Receiving Simultaneously
print("\n2. Yielding and Receiving Simultaneously:")
def interactive_calculator():
    result = 0
    while True:
        # Yields the current result to the caller, and waits for the next number to be sent in
        number = yield result
        result += number

calc = interactive_calculator()
print(next(calc))         # Prime it. Output: 0
print(calc.send(10))      # Sends 10, yields 10. Output: 10
print(calc.send(25))      # Sends 25, yields 35. Output: 35

# Trick 3: Throwing Exceptions into a Generator
print("\n3. Using .throw() to alter flow:")
def resilient_stall():
    while True:
        try:
            order = yield
            print(f"Brewing {order}")
        except ValueError:
            print("Sorry, invalid order received. Try again.")

r_stall = resilient_stall()
next(r_stall)
r_stall.send("Black Tea") # Output: Brewing Black Tea
r_stall.throw(ValueError) # Output: Sorry, invalid order received. Try again.

"""
--- NOTES: Generator Coroutines and `.send()` ---

1. Bidirectional Communication:
   - Standard generators strictly output data (using `yield` as a statement).
   - Python 2.5 (PEP 342) upgraded `yield` to be an *expression* that evaluates to a value. This allowed generators to act as "Coroutines" (functions that can pause, receive data, process it, and yield data back).
   - `.send(value)` resumes the generator and injects `value` right at the current `yield` expression.

2. Priming the Generator:
   - You cannot send a non-None value to a newly created generator. It must be "primed" (advanced to its first `yield` expression) by calling `next(gen)` or `gen.send(None)`.

3. Latest Python Features:
   - **Async Generators (Python 3.6+)**: You can now define `async def` functions that use `yield`. To send data into an asynchronous generator, Python provides the `.asend()` method.
   - **Performance Improvements (Python 3.12)**: Python 3.12 overhauled how execution frames are created and managed internally, making the constant pausing and resuming of heavily layered coroutines noticeably faster.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why do you get a `TypeError: can't send non-None value to a just-started generator` if you call `.send("Masala")` immediately?
A1: When a generator is just created, execution hasn't started, so there is no active `yield` expression waiting to receive a value. You must "prime" it by calling `next(gen)` (or `gen.send(None)`) to advance the execution to the first `yield`.

Q2: What is the difference between `next(gen)` and `gen.send(None)`?
A2: Functionally, there is absolutely no difference. Calling `next(gen)` is just syntactical sugar for calling `gen.send(None)`.

Q3: Can a generator yield a value AND receive a value at the exact same time?
A3: Yes! The syntax `received_val = yield output_val` does exactly this. It outputs `output_val` to the caller, pauses, and when the caller uses `.send()`, it resumes and assigns the sent data to `received_val`.

Q4: What does the `.throw()` method do on a generator?
A4: It resumes the generator but immediately raises an exception at the exact location of the `yield` expression where the generator was paused. If the generator catches it, it can continue execution; if not, the exception propagates back up to the caller.
"""