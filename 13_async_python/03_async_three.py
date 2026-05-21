import asyncio
import aiohttp

async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}") 
        # Output: Fetched https://httpbin.org/delay/2 with status 200 
        # (Prints 3 times simultaneously after roughly 2 seconds)

async def main():
    urls = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        # tasks = [t1, t2, t3]
        await asyncio.gather(*tasks)
        

asyncio.run(main())

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: Limiting Concurrency with Semaphores
print("\n1. Limiting Concurrency (Preventing IP Bans/Crashes):")
# If you have 10,000 URLs, running them all at once will crash your OS or get you blocked.
# A Semaphore restricts the number of active coroutines inside a block.
sem = asyncio.Semaphore(2) # Only allow 2 concurrent requests at any given time

async def safe_fetch(session, url):
    async with sem: # Wait for a slot to open up
        async with session.get(url) as response:
            return response.status

# Trick 2: Processing results immediately as they arrive
print("\n2. Processing results instantly (as_completed):")
async def fetch_fast():
    async with aiohttp.ClientSession() as session:
        urls = ["https://httpbin.org/delay/1", "https://httpbin.org/delay/3"]
        tasks = [safe_fetch(session, url) for url in urls]
        
        # as_completed yields the coroutines exactly when they finish!
        for coro in asyncio.as_completed(tasks):
            result = await coro
            print(f"Got status: {result}") 
            # Output: Got status: 200 (after 1s) \n Got status: 200 (after 3s)

asyncio.run(fetch_fast())

# Trick 3: Extracting JSON Data asynchronously
print("\n3. Async JSON parsing:")
async def fetch_json():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://httpbin.org/json") as response:
            # Parsing JSON is an I/O/CPU operation that must be awaited
            data = await response.json()
            print(f"Title from JSON: {data['slideshow']['title']}") # Output: Title from JSON: Sample Slide Show

asyncio.run(fetch_json())

"""
--- NOTES: Asynchronous HTTP Requests (`aiohttp`) ---

1. Why not use the standard `requests` library?
   - The standard `requests.get()` is entirely synchronous and blocking. If you put it inside an `async def` function, it will freeze the single `asyncio` Event Loop until the server responds, ruining the entire point of asynchronous concurrency.
   - `aiohttp` is an asynchronous HTTP client built explicitly for `asyncio`. It yields control back to the Event Loop while waiting for the server to reply.

2. The `ClientSession` object:
   - `aiohttp.ClientSession()` is the core of `aiohttp`. It maintains a pool of persistent connections (HTTP Keep-Alive). 
   - Best Practice: You should create exactly ONE `ClientSession` and pass it around to all your fetch functions (as demonstrated in the `main()` function), rather than creating a new session for every single request.

3. Latest Python Features (Python 3.11+):
   - **`asyncio.timeout()`**: Before Python 3.11, you had to wrap your tasks in `asyncio.wait_for(task, timeout=5)`. Python 3.11 introduced a native context manager `async with asyncio.timeout(5):`. This makes enforcing strict timeouts on network blocks vastly cleaner and easier to read.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What does `async with` do, and how is it different from a normal `with` statement?
A1: `async with` is an Asynchronous Context Manager. While a normal `with` calls `__enter__` and `__exit__`, `async with` calls `__aenter__` and `__aexit__`. This allows the setup and teardown phases of the context block (like connecting to a server or closing a socket) to be asynchronous and yield control back to the Event Loop.

Q2: How do you prevent an async script from trying to open 10,000 HTTP connections at exactly the same time?
A2: You use an `asyncio.Semaphore`. By wrapping the HTTP request logic inside an `async with semaphore:` block, you force the coroutines to wait in line. If the semaphore is set to 100, only 100 requests will process concurrently.

Q3: Why must you `await response.json()` in `aiohttp` but not in `requests`?
A3: In the synchronous `requests` library, the entire payload is downloaded and decoded immediately, so `response.json()` is just a standard method call. In `aiohttp`, the payload might still be streaming in over the network. Calling `await response.json()` asynchronously reads the stream chunks and parses them without blocking the event loop.
"""