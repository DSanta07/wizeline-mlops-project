from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from src.model_retraining import retrain_model
from src.data_ingestion import ingest_new_data
from src.data_preprocessing import preprocess

default_args = {
    "owner": "airflow",
    "start_date": datetime(2024, 8, 15),
    "retries": 1,
}

dag = DAG("retrain_model", default_args=default_args, schedule_interval="@monthly")


def retrain():
    data = ingest_new_data()
    processed_data = preprocess(data)
    X = processed_data.drop(columns=["is_canceled"])
    y = processed_data["is_canceled"]
    accuracy = retrain_model(X, y)
    print(f"Retrained model accuracy: {accuracy}")


retrain_task = PythonOperator(
    task_id="retrain_model_task",
    python_callable=retrain,
    dag=dag,
)

retrain_task
