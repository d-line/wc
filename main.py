import argparse
import sys


def safe_read_file(filename, mode="r", encoding="utf-8"):
    """Safely read a file, handling common errors."""
    try:
        with open(filename, mode, encoding=encoding if mode == "r" else None) as f:
            return f
    except FileNotFoundError:
        print(f"ccwc: {filename}: No such file or directory", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ccwc: Error reading {filename}: {e}", file=sys.stderr)
        sys.exit(1)


def count_bytes(filename):
    """Count the number of bytes in a file."""
    with safe_read_file(filename, mode="rb") as f:
        return len(f.read())


def count_lines(filename):
    """Count the number of lines in a file."""
    with safe_read_file(filename) as f:
        return sum(1 for _ in f)


def count_words(filename):
    """Count the number of words in a file."""
    with safe_read_file(filename) as f:
        return sum(len(line.split()) for line in f)


def count_chars(filename):
    """Count the number of characters in a file."""
    with safe_read_file(filename) as f:
        return sum(len(line) for line in f)


def main():
    parser = argparse.ArgumentParser(prog="ccwc", description="Count bytes in files")
    parser.add_argument("-c", "--bytes", action="store_true", help="Count bytes")
    parser.add_argument("-l", "--lines", action="store_true", help="Count lines")
    parser.add_argument("-w", "--words", action="store_true", help="Count words")
    parser.add_argument("-m", "--chars", action="store_true", help="Count characters")
    parser.add_argument("files", nargs="+", help="File(s) to process")

    args = parser.parse_args()

    # Map options to counting functions
    counters = {
        "bytes": count_bytes,
        "lines": count_lines,
        "words": count_words,
        "chars": count_chars,
    }

    option = next((key for key, enabled in vars(args).items() 
                   if enabled and key in counters), None)

    if not option:
        print("Usage: ccwc [-c|-l|-w|-m] <filename>", file=sys.stderr)
        sys.exit(1)

    counter = counters[option]
    for filename in args.files:
        count = counter(filename)
        print(f"{count} {filename}")


if __name__ == "__main__":
    main()
