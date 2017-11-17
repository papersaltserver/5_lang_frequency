from collections import Counter
import sys
import re


def load_data(filepath):
    with open(filepath) as text_file:
        text_data = text_file.read()
    return text_data


def get_most_frequent_words(text, frequent_words_number):
    word_list = re.sub(r'\W+_', '', text).lower().split()
    words_in_text_counter = Counter(word_list)
    most_common_list_counter = words_in_text_counter.most_common(
        frequent_words_number)
    most_common_list = [word for (word, _) in most_common_list_counter]
    return most_common_list


if __name__ == '__main__':
    text_data = load_data(sys.argv[1])
    frequent_words_number = 10
    most_frequent_words = get_most_frequent_words(
        text_data, frequent_words_number)
    print("The list of {} most frequent words in your text in \
    descending order: ".format(frequent_words_number))
    for frequent_word in most_frequent_words:
        print(frequent_word)
