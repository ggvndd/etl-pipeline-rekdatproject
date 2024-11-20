from etl.transform import transformed_news, transformed_stock
import psycopg2

def load_data_to_postgres(news_df, stock_df, db_config):
    # Connect to PostgreSQL
    conn = psycopg2.connect(**db_config)
    cur = conn.cursor()
    
    # Create tables if not exist
    cur.execute("""
        CREATE TABLE IF NOT EXISTS news (
            id SERIAL PRIMARY KEY,
            date DATE,
            avg_sentiment FLOAT,
            news_count INT
        );
    """)
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS stock (
            id SERIAL PRIMARY KEY,
            date DATE,
            open_price FLOAT,
            close_price FLOAT,
            volume BIGINT
        );
    """)

    # Insert data into 'news' table
    for _, row in news_df.iterrows():
        cur.execute("""
            INSERT INTO news (date, avg_sentiment, news_count)
            VALUES (%s, %s, %s);
        """, (row['publishedAt'], row['sentiment'], row['news_count']))

    # Insert data into 'stock' table
    for _, row in stock_df.iterrows():
        cur.execute("""
            INSERT INTO stock (date, open_price, close_price, volume)
            VALUES (%s, %s, %s, %s);
        """, (row['Date'], row['Open'], row['Close'], row['Volume']))
    
    # Commit and close connection
    conn.commit()
    cur.close()
    conn.close()

# Example usage
db_config = {
    'dbname': 'etl_db',
    'user': 'postgres',
    'password': 'joshuadun',
    'host': 'localhost',
    'port': '5432'
}
load_data_to_postgres(transformed_news, transformed_stock, db_config)
