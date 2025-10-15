# BookBot

BookBot is a simple Python command-line tool that analyzes text files (books) and reports word and character statistics.

## Features

- Counts the total number of words in a book.
- Counts the frequency of each alphabetical character (case-insensitive).
- Outputs a sorted list of character counts from most to least frequent.

## Usage

Run the script from the command line, providing the path to a text file:

```sh
python3 main.py <path_to_book>
```

Example:

```sh
python3 main.py books/frankenstein.txt
```

If no path is provided, the script prints a usage message and exits.

## Project Structure

- `main.py` — Main script to run the analysis.
- `stats.py` — Functions for counting words and characters.
- `books/` — Directory containing sample text files (books).

## Requirements

- Python 3.x

No external dependencies are required.
