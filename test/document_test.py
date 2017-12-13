from pytest import approx
from word_vectors.document import Document

test_document = "The St. Louis plant had to close. It would die of old age. Workers had been making cars there since the onset of mass automotive production in the 1920s."


def test_document_creation():
    document = Document(test_document)
    assert type(document.content) == str


def test_tokenization():
    document = Document(test_document)
    normalized = document.normalized()
    assert type(normalized) == list
    assert len(normalized) == 29


def test_normalization():
    document = Document(test_document)
    normalized = document.normalized()
    assert all(word.islower() for word in normalized)


