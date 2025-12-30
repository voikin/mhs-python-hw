import time
import threading
import multiprocessing


def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def run_sync(n: int, tasks: int):
    start = time.perf_counter()

    for _ in range(tasks):
        fib(n)

    end = time.perf_counter()
    return end - start


def run_threads(n: int, tasks: int):
    threads = []
    start = time.perf_counter()

    for _ in range(tasks):
        t = threading.Thread(target=fib, args=(n,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    end = time.perf_counter()
    return end - start


def run_processes(n: int, tasks: int):
    processes = []
    start = time.perf_counter()

    for _ in range(tasks):
        p = multiprocessing.Process(target=fib, args=(n,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    end = time.perf_counter()
    return end - start


if __name__ == "__main__":
    N = 35
    TASKS = 10

    sync_time = run_sync(N, TASKS)
    thread_time = run_threads(N, TASKS)
    process_time = run_processes(N, TASKS)

    results = (
        f"Sync:            {sync_time:.2f} seconds\n"
        f"Threading:       {thread_time:.2f} seconds\n"
        f"Multiprocessing: {process_time:.2f} seconds\n"
    )

    print(results)

    with open("artefacts/task_4_1_results.txt", "w", encoding="utf-8") as f:
        f.write(results)
