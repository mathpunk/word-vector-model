import string


class Document:
    def __init__(self, content):
        self.content = content
        self.metadata = {"source": "en_US.news.txt"}

    def normalized(self):
        tokens = self.content.split(" ")
        translator = str.maketrans('', '', string.punctuation)
        return [word.lower().translate(translator) for word in tokens]

    def get_window(self, radius=3, index=0):
        normalized = self.normalized()
        left_index = max(0, index - radius)
        right_index = min(0, index + radius, len(normalized))
        return normalized[left_index:right_index - 1]


