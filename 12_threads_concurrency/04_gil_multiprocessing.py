from multiprocessing import Process
import time

def crunch_number():
    print(f"Started the count process...") # Output: Started the count process... (x2)
    count = 0
    for _ in range(100_000_000):
        count += 1
    print(f"Ended the count process...") # Output: Ended the count process... (x2)

if __name__ == "__main__":
    start = time.time()

    p1 = Process(target=crunch_number)
    p2= Process(target=crunch_number)

    p1.start()
    p2.start()
    p1.join()
    p2.join()

    end = time.time()

    print(f"Total time with multi-processing is {end - start:.2f} seconds") 
    # Output: Total time with multi-processing is ~X.XX seconds (Noticeably faster than threading!)

    print("\n--- TRICK CODING EXAMPLES ---")

    # Trick 1: Proving they are separate OS processes
    print("\n1. Verifying Process IDs (PIDs):")
    import os
    def print_pid():
        print(f"Running in Process ID: {os.getpid()}")
    
    # Main process PID vs Child process PID
    print(f"Main Process ID: {os.getpid()}") # Output: Main Process ID: [e.g., 12345]
    p_test = Process(target=print_pid)
    p_test.start()
    p_test.join() # Output: Running in Process ID: [e.g., 12346] (Completely different ID!)

    # Trick 2: Sharing State (Which normally fails in multiprocessing)
    print("\n2. Sharing Memory (Value):")
    from multiprocessing import Value
    def increment_shared(shared_val):
        with shared_val.get_lock(): # Must lock it to prevent race conditions!
            shared_val.value += 1
            
    # 'i' means integer. This is stored in shared OS memory, escaping normal isolation.
    shared_counter = Value('i', 0)
    procs = [Process(target=increment_shared, args=(shared_counter,)) for _ in range(5)]
    for p in procs: p.start()
    for p in procs: p.join()
    print(f"Shared Counter Final Value: {shared_counter.value}") # Output: Shared Counter Final Value: 5

    # Trick 3: Pool.starmap for multiple arguments
    print("\n3. Using Pool.starmap for clean execution:")
    from multiprocessing import Pool
    def multiply(a, b):
        return a * b
        
    with Pool(processes=2) as pool:
        # starmap unpacks the tuples into arguments for the target function
        results = pool.starmap(multiply, [(2, 3), (4, 5), (6, 7)])
        print(f"Starmap results: {results}") # Output: Starmap results: [6, 20, 42]

"""
--- NOTES: Multiprocessing vs the GIL ---

1. Bypassing the Global Interpreter Lock:
   - In the previous threading example (`03_gil_threading.py`), the CPU-bound math loop failed to speed up because the GIL forced the threads to take turns.
   - `multiprocessing` solves this. By spinning up completely new Operating System processes, Python boots up a brand-new interpreter with its own memory space and its own isolated GIL for every single worker.
   - Result: Both processes max out their respective CPU cores simultaneously, cutting the total execution time nearly in half!

2. The Cost of Multiprocessing:
   - Spawning processes is computationally heavy. The OS has to allocate new memory segments, and Python has to serialize (pickle) any data passed to the child process.
   - It should be strictly reserved for heavy, CPU-bound tasks where the computation time drastically outweighs the slow process boot time.

3. Latest Python Features (Python 3.13):
   - **Free-Threading (PEP 703)**: The massive "No-GIL" feature introduced experimentally in Python 3.13 allows standard `threading` to finally run CPU-bound tasks in parallel without needing `multiprocessing`. If you run this file vs the threaded file in a Python 3.13+ Free-Threaded build, both will execute with true parallelism, vastly reducing the necessity for heavy `multiprocessing` overheads in the future.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why did the CPU-bound task finish faster here than it did in the threading example?
A1: Because standard threading shares memory and is bound by the GIL, forcing execution to be sequential. Multiprocessing spawns entirely new OS processes, meaning each process has its own GIL and can utilize separate physical CPU cores simultaneously.

Q2: Since multiprocessing is faster for math, should I just use it for everything?
A2: No. Spawning processes has massive overhead in terms of memory and startup time compared to threads. For I/O-bound tasks (like making 100 API requests), `threading` or `asyncio` is overwhelmingly superior and more memory-efficient.

Q3: If two processes modify a global variable `count`, will they see each other's changes?
A3: No. Because processes have entirely isolated memory spaces, they each get their own separate copy of the `count` variable when they boot up. To share data, you must use inter-process communication (IPC) tools like `multiprocessing.Queue` or `multiprocessing.Value`.
"""
