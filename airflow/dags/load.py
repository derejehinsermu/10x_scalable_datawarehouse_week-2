from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import pandas as pd

default_args = {
    "owner": "air",
    "email": [''],
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag_exec_scripts = DAG(
    dag_id="load_data_to_postgres",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description="Load data from CSV files to PostgreSQL",
)

# SQL query to create the table
create_table_sql = """
CREATE TABLE IF NOT EXISTS vehicles (
    id SERIAL PRIMARY KEY,
    track_id INT NOT NULL,
    vehicle_type VARCHAR(500) NOT NULL,
    traveled_d VARCHAR(500) NOT NULL,
    avg_speed FLOAT NOT NULL,
    lat FLOAT NOT NULL,
    lon FLOAT NOT NULL,
    speed FLOAT NOT NULL,
    lon_acc FLOAT NOT NULL,
    lat_acc FLOAT NOT NULL,
    time FLOAT NOT NULL
)
"""

# Python function to load data from CSV to PostgreSQL
def load_data_to_postgres(csv_file, table_name, postgres_conn_id="postgres_dwh"):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)
    
    # Write DataFrame to PostgreSQL table
    df.to_sql(table_name, con=postgres_conn_id, if_exists="replace", index=False)

# Tasks to create table and load data from CSV files to PostgreSQL
create_table = PostgresOperator(
    task_id="create_table",
    sql=create_table_sql,
    postgres_conn_id="postgres_dwh",
    dag=dag_exec_scripts,
)

load_data = PythonOperator(
    task_id="load_data_task",
    python_callable=load_data_to_postgres,
    op_kwargs={"csv_file": "../data/clean_dataset.csv", "table_name": "traj_vehicle"},
    dag=dag_exec_scripts,
)

# Define task dependencies
create_table >> load_data
