import pandas as pd
import yfinance as yf
from etl import extract_news, extract_stock_data, transform_news_data, transform_stock_data, load_data_to_postgres

# Test Configuration
API_KEY = 'a832dc14477649e4ae67b07416fa5023'  # Replace with your actual API key
TICKER = 'AAPL'
DB_CONFIG = {
    'dbname': 'etl_db',
    'user': 'postgres',
    'password': 'joshuadun',  # Replace with your actual password
    'host': 'localhost',
    'port': '5432'
}

# Step 1: Test Extraction
try:
    print("Testing news data extraction...")
    news_data = extract_news(API_KEY)
    print("News data extracted successfully.")
    print(news_data.head())

    print("\nTesting stock data extraction...")
    stock_data = extract_stock_data(TICKER)
    print("Stock data extracted successfully.")
    print(stock_data.head())
except Exception as e:
    print(f"Error during extraction: {e}")

# Step 2: Test Transformation
try:
    print("\nTesting news data transformation...")
    transformed_news = transform_news_data(news_data)
    print("News data transformed successfully.")
    print(transformed_news.head())

    print("\nTesting stock data transformation...")
    transformed_stock = transform_stock_data(stock_data)
    print("Stock data transformed successfully.")
    print(transformed_stock.head())
except Exception as e:
    print(f"Error during transformation: {e}")

# Step 3: Test Loading
try:
    print("\nTesting data loading to PostgreSQL...")
    load_data_to_postgres(transformed_news, transformed_stock, DB_CONFIG)
    print("Data loaded successfully to PostgreSQL.")
except Exception as e:
    print(f"Error during data loading: {e}")
