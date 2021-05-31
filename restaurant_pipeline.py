import operator 
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator 

from airflow import DAG 

default_args = {
    'owner': "airflow",
    'email':["airflow@airflow.com"],
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime(2021, 5, 26),
    'depends_on_past': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG("restaurant_pipeline",
            default_args = default_args,
            description = 'Orchestrate the load and transform data in Redshift',
            schedule_interval = '0 * * * *',
            catchup = False 
    )

end_operator = DummyOperator(task_id ='end_operator', dag=dag)

end_operator