import pytest
import pandas as pd
from unittest.mock import patch, mock_open
from src.data_ingestion import ingest_new_data

# Sample data to simulate what you expect from the database
dummy_data = pd.DataFrame(
    {
        "hotel": ["Resort Hotel", "City Hotel"],
        "is_canceled": [0, 1],
        "lead_time": [342, 120],
        "arrival_date_year": [2024, 2024],
        "arrival_date_month": ["July", "August"],
    }
)

# Mock the `yaml.safe_load` to provide mock configuration for the database
mock_config = {
    "database": {
        "user": "your_db_user",
        "password": "your_db_password",
        "host": "postgres_db",
        "port": 5432,
        "database": "hotel_bookings",
    }
}


# Mocking the database connection and query execution
@patch("src.data_ingestion.create_engine")
@patch("src.data_ingestion.pd.read_sql")
@patch("src.data_ingestion.yaml.safe_load", return_value=mock_config)
def test_ingest_new_data(mock_yaml, mock_read_sql, mock_engine):
    # Arrange: Set up the mock to return the dummy data
    mock_read_sql.return_value = dummy_data

    # Act: Call the function
    result = ingest_new_data()

    # Assert: Verify the function returns the expected data
    assert isinstance(result, pd.DataFrame)  # Ensure the result is a DataFrame
    assert len(result) == 2  # Ensure the correct number of rows
    assert "hotel" in result.columns  # Ensure the correct columns are present
    assert result.iloc[0]["hotel"] == "Resort Hotel"  # Verify content

    # Verify that the SQL query was executed
    mock_read_sql.assert_called_once_with(
        "SELECT * FROM hotel_bookings;",
        mock_engine(),
    )
