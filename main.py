import sys

from stats import get_num_appearances, get_num_words, sort_items


def main():
    # print(get_book_text("books/frankenstein.txt"))
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    num_words = get_num_words(get_book_text(book))
    num_appearances = get_num_appearances(get_book_text(book))
    pretty_print = sort_items(num_appearances)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in pretty_print:
        if i["char"].isalpha():
            print(f"{i['char']}: {i['num']}")
        else:
            continue
    print("============= END ===============")


def get_book_text(filepath_str):
    with open(filepath_str) as f:
        text = f.read()
    return text


main()
