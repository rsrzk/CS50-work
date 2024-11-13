import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Both arguments must end with .csv")

    try:
        scourge(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Could not read{sys.argv[1]}")


def scourge(source_path, destination_path):
    with open(source_path) as source, open(destination_path, 'w') as destination:
        reader = csv.DictReader(source)
        writer = csv.DictWriter(destination, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in reader:
            last, first = row["name"].split(", ")
            writer.writerow({"first": first, "last": last, "house": row["house"]})

if __name__ == "__main__":
    main()
