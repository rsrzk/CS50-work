groceries = {}
while(True):
    try:
        item = input().upper()
    except EOFError:
        print()
        break
    if item:
        if item in groceries:
            groceries[item] += 1
        else:
            groceries[item] = 1

keys = list(groceries.keys())
keys.sort()
sorted_groceries = {i: groceries[i] for i in keys}

for grocery in sorted_groceries:
    print(f"{sorted_groceries[grocery]} {grocery}")
