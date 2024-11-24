from textblob import TextBlob
from textblob.sentiments import PatternAnalyzer
from app.enum.sentiment import Sentiment


class TextBlobModel:

    def analyze_sentiment_of_text(self, text: str):
        sentiment_result = TextBlob(text, analyzer=PatternAnalyzer()).sentiment
        return Sentiment.P.value if sentiment_result.polarity > 0 else Sentiment.N.value
