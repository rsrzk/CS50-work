# Contract Management System

#### Video demo: https://youtu.be/3wIdySRkxiE

#### Description:

Welcome to the Contract Management System, a simple command-line application written in Python for managing and performing basic operations on text-based contract files.

## Project Overview

The Contract Management System allows users to interact with text files containing simplified contracts. Users can perform various operations on these contract files, such as extracting information, and editing the documents using a built-in command-line editor.

## Usage

Upon cloning the project repository, install the required dependencies:
```
pip install -r requirements.txt
```

Then follow the steps below:
1. Run the main script:

    ```
    python project.py
    ```

2. The Contract Management System will prompt you to choose a contract file and select an operation.

3. Follow the on-screen instructions to extract key information, edit the document, or navigate the file directory.

4. Exit the system when done.

Note: There are also downloadable files for use of the NLTK module written into contract_parser.py. When running the programme, these files should be automatically downloaded if not already available. For reference, this is the script containing the download commands:
- nltk.download('punkt')
- nltk.download('averaged_perceptron_tagger')



## Project Structure

- `project.py`: The main script serving as the entry point for the application. It handles user interaction and delegates tasks/operations to other modules.
- `contract_parser.py`: Module for extracting key information from contract files.
- `editor.py`: Module for editing contract documents.
- `files/`: Default directory containing sample contract files.


## `contract_parser.py`

This module is responsible for extracting key information from contract files. It uses NLTK for tokenization and part-of-speech tagging to identify names and regex to extract dates in the contract content. At this stage, the accuracy and quality of the extractions need further improvement. The names extraction can be improved by testing NLTK's other functions while the date extraction can be improved by adding more regex patterns as it is currently not comprehensive. The module can be used by either accessing it from the the operations menu in the main application by first calling:

```
python project.py
```
or through calling the module as a standalone python file and by supplying the text document to be accessed as an additional argument, i.e.:

```
python contract_parser.py directory/filename
```

## `editor.py`

This module allows for direct editing of the contract text files in the command line interface. It uses a library built in to Python called curses. Users may directly insert text into the document in line, add new lines, delete characters and scroll through the document. At the end of editing, the user will be prompted to either save the document as a new file, overwrite the existing document or to go back to the main application. Users may access the functions of this module either from the operations menu in the main application by first calling:
```
python project.py
```
or through calling the module as a standalone python file and by supplying the text document to be accessed as an additional argument, i.e.:

```
python editor.py directory/filename
```
Credits to the following blog for the tutorial on building the CLI editor: https://wasimlorgat.com/posts/editor.html
