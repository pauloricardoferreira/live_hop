import pendulum
from datetime import datetime, timedelta
from airflow import DAG
from airflow_hop.operators import HopWorkflowOperator

local_tz=pendulum.timezone('America/Sao_Paulo')

default_args = {
    'owner': '@OWNER',
    'depends_on_past': False,
    #'start_date': datetime.today() - timedelta(days=1),  #datetime(2021, 3, 13, 0, tzinfo=local_tz), datetime(yyyy,mm,dd,hh,mn,sc, tzinfo=local_tz),
    'start_date': datetime(2021, 3, 13, 0, tzinfo=local_tz), #datetime(yyyy,mm,dd,hh,mn,sc, tzinfo=local_tz),
    'email': ['@EMAIL'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(seconds=30)
}

dag = DAG(
    dag_id='@DAG_ID',
    default_args=default_args,
    schedule_interval='@SCHEDULER_INTERVAL',
    catchup=False,
    tags=['@TAGS']
)

job = HopWorkflowOperator(
    dag=dag,
    task_id='@TASK_ID',
    workflow='@JOB_NAME.@EXTENSAO',
    project_name='@PROJECT_NAME',
    environment='@ENVIRONMENT',
    log_level= 'Basic'
)
