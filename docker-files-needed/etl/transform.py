import pandas as pd
 

def clean_and_combine_data(social_data, news_data):
    # Convert data to DataFrame
    social_df = pd.DataFrame(social_data)
    news_df = pd.DataFrame(news_data)

    # Gabungkan data berdasarkan userId (contoh logika sederhana)
    combined_df = pd.merge(social_df, news_df, left_on="id", right_on="postId", how="inner")

    # Pilih kolom yang relevan
    combined_df = combined_df[["userId", "title", "body", "name", "email"]]

    return combined_df


