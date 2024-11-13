import sys
import inflect

names = []
while(True):
    try:
        name = input("Name: ")
    except EOFError:
        print()
        break
    if name:
        names.append(name)

if len(names) == 0:
    sys.exit


print("Adieu, adieu, to", end=" ")
p = inflect.engine()
print(p.join(names))

# OLD CODE
# if len(names) == 1:
#     print(names[0])
# elif len(names) == 2:
#     print(names[0], "and", names[1])
# else:
#     for n in range(len(names)):
#         if n == len(names) - 1:
#             print(f"and {names[n]}")
#         else:
#             print(names[n], end=", ")
