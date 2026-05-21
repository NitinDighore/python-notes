import threading
import time

def boil_milk():
    print(f"Boiling milk...") # Output: Boiling milk...
    time.sleep(2)
    print(f"Milk Boiled...") # Output: Milk Boiled... (approx 2s later)

def toast_bun():
    print(f"Toasting bun...") # Output: Toasting bun... (prints immediately after Boiling milk...)
    time.sleep(3)
    print(f"Done with bun toast...") # Output: Done with bun toast... (approx 3s later)
    
start = time.time()

t1 = threading.Thread(target=boil_milk)
t2 = threading.Thread(target=toast_bun)

t1.start()
t2.start()
t1.join()
t2.join()

end = time.time()

print(f"Breakfast is ready in {end - start:.2f} seconds") # Output: Breakfast is ready in ~3.00 seconds

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Subclassing threading.Thread
print("\n1. Subclassing Thread for custom behavior:")
class CoffeeMachine(threading.Thread):
    def __init__(self, coffee_type):
        super().__init__() # Must call the parent __init__!
        self.coffee_type = coffee_type
        
    def run(self):
        # The run() method is automatically executed when you call .start()
        print(f"Brewing {self.coffee_type}...")
        time.sleep(1)
        print(f"{self.coffee_type} is ready!")

machine = CoffeeMachine("Espresso")
machine.start()
machine.join() # Output: Brewing Espresso... \n Espresso is ready!

# Trick 2: Active Thread Count & Enumeration
print("\n2. Thread Introspection:")
# You can see how many threads are currently alive in the background
def quick_task(): time.sleep(0.5)
threading.Thread(target=quick_task).start()
print(f"Active threads right now: {threading.active_count()}")
print(f"List of active threads: {threading.enumerate()}")

# Trick 3: Using threading.Event for Synchronization
print("\n3. Synchronization with threading.Event:")
# Events are a clean way for one thread to signal to another thread that something has happened
water_boiled = threading.Event()

def heat_water():
    print("Heating water...")
    time.sleep(1)
    print("Water is hot!")
    water_boiled.set() # Signals all waiting threads

def make_tea():
    print("Waiting for water to boil...")
    water_boiled.wait() # Pauses this thread until .set() is called
    print("Adding tea leaves to hot water!")

t_heat = threading.Thread(target=heat_water)
t_tea = threading.Thread(target=make_tea)

t_tea.start()
t_heat.start()

t_tea.join()
t_heat.join()

"""
--- NOTES: Basic Threading (I/O Bound Tasks) ---

1. Core Concept:
   - This file (`05_thread_one.py`) demonstrates the primary superpower of Python threading: Concurrent I/O operations.
   - `time.sleep()` simulates an "I/O-bound task" (e.g., waiting for a file to read, an API to respond, or milk to boil).
   - If executed sequentially, this code would take 2 + 3 = 5 seconds. Because they run concurrently, the overall time is only bounded by the longest task (~3 seconds).

2. How it Bypasses the GIL:
   - Python's Global Interpreter Lock (GIL) prevents threads from executing Python bytecodes at the same time. However, whenever a thread performs an I/O operation (like sleeping or making a network request), it automatically RELEASES the GIL, allowing other threads to run freely while it waits.

3. Latest Python Features:
   - **Free-Threading / No-GIL (Python 3.13+)**: PEP 703 provides an experimental build of Python that entirely removes the GIL. While this file benefits from threading even with the GIL (because it's I/O bound), Free-Threading ensures that even heavy mathematical operations within threads would execute in true parallel on multi-core systems.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why did the breakfast take ~3 seconds instead of ~5 seconds?
A1: Because the tasks (`boil_milk` and `toast_bun`) were executed concurrently using threads. While the first thread was blocked (sleeping/waiting), it released the GIL, allowing the second thread to start immediately. The total execution time becomes roughly equal to the duration of the longest individual task.

Q2: What is the difference between `.run()` and `.start()` on a Thread object?
A2: Calling `.start()` creates a new OS-level thread and then invokes the `.run()` method inside that new thread. If you explicitly call `.run()` manually (e.g., `t1.run()`), it will NOT create a new thread; it will simply execute the function synchronously in the current main thread, completely defeating the purpose of threading.

Q3: What does `threading.Event()` do?
A3: An Event is a simple synchronization primitive. It acts as a boolean flag (initially False). One thread can call `event.wait()` to pause its execution until another thread calls `event.set()` to flip the flag to True. It's an elegant way to coordinate tasks that depend on each other without using messy `while` loops checking boolean variables.
"""