class Distribution:
    def __init__(self):
        print("hi")

    def count(data):
        words = data.normalized()
        from collections import Counter
        counts = Counter(words)
        return counts

    def probability(data):
        counts = Distribution.count(data)
        size = len(data.normalized())
        probabilities = {}
        for word in list(counts):
            count = counts[word]
            probabilities[word] = count / size
        return probabilities
