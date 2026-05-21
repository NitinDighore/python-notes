from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers...") # Output: Crunching some numbers... (x2)
    total = 0
    for i in range(10**9):
        total += i
    print("DONE ✅") # Output: DONE ✅ (x2)

if __name__ == "__main__":
    start = time.time()
    processes = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in processes]
    [t.join() for t in processes]

    print(f"Time taken: {time.time() - start:.2f} seconds") 
    # Output: Time taken: ~X.XX seconds (Runs in parallel across multiple CPU cores, heavily outperforming threading!)

    print("\n--- TRICK CODING EXAMPLES ---")

    # Trick 1: Checking the Process IDs and Names
    print("\n1. Verifying Process IDs:")
    import os, multiprocessing
    def who_am_i():
        print(f"Process '{multiprocessing.current_process().name}' running on OS PID: {os.getpid()}")

    p1 = Process(target=who_am_i, name="Worker-A")
    p1.start(); p1.join()
    # Output: Process 'Worker-A' running on OS PID: [Unique ID]

    # Trick 2: Daemon Processes (Background Workers)
    print("\n2. Daemon Processes:")
    def background_task():
        while True:
            time.sleep(1) # Runs infinitely
    
    daemon_p = Process(target=background_task, daemon=True)
    daemon_p.start()
    print(f"Daemon process {daemon_p.pid} started. It will be killed automatically when the main script exits.")

    # Trick 3: Using multiprocessing.Pool for map operations
    print("\n3. multiprocessing.Pool:")
    from multiprocessing import Pool
    def square(n):
        return n * n
    
    # A Pool manages a pool of worker processes and distributes tasks to them automatically
    with Pool(processes=2) as pool:
        results = pool.map(square, [1, 2, 3, 4, 5])
        print(f"Pool map results: {results}") # Output: Pool map results: [1, 4, 9, 16, 25]

"""
--- NOTES: Multiprocessing for CPU-Bound Tasks ---

1. Why use Multiprocessing here?
   - In `09_process_one.py`, using `threading` for a heavy mathematical loop resulted in terrible performance due to the Global Interpreter Lock (GIL) and context-switching overhead.
   - `10_process_two.py` uses `multiprocessing.Process`. This completely bypasses the GIL because it boots up two entirely separate Python instances at the OS level. 
   - Each process utilizes its own dedicated physical CPU core, allowing the two `10**9` loops to run simultaneously in true parallel, drastically reducing the total execution time!

2. The `if __name__ == '__main__':` Guard:
   - When you spawn a new process on platforms that use the "spawn" start method (like Windows and macOS), Python imports the main script inside the new child process from scratch.
   - If you do not put your process-creation code inside this guard, the child process will also execute `Process(target=...).start()`, endlessly creating an infinite loop of processes (a "fork bomb") until your computer crashes.

3. Latest Python Features:
   - **Free-Threading (Python 3.13+)**: The new experimental "No-GIL" feature will eventually allow developers to use lightweight `threading` to achieve this exact same parallel execution for CPU-bound tasks, without incurring the heavy memory overhead and startup time of OS-level `multiprocessing`.
   - **Start Method Defaults (Python 3.14+)**: Python 3.14 will officially change the default multiprocessing start method from `fork` to `spawn` or `forkserver` on POSIX systems (Linux). While `fork` is faster, it is notoriously unsafe when mixing threads and processes.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: For a CPU-bound application (like image processing or large mathematical calculations), should you use `threading` or `multiprocessing`?
A1: You should absolutely use `multiprocessing`. Because of Python's Global Interpreter Lock (GIL), `threading` cannot utilize multiple CPU cores for heavy calculations. `multiprocessing` spawns separate processes that bypass the GIL entirely.

Q2: Why is the `if __name__ == '__main__':` block strictly required when working with the `multiprocessing` module on Windows?
A2: Because Windows lacks the `fork()` system call found in Linux. Instead, it uses `spawn()`, which boots a fresh Python interpreter and imports the original script. The `__name__ == '__main__'` guard prevents the child interpreter from re-executing the process-spawning code, preventing an infinite loop of process creation.

Q3: If `multiprocessing` is so much faster for math, what are its downsides?
A3: Processes are extremely "heavy" compared to threads. They take significantly more time to boot up and require their own dedicated chunk of system RAM (because they don't share memory). Additionally, passing data between processes (IPC - Inter-Process Communication) requires serialization (`pickle`), which adds overhead.
"""