from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def fetch_data():
    print("Fetching data...")

def transform_data():
    print("Transforming data...")

def load_data():
    print("Loading data...")

with DAG(
    'etl_workflow',
    default_args={'start_date': datetime(2023, 1, 1)},
    schedule_interval='@daily',  # Jalankan setiap hari
    catchup=False,
) as dag:
    fetch_task = PythonOperator(
        task_id='fetch_data',
        python_callable=fetch_data,
    )
    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data,
    )
    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load_data,
    )

    fetch_task >> transform_task >> load_task