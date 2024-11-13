import sys
from pyfiglet import  Figlet
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
    f = sys.argv[2]
    if f not in fonts:
        print(f"{f} was not found.")
        sys.exit(1)

elif len(sys.argv) == 1:
    f = fonts[random.randint(0, len(fonts) - 1)]
else:
    print("Invalid usage")
    sys.exit(1)

text = input("Input: ")
figlet.setFont(font=f)
print(figlet.renderText(text))
sys.exit(0)