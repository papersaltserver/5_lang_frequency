from collections import Counter
import sys


def load_data(filepath):
    with open(filepath) as text_file:
        text_data = text_file.read()
    return text_data


def get_most_frequent_words(text):
    text_list = text.strip("\\\",.\'\n").lower().split()
    text_counter = Counter(text_list)
    most_common_list_counter = text_counter.most_common(10)
    most_common_list = [list_tuple[0] for list_tuple in most_common_list_counter]
    return most_common_list


if __name__ == '__main__':
    text_data = load_data(sys.argv[1])
    most_frequent_words = get_most_frequent_words(text_data)
    for frequent_word in most_frequent_words:
        print(frequent_word)
