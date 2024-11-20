import requests
import pandas as pd
import pandas as pd
import yfinance as yf
import psycopg2

# Extract Functions
def extract_news(api_key):
    # Your extraction logic for news
    params = {
        'q': 'AI regulation OR artificial intelligence ethics OR AI policy OR government AI rules',
        'language': 'en',
        'sortBy': 'relevance',
        'apiKey': api_key,
        'pageSize': 100
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

def extract_stock_data(ticker, period="6mo"):
    stock = yf.Ticker(ticker)
    historical_data = stock.history(period=period)
    stock_data = historical_data.reset_index()
    stock_data['Date'] = pd.to_datetime(stock_data['Date']).dt.date
    return stock_data

from textblob import TextBlob

def transform_news_data(news_data):
    # Perform sentiment analysis on news titles
    news_data['sentiment'] = news_data['title'].apply(lambda x: TextBlob(str(x)).sentiment.polarity)  # Sentiment score between -1 and 1
    # Group by date and calculate average sentiment and article count
    news_summary = news_data.groupby('publishedAt').agg({'sentiment': 'mean', 'title': 'count'}).reset_index()
    news_summary.rename(columns={'title': 'news_count'}, inplace=True)
    return news_summary

def transform_stock_data(stock_data):
    return stock_data

import psycopg2

def load_data_to_postgres(news_df, stock_df, db_config):
    # Connect to PostgreSQL
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    
    # Create tables if not exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id SERIAL PRIMARY KEY,
            date DATE,
            avg_sentiment FLOAT,
            news_count INT
        );
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock (
            id SERIAL PRIMARY KEY,
            date DATE,
            open_price FLOAT,
            close_price FLOAT,
            volume BIGINT
        );
    """)

    # Insert data into 'news' table
    for _, row in news_df.iterrows():
        cur.execute("""
            INSERT INTO news (date, avg_sentiment, news_count)
            VALUES (%s, %s, %s);
        """, (row['publishedAt'], row['sentiment'], row['news_count']))

    # Insert data into 'stock' table
    for _, row in stock_df.iterrows():
        cur.execute("""
            INSERT INTO stock (date, open_price, close_price, volume)
            VALUES (%s, %s, %s, %s);
        """, (row['Date'], row['Open'], row['Close'], row['Volume']))
    
    # Commit and close connection
    conn.commit()
    cur.close()
    conn.close()





