def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # All vanity plates must start with at least two letters.
    two_letters = s[:2].isalpha()

    #  vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    length = 2 <= len(s) <= 6

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # The first number used cannot be a ‘0’.
    num_end = True
    start_zero = True
    for i in range(len(s) - 1):
        if s[i].isdigit() and s[i + 1].isalpha():
            num_end = False
        if s[i].isalpha() and s[i + 1].isdigit() and s[i + 1] == '0':
            start_zero = False

    # No periods, spaces, or punctuation marks are allowed.
    alnum = s.isalnum()

    return two_letters and length and num_end and alnum and start_zero

main()
