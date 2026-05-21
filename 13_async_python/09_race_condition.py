import threading

chai_stock = 0

def restock():
    global chai_stock
    for _ in range(100000):
        chai_stock += 1

threads = [ threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print("Chai stock: ", chai_stock) 
# Output: Chai stock: 134562 (Will be a random, corrupted number less than 200000!)

print("\n--- TRICK CODING EXAMPLES ---")

import asyncio

# Trick 1: The Asyncio "Safe" Increment
print("\n1. Asyncio without 'await' is natively thread-safe:")
# Because asyncio runs on a single thread, it ONLY context-switches at an `await` statement.
# A synchronous loop inside an async function will NEVER be interrupted by another coroutine!
async_stock = 0

async def async_safe_restock():
    global async_stock
    for _ in range(100000):
        async_stock += 1 # No `await` here, so no other coroutine can steal control!

async def run_safe_async():
    await asyncio.gather(async_safe_restock(), async_safe_restock())
    print(f"Safe Async Stock: {async_stock} (Perfect 200000!)") # Output: Safe Async Stock: 200000 (Perfect 200000!)

asyncio.run(run_safe_async())

# Trick 2: The Asyncio Race Condition (The 'await' trap)
print("\n2. Inducing a Race Condition in Asyncio:")
# If you put an `await` inside a critical section, you yield control to the Event Loop,
# allowing other coroutines to jump in and corrupt your shared state!
unsafe_async_stock = 0

async def async_unsafe_restock():
    global unsafe_async_stock
    for _ in range(100):
        temp = unsafe_async_stock
        await asyncio.sleep(0) # ⚠️ Yields control! Another task jumps in and reads the old temp!
        unsafe_async_stock = temp + 1

async def run_unsafe_async():
    await asyncio.gather(*[async_unsafe_restock() for _ in range(10)])
    print(f"Unsafe Async Stock: {unsafe_async_stock} (Corrupted!)") # Output: Unsafe Async Stock: ~100 (Expected 1000)

asyncio.run(run_unsafe_async())

# Trick 3: Fixing Async Race Conditions with asyncio.Lock
print("\n3. Fixing Async Races with asyncio.Lock:")
locked_async_stock = 0
async_lock = asyncio.Lock()

async def async_locked_restock():
    global locked_async_stock
    for _ in range(100):
        async with async_lock: # Safely locks the critical section
            temp = locked_async_stock
            await asyncio.sleep(0)
            locked_async_stock = temp + 1

async def run_locked_async():
    await asyncio.gather(*[async_locked_restock() for _ in range(10)])
    print(f"Locked Async Stock: {locked_async_stock} (Safe!)") # Output: Locked Async Stock: 1000 (Safe!)

asyncio.run(run_locked_async())

"""
--- NOTES: Race Conditions (Threading vs Asyncio) ---

1. Threading Race Conditions:
   - The original code above demonstrates a classic race condition. The Operating System (and Python's GIL) preemptively pauses threads at random intervals. If Thread A is paused halfway through `chai_stock += 1`, Thread B will overwrite Thread A's progress, causing massive data loss.

2. Asyncio Cooperative Multitasking:
   - `asyncio` works differently. It is "cooperative." A coroutine will NEVER be interrupted by another coroutine unless it explicitly hits an `await` keyword.
   - This means simple blocking operations (like standard math or list appends) are inherently thread-safe in `asyncio` because the event loop cannot pause the function halfway through.
   - However, if your shared state modification spans across an `await` call (like fetching a value from a database, `await`ing the response, and writing it back), you MUST use an `asyncio.Lock()`.

3. Latest Python Features (Python 3.13 No-GIL):
   - **Free-Threading Implications**: In Python 3.13 with the GIL disabled, standard threading race conditions become far more frequent and dangerous. Operations that were "accidentally" safe in older Python versions due to the GIL protecting single bytecode instructions will now corrupt memory if not properly guarded with a `threading.Lock()`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Is `asyncio` immune to race conditions?
A1: No. While `asyncio` protects against preemptive OS-level context switching, logical race conditions can absolutely still occur if shared state is modified across an `await` boundary. If Task A reads a value, `await`s an I/O operation, and then writes the value back, Task B might have modified that value during the `await` period.

Q2: Why is `chai_stock += 1` not thread-safe?
A2: Because `+= 1` is not an atomic operation. Under the hood, Python compiles it to three distinct bytecode instructions: `LOAD_GLOBAL`, `INPLACE_ADD`, and `STORE_GLOBAL`. A thread can be preemptively paused by the OS between any of these steps, allowing another thread to read stale data.

Q3: How do you fix the threading race condition in the original code?
A3: By wrapping the `chai_stock += 1` operation inside a `with threading.Lock():` context manager. This ensures only one thread can execute the read-modify-write cycle at a time.
"""