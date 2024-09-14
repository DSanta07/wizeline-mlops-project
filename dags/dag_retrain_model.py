from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from operators.model_retraining import retrain_model
from operators.data_ingestion import ingest_new_data
from operators.data_preprocessing import preprocess

default_args = {
    "owner": "david",
    "retries": 1,
    'retry_delay': timedelta(minutes=5)
}

def retrain():
    data = ingest_new_data()
    processed_data = preprocess(data)
    X = processed_data.drop(columns=["is_canceled"])
    y = processed_data["is_canceled"]
    accuracy = retrain_model(X, y)
    print(f"Retrained model accuracy: {accuracy}")

with DAG(
    dag_id='retrain_model_v04',
    default_args=default_args,
    start_date=datetime(2024, 10, 9),
    schedule_interval='@monthly'
) as dag:
    retrain_task = PythonOperator(
        task_id="retrain_model_task",
        python_callable=retrain,
        dag=dag,
    )
    
    retrain_task






