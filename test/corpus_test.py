from word_vectors.corpus import Corpus

# document 1
test_document = "The St. Louis plant had to close. It would die of old age. Workers had been making cars there since the onset of mass automotive production in the 1920s."


corpus = Corpus("/home/man/dailies/saturday/word_vectors/data/en_US/en_US.news.txt")
document = corpus.documents[1]


def test_corpus_creation():
    len(corpus.documents) > 0
    assert type(document) == str
    assert document == test_document
