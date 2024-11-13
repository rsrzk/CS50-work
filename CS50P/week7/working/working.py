import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if times := re.search(r"^(\d\d?)(?::(\d{2}))? ([AP]M) to (\d\d?)(?::(\d{2}))? ([AP]M)$", s):
        return f"{change(times.group(1), times.group(2), times.group(3))} to {change(times.group(4), times.group(5), times.group(6))}"
    else:
        raise ValueError("Invalid format")

def change(hour, min, meridiem):
    if not min:
        min = ":00"
    elif 0 <= int(min) <= 59:
        min = f":{min}"
    else:
        raise ValueError("Invalid minute time")

    add = 12 if meridiem == "PM" else 0

    if 1 <= int(hour) <= 11:
        hour = f"{int(hour) + add:02}"
    elif hour == "12":
        hour = f"{int(hour) + add - 12:02}"
    else:
        raise ValueError("Invalid hour time")

    return hour + min


if __name__ == "__main__":
    main()
