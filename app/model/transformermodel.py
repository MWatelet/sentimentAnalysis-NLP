from transformers import pipeline
from app.enum.sentiment import Sentiment


class TransformerModel:

    def __init__(self):
        self.sentiment_analysis = pipeline("sentiment-analysis")

    def analyze_sentiment_of_text(self, text: str):
        sentiment_result = self.sentiment_analysis(text)
        return Sentiment.P.value if sentiment_result[0]['label'] == 'POSITIVE' else Sentiment.N.value
