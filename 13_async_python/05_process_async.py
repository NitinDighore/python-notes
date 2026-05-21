import asyncio
from concurrent.futures import ProcessPoolExecutor

def encrypt(data):
    return f"🔒 {data[::-1]}"

async def main():
    loop = asyncio.get_running_loop()
    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, encrypt, "credit_card_1234")
        print(f"{result}") # Output: 🔒 4321_drac_tiderc

if __name__ == "__main__":
    asyncio.run(main())

    print("\n--- TRICK CODING EXAMPLES ---")

    # Trick 1: Running multiple CPU-bound tasks concurrently
    print("\n1. Batch CPU Processing in Async:")
    async def batch_encrypt():
        loop = asyncio.get_running_loop()
        data_list = ["apple", "banana", "cherry"]
        
        # We instantiate ONE pool and reuse it for all tasks to save massive overhead
        with ProcessPoolExecutor(max_workers=3) as pool:
            # Schedule all the CPU tasks simultaneously 
            tasks = [loop.run_in_executor(pool, encrypt, item) for item in data_list]
            
            # Gather waits for all processes to finish and returns their results
            results = await asyncio.gather(*tasks)
            print(f"Batch encrypted: {results}") 
            # Output: Batch encrypted: ['🔒 elppa', '🔒 ananab', '🔒 yrrehc']
            
    asyncio.run(batch_encrypt())

    # Trick 2: Passing Keyword Arguments to run_in_executor
    print("\n2. Passing kwargs using functools.partial:")
    import functools
    
    def complex_encrypt(data, shift_key="A"):
        return f"🔒 {data[::-1]} (key: {shift_key})"
        
    async def kwarg_encrypt():
        loop = asyncio.get_running_loop()
        # run_in_executor DOES NOT accept **kwargs directly. 
        # You must bind them using partial before passing the function.
        bound_func = functools.partial(complex_encrypt, "secret", shift_key="X99")
        
        with ProcessPoolExecutor() as pool:
            res = await loop.run_in_executor(pool, bound_func)
            print(f"Kwarg result: {res}") # Output: Kwarg result: 🔒 terces (key: X99)
            
    asyncio.run(kwarg_encrypt())

"""
--- NOTES: Process Pools in Asyncio (CPU-Bound Tasks) ---

1. The Async CPU Bottleneck:
   - Python's `asyncio` Event Loop runs on a single thread. If you execute a heavy mathematical or CPU-bound function (like `encrypt` simulating deep cryptography), it will completely block the event loop, causing all other async tasks (like web requests) to freeze.
   - While we previously used `ThreadPoolExecutor` (or `asyncio.to_thread`) to offload I/O blocking tasks, threads suffer from the Global Interpreter Lock (GIL) and cannot perform CPU-heavy math in parallel.
   - The solution is to offload the CPU-bound task to a `ProcessPoolExecutor`. This boots up an entirely separate OS process (bypassing the GIL) to crunch the numbers, and signals the Event Loop when it is finished.

2. `loop.run_in_executor(pool, func, *args)`:
   - This method takes a custom executor (in this case, our Process Pool). It submits the function to the pool, returns an `asyncio.Future` representing the task, and yields control back to the event loop. The main script can continue doing other async work while the background process handles the heavy lifting.

3. Latest Python Features (Python 3.13 No-GIL):
   - **Free-Threading (PEP 703)**: With the experimental removal of the GIL in Python 3.13, you might soon be able to use standard `ThreadPoolExecutor` (or `asyncio.to_thread()`) for CPU-bound tasks in async applications, drastically reducing the heavy memory footprint and boot times associated with spawning separate OS processes.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why are we using `ProcessPoolExecutor` here instead of `asyncio.to_thread` or `ThreadPoolExecutor`?
A1: `asyncio.to_thread` uses a thread pool under the hood. Threads in standard Python are bound by the GIL, meaning they cannot run CPU-intensive tasks in parallel. Because `encrypt()` represents a heavy CPU-bound task, we must use `ProcessPoolExecutor` to spawn a new OS process, bypass the GIL, and utilize a separate physical CPU core.

Q2: What happens if you forget the `if __name__ == "__main__":` guard block in this file?
A2: Because this file uses `ProcessPoolExecutor`, it relies on the `multiprocessing` module. On Windows and macOS (which use the "spawn" start method), the new child process attempts to import the main script to reconstruct its state. Without the guard, the child process would endlessly spawn more child processes, causing a catastrophic "fork bomb" that crashes the system.

Q3: How does `asyncio` know when the separate process has finished its work?
A3: `loop.run_in_executor()` returns an `asyncio.Future`. Under the hood, the executor runs the task and, upon completion, triggers a thread-safe callback that marks the Future as "done" and attaches the result. The `await` keyword simply pauses the coroutine until that Future is marked done.
"""