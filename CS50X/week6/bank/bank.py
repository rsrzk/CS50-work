greet = input("Greeting: ")
greet = greet.lower()
greet = greet.lstrip()
if 'hello' in greet:
    print('$0')
elif 'h' in greet[0:1]:
    print('$20')
else:
    print('$100')