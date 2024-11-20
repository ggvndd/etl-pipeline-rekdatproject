from etl.extract import extract_news, extract_stock_data
from etl.extract import news_data
from etl.extract import stock_data
from textblob import TextBlob

def transform_news_data(news_data):
    # Perform sentiment analysis on news titles
    news_data['sentiment'] = news_data['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)  # Sentiment score between -1 and 1
    # Group by date and calculate average sentiment and article count
    news_summary = news_data.groupby('publishedAt').agg({'sentiment': 'mean', 'title': 'count'}).reset_index()
    news_summary.rename(columns={'title': 'news_count'}, inplace=True)
    return news_summary

def transform_stock_data(stock_data):
    # Optionally, any stock-specific transformations can go here
    # For now, return as-is
    return stock_data

transform_news_data()
transform_stock_data()