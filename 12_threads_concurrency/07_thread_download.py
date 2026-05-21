import threading
import requests
import time

def download(url):
    print(f"Starting download from {url}") 
    # Output: Starting download from https://httpbin.org/image/jpeg (Messages will interleave)
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes") 
    # Output: Finished downloading from https://httpbin.org/image/jpeg, size: 35588 bytes

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"All downloads done in {end - start:.2f} seconds") 
# Output: All downloads done in ~X.XX seconds (Much faster than sequential execution!)

print("\n--- TRICK CODING EXAMPLES ---")

# Trick 1: The Modern Way - ThreadPoolExecutor
print("\n1. ThreadPoolExecutor (concurrent.futures):")
from concurrent.futures import ThreadPoolExecutor

def fetch_size(url):
    return len(requests.get(url).content)

# ThreadPoolExecutor automatically manages the threads, limits concurrency, and captures return values cleanly.
with ThreadPoolExecutor(max_workers=3) as executor:
    # .map() automatically returns the results in the exact same order as the input list!
    results = executor.map(fetch_size, urls)
    for url, size in zip(urls, results):
        print(f"{url} is {size} bytes")

# Trick 2: Rate Limiting / Semaphores
print("\n2. Rate Limiting with Semaphores:")
# If downloading 1000 URLs, you don't want 1000 threads crashing your system or getting you IP banned.
# Semaphores act like bouncers, strictly limiting how many threads can execute a block of code at once.
max_concurrent_downloads = threading.Semaphore(2)

def safe_download(url):
    with max_concurrent_downloads:
        print(f"Safe downloading: {url}")
        requests.get(url)
# You would normally spawn your threads here to call safe_download

# Trick 3: Collecting Data safely using a Queue
print("\n3. Collecting Data Safely (queue.Queue):")
import queue
# Queues are perfectly thread-safe. Multiple threads can safely push data into it without race conditions.
q = queue.Queue()

def download_to_queue(url, q_out):
    resp = requests.get(url)
    q_out.put((url, len(resp.content)))

t_queue = threading.Thread(target=download_to_queue, args=(urls[0], q))
t_queue.start()
t_queue.join()
print(f"Data safely extracted from Queue: {q.get()}")

"""
--- NOTES: Concurrent Network Requests (I/O Bound) ---

1. Why Threading Shines Here:
   - Network requests are heavily I/O bound. The CPU spends 99% of the time just waiting for the external server (httpbin.org) to respond over the internet.
   - Python's Global Interpreter Lock (GIL) is automatically released during I/O operations. This means all three threads can wait for their respective network responses at the exact same time without blocking each other.

2. Managing Threads Manually vs Pools:
   - Manually appending `threading.Thread` instances to a list and joining them in a `for` loop (as done in the main code) is the traditional, low-level way.
   - The modern, highly preferred way is using `concurrent.futures.ThreadPoolExecutor` (Trick 1). It abstracts away thread lifecycle management and makes retrieving return values effortless.

3. Latest Python Features:
   - **Asyncio and `aiohttp`**: While threading works great for dozens of concurrent network requests, modern Python heavily favors `asyncio` for *thousands* of simultaneous connections. Python 3.11 introduced `asyncio.TaskGroup`, offering a much safer and cleaner syntax for coordinating multiple async network requests compared to raw threads.
   - **`asyncio.to_thread` (Python 3.9+)**: If you are inside an async event loop but need to run a legacy synchronous blocking library (like `requests`), you can use `await asyncio.to_thread(requests.get, url)` to effortlessly offload it to a background thread without freezing your async loop.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why is threading used for network requests instead of multiprocessing?
A1: Network requests are I/O bound, meaning the program is mostly waiting, not calculating. Threads are perfectly capable of waiting concurrently because the GIL is released during I/O. Multiprocessing would spawn entirely new OS processes, consuming significantly more system memory and boot time for absolutely no performance benefit in this scenario.

Q2: What happens if you try to spawn 10,000 threads at once to download 10,000 URLs?
A2: The Operating System will likely crash or forcefully kill your program due to "thread exhaustion" (running out of RAM to allocate thread stacks) or massive context-switching overhead. To handle 10,000 requests, you should either use a `ThreadPoolExecutor` with a fixed number of workers (e.g., `max_workers=50`) to reuse threads, or switch to asynchronous programming (`asyncio`), which can handle thousands of connections on a single thread.

Q3: How do you safely get the return values (like the HTML response or image data) from multiple threads?
A3: The raw `threading.Thread` class does not natively return values. You must either pass a mutable, thread-safe data structure (like a `queue.Queue` or a dictionary/list with a `Lock`) for the threads to write their results into, or use `concurrent.futures.ThreadPoolExecutor.submit()`, which returns a `Future` object containing the result.
"""