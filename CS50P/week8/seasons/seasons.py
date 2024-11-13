from datetime import date
import re
import sys
import inflect


def main():
    dob = input("Date of birth: ")
    today = date.today()
    try:
        mins = get_mins(dob, today)
    except ValueError:
        sys.exit("Invalid date")
    except TypeError:
        sys.exit("Missing value")
    else:
        print(get_text(mins))


def get_mins(dob, today):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", dob):
        delta = today - date.fromisoformat(dob)
        return round(delta.total_seconds()/60)
    else:
        raise ValueError()

def get_text(mins):
    p = inflect.engine()
    return f"{p.number_to_words(mins, andword="").capitalize()} minutes"

if __name__ == "__main__":
    main()
