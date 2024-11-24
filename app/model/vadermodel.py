from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from app.enum.sentiment import Sentiment


class VaderModel:

    def analyze_sentiment_of_text(self, text: str):
        sentiment = SentimentIntensityAnalyzer()
        sentiment_result = sentiment.polarity_scores(text)
        return Sentiment.P.value if sentiment_result['compound'] > 0 else Sentiment.N.value
