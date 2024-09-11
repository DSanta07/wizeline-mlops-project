
FROM apache/airflow:2.10.0

USER root

RUN apt-get update && apt-get -y install libpq-dev gcc

USER airflow

RUN pip install --upgrade pip

COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt