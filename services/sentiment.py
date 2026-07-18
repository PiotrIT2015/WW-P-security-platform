"""
Sentiment Analysis
"""

from textblob import TextBlob


class SentimentAnalyzer:

    @staticmethod
    def analyze(text):

        polarity = TextBlob(

            text

        ).sentiment.polarity

        if polarity > 0.1:

            return "Positive"

        elif polarity < -0.1:

            return "Negative"

        return "Neutral"