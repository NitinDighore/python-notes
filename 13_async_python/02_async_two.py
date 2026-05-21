import asyncio
import time
async def brew(name):
    print(f"Brewing {name}...") 
    # Output order: All 3 "Brewing..." messages print instantly
    await asyncio.sleep(3)
    # time.sleep(3)
    print(f" {name} is ready...") 
    # Output order: All 3 "...is ready..." messages print ~3s later


async def main():
    await asyncio.gather(
        brew("Masala chai"),
        brew("Green chai"),
        brew("Ginger chai"),
    )

asyncio.run(main())

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Returning ordered values from asyncio.gather
print("\n1. Capturing Return Values:")
async def fetch_data(id, delay):
    await asyncio.sleep(delay)
    return f"Data {id}"

async def get_all_data():
    # Even though Data 2 finishes first, gather ALWAYS returns the results
    # in the exact order the coroutines were originally passed!
    results = await asyncio.gather(
        fetch_data(1, delay=2),
        fetch_data(2, delay=1)
    )
    print(f"Ordered Results: {results}") # Output: Ordered Results: ['Data 1', 'Data 2']

asyncio.run(get_all_data())

# Trick 2: Safe Exception Handling in gather
print("\n2. Handling Exceptions (return_exceptions=True):")
async def risky_brew(name):
    if name == "Poison": raise ValueError("Toxic!")
    return f"{name} is safe"

async def test_brews():
    # By default, if one coroutine fails, gather throws the error and ruins everything.
    # return_exceptions=True catches the error and puts it in the result list safely!
    results = await asyncio.gather(risky_brew("Tea"), risky_brew("Poison"), return_exceptions=True)
    print(f"Safe gather: {results}") # Output: Safe gather: ['Tea is safe', ValueError('Toxic!')]

asyncio.run(test_brews())

# Trick 3: The Modern Way -> asyncio.TaskGroup (Python 3.11+)
print("\n3. Modern Concurrency with TaskGroup (Python 3.11+):")
async def modern_main():
    # TaskGroups replace gather(). They are safer context managers that automatically
    # cancel sibling tasks if one task fails, preventing memory leaks!
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(fetch_data(10, 1))
        task2 = tg.create_task(fetch_data(20, 1))
    # Code here only runs AFTER all tasks in the group are completely finished
    print(f"TaskGroup done: {task1.result()}, {task2.result()}")

asyncio.run(modern_main())

"""
--- NOTES: Concurrency and `asyncio.gather` ---

1. The blocking `time.sleep(3)` trap:
   - In the `brew()` function, you'll notice `time.sleep(3)` is commented out. This is highly intentional!
   - If you uncommented it and removed `await asyncio.sleep(3)`, the entire event loop would freeze. The coroutines would run synchronously (taking 9 seconds total instead of 3).
   - Rule of thumb: Never use synchronous blocking I/O inside an `async def` function. Always use `await`.

2. `asyncio.gather()`:
   - Takes a sequence of awaitables (like coroutines or Futures), schedules them concurrently, and waits for all of them to finish.
   - It returns a list of results in the exact same order as the inputs, regardless of which task actually finished first.

3. Latest Python Features (Python 3.11+):
   - **`asyncio.TaskGroup`**: Python 3.11 introduced `TaskGroup`, which is now the recommended alternative to `asyncio.gather()`. It heavily improves error handling. With `gather`, if one task crashes, the other tasks keep running in the background unattended. With `TaskGroup`, if one task crashes, it cleanly and automatically cancels all other running tasks inside the group.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What would happen to the execution time if you used `time.sleep(3)` instead of `await asyncio.sleep(3)` in the `brew` coroutine?
A1: The execution time would jump from ~3 seconds to ~9 seconds. `time.sleep(3)` is a blocking call that freezes the entire thread (and thus the single asyncio Event Loop) for 3 seconds. The coroutines would be forced to execute sequentially.

Q2: Does `asyncio.gather()` execute tasks in parallel?
A2: No, it executes them *concurrently*. Because standard Python `asyncio` runs on a single thread with a single Event Loop, only one coroutine is actively executing Python bytecode at any given millisecond. However, when a coroutine hits an `await` (I/O wait), it yields control, allowing the Event Loop to quickly switch to another coroutine.

Q3: If I pass three coroutines into `asyncio.gather()`, and the third one finishes first, what will the output list look like?
A3: The output list will still match the order of the inputs you passed in. `gather()` handles reordering the results behind the scenes so you don't have to guess which result belongs to which task.
"""