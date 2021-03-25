import io
import collections
import random


def words(file_name):
    language = []
    delimiter = ' '
    with open(file_name, encoding='utf-8') as file:
        for line in file.readlines():
            handle = io.StringIO(line)
            language += handle.getvalue().split(delimiter)
    return language


def transition_matrix(language):
    pairs = []
    for i in range(len(language)):
        for j in range(len(language)):
            if i != j:
                pairs.append([language[i], language[j]])
    d = collections.defaultdict(list)
    for pair in pairs:
        matches = [language[i + 2] for i, x in enumerate(language) if i < len(language) - 2 and x == pair[0] and language[i + 1] == pair[1]]
        if matches:
            d[tuple(pair)] = matches
    return d


def get_indexes(length):
    i, j = 0, 0
    while i == j:
        i, j = random.randint(0, length) - 1, random.randint(0, length) - 1
    return i, j


def markov_chain(language, d, n):
    i, j = get_indexes(len(language))
    pair = (language[i], language[j])
    offer = []
    offer += pair
    for _ in range(2, n):
        if pair in d:
            word = random.choice(d[pair])
            offer.append(word)
        else:
            offer.append(language[random.randint(0, len(language)) - 1])
        pair = (offer[-2], offer[-1])
    return offer


def get_str(offer):
    string = ''
    for word in offer:
        if word.endswith('\n'):
            string += word
        else:
            string += word + ' '
    return string


def snoop_says(file_name, n):
    language = words(file_name)
    d = transition_matrix(language)
    offer = markov_chain(language, d, n)
    return get_str(offer)


file_name = 'snoop279.txt'
length = 10
print(snoop_says(file_name, length))
