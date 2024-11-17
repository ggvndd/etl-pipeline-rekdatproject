import numpy as np
import pandas as pd
import requests

from etl.extract import fetch_social_media_data, fetch_news_data
from etl.transform import clean_and_combine_data
from etl.load import save_to_csv, load_to_postgresql

def main():
    print("Starting ETL process...")
    
    # Extract
    print("Extracting data...")
    twitter_data = fetch_social_media_data()  # Twitter API
    news_data = fetch_news_data()  #Google Trends

    # Transform
    print("Transforming data...")
    combined_data = clean_and_combine_data(twitter_data, news_data)

    # Load
    print("Loading data...")
    load_to_postgresql(combined_data)

    print("ETL process completed!")

if __name__ == "__main__":
    main()
