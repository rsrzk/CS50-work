def main():
    time = input("What time is it? ")
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    add = 0
    if time.endswith(" a.m."):
        time = time.removesuffix(" a.m.")
    elif time.endswith(" p.m."):
        time = time.removesuffix(" p.m.")
        add = 12
    hour, colon, min = time.partition(":")
    return float(hour) + float(min)/60 + add


if __name__ == "__main__":
    main()
