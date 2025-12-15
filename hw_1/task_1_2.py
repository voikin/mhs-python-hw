import sys


def tail_lines(lines, n):
    return lines[-n:] if len(lines) > n else lines


def process_file(filename, n_lines):
    if filename:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    else:
        lines = sys.stdin.readlines()

    last_lines = tail_lines(lines, n_lines)

    for line in last_lines:
        print(line, end="")


def main():
    if len(sys.argv) > 1:
        multiple_files = len(sys.argv) > 2

        for i, filename in enumerate(sys.argv[1:], 1):
            if multiple_files:
                if i > 1:
                    print()
                print(f"==> {filename} <==")

            process_file(filename, 10)
    else:
        process_file(None, 17)


if __name__ == "__main__":
    main()
