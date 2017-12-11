from word_vectors.acquire import Corpus

# document 1
test_document = "The St. Louis plant had to close. It would die of old age. Workers had been making cars there since the onset of mass automotive production in the 1920s."

def test_sanity():
    assert 1 + 1 == 2

def test_corpus_creation():
    corpus = Corpus("../data/en_US/en_US.news.txt")
#     len(corpus.documents) > 0
