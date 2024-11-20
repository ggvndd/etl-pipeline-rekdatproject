from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from etl.etl import extract_news, extract_stock_data, transform_news_data, transform_stock_data, load_data_to_postgres

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 1),
    'retries': 1,
}

def etl_pipeline():
    api_key = 'a832dc14477649e4ae67b07416fa5023'
    news_data = extract_news(api_key)
    stock_data = extract_stock_data('AAPL')

    transformed_news = transform_news_data(news_data)
    transformed_stock = transform_stock_data(stock_data)

    db_config = {
        'dbname': 'etl_db',
        'user': 'postgres',
        'password': 'joshuadun',
        'host': 'postgres',
        'port': '5432'
    }
    
    load_data_to_postgres(transformed_news, transformed_stock, db_config)

with DAG(
    'etl_pipeline_dag',
    default_args=default_args,
    description='Combined ETL pipeline DAG',
    schedule_interval='@daily',
) as dag:

    etl_task = PythonOperator(
        task_id='etl_pipeline_task',
        python_callable=etl_pipeline,
    )

    etl_task
