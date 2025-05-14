import sys

from stats import get_num_words, get_count_per_char, get_sorted_list

def get_book_text(path):
    with open(path) as f:
        text = f.read()
    return text

def main():
    
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    book_text = get_book_text(book)
    num_words = get_num_words(book_text)
    count_per_char = get_count_per_char(book_text)
    sorted_list = get_sorted_list(count_per_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")

main()