def main():
    text = input("Input: ")
    text = convert(text)
    print(text)

def convert(input):
    return input.replace(":)", "🙂").replace(":(", "🙁")

main()
