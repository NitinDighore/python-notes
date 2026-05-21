import asyncio
import time
from concurrent.futures import ThreadPoolExecutor

def check_stock(item):
    print(f"Checking {item} in store...") # Output: Checking Masala chai in store...
    time.sleep(3) # Blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala chai")
        print(result) # Output: Masala chai stock: 42 (after ~3s)

asyncio.run(main())

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The Modern Shortcut -> asyncio.to_thread (Python 3.9+)
print("\n1. asyncio.to_thread (Python 3.9+):")
# You no longer need to manually get the loop and create a ThreadPoolExecutor!
async def modern_offload():
    print("Starting modern offload...")
    # This automatically uses the default ThreadPoolExecutor and handles the boilerplate
    res = await asyncio.to_thread(check_stock, "Green chai")
    print(f"Modern result: {res}") # Output: Modern result: Green chai stock: 42

asyncio.run(modern_offload())

# Trick 2: Passing Keyword Arguments to run_in_executor
print("\n2. Passing kwargs using functools.partial:")
import functools
def complex_check(item, location="Warehouse"):
    return f"{item} found in {location}"

async def kwarg_offload():
    loop = asyncio.get_running_loop()
    # run_in_executor ONLY accepts *args. If your blocking function needs **kwargs,
    # you MUST bind them first using functools.partial!
    bound_func = functools.partial(complex_check, "Oolong", location="Storefront")
    res = await loop.run_in_executor(None, bound_func) # None uses the default executor
    print(f"Kwargs result: {res}") # Output: Kwargs result: Oolong found in Storefront

asyncio.run(kwarg_offload())

# Trick 3: Running multiple blocking tasks concurrently
print("\n3. Multiple Blocking Tasks concurrently:")
async def multiple_offloads():
    # We can offload multiple synchronous sleep functions to threads and await them all concurrently!
    results = await asyncio.gather(
        asyncio.to_thread(check_stock, "Lemon chai"),
        asyncio.to_thread(check_stock, "Mint chai")
    )
    print(f"Batch results: {results}") # Output: Batch results: ['Lemon chai stock: 42', 'Mint chai stock: 42']

asyncio.run(multiple_offloads())

"""
--- NOTES: Mixing Threads and Async (`run_in_executor`) ---

1. Why mix Threads with Asyncio?
   - Python's `asyncio` runs on a single event loop in a single thread. If you execute a blocking, synchronous function (like `time.sleep()`, `requests.get()`, or heavy DB queries), the entire event loop freezes, starving all other concurrent coroutines.
   - To fix this, we "offload" the blocking task to a background worker thread. The Thread Pool executes the blocking code, while the main `asyncio` event loop continues running freely. Once the background thread finishes, it sends the result back to the awaited coroutine.

2. Latest Python Features (Python 3.9+):
   - **`asyncio.to_thread()`**: Prior to Python 3.9, developers had to write the verbose `loop.run_in_executor()` boilerplate seen in the `main()` function. Python 3.9 introduced `asyncio.to_thread(func, *args, **kwargs)`, which dramatically simplifies the syntax and natively supports keyword arguments without needing `functools.partial`.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What happens if I forget to use `run_in_executor` and just call a 5-second `time.sleep()` inside an `async def` function?
A1: The single thread running the asyncio event loop will completely block for 5 seconds. All other concurrent tasks (like responding to incoming web requests) will freeze and time out during that window.

Q2: What is the `None` parameter in `loop.run_in_executor(None, func)`?
A2: Passing `None` as the first argument tells the event loop to use its default `ThreadPoolExecutor`. This is highly convenient because you don't have to manually instantiate and manage a ThreadPool with a `with` block yourself.

Q3: If `asyncio.to_thread` uses threads anyway, why use `asyncio` at all? Why not just use multithreading for the whole program?
A3: Because standard threads are "heavy". The OS can only efficiently manage a few hundred or thousand threads before memory and context-switching overheads crash the system. Asyncio can handle tens of thousands of concurrent connections on a single thread. We only offload specific legacy blocking functions to threads to keep the async loop fast and unblocked.
"""