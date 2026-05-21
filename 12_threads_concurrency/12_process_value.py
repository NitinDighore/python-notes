from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value('i', 0)
    processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final counter value: ",counter.value ) # Output: Final counter value:  400000

    print("\n--- TRICK CODING EXAMPLES ---")

    # Trick 1: The Race Condition in Processes
    print("\n1. Race Condition without a Lock:")
    def unsafe_increment(unsafe_counter):
        for _ in range(100000):
            # Without acquiring the lock, processes will overwrite each other's increments!
            unsafe_counter.value += 1

    unsafe_counter = Value('i', 0)
    unsafe_procs = [Process(target=unsafe_increment, args=(unsafe_counter,)) for _ in range(4)]
    for p in unsafe_procs: p.start()
    for p in unsafe_procs: p.join()
    print(f"Unsafe counter expected 400000, got: {unsafe_counter.value} (Data corruption!)")

    # Trick 2: Sharing Arrays (Multiple Values)
    print("\n2. Sharing an Array of data:")
    from multiprocessing import Array
    def square_array(shared_arr):
        # Arrays also have built-in locks
        with shared_arr.get_lock():
            for i in range(len(shared_arr)):
                shared_arr[i] = shared_arr[i] ** 2

    # 'i' is for integer, initializing an array with [1, 2, 3, 4]
    arr = Array('i', [1, 2, 3, 4])
    p_arr = Process(target=square_array, args=(arr,))
    p_arr.start(); p_arr.join()
    print(f"Squared Shared Array: {list(arr)}") # Output: Squared Shared Array: [1, 4, 9, 16]

    # Trick 3: High-Performance Shared Memory (Python 3.8+)
    print("\n3. multiprocessing.shared_memory (Python 3.8+):")
    from multiprocessing import shared_memory
    
    # Create a shared memory block of 10 bytes directly in the OS RAM
    shm = shared_memory.SharedMemory(create=True, size=10)
    buffer = shm.buf # Returns a memoryview
    buffer[0] = 255 # Write directly to the physical RAM
    print(f"Direct RAM write: {buffer[0]}") # Output: Direct RAM write: 255
    shm.close()
    shm.unlink() # ALWAYS clean up shared memory blocks to prevent OS memory leaks!

"""
--- NOTES: Process Synchronization and Shared Memory ---

1. Sharing State Between Processes:
   - By default, OS processes do NOT share memory. If you pass a normal integer or list to a process, it receives a completely distinct copy (via pickling).
   - To share state, you must use specific IPC objects like `multiprocessing.Value` (for a single variable) or `multiprocessing.Array` (for a sequence).
   - These objects store data in a shared memory map provided by the Operating System, allowing all child processes to read and write to the exact same physical RAM address.

2. Process Race Conditions and Locks:
   - Just like threads, processes can suffer from Race Conditions when they modify shared memory simultaneously.
   - `Value` and `Array` automatically create a hidden `multiprocessing.Lock` under the hood. 
   - You MUST explicitly acquire this lock using `with counter.get_lock():` before performing compound operations like `+=` to prevent data corruption.

3. Latest Python Features:
   - **`multiprocessing.shared_memory` (Python 3.8+)**: Traditional `Value` and `Array` are great for basic variables, but they are limited to simple C-types (like integers and doubles). Python 3.8 introduced the `shared_memory` module, which allows you to allocate raw blocks of RAM and share them across processes. This is an absolute game-changer for data science, as you can map massive multi-gigabyte NumPy arrays or Pandas DataFrames directly into this memory block, allowing multiple processes to read and write instantly without the enormous overhead of serialization (pickling).

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: Why do we need `with counter.get_lock():` if `Value` is supposed to be for shared multiprocessing?
A1: While `Value` places the integer in shared memory, the operation `counter.value += 1` is not atomic. It involves reading, adding, and writing. If two processes do this simultaneously, they will overwrite each other. The lock ensures that one process finishes the entire read-add-write cycle before the next process is allowed to touch the memory block.

Q2: What do the `'i'` and `'d'` string arguments mean when creating a `Value('i', 0)`?
A2: They are type codes used by the underlying C-language structures (from the `ctypes` module). `'i'` stands for a signed integer, and `'d'` stands for a double-precision float. Because this data is shared directly with the OS memory, Python needs to know exactly how many bytes to allocate.

Q3: Which is faster for IPC (Inter-Process Communication): a `Queue` or `Shared Memory` (`Value`/`Array`)?
A3: Shared Memory is significantly faster. A `Queue` requires serializing (pickling) the object, sending it through an OS pipe, and deserializing it on the other side. Shared memory (`Value` or `shared_memory.SharedMemory`) reads and writes directly to the physical RAM, avoiding serialization overhead entirely. However, Queues are much easier and safer to use for complex data structures and event-driven architectures.
"""