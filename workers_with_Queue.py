import logging
import queue
import threading
import time

logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

def worker(tasks):
    while True:
        task = tasks.get()
        if task is None:
            tasks.task_done()
            break
        logging.info(f"processing {task}")
        time.sleep(1)
        tasks.task_done()

tasks = queue.Queue()
for task in ["task1", "task2", "task3", "task4", "task5"]:
    tasks.put(task)

num_workers = 2
for _ in range(num_workers):
    tasks.put(None)

threads = [
threading.Thread(target=worker, args=(tasks,)) for _ in range(num_workers)
]
for thread in threads:
    thread.start()

tasks.join()
for thread in threads:
    thread.join()

# Output:
# Thread-1 (worker) processing task1
# Thread-2 (worker) processing task2
# Thread-1 (worker) processing task3
# Thread-2 (worker) processing task4
# Thread-1 (worker) processing task5