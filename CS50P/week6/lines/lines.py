import sys

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    try:
        print(count_lines(sys.argv[1]))
    except FileNotFoundError:
        sys.exit("File does not exist")

def count_lines(path):
    with open(path) as file:
        count = 0
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                count +=1
        return count

if __name__ == "__main__":
    main()
