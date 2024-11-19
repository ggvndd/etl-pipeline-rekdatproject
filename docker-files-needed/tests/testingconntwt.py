import tweepy

def test_twitter_connection(api_key, api_key_secret, access_token, access_token_secret):
    """
    Test connection to Twitter API by retrieving account information or rate limits.
    """
    try:
        # Authenticate with Twitter API v1.1
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        api = tweepy.API(auth)

        # Test API call (rate limit status is a lightweight call)
        rate_limit_status = api.rate_limit_status()
        print("Successfully connected to Twitter API.")
        print("Rate Limit Status:", rate_limit_status['rate_limit_context'])
        return True

    except Exception as e:
        print(f"Failed to connect to Twitter API: {e}")
        return False

# Test your connection
if __name__ == "__main__":
    test_twitter_connection(
        api_key = 'qvX4Zq69gxYO9bmPpcE2HBzWR',
        api_key_secret = 'CNhVsfWIH8wkB7xNMHXmhQVlmUrSm8ruO3p8XpUBKRApFzhR7k',
        access_token = '1081790378729066497-ISlmB5WusykCcDjwftd3TtfaLTsKiV',
        access_token_secret = '6yYU43aRCmnliSUOymRXFKFwVSiDZOzOMtLKZNg8NzHtw'
    )
