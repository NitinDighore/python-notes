from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Masala chai is ready")



if __name__ == '__main__':
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()
    print(queue.get()) # Output: Masala chai is ready

    print("\n--- TRICK CODING EXAMPLES ---")

    # Trick 1: Using multiprocessing.Pipe for fast 2-way communication
    print("\n1. multiprocessing.Pipe (Fast 1-to-1 IPC):")
    from multiprocessing import Pipe
    def send_order(conn):
        conn.send("Order: 1 Lemon Tea")
        conn.close()
        
    parent_conn, child_conn = Pipe()
    p2 = Process(target=send_order, args=(child_conn,))
    p2.start()
    print(f"Received via Pipe: {parent_conn.recv()}") # Output: Received via Pipe: Order: 1 Lemon Tea
    p2.join()

    # Trick 2: Safe Queue reading with timeouts
    print("\n2. Safe Queue reading with timeouts:")
    import queue as std_queue # The standard queue module for the Empty exception
    q = Queue()
    q.put("Only one cup")
    print(q.get()) # Works fine
    try:
        # If we just did q.get(), the program would hang infinitely waiting for data!
        # timeout=1 forces it to give up after 1 second
        q.get(timeout=1)
    except std_queue.Empty:
        print("Queue is empty, stopped waiting!") # Output: Queue is empty, stopped waiting!

    # Trick 3: Multiple Producers sharing one Queue
    print("\n3. Multiple Producers to a single Queue:")
    def worker(q_out, worker_id):
        q_out.put(f"Result from Worker {worker_id}")

    shared_q = Queue()
    workers = [Process(target=worker, args=(shared_q, i)) for i in range(3)]
    for w in workers: w.start()
    for w in workers: w.join()

    # Read all results safely
    while not shared_q.empty():
        print(shared_q.get()) 
    # Output: Result from Worker 0 \n Result from Worker 1 \n Result from Worker 2 (order may vary)

"""
--- NOTES: Inter-Process Communication (IPC) and Queues ---

1. Inter-Process Communication (IPC):
   - Because OS processes have entirely isolated memory spaces, they cannot share standard Python variables (like a normal `list` or `dict`). If Process A appends to a list, Process B will not see it.
   - To send data from one process to another, you must use IPC mechanisms. `multiprocessing.Queue` is the safest and most commonly used IPC tool in Python.

2. `multiprocessing.Queue`:
   - It is a thread-safe and process-safe First-In, First-Out (FIFO) data structure.
   - Under the hood, it uses an OS pipe and a background thread to serialize (pickle) the Python objects and send them across process boundaries safely.

3. Latest Python Features:
   - **Shared Memory (`multiprocessing.shared_memory`) (Python 3.8+)**: While Queues are great, pickling large objects (like massive NumPy arrays or images) to send over a queue is very slow. Python 3.8 introduced direct Shared Memory blocks, allowing multiple processes to read and write to the exact same physical block of RAM without any serialization overhead, drastically improving IPC performance for big data.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: What is the difference between `queue.Queue` and `multiprocessing.Queue`?
A1: `queue.Queue` is only thread-safe; it is used to share data between threads within the *same* process. `multiprocessing.Queue` is process-safe; it handles the complex OS-level locking and data serialization (pickling) required to safely send data between *different* isolated processes.

Q2: What happens if you call `queue.get()` on an empty queue?
A2: By default, `queue.get()` is a blocking operation. The calling process will freeze and wait infinitely until another process puts something into the queue. To avoid deadlocks, you should use `queue.get(block=False)` (or `queue.get_nowait()`) or provide a timeout like `queue.get(timeout=3)`.

Q3: When should you use a `Pipe` instead of a `Queue`?
A3: `Pipe` is generally faster than `Queue`, but it strictly only connects two endpoints (1-to-1 communication). A `Queue` is designed for Multiple-Producers/Multiple-Consumers (M-to-N communication). Use `Pipe` for simple two-way data passing between a parent and child, and `Queue` for distributing tasks among a pool of workers.
"""