import os

english_news_path = "../data/en_US/en_US.news.txt"
news_file = open(english_news_path, 'r')
data = news_file.read()
lines = data.splitlines()
document = lines[1]

import string

def normalize(document):
    tokens = document.split(" ")
    translator = str.maketrans('', '', string.punctuation)
    return [word.lower().translate(translator) for word in tokens]

from collections import Counter

def unigram_probabilities(document):
    words = normalize(document) 
    counts = Counter(words)
    probabilities = {}
    for word, count in counts.items():
        probabilities[word] = count/len(words)
    return probabilities
    
unigram_probabilities(document)

sum(get_probability(document).values())

WINDOW_RADIUS = 3

def compute_skipgrams(document):
    skipgram_counts = {}
    thisgram_counts = {}
    input_index = 0
    left_index = max(0, input_index - WINDOW_RADIUS)
    right_index = min(input_index + WINDOW_RADIUS, len(normalized))
    center_index = input_index - left_index

    window = normalized[left_index:right_index]
    del window[center_index]

    for word in window:
        thisgram_counts[word] = thisgram_counts.get(word, 0) + 1
    skipgram_counts[input_word] = thisgram_counts
    return skipgram_counts

compute_skipgrams(document)
