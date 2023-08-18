from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from HouseMatch.HouseMatch.cleaning.clean import Clean
from HouseMatch.HouseMatch.utils.utils import delete_tmp_files, drop_duplicates, add_headers_csv
from airflow.contrib.sensors.file_sensor import FileSensor
import HouseMatch.HouseMatch.config as cf

"""
this file contains the airflow dag for scraping the 
data and saving it to elasticsearch and postgres.
"""

default_args = {
    'owner': 'amin',
    'depends_on_past': False,
    'start_date': datetime(2023, 8, 10),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'scraping_houses',
    default_args=default_args,
    description='This Dag is for Extracting data from divar and Sheypoor.',
    schedule_interval=timedelta(minutes=5),
    max_active_runs=1
)

extract_task = BashOperator(
    task_id='extract_task',
    bash_command=f'bash {cf.HOME_PATH}/HouseMatch/HouseMatch/start_scrape.sh ' ,
    dag=dag
)

file_sensor_task = FileSensor(
        task_id='file_sensor_task',
        filepath=f'{cf.HOME_PATH}/HouseMatch/HouseMatch/data_temp/items.jsonl',
        mode='poke',
        poke_interval=20,
        dag=dag  
    )

clean_data = BashOperator(
    task_id='clean_and_save_csv',
    bash_command=f'bash {cf.HOME_PATH}/HouseMatch/HouseMatch/cleaning/clean.sh ',
    dag=dag
)

add_headers = PythonOperator(
    task_id='add_headers',
    python_callable=add_headers_csv,
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

save_to_elastic = BashOperator(
    task_id='save_to_elastic',
    bash_command=f'bash {cf.HOME_PATH}/HouseMatch/HouseMatch/elastic/add_elastic.sh ',
    dag=dag
)

save_to_postgres = BashOperator(
    task_id='save_to_postgres',
    bash_command=f'bash {cf.HOME_PATH}/HouseMatch/HouseMatch/postgres/add_postgres.sh ',
    dag=dag
)

extract_task >> file_sensor_task >> clean_data >> add_headers >> remove_temp_files >> drop_duplicates_task >> \
[save_to_postgres, save_to_elastic]