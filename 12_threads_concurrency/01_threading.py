import threading
import time

def take_orders():
    for i in range(1, 4):
        print(f"Taking order for #{i}") 
        # Output order: #1 instantly, #2 at 2s, #3 at 4s
        time.sleep(2)

def brew_chai():
    for i in range(1, 4):
        print(f"Brewing chai for #{i}") 
        # Output order: #1 instantly, #2 at 3s, #3 at 6s
        time.sleep(3)
        
# create threads
order_thread = threading.Thread(target=take_orders)
brew_thread = threading.Thread(target=brew_chai)

order_thread.start()
brew_thread.start()

# wait for both to finish
order_thread.join()
brew_thread.join()

print(f"All orders taken and chai brewed") # Output at ~9s: All orders taken and chai brewed

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Passing Arguments to Threads
print("\n1. Passing arguments:")
def serve_specific_chai(flavor):
    print(f"Serving {flavor} chai...")
# Must pass args as a tuple! Note the trailing comma: (flavor,)
t1 = threading.Thread(target=serve_specific_chai, args=("Masala",))
t1.start()
t1.join() # Output: Serving Masala chai...

# Trick 2: Daemon Threads (Background tasks)
print("\n2. Daemon Threads:")
def background_cleanup():
    while True:
        time.sleep(1)
        # This loop runs forever, but won't prevent the script from exiting
daemon_thread = threading.Thread(target=background_cleanup, daemon=True)
daemon_thread.start()
print("Daemon thread started. It will die silently when the main program finishes.")

# Trick 3: Delayed Execution with Timer
print("\n3. Delayed Execution (threading.Timer):")
def delayed_hello():
    print("Hello from the future (0.1 seconds later)!")
# Timer inherits from Thread and schedules execution without blocking the main program
timer = threading.Timer(0.1, delayed_hello)
timer.start()
timer.join()

# Trick 4: Modern Threading using ThreadPoolExecutor (Python 3.2+)
print("\n4. ThreadPoolExecutor (Best Practice):")
from concurrent.futures import ThreadPoolExecutor
def brew_cup(cup_id):
    return f"Cup {cup_id} is ready!"

# The 'with' statement handles pool shutdown and joining automatically
with ThreadPoolExecutor(max_workers=3) as executor:
    # .map() applies the function to the iterable, distributing tasks across threads
    results = executor.map(brew_cup, [101, 102, 103])
    for res in results:
        print(res) # Output: Cup 101 is ready! \n Cup 102 is ready! \n Cup 103 is ready!

"""
--- NOTES: Threading and Concurrency ---

1. What is Threading?
   - Threading is a concurrent execution model. It allows multiple threads (smaller units of a process) to run concurrently within the same process, sharing the same memory space.
   - The `12_threads_concurrency` folder explores how to execute tasks simultaneously. 
   - Threading is heavily favored for I/O-bound tasks (e.g., waiting for network responses, reading files, or `time.sleep()`).
   - Because threads run simultaneously in the background, we use `thread.join()` to tell the main program to wait until the thread completes before moving forward.

2. The GIL (Global Interpreter Lock):
   - Python's standard implementation (CPython) has a mutex called the GIL.
   - The GIL ensures that only one thread executes Python bytecode at a time.
   - This means that standard Python threading does NOT provide true parallel execution for CPU-bound tasks (like heavy math loops). For CPU-heavy tasks, `multiprocessing` is required.

3. Latest Python Features (Python 3.12 & 3.13):
   - **Per-Interpreter GIL (Python 3.12)**: PEP 684 introduced sub-interpreters with their own separate GILs, allowing much better parallelism for C-extension developers.
   - **Free-Threading / No-GIL (Python 3.13+)**: PEP 703 is monumental! Python 3.13 includes an experimental build flag to completely remove the GIL, finally paving the way for true multi-threaded parallelism for CPU-bound Python code without relying on multiprocessing.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between Concurrency and Parallelism?
A1: Concurrency is about *dealing* with multiple things at once (interleaving tasks, like taking an order while tea is brewing). Parallelism is about *doing* multiple things at the exact same physical time (requires multiple CPU cores). Standard Python threading achieves concurrency, not parallelism, due to the GIL.

Q2: What does the `.join()` method do?
A2: It blocks the execution of the calling thread (usually the main thread) until the thread whose `join()` method is called is completely terminated. If you don't call `.join()`, the main program might finish and exit before the threads complete their work.

Q3: What is a Daemon thread?
A3: A daemon thread is a background thread that does not prevent the program from exiting. When all non-daemon threads (like the main execution thread) finish, Python automatically terminates all alive daemon threads and shuts down.

Q4: Why do modern Python developers use `concurrent.futures.ThreadPoolExecutor` instead of raw `threading.Thread`?
A4: `ThreadPoolExecutor` provides a higher-level, robust API. It manages a reusable pool of worker threads, drastically reducing the overhead of spinning up and tearing down threads manually. It also natively returns values from threads via `Futures` objects, which is notoriously difficult to do cleanly with raw `threading.Thread`.
"""