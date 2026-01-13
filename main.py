import argparse
import sys


def count_bytes(filename):
    """Count the number of bytes in a file."""
    try:
        with open(filename, "rb") as f:
            return len(f.read())
    except FileNotFoundError:
        print(f"ccwc: {filename}: No such file or directory", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"ccwc: Error reading {filename}: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(prog="ccwc", description="Count bytes in files")
    parser.add_argument("-c", "--bytes", action="store_true", help="Count bytes")
    parser.add_argument("files", nargs="+", help="File(s) to process")

    args = parser.parse_args()

    if args.bytes:
        for filename in args.files:
            byte_count = count_bytes(filename)
            print(f"{byte_count} {filename}")
    else:
        print("Usage: ccwc -c <filename>", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
