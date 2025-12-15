import sys


def count_stats(content):
    text = content.decode()

    lines = text.count("\n")
    words = len(text.split())
    bytes_count = len(content)

    return lines, words, bytes_count


def process_file(filename):
    if filename:
        with open(filename, "rb") as f:
            content = f.read()
    else:
        content = sys.stdin.buffer.read()

    return count_stats(content)


def format_output(lines, words, bytes_count, filename=None):
    output = f"{lines:8}{words:8}{bytes_count:8}"
    if filename:
        output += f" {filename}"
    print(output)


def main():
    if len(sys.argv) > 1:
        total_lines = 0
        total_words = 0
        total_bytes = 0

        for filename in sys.argv[1:]:
            lines, words, bytes_count = process_file(filename)
            format_output(lines, words, bytes_count, filename)

            total_lines += lines
            total_words += words
            total_bytes += bytes_count

        if len(sys.argv) > 2:
            format_output(total_lines, total_words, total_bytes, "total")
    else:
        lines, words, bytes_count = process_file(None)
        format_output(lines, words, bytes_count)


if __name__ == "__main__":
    main()
