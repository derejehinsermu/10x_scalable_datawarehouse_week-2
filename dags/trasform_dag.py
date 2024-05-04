from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'dbt_dag',
    default_args=default_args,
    description='Dicription',
    schedule_interval=timedelta(days=1),
)

run_dbt = BashOperator(
    task_id='run_dbt_models',
    bash_command='../my_dbt_project && dbt run',
    dag=dag,
)

