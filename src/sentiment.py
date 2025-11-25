import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def add_sentiment_scores(news_df):
    """
    Adds sentiment scores to the news dataframe using VADER
    """

    def get_sentiment(text):
        score = analyzer.polarity_scores(str(text))
        return score['compound']

    news_df['sentiment_score'] = news_df['headline'].apply(get_sentiment)
    return news_df


def save_sentiment_data(news_df, output_path="output/news_with_sentiment.csv"):
    """
    Saves sentiment-scored news data
    """
    news_df.to_csv(output_path, index=False)
