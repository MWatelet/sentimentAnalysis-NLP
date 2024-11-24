from flair.models import TextClassifier
from flair.data import Sentence
from app.enum.sentiment import Sentiment


class FlairModel:

    def __init__(self):
        self.classifier = TextClassifier.load('en-sentiment')

    def analyze_sentiment_of_text(self, text: str):
        sentence = Sentence(text)
        self.classifier.predict(sentence)
        return Sentiment.P.value if sentence.labels[0].value == 'POSITIVE' else Sentiment.N.value
