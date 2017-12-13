class Distribution:
    def __init__(self):
        print("hi")

    def count(data):
        words = data.normalized()
        from collections import Counter
        counts = Counter(words)
        return counts

    def ngram_probabilities(n, data):
        if n == 1:
            counts = Distribution.count(data)
            size = len(data.normalized())
            probabilities = {}
            for word in list(counts):
                count = counts[word]
                probabilities[word] = count / size
            return probabilities
        else:
            print('hi')

    def unigram_probabilities(data):
        return Distribution.ngram_probabilities(1, data)
