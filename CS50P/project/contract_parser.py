# contract_parser.py

import nltk
from nltk import pos_tag
from nltk.tokenize import word_tokenize
import argparse
import re

# Download NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def extract_information(file):
    print(f"\nExtracting information from {file}")

    # Extract information by reading lines from the contract file
    with open(file, 'r') as f:
        content = f.read()

    # Tokenize the content
    words = word_tokenize(content)

    # Perform part-of-speech tagging
    pos_tags = pos_tag(words)

    # Extract names and proper nouns
    names = set()
    current_name=""

    for word, tag in pos_tags:
        if tag in ['NNP', 'NNPS']:
            current_name += " " + word if current_name else word
        elif current_name:
            names.add(current_name.strip())
            current_name = ""

    # Extract dates
    dates = {word for word in words if is_date(word)}

    if names:
        print("\nExtracted Names:", names)
    if dates:
        print("\nExtracted Dates:", dates)
    if not names and not dates:
        print("\nNo information to extract")


def is_date(word):
    date_formats = [
        r'\d{4}-\d{2}-\d{2}',    # YYYY-MM-DD
        r'\d{2}/\d{2}/\d{4}',    # MM/DD/YYYY
        r'\d{2}-\d{2}-\d{4}',    # DD-MM-YYYY
        r'\d{1,2}/\d{1,2}/\d{2}',  # MM/DD/YY or M/D/YY
        r'\d{2}/\d{1,2}/\d{1,2}',  # YY/MM/DD or YY/M/D
        r'\d{1,2}-\d{1,2}-\d{2}',  # DD-MM-YY or D-M-YY
        r'\d{2}-\d{1,2}-\d{1,2}',  # YY-DD-MM or YY-D-M
        # Add more formats as needed
    ]

    for date_format in date_formats:
        if re.match(date_format, word):
            return True
    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    args = parser.parse_args()
    file = args.filename
    extract_information(file)
