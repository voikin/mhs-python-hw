import math
import time
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def integrate_chunk(f, a, step, start, end):
    acc = 0.0
    for i in range(start, end):
        acc += f(a + i * step) * step
    return acc


def integrate_parallel(
    f,
    a,
    b,
    *,
    n_jobs=1,
    n_iter=10_000_000,
    executor_cls=ThreadPoolExecutor,
):
    step = (b - a) / n_iter
    chunk_size = n_iter // n_jobs

    ranges = []
    for i in range(n_jobs):
        start = i * chunk_size
        end = n_iter if i == n_jobs - 1 else (i + 1) * chunk_size
        ranges.append((start, end))

    start_time = time.perf_counter()

    with executor_cls(max_workers=n_jobs) as executor:
        futures = [
            executor.submit(integrate_chunk, f, a, step, start, end)
            for start, end in ranges
        ]
        result = sum(f.result() for f in futures)

    elapsed = time.perf_counter() - start_time
    return result, elapsed


def main():
    cpu_num = os.cpu_count()
    max_jobs = cpu_num * 2

    result_logs = []

    for n_jobs in range(1, max_jobs + 1):
        _, t_thread = integrate_parallel(
            math.cos,
            0,
            math.pi / 2,
            n_jobs=n_jobs,
            executor_cls=ThreadPoolExecutor,
        )

        _, t_process = integrate_parallel(
            math.cos,
            0,
            math.pi / 2,
            n_jobs=n_jobs,
            executor_cls=ProcessPoolExecutor,
        )

        result_log = (
            f"jobs={n_jobs:<2} | threads={t_thread:.3f}s | processes={t_process:.3f}s"
        )
        print(result_log)
        result_logs.append(result_log)

    with open("artefacts/task_4_2_results.txt", "w", encoding="utf-8") as f:
        f.write("\n".join(result_logs) + "\n")


if __name__ == "__main__":
    main()
