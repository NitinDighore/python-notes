import threading

counter = 0
lock = threading.Lock()

def increament():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increament) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}") # Output: Final counter: 1000000

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The Race Condition (What happens WITHOUT a lock?)
print("\n1. Race Condition (No Lock):")
unsafe_counter = 0
def unsafe_increment():
    global unsafe_counter
    for _ in range(100000):
        unsafe_counter += 1 # Not thread-safe!

unsafe_threads = [threading.Thread(target=unsafe_increment) for _ in range(10)]
[t.start() for t in unsafe_threads]
[t.join() for t in unsafe_threads]
# Because multiple threads overwrite each other, the result is wildly unpredictable and less than 1,000,000!
print(f"Unsafe counter expected 1000000, got: {unsafe_counter} (Data corruption!)")

# Trick 2: Manual Lock Management and Timeouts
print("\n2. Lock Timeouts to prevent Deadlocks:")
# Instead of 'with lock:', you can acquire and release manually.
# The timeout prevents the thread from waiting infinitely if the lock is held elsewhere.
def timeout_task():
    if lock.acquire(timeout=0.5):
        try:
            print("Lock acquired safely!")
        finally:
            lock.release() # ALWAYS put release() in a finally block if doing it manually!
    else:
        print("Could not acquire lock within 0.5 seconds!")

timeout_task() # Output: Lock acquired safely!

# Trick 3: Reentrant Locks (RLock)
print("\n3. Reentrant Locks (RLock):")
rlock = threading.RLock()
# A standard Lock blocks if the SAME thread tries to acquire it twice.
# An RLock allows the same thread to acquire the lock multiple times (useful for recursive functions).
def recursive_task(n):
    with rlock: 
        if n > 0:
            print(f"Acquired RLock at depth {n}")
            recursive_task(n - 1)

recursive_task(2)
# Output: 
# Acquired RLock at depth 2
# Acquired RLock at depth 1

"""
--- NOTES: Race Conditions and `threading.Lock` ---

1. What is a Race Condition?
   - A race condition occurs when two or more threads attempt to read and write to shared data at the exact same time, leading to unpredictable and corrupted results.
   - Why isn't `counter += 1` safe? In Python bytecode, this is actually three steps: 1) Read the current value of `counter`, 2) Add 1, 3) Write the new value back. If Thread A and Thread B both read the value as `5`, they both add 1 and both write back `6`, effectively deleting one of the increments.

2. The Mutex (`threading.Lock`):
   - A Lock (or Mutex - Mutual Exclusion) is a synchronization primitive. 
   - Only ONE thread can "acquire" the lock at a time. If Thread A has the lock, Thread B will pause and wait until Thread A releases it before moving forward.
   - Using the `with lock:` context manager is highly recommended because it absolutely guarantees the lock will be released even if an exception crashes the code inside the block.

3. Latest Python Features (Python 3.13 No-GIL Implications):
   - With the experimental removal of the Global Interpreter Lock (GIL) in Python 3.13 (Free-Threading), locks become **exponentially more critical**. 
   - Historically, the GIL protected many basic dictionary and list operations from corrupting the CPython internals. Without the GIL, true multi-core parallel execution is possible, meaning data races will happen far more frequently if you do not strictly enforce your own `threading.Lock()` wrappers around shared state!

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between a `Lock` and an `RLock`?
A1: A standard `Lock` can only be acquired once. If the thread holding the lock tries to acquire it again, it will block itself, causing a Deadlock. An `RLock` (Reentrant Lock) allows the thread that currently owns the lock to acquire it multiple times without blocking (it keeps an internal counter of how many times it was acquired, and must be released that many times).

Q2: What is a Deadlock?
A2: A deadlock happens when two or more threads are permanently blocked, waiting on each other to release locks. For example, Thread A holds Lock 1 and waits for Lock 2. Thread B holds Lock 2 and waits for Lock 1. Neither can proceed.

Q3: If the GIL only lets one thread run Python bytecode at a time, why do we even need `threading.Lock`?
A3: Because the GIL can force a thread context-switch *between* bytecodes. An operation like `counter += 1` consists of multiple bytecode instructions. The GIL might pause a thread right after it reads the value but before it writes it back, allowing another thread to jump in and read the old value. A `threading.Lock` guarantees an entire block of code finishes atomically without interference.
"""