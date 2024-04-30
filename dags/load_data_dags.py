from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.models import Variable
from airflow.utils.dates import days_ago
from airflow.models import Variable

default_args = {
    "owner": "",
    "email": [""],
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

# Retrieve the connection ID from Airflow Variables, default to 'postgres_dwh_dev' if not set
env = Variable.get("environment", default_var="dev")
postgres_conn_id = f"postgres_dwh_{env}"

dag_exec_scripts = DAG(
    dag_id="create_table_and_load_data",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description="executing the sql scripts for " + env + " environment.",
    tags=['env:' + env],  # Tagging for easy filtering in the Airflow UI
)

# Assuming you have different SQL files for each environment in the 'sql/{env}/' directory
create_table = PostgresOperator(
    sql=f"sql/{env}/create_table.sql",
    task_id="create_table_task",
    postgres_conn_id=postgres_conn_id,
    dag=dag_exec_scripts,
)

load_data = PostgresOperator(
    sql=f"sql/{env}/load_data.sql",
    task_id="load_data_task",
    postgres_conn_id=postgres_conn_id,
    dag=dag_exec_scripts,
)

create_table >> load_data
