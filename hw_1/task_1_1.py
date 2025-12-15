import sys


def number_lines(input_file, line_number_start=1):
    line_number = line_number_start
    for line in input_file:
        print(f"{line_number:6}\t{line}", end="")
        line_number += 1
    return line_number


def main():
    if len(sys.argv) > 1:
        for filename in sys.argv[1:]:
            with open(filename, "r", encoding="utf-8") as f:
                number_lines(f)
    else:
        number_lines(sys.stdin)


if __name__ == "__main__":
    main()
