# Base image
FROM python:3.12


# Set environment variables for Airflow
ENV AIRFLOW_HOME=/usr/src/app/airflow

# Set working directory
WORKDIR /usr/src/app

# Copy project files
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose ports for Airflow webserver (8080) and scheduler (8793, if needed)
EXPOSE 8080 8793

# Make sure the correct DB initialization happens before the webserver and scheduler are started
CMD ["airflow", "scheduler"]