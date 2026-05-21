import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...") # Output: Monitoring tea temperature... (Prints maybe once before abrupt exit)
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done") # Output: Main program done (Program immediately exits, killing the daemon thread)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The Danger of Daemon Threads (Abrupt Termination)
print("\n1. Why Daemon threads are unsafe for I/O:")
def dangerous_daemon():
    print("Daemon: Opening a file...")
    time.sleep(1)
    # If the main program ends right here, this thread is KILLED instantly!
    # The file remains open/corrupted because the finally block or file.close() never runs.
    print("Daemon: Writing to file...") 

d_t = threading.Thread(target=dangerous_daemon, daemon=True)
d_t.start()

# Trick 2: Graceful Shutdown (The preferred alternative to Daemon threads)
print("\n2. Graceful Shutdown with threading.Event():")
stop_event = threading.Event()

def safe_monitor():
    # Instead of an infinite `while True`, we check the event flag!
    while not stop_event.is_set():
        print("Safe Monitor: Checking temp...")
        # Wait acts like time.sleep(), but wakes up instantly if the event is set!
        stop_event.wait(0.5)
    print("Safe Monitor: Shutting down cleanly. Releasing resources.")

safe_t = threading.Thread(target=safe_monitor) # NOT a daemon
safe_t.start()
time.sleep(1) # Let it run briefly
print("Main: Telling monitor to stop...")
stop_event.set() # Signals the thread to exit the while loop
safe_t.join() # Wait for it to cleanly finish

# Trick 3: The Asyncio Equivalent of a Daemon
print("\n3. Asyncio Background Tasks (Modern alternative):")
import asyncio

async def async_monitor():
    try:
        while True:
            print("Async Monitor: Checking...")
            await asyncio.sleep(0.5)
    except asyncio.CancelledError:
        print("Async Monitor: Canceled gracefully!")

async def main_async():
    # Fire and forget task (runs in background)
    task = asyncio.create_task(async_monitor())
    await asyncio.sleep(1)
    print("Main async done, cancelling background tasks...")
    task.cancel() # Safely terminates the "daemon"
    await task

# asyncio.run(main_async()) # Uncomment to run the async version

"""
--- NOTES: Daemon Threads ---

1. What is a Daemon Thread?
   - A Daemon thread runs entirely in the background. 
   - By default, Python programs wait for all active non-daemon threads to finish before shutting down. 
   - If a thread is marked as `daemon=True`, Python will completely ignore it during the shutdown sequence. The exact millisecond the main program finishes, the OS abruptly kills the daemon thread, regardless of what code it was currently executing.

2. When to use them (and when NOT to):
   - **Good Use Cases**: Garbage collection, periodic health pinging, or UI background UI rendering (where abrupt death has zero consequences).
   - **Terrible Use Cases**: Writing to files, closing database transactions, or saving states. Because they die abruptly, they will inevitably cause data corruption. Use Trick 2 (`threading.Event`) for these instead.

3. Latest Python Features (Python 3.13 No-GIL):
   - **Free-Threading (PEP 703)**: With the experimental removal of the GIL in Python 3.13, background monitoring threads (like health checks) become vastly more efficient, as they no longer steal the GIL from the main execution thread to perform simple loop checks.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if I forget to set `daemon=True` on a thread that runs a `while True` loop?
A1: Your program will "hang" forever. The main thread will reach the end of its code, but the Python interpreter will refuse to exit because a non-daemon thread is still alive and running an infinite loop.

Q2: Is it safe to write to a database inside a daemon thread?
A2: No! It is highly dangerous. Daemon threads are terminated abruptly by the OS when the main program finishes. If the termination occurs halfway through a database write, it will leave your database in a corrupted or locked state.

Q3: If daemon threads are dangerous, how do I safely run an infinite background thread and stop it when my program ends?
A3: You should leave `daemon=False` (the default) and use a `threading.Event()`. The background thread checks the event flag inside its `while` loop. When the main program wants to exit, it calls `event.set()`, which signals the thread to cleanly finish its current loop, release its resources, and terminate properly.
"""