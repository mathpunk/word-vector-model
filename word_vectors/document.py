import string


class Document:
    def __init__(self, content):
        self.content = content
        self.metadata = {"source": "en_US.news.txt"}

    def normalized(self):
        tokens = self.content.split(" ")
        translator = str.maketrans('', '', string.punctuation)
        return [word.lower().translate(translator) for word in tokens]

