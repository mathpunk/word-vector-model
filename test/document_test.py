from pytest import approx
from word_vectors.document import Document

test_document = "The St. Louis plant had to close. It would die of old age. Workers had been making cars there since the onset of mass automotive production in the 1920s."

document = Document(test_document)
normalized = document.normalized()


def test_document_creation():
    assert type(document.content) == str


def test_tokenization():
    assert type(normalized) == list
    assert len(normalized) == 29


def test_normalization():
    assert all(word.islower() for word in normalized)


def test_window_computation():
    neighborhood = document.nearby_words(radius=3, index=0)
    assert any(word == "st" for word in neighborhood)
    assert any(word == "louis" for word in neighborhood)
    assert any(word != "the" for word in neighborhood)
