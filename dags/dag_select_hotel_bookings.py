from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator


default_args = {
    'owner': 'david',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    dag_id='dag_select_hotel_bookings_v01',
    default_args=default_args,
    start_date=datetime(2024, 10, 9),
    schedule_interval='@daily'
) as dag:
    task1 = PostgresOperator(
        task_id='select_hotel_bookings',
        postgres_conn_id='postgres_db_hotel',
        sql="""
            SELECT * FROM public.hotel_bookings
            ORDER BY id ASC 
        """
    )

    task1