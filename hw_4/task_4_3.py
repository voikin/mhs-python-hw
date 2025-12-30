import multiprocessing as mp
import time
import sys
import codecs
from datetime import datetime


def log_write(message: str, lock: mp.Lock):
    timestamp = datetime.now().strftime("%H:%M:%S")
    with lock:
        with open("artefacts/task_4_3_log.txt", "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {message}\n")


def process_a(input_queue: mp.Queue, output_queue: mp.Queue, lock: mp.Lock):
    buffer = []

    while True:
        msg = input_queue.get()
        if msg is None:
            break

        log_write(f"MAIN -> A: {msg}", lock)

        buffer.append(msg)

        while buffer:
            original = buffer.pop(0)
            lowered = original.lower()

            output_queue.put(lowered)

            log_write(f"A -> B: {lowered}", lock)

            time.sleep(5)


def process_b(input_queue: mp.Queue, result_queue: mp.Queue, lock: mp.Lock):
    while True:
        msg = input_queue.get()
        if msg is None:
            break

        encoded = codecs.encode(msg, "rot_13")
        print(f"[B stdout] {encoded}", flush=True)

        log_write(f"B -> STDOUT: {encoded}", lock)

        timestamp = datetime.now().strftime("%H:%M:%S")
        result_queue.put((timestamp, encoded))

        log_write(f"B -> MAIN: {encoded}", lock)


def main():
    queue_main_to_a = mp.Queue()
    queue_a_to_b = mp.Queue()
    queue_b_to_main = mp.Queue()
    lock = mp.Lock()

    with open("artefacts/task_4_3_log.txt", "w", encoding="utf-8"):
        pass

    proc_a = mp.Process(
        target=process_a,
        args=(queue_main_to_a, queue_a_to_b, lock),
        daemon=True,
    )
    proc_b = mp.Process(
        target=process_b,
        args=(queue_a_to_b, queue_b_to_main, lock),
        daemon=True,
    )

    proc_a.start()
    proc_b.start()

    print("Введите строки (exit для выхода):")

    try:
        while True:
            line = sys.stdin.readline().strip()
            if line == "exit":
                break

            log_write(f"STDIN -> MAIN: {line}", lock)

            queue_main_to_a.put(line)

            while not queue_b_to_main.empty():
                queue_b_to_main.get()

    except KeyboardInterrupt:
        pass
    finally:
        queue_main_to_a.put(None)
        queue_a_to_b.put(None)

        proc_a.join(timeout=5)
        proc_b.join(timeout=5)


if __name__ == "__main__":
    mp.set_start_method("spawn")
    main()
