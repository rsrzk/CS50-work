import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x, y = generate_integer(level), generate_integer(level)
        for i in range(3):
            try:
                guess = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
            else:
                if guess == x + y:
                    score += 1
                    break
                else:
                    print("EEE")
            if i == 2:
                print(f"{x} + {y} = {x+y}")
    print(f"Score: {score}")


def get_level():
    while(True):
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    if not level in [1, 2, 3]:
        raise ValueError
    match level:
        case 1:
            return random.randint(0,9)
        case 2:
            return random.randint(10,99)
        case 3:
            return random.randint(100,999)


if __name__ == "__main__":
    main()
