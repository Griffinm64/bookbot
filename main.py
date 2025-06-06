
from stats import count_book_words,count_book_letters, sorted_dict_word_list, sorted_dict_list, common_book_words
import sys

#Checks for required arguments (2)
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_file_path = sys.argv[1]

def main():
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_file_path}")

    print("----------- Word Count ---------")
    print(f"Found {count_book_words(
        book_file_path)} total words")

    print("--------- Character Count -------")
    for k,v in sorted_dict_list(book_file_path):
        if k.isalpha(): print(f"{k}: {v}")

    print("---------- Common Words --------")
    for k,v in sorted_dict_word_list(book_file_path):
        print(f"{k}: {v}")
    print("============= END ===============")

main()