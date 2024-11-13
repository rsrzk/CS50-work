def main():
    var = input("camelCase: ")
    print("snake_case: " + convert(var))

def convert(text):
    new_text = ""
    for char in text:
        if char.isupper():
            new_text += "_" + char.lower()
        else:
            new_text += char
    return new_text


if __name__ == "__main__":
    main()
