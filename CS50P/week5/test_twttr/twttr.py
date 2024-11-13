def main():
    text = input("Input: ")
    print("Output: " + shorten(text))

def shorten(word):
    new_word = ""
    vowels = "aeiouAEIOU"
    for char in word:
        is_vowel = False
        for vowel in vowels:
            if char == vowel:
                is_vowel = True
        if not is_vowel:
            new_word += char
    return new_word


if __name__ == "__main__":
    main()
