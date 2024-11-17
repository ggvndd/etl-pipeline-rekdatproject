import tweepy
import pytrends

def fetch_twitter_trends(bearer_token, location_woeid=1):
    try:
        # Authenticate using Bearer Token
        client = tweepy.Client(bearer_token='Y4K5XS0tSgQenATkq51A0XGAGGsuYDux2lMr7Gj06ooEzePp09')

        # Get trending topics for the location
        response = client.get_trends_place(1)
        trends = response[0]["trends"]  # Extract trends list

        # Parse trends data
        parsed_trends = [
            {"topic": trend["name"], "tweet_volume": trend.get("tweet_volume", 0)}
            for trend in trends
        ]

        print(f"Successfully fetched {len(parsed_trends)} trending topics from Twitter.")
        return parsed_trends

    except Exception as e:
        print(f"Error fetching Twitter trends: {e}")
        return []

from pytrends.request import TrendReq    
def fetch_google_trends():
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list=["technology", "news"], timeframe="now 1-d")
    trends = pytrends.related_queries()
    return trends

