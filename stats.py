def count_book_words(file_path):
    num_words = 0
    with open(file_path) as f:
        book = f.read().split()
    for word in book:
        num_words += 1
    return num_words

def common_book_words(file_path):
    dict_words = {}
    with open(file_path) as f:
        book = f.read().split()
    for word in book:
            if word.lower() in dict_words:
                dict_words[word.lower()] += 1
            else:
                dict_words[word.lower()] = 1
    return dict_words

def count_book_letters(file_path):
    num_letters = {}
    with open(file_path) as f:
        book = f.read().split()
    for word in book:
        for letter in word:
            if letter.lower() in num_letters:
                num_letters[letter.lower()] += 1
            else:
                num_letters[letter.lower()] = 1
    return num_letters


def sorted_dict_list(file_path):
    dict = count_book_letters(file_path)
    return sorted(
        dict.items(),key=lambda item:
        item[1], reverse=True)

def sorted_dict_word_list(file_path):
    dict = common_book_words(file_path)
    return sorted(
        dict.items(),key=lambda item:
        item[1], reverse=True)