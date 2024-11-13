import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    try:
        print(tabulate(table(sys.argv[1]), header(sys.argv[1]), tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

def header(path):
    with open(path) as file:
        reader = csv.reader(file)
        return next(reader)

def table(path):
    rows = []
    with open(path) as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)
    return rows[1:]


if __name__ == "__main__":
    main()
