import tweepy
import pytrends

def fetch_twitter_trends(api_key, api_key_secret, access_token, access_token_secret, location_woeid=1):
    """
    Fetch Twitter trends for a specific location using Twitter's v1.1 API.
    """
    try:
        # Authenticate with API v1.1
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # Get trends for the specified location (default: worldwide)
        trends = api.get_place_trends(location_woeid)

        # Debugging: Log raw API response
        print("Raw Twitter API Response:", trends)

        # Validate and parse trends
        if trends and isinstance(trends, list) and "trends" in trends[0]:
            parsed_trends = [
                {
                    "topic": trend.get("name").strip().lower() if trend.get("name") else None,
                    "tweet_volume": trend.get("tweet_volume", 0),
                }
                for trend in trends[0]["trends"]
                if trend.get("name") and trend.get("tweet_volume") and trend["tweet_volume"] > 0
            ]
            print(f"Fetched {len(parsed_trends)} trending topics with significant tweet volume.")
        else:
            parsed_trends = []
            print("No trends found or invalid response format.")

        return parsed_trends

    except Exception as e:
        print(f"Error fetching Twitter trends: {e}")
        return []


from pytrends.request import TrendReq

def fetch_google_trends(keywords):
    """
    Fetch Google Trends data for the specified keywords.
    """
    try:
        if not keywords or len(keywords) == 0:
            raise ValueError("Keyword list is empty. Provide at least one keyword.")

        pytrends = TrendReq(hl="en-US", tz=360)
        pytrends.build_payload(kw_list=keywords, timeframe="now 1-d")
        
        trends = pytrends.related_queries()
        print(f"Successfully fetched Google trends for keywords: {keywords}")
        return trends

    except Exception as e:
        print(f"Error fetching Google Trends: {e}")
        return {}
