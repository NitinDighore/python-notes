from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing") 
    # Output order: All 3 "Start" messages will print almost simultaneously
    time.sleep(3)
    print(f"End of {name} chai brewing")
    # Output order: All 3 "End" messages will print ~3 seconds later

if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
        for i in range(3)
    ]

    # Start all process
    for p in chai_makers:
        p.start()

    # wait for all to complete
    for p in chai_makers:
        p.join()

    print("All chai served") # Output: All chai served

    print("\n--- TRICK CODING EXAMPLES ---")

    # Trick 1: Getting CPU Cores to optimize worker counts
    print("\n1. Getting maximum CPU cores:")
    import multiprocessing
    cores = multiprocessing.cpu_count()
    print(f"Your system has {cores} CPU cores available for parallel processing.")

    # Trick 2: Modern Multiprocessing with ProcessPoolExecutor
    print("\n2. ProcessPoolExecutor (Best Practice for return values):")
    from concurrent.futures import ProcessPoolExecutor
    
    def fast_brew(cup_id):
        return f"Cup #{cup_id} perfectly brewed in parallel!"

    # The executor abstracts away manual .start() and .join() calls
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(fast_brew, [101, 102, 103])
        for res in results:
            print(res) # Output: Cup #101 perfectly brewed in parallel! ...

"""
--- NOTES: Multiprocessing in Python ---

1. What is Multiprocessing?
   - `multiprocessing` is a package that supports spawning completely independent OS processes.
   - Unlike threading (which shares memory and is bound by Python's Global Interpreter Lock), each process created by `multiprocessing` gets its own memory space and its own Python interpreter.
   - This is the ONLY way in standard Python (prior to 3.13) to achieve true CPU-bound parallelism (utilizing multiple CPU cores at the exact same time for heavy math/processing).

2. The `if __name__ == "__main__":` Guard:
   - This guard is absolutely MANDATORY when using multiprocessing in Python on Windows and macOS.
   - Because these OSes use the `spawn` start method, Python imports the main module in the new child process. Without the guard, the child process would endlessly spawn its own child processes, leading to a catastrophic fork bomb (RuntimeError).

3. Latest Python Features:
   - **Free-Threading / No-GIL (Python 3.13+)**: PEP 703 introduces an experimental build of Python that completely removes the Global Interpreter Lock (GIL). Once widely adopted, developers will be able to use standard `threading` for CPU-bound parallelism, which may greatly reduce the need for `multiprocessing` and its massive memory overhead in the future.
   - **Start Method Changes (Python 3.14+)**: Historically, Linux used the `fork` start method, which was fast but inherently unsafe in multi-threaded contexts. Python 3.14 officially defaults to `spawn` or `forkserver` across all platforms to eliminate these obscure bugs.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: When should you use `multiprocessing` instead of `threading`?
A1: Use `threading` for I/O-bound tasks (like making network requests or reading files) because threads are lightweight. Use `multiprocessing` for CPU-bound tasks (like image processing, big data calculations, or machine learning) because it bypasses the GIL to use multiple physical CPU cores.

Q2: Do processes share global variables?
A2: No. Because each process gets a completely isolated memory space, if Process A modifies a global variable, Process B will not see that change. To share state, you must explicitly use Inter-Process Communication (IPC) tools like `multiprocessing.Queue`, `multiprocessing.Pipe`, or `multiprocessing.Value`.

Q3: Why does `multiprocessing` have a higher overhead than `threading`?
A3: Spinning up a new thread just requires allocating a small stack within the existing process. Spinning up a new process requires the Operating System to allocate a brand-new, isolated memory space, copy the Python executable, and boot up an entirely new interpreter environment.
"""