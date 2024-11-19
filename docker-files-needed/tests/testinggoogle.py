from etl.extract import fetch_google_trends

if __name__ == "__main__":
    # Test with some sample keywords
    keywords = ["technology", "news"]
    trends = fetch_google_trends(keywords)
    print(trends)