from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Import functions from the ETL scripts
from etl.extract import extract_function
from etl.transform import transform_function
from etl.load import load_function

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

    extract_task = PythonOperator(
        task_id='extract',
        python_callable=extract_function,
    )

    transform_task = PythonOperator(
        task_id='transform',
        python_callable=transform_function,
    )

    load_task = PythonOperator(
        task_id='load',
        python_callable=load_function,
    )

    # Set task dependencies
    extract_task >> transform_task >> load_task
