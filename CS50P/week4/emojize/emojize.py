import emoji

input = input("Input: ")
try:
    print(emoji.emojize(f'Output: {input}', language='alias'))
except:
    pass
