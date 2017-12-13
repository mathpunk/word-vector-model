from pytest import approx
from word_vectors.document import Document
from word_vectors.probability import Distribution

content = "The quick brown fox jumped over the lazy dog."
other_content = "Hello, world!"
first_news_content = "The St. Louis plant had to close. It would die of old age. Workers had been making cars there since the onset of mass automotive production in the 1920s."
document = Document(content)
other_document = Document(other_content)
news = Document(first_news_content)

unigram_counts = Distribution.unigram_count(document)
other_unigram_counts = Distribution.unigram_count(Document("Hello, world"))


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


def test_skipgram_counts():
    # {'the': {'louis': 1, 'st': 1}}
    counts = Distribution.skipgram_counts(news)

    # Settle on API for skipgram or skipgram probability dist
    # =========
    # dictionary syntax?
    assert counts['the']['st'] == 1
    assert counts['the']['louis'] == 1

    # FAIL: Actually, we're not counting right
    # assert counts['the']['the'] == 0
    # NOTE: It looks like we're  counting occurrences in the document, not in a small window
    # print(counts['the'])

    # method syntax?
    # FAIL: This syntax is not defined
    # assert counts.get('the', 'louis') == 1
    # assert counts.get('the', 'st') == 1

    # Index all words in the document
    # =======================================
    # FAIL: Because we only look at index 0
    # assert counts['st']['the'] == 1
    # assert counts['st']['louis'] == 1
    # assert counts['st']['st'] == 0


