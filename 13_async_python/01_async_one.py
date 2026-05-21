import asyncio

async def brew_chai():
    print("Brwing chai...") # Output: Brwing chai...
    await asyncio.sleep(2)
    print("Chai is ready") # Output: Chai is ready (approx 2s later)

asyncio.run(brew_chai())

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Running multiple coroutines concurrently (asyncio.gather)
print("\n1. Concurrent Execution:")
async def fast_brew(name, delay):
    await asyncio.sleep(delay)
    return f"{name} ready in {delay}s"

async def make_multiple_teas():
    # gather() runs all passed coroutines concurrently and waits for them all to finish
    results = await asyncio.gather(
        fast_brew("Green", 1),
        fast_brew("Oolong", 2)
    )
    print(f"Results: {results}") # Output: Results: ['Green ready in 1s', 'Oolong ready in 2s']

asyncio.run(make_multiple_teas())

# Trick 2: Background Tasks (asyncio.create_task)
print("\n2. Fire-and-forget Background Tasks:")
async def background_music():
    print("Music started...")
    await asyncio.sleep(3)
    print("Music stopped!")

async def cafe_routine():
    # create_task schedules the coroutine to run on the event loop immediately, without waiting for it!
    task = asyncio.create_task(background_music())
    print("Taking orders while music plays...")
    await asyncio.sleep(1) # We can do other things while the music plays!
    await task # Now we explicitly wait for the background task to finish

asyncio.run(cafe_routine())

# Trick 3: Handling Timeouts (asyncio.wait_for)
print("\n3. Enforcing Timeouts:")
async def slow_supplier():
    await asyncio.sleep(10)
    return "Supplies arrived"

async def safe_restock():
    try:
        # If the coroutine takes longer than 1 second, it raises a TimeoutError
        result = await asyncio.wait_for(slow_supplier(), timeout=1.0)
    except asyncio.TimeoutError:
        print("Supplier took too long! Canceling order.") # Output: Supplier took too long! Canceling order.

asyncio.run(safe_restock())

"""
--- NOTES: Asynchronous Programming (asyncio) ---

1. What is `asyncio`?
   - Asynchronous I/O (`asyncio`) is a library to write concurrent code using the `async/await` syntax.
   - Unlike threading (which uses OS threads), asyncio uses a single "Event Loop" running on a single thread. This is known as "Cooperative Multitasking".
   - When an `async def` function hits an `await` statement (like `await asyncio.sleep(2)`), it pauses its own execution and voluntarily yields control back to the Event Loop, allowing the loop to execute other tasks while it waits.

2. The Danger of Blocking Code:
   - You must NEVER use `time.sleep()` or standard blocking network requests (like `requests.get`) directly inside an `async def` function! Because asyncio runs on a single thread, a blocking call will completely freeze the entire Event Loop, stopping all other concurrent tasks. You must use `await asyncio.sleep()` or async-native libraries like `aiohttp`.

3. Latest Python Features:
   - **`asyncio.TaskGroup` (Python 3.11+)**: Replaces complex `asyncio.gather()` workflows. It is a context manager (`async with asyncio.TaskGroup() as tg:`) that provides strict guarantees: if one task fails, all other running tasks in the group are safely and automatically canceled, preventing dangling background tasks and memory leaks.
   - **`asyncio.to_thread` (Python 3.9+)**: If you are forced to use a synchronous, blocking library inside an async app, you can use `await asyncio.to_thread(sync_function)` to effortlessly offload it to a background worker thread, ensuring the Event Loop never freezes.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between `asyncio` and `threading`?
A1: `threading` uses preemptive multitasking managed by the Operating System, which forces context switches between multiple threads. `asyncio` uses cooperative multitasking managed by an Event Loop running on a single thread; tasks manually yield control using the `await` keyword. Asyncio is generally much more memory-efficient for high-volume I/O bounds (like handling 10,000 WebSockets).

Q2: What is a Coroutine?
A2: A Coroutine is a specialized version of a Python generator function defined using `async def`. Calling a coroutine does not execute it; it returns a coroutine object. It only executes when you schedule it on the event loop (e.g., using `await`, `asyncio.run()`, or `asyncio.create_task()`).

Q3: What does `asyncio.run(main())` do?
A3: It is the main entry point for an asyncio program. It automatically creates a new Event Loop, runs the passed coroutine (`main()`) until it completes, cleanly cancels any pending background tasks, and then closes the Event Loop.
"""