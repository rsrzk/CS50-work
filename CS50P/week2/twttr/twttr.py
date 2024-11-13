def main():
    text = input("Input: ")
    print("Output: " + convert(text))

def convert(text):
    new_text = ""
    vowels = "aeiouAEIOU"
    for char in text:
        is_vowel = False
        for vowel in vowels:
            if char == vowel:
                is_vowel = True
        if not is_vowel:
            new_text += char
    return new_text


if __name__ == "__main__":
    main()
