def main():
    while(True):
        fraction = input("Fraction: ")
        try:
            percentage = convert(fraction)
        except ValueError:
            print("Value Error")
        except ZeroDivisionError:
            print("Can't divide by zero")
        else:
            print(gauge(percentage))



def convert(fraction):
    num, _, denom = fraction.partition("/")
    if int(denom) == 0:
        raise ZeroDivisionError
    if int(num) > int(denom):
        raise ValueError
    else:
        percent = int(num)/int(denom)
    return int(round(percent*100))


def gauge(percent):
    if percent <= 1:
        return "E"
    elif percent >= 99:
        return "F"
    else:
        return f"{percent}%"


if __name__ == "__main__":
    main()



