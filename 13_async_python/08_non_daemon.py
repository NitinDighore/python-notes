import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...") # Output: Monitoring tea temperature... (Prints continuously every 2s)
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp)
# t.start() # Commented out so the trick examples below can run without hanging your console!

print("Main program done") # Output: Main program done (But the script DOES NOT exit if t.start() was called!)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Finding out WHY your program is hanging
print("\n1. Inspecting active threads:")
# If your script refuses to exit, you can print all alive threads to find the culprit
t.start() # We start the thread now
alive_threads = threading.enumerate()
print(f"Alive threads preventing exit: {[th.name for th in alive_threads]}") 
# Output: Alive threads preventing exit: ['MainThread', 'Thread-1 (monitor_tea_temp)']

# Trick 2: Joining with a Timeout
print("\n2. Joining with a Timeout:")
# You can tell the main thread to wait for a background thread, but give up if it takes too long
print("Waiting for monitor thread for exactly 3 seconds...")
t.join(timeout=3.0)
print(f"Is thread still alive after timeout? {t.is_alive()}") # Output: Is thread still alive after timeout? True

# Trick 3: Forcefully Killing the Interpreter (The Nuclear Option)
print("\n3. Forcefully exiting the Python process:")
import os
# Since 't' is a non-daemon thread in an infinite loop, a normal `sys.exit()` or finishing the script
# will NOT kill it. Python will hang forever waiting for it.
# os._exit() tells the Operating System to violently kill the process immediately, bypassing Python's thread-waiting logic.
print("Executing os._exit(0) to forcefully kill the rogue non-daemon thread...")
os._exit(0) 

"""
--- NOTES: Non-Daemon Threads and Thread Lifecycles ---

1. What is a Non-Daemon Thread?
   - By default, whenever you create a `threading.Thread`, it is a "non-daemon" thread (specifically, it inherits the daemon status of the thread that spawned it).
   - The Python interpreter has a strict rule: **It will not shut down until ALL non-daemon threads have finished executing.**
   - Because `monitor_tea_temp` contains a `while True:` infinite loop, the thread will never finish. Therefore, your Python script will hang forever, even after printing "Main program done".

2. Why is this file in the `13_async_python` folder?
   - It contrasts the threading model with `asyncio`. In pure `asyncio`, if the main event loop finishes or `asyncio.run()` completes, all pending background tasks are automatically discarded and the program exits cleanly. Threading requires much more manual lifecycle management.

3. Latest Python Features:
   - **`asyncio.TaskGroup` (Python 3.11+)**: In modern async programming, `TaskGroup` strictly manages the lifecycles of background tasks, ensuring no task "goes rogue" and hangs the system indefinitely like a forgotten non-daemon thread can.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why doesn't the program exit after it prints "Main program done"?
A1: Because the background thread `t` is running an infinite loop and it was created as a non-daemon thread (the default). Python's garbage collector and shutdown sequence will wait indefinitely for all non-daemon threads to return before exiting.

Q2: Can I forcefully kill or terminate a `threading.Thread` object in Python?
A2: No. Python's `threading` module does not provide a `.kill()`, `.stop()`, or `.terminate()` method. Forcing a thread to die could interrupt a lock release or a file write, leading to corrupted data or deadlocks. You must signal the thread to exit gracefully (e.g., using `threading.Event`).

Q3: What is the difference between `sys.exit()` and `os._exit()`?
A3: `sys.exit()` raises a `SystemExit` exception, which allows `finally` blocks to run, objects to be cleaned up, and causes the main thread to wait for non-daemon threads. `os._exit()` skips all Python-level cleanup and asks the Operating System to immediately abort the entire process.
"""