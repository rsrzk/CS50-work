import sys
from PIL import Image, ImageOps
from os import path

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    shirt_path = "shirt.png"

    person_path, new_path = sys.argv[1].lower(), sys.argv[2].lower()

    _, person_ext = path.splitext(person_path)
    _, new_ext = path.splitext(new_path)

    if person_ext not in ['.jpg', '.jpeg', '.png']:
        sys.exit("Invalid input")

    if new_ext not in ['.jpg', '.jpeg', '.png']:
        sys.exit("Invalid output")

    if new_ext != person_ext:
        sys.exit("Input and output have different extensions")

    try:
        overlay(shirt_path, person_path, new_path)
    except FileNotFoundError:
        sys.exit(f"Input does not exist")

def overlay(shirt_path, person_path, new_path):
    with Image.open(shirt_path) as shirt, Image.open(person_path) as person:
        person = ImageOps.fit(person, shirt.size)
        person.paste(shirt, shirt)
        person.save(new_path)


if __name__ == "__main__":
    main()
