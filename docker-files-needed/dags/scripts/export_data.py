import psycopg2
import pandas as pd

def export_tables_to_csv(db_config, news_output_path, stock_output_path):
    # Connect to PostgreSQL
    conn = psycopg2.connect(**db_config)
    
    # Export 'news' table
    news_query = "SELECT * FROM news;"
    news_df = pd.read_sql_query(news_query, conn)
    news_df.to_csv(news_output_path, index=False)
    
    # Export 'stock' table
    stock_query = "SELECT * FROM stock;"
    stock_df = pd.read_sql_query(stock_query, conn)
    stock_df.to_csv(stock_output_path, index=False)
    
    # Close the connection
    conn.close()
