import tweepy
import pytrends

def fetch_twitter_trends(api_key, api_key_secret, access_token, access_token_secret, location_woeid=1):
    try:
        # Authenticate with OAuth1
        auth = tweepy.OAuth1UserHandler(
            api_key, api_key_secret, access_token, access_token_secret
        )
        client = tweepy.API(auth)

        # Get trends
        response = client.trends_place(location_woeid)
        trends = response[0]["trends"]

        # Parse trends
        parsed_trends = [
            {
                "topic": trend["name"],
                "tweet_volume": trend.get("tweet_volume", 0),
                "timestamp": response[0]["as_of"]
            }
            for trend in trends
        ]

        print(f"Fetched {len(parsed_trends)} trending topics from Twitter.")
        return parsed_trends

    except Exception as e:
        print(f"Error fetching Twitter trends: {e}")
        return []

from pytrends.request import TrendReq    

def fetch_google_trends(keywords, timeframe="now 1-d"):
    try:
        pytrends = TrendReq(hl='en-US', tz=360)
        pytrends.build_payload(kw_list=keywords, timeframe=timeframe)
        interest_over_time = pytrends.interest_over_time()

        if not interest_over_time.empty:
            trends = interest_over_time.reset_index()[["date"] + keywords]
            print(f"Fetched Google trends for {len(keywords)} keywords.")
            return trends
        else:
            print("No Google Trends data available for the given keywords.")
            return []

    except Exception as e:
        print(f"Error fetching Google Trends: {e}")
        return []
