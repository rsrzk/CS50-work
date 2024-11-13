# project.py

from contract_parser import extract_information
from editor import edit_contract
import os
import sys

DEFAULT_DIRECTORY = "files"

def main():
    print("Welcome to the Contract Management System!")
    directory = DEFAULT_DIRECTORY
    while True:
        selected_file = file_selection(directory)
        operation_selection(selected_file, directory)


def file_selection(directory='.'):
    while True:
        files = list_txt_files(directory)
        print("\nAvailable contracts:")
        for i, file in enumerate(files, start=1):
            print(f"{i}. {file}")
        print("0. Change directory")
        while True:
            try:
                choice = int(input("Enter the number of the file you want to select: "))
                if choice != 0:
                    return select_file(choice, files, directory)
                else:
                    while True:
                        new_directory = input("Enter the path to the new directory folder: ")
                        if directory := change_directory(new_directory):
                            print(f"Directory changed to '{directory}'")
                            break
                        else:
                            print(f"Invalid. '{new_directory}' is not a folder directory or does not exist.")
                    break
            except (ValueError, IndexError):
                print("Invalid choice. Please enter a valid number.")


def list_txt_files(directory='.'):
    files = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            files.append(file)
    return files


def select_file(choice, files, directory='.'):
    file_name = files[choice - 1]
    print(f"Selected file: {file_name}")
    return f"{directory}/{file_name}"


def change_directory(new_directory):
    if os.path.isdir(new_directory):
        return new_directory


def operation_selection(selected_file, directory):
    while True:
        print("\nOperations:")
        print("1. Extract key information")
        print("2. Edit document")
        print("3. Go back to file directory")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            extract_information(selected_file)
        elif choice == '2':
            edit_contract(selected_file, directory)
        elif choice == '3':
            break
        elif choice == '4':
            print("Exiting the Contract Management System. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
