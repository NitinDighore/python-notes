import threading

lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    with lock_a:
        print("Task 1 acquired lock a") # Output: Task 1 acquired lock a
        with lock_b:
            print("Task 1 acquired lock b") # Output: Task 1 acquired lock b

def task2():
    with lock_b:
        print("Task 2 acquired lock b") # Output: Task 2 acquired lock b
        with lock_a:
            print("Task 2 acquired lock a") # Output: Task 2 acquired lock a

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()

t1.join()
t2.join()

# Note: Without `time.sleep()` forcing a context switch, Task 1 usually finishes entirely
# before Task 2 even starts, completely bypassing the intended deadlock by pure luck!

print("\n--- TRICK CODING EXAMPLES ---")

import time

# Trick 1: Guaranteeing the Deadlock (Conceptual)
print("\n1. How the deadlock actually triggers:")
# If we added `time.sleep(0.1)` inside task1 right after acquiring lock_a, 
# it would force Python to switch to task2. Task 2 would acquire lock_b.
# Then, Task 1 waits for lock_b (held by Task 2), and Task 2 waits for lock_a (held by Task 1).
# Result: INFINITE FREEZE.

# Trick 2: Fixing Deadlocks using "Strict Lock Ordering"
print("\n2. Fixing Deadlocks (Strict Lock Ordering):")
def safe_task2():
    # SOLUTION: Always acquire locks in the exact same global order!
    # If both tasks acquire 'a' then 'b', a circular wait is mathematically impossible.
    with lock_a: 
        print("Safe Task 2 acquired lock a")
        with lock_b:
            print("Safe Task 2 acquired lock b")

t3 = threading.Thread(target=safe_task2)
t3.start(); t3.join()

# Trick 3: Fixing Deadlocks using "Timeouts"
print("\n3. Fixing Deadlocks (Timeouts & Backoffs):")
def timeout_task():
    # Instead of waiting forever with `with lock:`, we use `.acquire(timeout)`
    if lock_b.acquire(timeout=0.5):
        try:
            print("Timeout Task safely acquired lock_b")
        finally:
            lock_b.release()
    else:
        print("Could not acquire lock! Backing off instead of freezing.")

timeout_task()

"""
--- NOTES: Deadlocks in Concurrency ---

1. What is a Deadlock?
   - A deadlock is a state where two or more threads are blocked forever, each waiting for a resource (lock) that the other thread currently holds.
   - As shown in the original code's intent: Task 1 holds A and wants B. Task 2 holds B and wants A. Neither can proceed.

2. The Coffman Conditions:
   - For a deadlock to occur, 4 conditions must be met simultaneously:
     1. Mutual Exclusion (Locks can only be held by one thread).
     2. Hold and Wait (A thread holds a lock while waiting for another).
     3. No Preemption (The OS cannot forcefully take the lock away from a thread).
     4. Circular Wait (A chain of threads waiting on each other).
   - Fixing a deadlock simply requires breaking just ONE of these conditions (like enforcing Lock Ordering to break Circular Wait, or using Timeouts to break Hold and Wait).

3. Latest Python Features (Python 3.13 No-GIL):
   - **Free-Threading Implications**: In traditional Python, the GIL prevented true parallelism, meaning timing-based deadlocks were sometimes hard to reproduce without `time.sleep()`. With the GIL disabled in Python 3.13+, threads run truly simultaneously on multiple cores. This means race conditions and deadlocks will happen far more aggressively and predictably if your lock hierarchy is flawed.

--- INTERVIEW QUESTIONS & ANSWERS ---

Q1: How do you prevent deadlocks when dealing with multiple locks?
A1: The most robust way is to implement a strict "Lock Ordering" hierarchy. If all threads must always acquire `Lock A` before `Lock B`, and `Lock B` before `Lock C`, a circular wait becomes impossible, entirely preventing deadlocks.

Q2: What happens if I use `.join()` on a thread that is currently deadlocked?
A2: The `.join()` method will block infinitely. The main thread will freeze waiting for the deadlocked thread to finish, completely freezing your application.

Q3: Why doesn't standard Python (with the GIL) protect us from deadlocks?
A3: The GIL (Global Interpreter Lock) only protects the internal memory states of the Python interpreter (preventing simultaneous bytecode execution). It does NOT manage your custom `threading.Lock` objects. If you explicitly write logic that creates a circular wait with `threading.Lock`, Python will happily pause the threads and hang forever, regardless of the GIL.
"""