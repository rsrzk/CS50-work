import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    count = 0
    if numbers := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for number in numbers.groups():
            if 0 <= int(number) <= 255:
                count += 1
    if count == 4:
        return True
    else:
        return False

if __name__ == "__main__":
    main()
