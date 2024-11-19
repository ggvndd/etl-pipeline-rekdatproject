import requests
import pandas as pd

def extract_news(api_key):
    # Define search parameters
    params = {
        'q': 'AI regulation OR artificial intelligence ethics OR AI policy OR government AI rules',
        'language': 'en',
        'sortBy': 'relevance',
        'apiKey': api_key,
        'pageSize': 100  # Number of articles per request
    }

    # Make request
    news_url = 'https://newsapi.org/v2/everything'
    response = requests.get(news_url, params=params)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data.get('articles', [])
        
        # Convert articles to DataFrame
        news_df = pd.DataFrame(articles)
        # Keep only relevant columns
        news_df['publishedAt'] = pd.to_datetime(news_df['publishedAt']).dt.date
        news_df = news_df[['title', 'description', 'publishedAt', 'source']]
        return news_df
    else:
        raise Exception(f"Error fetching news: {response.status_code}")

import yfinance as yf

def extract_stock_data(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    historical_data = stock.history(period=period)
    # Reset index for easy merging later
    stock_data = historical_data.reset_index()
    stock_data['Date'] = pd.to_datetime(stock_data['Date']).dt.date
    return stock_data


