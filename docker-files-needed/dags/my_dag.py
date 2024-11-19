from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Import functions from the ETL scripts
from etl.extract import extract_news, extract_stock_data
from etl.transform import transform_news_data, transform_stock_data
from etl.load import load_data_to_postgres

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 11, 1),
    'retries': 1,
}

with DAG(
    'my_etl_dag',
    default_args=default_args,
    description='An example ETL DAG',
    schedule_interval='@daily',
) as dag:

    # Separate extraction tasks
    extract_news_task = PythonOperator(
        task_id='extract_news',
        python_callable=extract_news,
    )

    extract_stock_task = PythonOperator(
        task_id='extract_stock',
        python_callable=extract_stock_data,
    )

    # Separate transformation tasks
    transform_news_task = PythonOperator(
        task_id='transform_news',
        python_callable=transform_news_data,
    )

    transform_stock_task = PythonOperator(
        task_id='transform_stock',
        python_callable=transform_stock_data,
    )

    # Load task (assuming it takes transformed data as input)
    load_task = PythonOperator(
        task_id='load',
        python_callable=load_data_to_postgres,
    )

    # Set task dependencies
    extract_news_task >> transform_news_task
    extract_stock_task >> transform_stock_task
    [transform_news_task, transform_stock_task] >> load_task
