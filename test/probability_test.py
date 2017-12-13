from pytest import approx
from word_vectors.document import Document
from word_vectors.probability import Distribution

content = "The quick brown fox jumped over the lazy dog."
other_content = "Hello, world!"
document = Document(content)
other_document = Document(other_content)

unigram_counts = Distribution.count(document)
other_unigram_counts = Distribution.count(Document("Hello, world"))


def test_unigram_counts():
    assert unigram_counts['fox'] == 1
    assert unigram_counts['the'] == 2
    assert unigram_counts.get('dog.', 0) == 0
    assert other_unigram_counts['world'] == 1
    assert other_unigram_counts['Hello,'] == 0
    assert other_unigram_counts['hello'] == 1


def test_unigram_counts_unique_words():
    words = document.normalized()
    unique_words_noted = list(unigram_counts)
    vocabulary = set(words)
    len(vocabulary) == len(unique_words_noted)


def test_unigram_probabilities_is_a_probability_distribution():
    distribution = Distribution.unigram_probabilities(document)
    other_distribution = Distribution.unigram_probabilities(other_document)
    probabilities = distribution.values()
    other_probabilities = other_distribution.values()
    assert all(p > 0 for p in probabilities)
    assert all(p > 0 for p in other_probabilities)
    assert sum(probabilities) < 2
    assert sum(other_probabilities) < 2
    assert sum(probabilities) == approx(1.0)
    assert sum(other_probabilities) == approx(1.0)

