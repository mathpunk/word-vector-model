from pytest import approx
from word_vectors.document import Document
from word_vectors.probability import Distribution

content = "The quick brown fox jumped over the lazy dog."
other_content = "Hello, world!"
document = Document(content)
other_document = Document(other_content)


def test_unigram_counts():
    unigram_counts = Distribution.count(document)
    assert unigram_counts['fox'] == 1
    assert unigram_counts['the'] == 2
    assert unigram_counts.get('dog.', 0) == 0
    unigram_counts_too = Distribution.count(Document("Hello, world"))
    assert unigram_counts_too['world'] == 1
    assert unigram_counts_too['Hello,'] == 0
    assert unigram_counts_too['hello'] == 1


def test_unigram_counts_unique_words():
    words = document.normalized()
    distribution = Distribution.count(document)
    vocabulary = set(words)
    len(vocabulary) == len(list(distribution))


def test_unigram_probabilities_is_a_probability_distribution():
    distribution = Distribution.probability(document)
    other_distribution = Distribution.probability(other_document)

    probabilities = distribution.values()
    other_probabilities = other_distribution.values()
    assert all(p > 0 for p in probabilities)
    assert all(p > 0 for p in other_probabilities)
    assert sum(probabilities) < 2
    assert sum(other_probabilities) < 2
    assert sum(probabilities) == approx(1.0)
    assert sum(other_probabilities) == approx(1.0)
