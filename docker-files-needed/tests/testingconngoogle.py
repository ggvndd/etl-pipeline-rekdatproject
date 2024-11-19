from pytrends.request import TrendReq

def test_google_trends_connection():
    """
    Test connection to Google Trends by building a simple payload.
    """
    try:
        pytrends = TrendReq(hl="en-US", tz=360)
        pytrends.build_payload(kw_list=["test"], timeframe="now 1-d")
        print("Successfully connected to Google Trends API.")
        return True

    except Exception as e:
        print(f"Failed to connect to Google Trends API: {e}")
        return False

# Test your connection
if __name__ == "__main__":
    test_google_trends_connection()
