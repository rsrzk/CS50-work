# TODO

from cs50 import get_string

text = get_string("Text: ")
letters = 0
words = 0
sentences = 0
letterseq = False
sentenceseq = False

for c in text:
    # any sequence of characters separated by spaces should count as a word
    if c == " ":
        letterseq = False

    # any occurrence of a period, exclamation point, or question mark indicates the end of a sentence
    if c in [".", "!", "?"]:
        letterseq = False
        sentenceseq = False

    # any lowercase character from a to z or any uppercase character from A to Z
    if c.isalpha():
        letters += 1
        if letterseq == False:
            words += 1
        if sentenceseq == False:
            sentences += 1
        letterseq = True
        sentenceseq = True

# L is the average number of letters per 100 words in the text
L = letters / words * 100

# S is the average number of sentences per 100 words in the text
S = sentences / words * 100

# Coleman-Liau index
index = 0.0588 * L - 0.296 * S - 15.8

if index >= 16:
    print("Grade 16+")
elif index < 1:
    print("Before Grade 1")
else:
    print("Grade " + str(round(index)))
