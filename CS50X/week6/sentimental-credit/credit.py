# TODO
from cs50 import get_int
from sys import exit

number = get_int("Number: ")
text = str(number)
length = len(text)
luhnsum = 0

# Luhn’s Algorithm
## ref from Stackoverflow (https://stackoverflow.com/questions/51121911/iterate-over-every-nth-element-in-string-in-loop-python)
## ref from codeacademy (https://discuss.codecademy.com/t/how-can-i-loop-through-text-starting-from-the-last-character/339346)

## Multiply every other digit by 2, starting with the number’s second-to-last digit, and then add those products’ digits together.
for c in text[-2::-2]:
    digits = int(c) * 2
    for d in str(digits):
        luhnsum += int(d)

## Add the sum to the sum of the digits that weren’t multiplied by 2.
for c in text[::-2]:
    luhnsum += int(c)

## If the total’s last digit is 0 (or, put more formally, if the total modulo 10 is congruent to 0), the number is valid!
if luhnsum % 10 != 0:
    print("INVALID")
    exit(1)

# American Express uses 15-digit numbers, start with 34 or 37
if length == 15 and text[:2] in ["34", "37"]:
    print("AMEX")
    exit(0)

# MasterCard uses 16-digit numbers, start with 51, 52, 53, 54, or 55
elif length == 16 and text[:2] in ["51", "52", "53", "54", "55"]:
    print("MASTERCARD")
    exit(0)

# Visa uses 13- and 16-digit numbers, start with 4
elif (length == 13 or length == 16) and text[0] == "4":
    print("VISA")
    exit(0)

else:
    print("INVALID")
    exit(1)
