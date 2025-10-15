import sys
from stats import calculate_character_count, calculate_word_count, character_with_num

def get_book_text(path):
    with open(path, "r") as file:
        return file.read()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = calculate_word_count(text)
    char_count = calculate_character_count(text)
    sorted_chars = character_with_num(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count --------")
    for item in sorted_chars:
        char = item["char"]
        num = item["num"]
        print(f'{char}: {num}')
    print("============= END ===============")
