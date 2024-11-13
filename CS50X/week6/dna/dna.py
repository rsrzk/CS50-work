import csv
import sys


def main():
    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        print("Usage: python dna.py data.csv sequence.txt")
        sys.exit(1)

    database_f = sys.argv[1]
    sequence_f = sys.argv[2]

    # TODO: Read database file into a variable
    with open(database_f, "r") as file:
        database = []
        reader = csv.DictReader(file)
        ## reference: https://www.geeksforgeeks.org/get-column-names-from-csv-using-python/
        rows = list(reader)
        dict_temp = dict(rows[0])
        columns = list(dict_temp.keys())
        for row in rows:
            database.append(row)

    # TO REMOVE
    # print("Columns: " + str(columns))
    # print("Database: " + str(database))

    # TODO: Read DNA sequence file into a variable
    with open(sequence_f, "r") as file:
        sequence = file.read()
        # TO REMOVE
        # print(sequence)

    # TODO: Find longest match of each STR in DNA sequence
    person = {}
    for str_seq in columns[1:]:
        person[str_seq] = longest_match(sequence, str_seq)
        # print(str_seq + ": " + str(person[str_seq]))

    # TODO: Check database for matching profiles
    num_sequences = len(columns[1:])
    for row in database:
        check = 0
        for str_seq in columns[1:]:
            if int(row[str_seq]) == person[str_seq]:
                check += 1
            else:
                break
        if check == num_sequences:
            print(row["name"])
            sys.exit(0)
    print("No match")
    return sys.exit(0)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()
