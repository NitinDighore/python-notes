import asyncio
import threading
import time

def background_worker():
    while True:
        time.sleep(1)
        print(f"Logging the system health 🕰️") # Output: Logging the system health 🕰️ (x3, once per second)

async def fetch_orders():
    await asyncio.sleep(3)
    print("🎁 order fetched") # Output: 🎁 order fetched (after 3 seconds, then the program exits)


threading.Thread(target=background_worker, daemon=True).start()

asyncio.run(fetch_orders())

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Pure Async Background Task (No Threading needed!)
print("\n1. Pure Async Background Task:")
async def async_health_check():
    try:
        while True:
            await asyncio.sleep(0.5)
            print("Async health check 🩺")
    except asyncio.CancelledError:
        print("Health check stopped cleanly.")

async def main_async():
    # Start the background worker inside the event loop!
    bg_task = asyncio.create_task(async_health_check())
    
    print("Doing main work...")
    await asyncio.sleep(1.5) # Output: Async health check 🩺 (x3)
    print("Main work done!")
    
    # Cleanly cancel the background task before exiting
    bg_task.cancel()
    await bg_task

asyncio.run(main_async())

# Trick 2: Offloading a truly blocking infinite loop to a thread via to_thread
print("\n2. Thread offloading for blocking loops:")
def heavy_legacy_worker():
    import time
    time.sleep(1)
    return "Legacy worker finished"

async def modern_mix():
    print("Starting legacy worker in background...")
    # This runs the synchronous function in a background thread, awaiting its result
    # without freezing the async loop!
    result = await asyncio.to_thread(heavy_legacy_worker)
    print(result) # Output: Legacy worker finished

asyncio.run(modern_mix())

"""
--- NOTES: Combining Asyncio with Background Threads ---

1. Why use a Daemon Thread here?
   - The `background_worker()` function uses a blocking `while True:` loop and `time.sleep(1)`. If we ran this inside the `asyncio` event loop natively without an `await`, it would completely freeze the loop, and `fetch_orders()` would never execute.
   - By spinning up a completely separate `threading.Thread(..., daemon=True)`, the blocking loop runs safely in the background. Because it is a `daemon=True` thread, it automatically dies the exact moment `asyncio.run(fetch_orders())` finishes and the main program exits.

2. Pure Async vs Threading:
   - If the background task involves I/O operations that support `await` (like Trick 1), it is vastly better to use `asyncio.create_task()` to run it concurrently on the single event loop.
   - You only need to mix `threading` with `asyncio` if you are forced to use a legacy, blocking, synchronous library that does not support `await`.

3. Latest Python Features:
   - **`asyncio.to_thread` (Python 3.9+)**: As shown in Trick 2, if you have a blocking function, `asyncio.to_thread` seamlessly runs it in a separate thread and returns an awaitable coroutine, replacing the bulky `loop.run_in_executor()` boilerplate.
   - **`asyncio.TaskGroup` (Python 3.11+)**: Makes managing background async tasks much safer. If any task inside the `TaskGroup` crashes, all other background tasks are automatically and safely canceled, preventing memory leaks and orphaned loops.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is a daemon thread?
A1: A daemon thread is a background thread that executes independently and does not prevent the Python interpreter from exiting. Once the main program (non-daemon threads) finishes execution, the Python interpreter forcefully terminates all alive daemon threads and exits.

Q2: Why didn't we just call `await background_worker()` inside `fetch_orders()`?
A2: First, `background_worker` is not an `async def` function, so it cannot be `await`ed. Second, even if it were, it contains a `while True` infinite loop. Awaiting an infinite loop would trap the event loop forever, preventing any further lines of code from executing.

Q3: How do you gracefully shut down a pure `asyncio` background task?
A3: If a background task was created using `asyncio.create_task()`, you can shut it down by calling `task.cancel()`. The next time the task hits an `await` statement, it will raise an `asyncio.CancelledError`, which you can catch inside the task to perform any necessary cleanup before exiting.
"""