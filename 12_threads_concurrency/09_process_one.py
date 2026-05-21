import threading
import time

def cpu_heavy():
    print(f"Crunching some numbers...") # Output: Crunching some numbers... (x2)
    total = 0
    for i in range(10**7):
        total += i
    print("DONE ✅") # Output: DONE ✅ (x2)

start = time.time()
threads = [threading.Thread(target=cpu_heavy) for _ in range(2)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Time taken: {time.time() - start:.2f} seconds") 
# Output: Time taken: ~X.XX seconds (Notice this is often SLOWER than running them sequentially!)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Sequential Execution Comparison
print("\n1. Sequential Execution (Often faster than threading for CPU-bound tasks!):")
start_seq = time.time()
cpu_heavy()
cpu_heavy()
print(f"Sequential Time taken: {time.time() - start_seq:.2f} seconds")
# Because there is no "context switching overhead" fighting for the GIL, sequential execution wins here!

# Trick 2: Modifying the GIL Switch Interval
print("\n2. Modifying GIL Switch Interval:")
import sys
# Python forces threads to release the GIL after a certain amount of time so other threads can run.
old_interval = sys.getswitchinterval()
sys.setswitchinterval(0.001) # Force threads to switch context much more frequently
print(f"Changed GIL switch interval from {old_interval} to {sys.getswitchinterval()}")
# Running the threaded version now would likely be even SLOWER due to the massive increase in context switching!
sys.setswitchinterval(old_interval) # Restore back to default

# Trick 3: Bypassing the GIL with C-Extensions (Conceptual)
print("\n3. Bypassing the GIL natively:")
# If you were to use a library like NumPy to crunch these numbers:
# import numpy as np
# np.sum(np.arange(10**7)) 
# NumPy is written in C and explicitly RELEASES the GIL while it does heavy math, allowing true multi-threading!

"""
--- NOTES: CPU-Bound Tasks and Threading Limitations ---

1. CPU-Bound vs I/O-Bound:
   - `cpu_heavy()` is purely a **CPU-Bound** task. It relies entirely on the processor's calculation speed (adding numbers in a massive loop) and does no waiting (no sleeping, no network requests).
   - Threading is fantastic for **I/O-Bound** tasks, but it is terrible for CPU-Bound tasks in Python.

2. The Context Switching Overhead:
   - Because of the Global Interpreter Lock (GIL), only one thread can execute Python bytecode at a time.
   - When Thread 1 is running, Thread 2 is blocked. After a few milliseconds, Python forces Thread 1 to pause and gives the lock to Thread 2. 
   - This constant pausing, locking, unlocking, and resuming takes valuable CPU cycles (Context Switching Overhead), making the multi-threaded version execute slower than if you just ran the two functions back-to-back synchronously.

3. Latest Python Features (Python 3.13 No-GIL):
   - **Free-Threading (PEP 703)**: Python 3.13 introduces an experimental build that completely strips the GIL from the Python interpreter. In a Free-Threaded Python 3.13 environment, the threads in this file WOULD run on separate CPU cores simultaneously, successfully cutting the execution time in half!

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why doesn't multithreading speed up `cpu_heavy()`?
A1: Because of the Global Interpreter Lock (GIL). The GIL ensures only one thread executes Python bytecode at a time. Since `cpu_heavy()` does not perform any I/O operations (which would naturally release the GIL), the threads simply fight for the lock, adding context-switching overhead without providing any parallel execution.

Q2: What is "Context Switching"?
A2: Context switching is the process where an operating system or the Python interpreter saves the state of an active thread or process, pauses it, and loads the state of a different thread to execute it. This process is computationally expensive.

Q3: If standard threading doesn't work for CPU-bound tasks, what should you use instead?
A3: You should use the `multiprocessing` module (as seen in later files). `multiprocessing` spawns completely independent OS processes. Each process gets its own memory space and its own GIL, allowing them to run truly in parallel across multiple physical CPU cores.
"""