from textblob import TextBlob

class TextAnalysis:
    def __init__(self, text):
        self.text = text
        self.blob = TextBlob(text)

    def sentiment(self):
        sentiment = self.blob.sentiment
        return sentiment

    def keywords(self, num=5):
        words = self.blob.noun_phrases
        return words[:num]
