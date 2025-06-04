
from stats import count_book_words

def main():
    print(f"{count_book_words("./books/frankenstein.txt")} words found in the document")

main()