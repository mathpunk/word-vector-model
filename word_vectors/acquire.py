import os

class Corpus:
    documents = []

    def __init__(self, path):
        file = open(path, 'r')
        data = file.read()
        self.documents = data.splitlines()


# english_news = "data/en_US/en_US.news.txt"
# import os

# news_file = open(english_news, 'r')
# data = news_file.read()

# type(data)


# class Corpus:
#     documents = []

#     def __init__(self, path):
#         for filename in os.listdir(path):
#             document = Document()
#             self.documents.append(document)

