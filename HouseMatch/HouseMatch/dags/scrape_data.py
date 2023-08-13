from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from HouseMatch.HouseMatch.cleaning.clean import Clean
from HouseMatch.HouseMatch.utils.utils import delete_tmp_files, drop_duplicates
from airflow.contrib.sensors.file_sensor import FileSensor

default_args = {
    'owner': 'amin',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
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

file_sensor_task = FileSensor(
        task_id='file_sensor_task',
        filepath='/home/amin/vscode/HouseMatch/HouseMatch/HouseMatch/data_temp/items.jsonl',
        mode='poke',
        poke_interval=20,
        dag=dag  # Specify the interval to check for the file existence
    )

clean_data = PythonOperator(
    task_id='clean_and_save_csv',
    python_callable=Clean().clean_and_save,
    dag=dag
)

remove_temp_files = PythonOperator(
    task_id='remove_temporary',
    python_callable=delete_tmp_files,
    dag=dag
)

drop_duplicates_task = PythonOperator(
    task_id='drop_duplicates',
    python_callable=drop_duplicates,
    dag=dag
)
extract_task >> file_sensor_task >> clean_data >> remove_temp_files >> drop_duplicates_task