import re
import sys

def main():
    print(parse(input("HTML: ")))

def parse(s):
    if url := re.search(r"src=\"(https?://)(?:www\.)?youtube\.com/embed/(\w+)\"", s, re.IGNORECASE):
        return f"https://youtu.be/{url.group(2)}"

if __name__ == "__main__":
    main()
