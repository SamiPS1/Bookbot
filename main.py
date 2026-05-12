import sys

def get_book_text(file_path: str):
    with open(file_path, "r") as f:
        return f.read()

from stats import word_count
from stats import num_characters
from stats import sort_by

def main():
    # require exactly one argument: path to book file
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    book_text = get_book_text(book_path)

    words = word_count(book_text)
    chars = num_characters(book_text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at: {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    
    # show sorted character frequencies instead of printing the function itself
    sorted_chars = sort_by(chars)
    for ch, cnt in sorted_chars.items():
        if ch.isalpha():  # only print alphabetic characters
            print(f"{ch}: {cnt}")

main()