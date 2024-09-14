
FROM apache/airflow:2.10.0

USER root

# Updates the package lists and install libpq-dev gcc packages
RUN apt-get update && apt-get -y install libpq-dev gcc

USER airflow

# Upgrade pip
RUN pip install --upgrade pip

# Copy the dependencies file to the working directory
COPY requirements.txt /requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r /requirements.txt

# Copy the content of the local src directory to the working directory
COPY src/ ./src