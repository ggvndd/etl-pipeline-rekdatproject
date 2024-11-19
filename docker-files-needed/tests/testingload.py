from etl.load import load_to_postgresql

# Sample data to insert into the database
test_data = [
    {"platform": "Twitter", "topic": "Topic A", "source": "API"},
    {"platform": "Google", "topic": "Topic B", "source": "API"}
]

# Load data into PostgreSQL
load_to_postgresql(test_data, db_name="etl_db", user="postgres", password="joshuadun", host="localhost", port="5432")

print("Data successfully loaded into PostgreSQL!")
