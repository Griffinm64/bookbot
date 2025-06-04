def count_book_words(file_path):
    num_words = 0
    with open(file_path) as f:
        book = f.read().split()
    for word in book:
        num_words += 1
    return num_words