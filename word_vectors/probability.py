from collections import Counter


class Distribution:
    window_radius = 3

    def __init__(self):
        self.window_radius = 3

    def unigram_count(data):
        words = data.normalized()
        from collections import Counter
        counts = Counter(words)
        return counts

    def unigram_probabilities(data):
        counts = Distribution.unigram_count(data)
        size = len(data.normalized())
        probabilities = {}
        for word in list(counts):
            count = counts[word]
            probabilities[word] = count / size
        return probabilities

    def skipgram_counts(data):
        normalized = data.normalized()
        counts = {}
        input_index = 0
        input_word = normalized[input_index]
        left_index = max(0, input_index - Distribution.window_radius)
        right_index = min(0, input_index + Distribution.window_radius, len(normalized))
        window = normalized[left_index:right_index - 1]
        nearby_words = filter(lambda w: w != input_word, window)
        counter = Counter(nearby_words)
        counts[input_word] = counter
        return counts
