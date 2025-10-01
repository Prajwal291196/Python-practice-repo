import threading
import queue
import time
import random

# Shared queue
task_queue = queue.Queue()

# Producer: generates tasks and puts them into the queue
def producer(num_tasks=10):
    for i in range(num_tasks):
        task = f"image_{i}.jpg"
        print(f"📤 Producer: Created task {task}")
        task_queue.put(task)
        time.sleep(random.uniform(0.1, 0.3))  # simulate task creation delay
    
    # Signal consumers to exit
    for _ in range(NUM_WORKERS):
        task_queue.put(None)  # special 'stop' signal
    print("✅ Producer: All tasks created and stop signals sent.")

# Consumer: worker thread that processes tasks
def consumer(worker_id):
    while True:
        task = task_queue.get()
        if task is None:
            print(f"🛑 Worker-{worker_id}: Received stop signal. Exiting.")
            task_queue.task_done()
            break

        print(f"⚙️  Worker-{worker_id}: Processing {task}...")
        time.sleep(random.uniform(0.5, 1.5))  # simulate processing time
        print(f"✅ Worker-{worker_id}: Finished {task}")
        task_queue.task_done()

# Number of worker threads
NUM_WORKERS = 3

def main():
    start_time = time.time()

    # Start consumer threads
    workers = []
    for i in range(NUM_WORKERS):
        t = threading.Thread(target=consumer, args=(i+1,))
        t.start()
        workers.append(t)

    # Start producer
    producer_thread = threading.Thread(target=producer, args=(12,))
    producer_thread.start()

    # Wait for all tasks to be processed
    producer_thread.join()
    task_queue.join()

    # Wait for all workers to finish
    for w in workers:
        w.join()

    print(f"🏁 All tasks completed in {time.time() - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
