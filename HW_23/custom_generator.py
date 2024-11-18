import random
import nltk
from nltk.corpus import words

nltk.download("words")


def custom_generator(words_count):
    max_words = 10_000
    if words_count > max_words:
        raise ValueError(f"max count of words must be greater than {max_words}")
    word_list = [word for word in set(words.words()) if word.isalpha()]
    random.shuffle(word_list)
    for i in range(words_count):
        yield word_list[i]


for word in custom_generator(10000):
    print(word)
