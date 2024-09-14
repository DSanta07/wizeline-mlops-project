import pandas as pd
from sqlalchemy import create_engine
import yaml

# Load database configuration from YAML file
with open("config/db_config.yaml", "r") as file:
    config = yaml.safe_load(file)

# Database connection string for PostgreSQL
DB_URI = (
    f"postgresql://{config['database']['user']}:{config['database']['password']}@"
    f"{config['database']['host']}:{config['database']['port']}/{config['database']['database']}"
)


# Ingest new data from the PostgreSQL database
def ingest_new_data():
    engine = create_engine(DB_URI)
    query = "SELECT * FROM hotel_bookings;"
    new_data = pd.read_sql(query, engine)
    print("INFO: Data ingested...")
    return new_data
