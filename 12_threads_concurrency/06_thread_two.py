import threading
import time

def prepare_chai(type_, wait_time ):
    print(f"{type_} chai: brewing...") # Output: Masala chai: brewing... (then immediately) Ginger chai: brewing...
    time.sleep(wait_time)
    print(f"{type_} chai: Ready.") # Output: Masala chai: Ready. (after 2s), then Ginger chai: Ready. (after 3s)


t1 = threading.Thread(target=prepare_chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_chai, args=("Ginger", 3))

t1.start()
t2.start()
t1.join()
t2.join()

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Passing arguments via kwargs
print("\n1. Using kwargs in Thread:")
t3 = threading.Thread(target=prepare_chai, kwargs={"type_": "Lemon", "wait_time": 1})
t3.start()
t3.join() # Output: Lemon chai: brewing... \n Lemon chai: Ready.

# Trick 2: Returning values using concurrent.futures
print("\n2. Getting Return Values (concurrent.futures):")
from concurrent.futures import ThreadPoolExecutor, as_completed

def fast_chai(type_, wait_time):
    time.sleep(wait_time)
    return f"{type_} is done in {wait_time}s!"

with ThreadPoolExecutor(max_workers=2) as executor:
    # Submit tasks and get future objects
    futures = [
        executor.submit(fast_chai, "Mint", 2),
        executor.submit(fast_chai, "Oolong", 1)
    ]
    
    # as_completed yields futures as soon as they finish, regardless of submission order
    for future in as_completed(futures):
        print(future.result()) 
        # Output: Oolong is done in 1s! (Finishes first!)
        # Output: Mint is done in 2s!

# Trick 3: Thread-local data
print("\n3. Thread-Local Storage:")
# threading.local() creates an object whose attributes are strictly local to the current thread!
thread_data = threading.local()

def set_and_print_data(val):
    thread_data.my_val = val
    time.sleep(0.5)
    print(f"Thread {threading.current_thread().name} sees: {thread_data.my_val}")

t_a = threading.Thread(target=set_and_print_data, args=("A",), name="Thread-A")
t_b = threading.Thread(target=set_and_print_data, args=("B",), name="Thread-B")
t_a.start(); t_b.start()
t_a.join(); t_b.join()
# Output:
# Thread Thread-A sees: A
# Thread Thread-B sees: B

"""
--- NOTES: Threading with Arguments and Variable Sleep Times ---

1. Passing Arguments to Threads:
   - When creating a `threading.Thread`, you CANNOT pass arguments to the target function directly like `target=prepare_chai("Masala", 2)`. This would immediately execute the function in the main thread and assign its return value to `target`.
   - Instead, you pass the function reference `target=prepare_chai`, and provide the arguments separately using the `args` tuple or `kwargs` dictionary.

2. Concurrent Wait Times:
   - This file demonstrates that thread execution is asynchronous and non-blocking. 
   - `t1` takes 2 seconds and `t2` takes 3 seconds. Because they run concurrently, the entire script finishes in 3 seconds (the longest task), not 5 seconds.

3. Latest Python Features (Python 3.11+):
   - **`asyncio` improvements (TaskGroups)**: While threading handles concurrent I/O well, modern Python often relies on `asyncio` for this exact scenario (many I/O bound waits). Python 3.11 introduced `asyncio.TaskGroup`, which provides a much cleaner, safer syntax for running multiple asynchronous tasks concurrently and handling their errors, acting as a modern alternative to raw threading for network/I/O tasks.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why do we pass arguments to `threading.Thread` using the `args` parameter instead of just calling the function in `target`?
A1: Because the `target` parameter requires a "callable" object (a function reference). If you write `target=my_func(1, 2)`, Python evaluates `my_func(1, 2)` synchronously *before* creating the thread, blocking the main thread and passing the return value of that function to the `target` parameter. Using `args=(1, 2)` tells the Thread object to execute the callable with those arguments internally *after* the new thread has been spawned.

Q2: In Trick 2, what does `concurrent.futures.as_completed` do?
A2: It takes an iterable of Future objects and yields them precisely as they complete (either successfully or by raising an exception). This allows your main program to process the results of fastest threads immediately, rather than waiting for all threads to finish in order.

Q3: What is `threading.local()` used for?
A3: Thread-local storage (`threading.local()`) is used to create variables that are globally accessible but hold completely different, isolated values for each thread. This is incredibly useful for thread safety, ensuring that one thread doesn't accidentally overwrite another thread's working data (like database connections or user session tokens) in a shared execution environment.
"""
