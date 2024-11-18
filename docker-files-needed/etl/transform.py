import pandas as pd

def clean_and_combine_data(social_data, news_data, merge_key_left="id", merge_key_right="postId"):
    """
    Cleans and combines social media and news data into a unified DataFrame.

    Parameters:
        social_data (list of dict): Data from social media (e.g., Twitter trends).
        news_data (list of dict): Data from news trends (e.g., Google trends).
        merge_key_left (str): Key to join on in the social data.
        merge_key_right (str): Key to join on in the news data.

    Returns:
        pandas.DataFrame: Combined and cleaned DataFrame.
    """
    try:
        # Convert data to DataFrame
        social_df = pd.DataFrame(social_data)
        news_df = pd.DataFrame(news_data)

        # Merge dataframes
        combined_df = pd.merge(social_df, news_df, left_on=merge_key_left, right_on=merge_key_right, how="inner")

        # Select relevant columns (update to match your data)
        relevant_columns = ["userId", "title", "body", "name", "email"]
        combined_df = combined_df[relevant_columns]

        return combined_df

    except KeyError as e:
        print(f"Key error: {e}. Check that the input data has the required columns.")
        return pd.DataFrame()

    except Exception as e:
        print(f"An error occurred during transformation: {e}")
        return pd.DataFrame()
