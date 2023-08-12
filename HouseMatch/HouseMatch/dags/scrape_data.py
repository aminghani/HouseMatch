from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'amin',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=3)
}
def func():
    pass
dag = DAG(
    'scraping_houses',
    default_args=default_args,
    description='This Dag is for Extracting data from divar and Sheypoor.',
    schedule_interval=timedelta(minutes=5),
    max_active_runs=1
)

extract_task = BashOperator(
    task_id='extract_task',
    bash_command='bash /home/amin/vscode/HouseMatch/HouseMatch/HouseMatch/start_scrape.sh ' ,
    dag=dag
)



extract_task