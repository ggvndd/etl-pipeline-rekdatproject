from etl.transform import clean_and_combine_data

# Sample social and news data
social_data = [
    {"id": 1, "userId": 101, "title": "Trending Topic 1", "body": "Details about topic 1"},
    {"id": 2, "userId": 102, "title": "Trending Topic 2", "body": "Details about topic 2"}
]

news_data = [
    {"postId": 1, "name": "News Source A", "email": "newsA@example.com"},
    {"postId": 2, "name": "News Source B", "email": "newsB@example.com"}
]

# Perform the transformation
combined_data = clean_and_combine_data(social_data, news_data)

# Print the results
print("Combined Data:")
print(combined_data)

# Verify the output
assert not combined_data.empty, "The combined DataFrame is empty."
assert "userId" in combined_data.columns, "Expected column 'userId' missing."
assert "name" in combined_data.columns, "Expected column 'name' missing."
