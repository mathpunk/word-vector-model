class Corpus:
    documents = []

    def __init__(self, path):
        file = open(path, 'r')
        data = file.read()
        self.documents = data.splitlines()
