import sys
import random

def main():
    level = get_level()
    ans = random.randint(1, level)
    while(True):
        guess = get_guess(level)
        check_ans(guess, ans)

def get_level():
    while(True):
        n = input("Level: ")
        try:
            if int(n) > 0:
                return int(n)
        except ValueError:
            pass

def get_guess(level):
    while(True):
        guess = input("Guess: ")
        try:
            if 1 <= int(guess) <= level:
                return int(guess)
        except ValueError:
            pass

def check_ans(guess, ans):
    match guess:
        case _ if guess < ans:
            print("Too small!")
        case _ if guess > ans:
            print("Too large!")
        case ans:
            sys.exit("Just right!")

main()
