
from stats import count_book_words, count_book_letters, sorted_dict_list

def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ---------")
    print(f"Found {count_book_words(
        "./books/frankenstein.txt")} total words")
    print("--------- Character Count -------")
    #print(f"{sorted_dict_list(("./books/frankenstein.txt"))}")
    for k,v in sorted_dict_list("./books/frankenstein.txt"):
        if k.isalpha(): print(f"{k}: {v}")
    print("============= END ===============")

main()