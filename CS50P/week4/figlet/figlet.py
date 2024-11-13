import sys
from pyfiglet import Figlet
import random

if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    font = sys.argv[2]
elif len(sys.argv) == 1:
    figlet = Figlet()
    font = random.choice(figlet.getFonts())
else:
    sys.exit("Invalid usage")


try:
    f = Figlet(font=font)
except:
    sys.exit("Invalid usage")

input = input("Input: ")
print(f.renderText(input))
