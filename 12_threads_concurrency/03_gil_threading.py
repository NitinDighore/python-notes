import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...") 
    # Output: Barista-1 started brewing... (followed immediately by Barista-2)
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"{threading.current_thread().name} finished brewing...") 
    # Output: Barista-1 finished brewing... (followed by Barista-2)

thread1 =threading.Thread(target=brew_chai, name="Barista-1")
thread2 = threading.Thread(target=brew_chai, name="Barista-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"total time taken: {end - start:.2f} seconds") 
# Output: total time taken: ~X.XX seconds (Notice it is NOT faster than running sequentially!)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The I/O Bound GIL Drop
print("\n1. I/O tasks release the GIL automatically:")
def io_bound_task():
    # time.sleep() simulates an I/O operation (like a network request or reading a file).
    # Python explicitly RELEASES the GIL during I/O, allowing true concurrency here!
    time.sleep(1)

t_io_start = time.time()
t_io1, t_io2 = threading.Thread(target=io_bound_task), threading.Thread(target=io_bound_task)
t_io1.start(); t_io2.start()
t_io1.join(); t_io2.join()
# Runs in ~1 second total, not 2!
print(f"I/O Bound time: {time.time() - t_io_start:.2f} seconds") # Output: I/O Bound time: 1.00 seconds

# Trick 2: Checking the GIL Switch Interval
print("\n2. Checking GIL Switch Interval:")
import sys
# How long does a thread hold the GIL before Python forces it to let another thread run?
# Default is usually 0.005 seconds (5 milliseconds) in modern Python.
print(f"Current GIL switch interval: {sys.getswitchinterval()} seconds")

# Trick 3: Demonstrating Context Switching Overhead (Conceptual)
print("\n3. Context Switching Overhead:")
# If you run the 100M loop sequentially (without threads), it often finishes FASTER
# than running it in 2 threads. The threads waste CPU time constantly fighting over the GIL!
# sequential_start = time.time()
# brew_chai()
# brew_chai()
# print(f"Sequential time: {time.time() - sequential_start:.2f} seconds")

"""
--- NOTES: The Global Interpreter Lock (GIL) ---

1. What is the GIL?
   - The GIL (Global Interpreter Lock) is a mutex lock used in CPython (the standard Python implementation).
   - It explicitly prevents multiple native threads from executing Python bytecodes at the exact same time.
   - This was originally implemented to protect Python's internal memory management (Reference Counting) from race conditions.

2. The Problem with the GIL (Demonstrated Above):
   - The `brew_chai()` function contains a `for` loop that runs 100 million times. This is purely a "CPU-bound" mathematical task.
   - Because of the GIL, `Barista-1` and `Barista-2` cannot calculate numbers at the same time. They constantly context-switch, passing the lock back and forth. 
   - Result: Multi-threading for CPU-bound tasks in standard Python does absolutely nothing to speed up the code.

3. Latest Python Features (Python 3.12 & 3.13):
   - **Per-Interpreter GIL (Python 3.12)**: PEP 684 introduced sub-interpreters with their own separate GILs, allowing much better parallelism for C-extension developers.
   - **Free-Threading / No-GIL (Python 3.13+)**: PEP 703 is monumental! Python 3.13 includes an experimental build flag (`--disable-gil`) to completely remove the GIL. If you run this exact file on a Free-Threaded build of Python 3.13+, it WILL finish roughly 2x faster, successfully utilizing multiple CPU cores!

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the Global Interpreter Lock (GIL)?
A1: The GIL is a mutex in standard Python (CPython) that allows only one thread to execute Python bytecode at a time, effectively preventing true parallel execution of CPU-bound tasks.

Q2: If the GIL prevents multiple threads from running at once, why is `threading` still so popular in Python?
A2: Because the GIL is automatically released during "I/O-bound" operations (like network requests, database queries, reading files, or `time.sleep()`). Threading provides massive speedups for I/O-bound programs because multiple threads can wait for external responses concurrently.

Q3: Why did adding a second thread to the `100_000_000` loop (CPU-bound) make the overall program slightly slower?
A3: Because of "Context Switching Overhead". The threads cannot run in parallel. Instead, the OS and Python constantly pause one thread, acquire/release the lock, and resume the other. This fighting over the lock takes time, making threaded CPU-bound math slower than running it synchronously.

Q4: How can you bypass the GIL to achieve true parallelism for CPU-bound tasks?
A4: Prior to Python 3.13's experimental No-GIL build, the main ways were to use the `multiprocessing` module (which spawns entirely separate OS processes, each with its own memory and own GIL) or to write performance-critical code in C-extensions (like NumPy) which can release the GIL during execution.
"""