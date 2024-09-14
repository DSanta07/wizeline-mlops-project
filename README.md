# ReservAI: Hotel Booking Cancellation Prediction MLOps Project

## Overview
This project aims to predict hotel booking cancellations using machine learning models. The model helps in reducing cancellation rates, enhancing revenue management, improving customer experience, and supporting strategic expansion. The project uses an MLOps pipeline to automate the process of data ingestion, preprocessing, model training, retraining, deployment, and monitoring.

## Business Goals and Objectives
- **Reduce Cancellation Rates**: Implement targeted interventions to reduce the overall cancellation rate.
- **Enhance Revenue Management**: Use data-driven insights to optimize pricing strategies.
- **Improve Customer Experience**: Offer personalized offers and flexible cancellation policies.
- **Operational Efficiency**: Optimize resource allocation and reduce costs related to cancellations.
- **Support Strategic Expansion**: Provide a stable revenue base for opening new hotels.
- **Maintain Model Performance**: Ensure continuous model improvement through regular retraining and feedback.

## Project Structure
- `airflow_dags/`: Airflow DAGs for model retraining and data pipeline.
- `config/`: Configuration files for database, logging, and model settings.
- `dags/`: Additional DAGs for data processing and testing.
- `notebooks/`: Jupyter Notebooks for exploratory data analysis, preprocessing, training, and testing.
- `plugins/operators/`: Custom Airflow operators for data processing, model deployment, and monitoring.
- `scripts/`: Shell scripts for deployment and DVC integration.
- `src/`: Source code for data ingestion, preprocessing, model deployment, and monitoring.
- `tests/`: Unit tests for the project's components.

## Getting Started
### Prerequisites
- Python 3.x
- Docker
- Airflow
- DVC
- MLflow
- Prometheus and Grafana

### Installation
1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```
2. Navigate to the project directory:
    ```bash
    cd project
    ```
3. Install Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up the environment variables:
    ```bash
    cp .env.example .env
    ```
   Update the `.env` file with the necessary configuration.

5. Build and run Docker containers:
    ```bash
    docker-compose up --build
    ```

### Running the Project
1. **Data Ingestion**: Run the Airflow DAG `dag_select_hotel_bookings` to ingest new data.
2. **Model Training**: Use the notebook `notebooks/3_model_training.ipynb` for initial model training.
3. **Model Retraining**: The Airflow DAG `retrain_model_dag` is scheduled to retrain the model monthly.
4. **Model Deployment**: Deploy the trained model using the script:
    ```bash
    ./scripts/deploy_model.sh
    ```

### Model Performance
The Random Forest model was selected due to its superior performance with an accuracy of 89.4%. The model provides balanced predictions for both cancellations and non-cancellations.

### Monitoring and Retraining
- **Monitoring**: Prometheus and Grafana are used to monitor model performance.
- **Retraining**: The model is retrained monthly using the latest data to adapt to changing patterns.

## Usage
- **API Endpoints**: The project uses FastAPI for serving the model. Use the following endpoint for predictions:
    ```
    POST /predict
    ```
    Sample request:
    ```json
    {
        "lead_time": 45,
        "arrival_date_year": 2017,
        ...
    }
    ```
- **Model Registry**: Models are versioned and stored in MLflow.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or feedback, please reach out to David Santander and Aldo Arellano at santander.david.19@gmail.com, aldo.arellano@wizeline.com.
