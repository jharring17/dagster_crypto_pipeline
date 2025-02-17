### Process API Data Ops ###
import pandas as pd
from datetime import datetime
from dagster import op, RetryPolicy, Backoff, In, Out
from logger import dagster_logger

@op(
    name="process_data",
    description="Process data from cryptocompare.com API.",
    ins={"raw_data": In(dict)},
    out=Out(pd.DataFrame),
    retry_policy=RetryPolicy(
        max_retries=3,
        delay=2.0,
        backoff=Backoff.EXPONENTIAL,
    ),
)
def process_data(raw_data: dict) -> pd.DataFrame:
    """Process data from cryptocompare.com API."""
    
    # Check if data is None.
    if raw_data is None:
        dagster_logger.error("ERROR: No data received from cryptocompare.com.")

    # Check if data is empty.
    if not raw_data:
        dagster_logger.error("ERROR: Empty data received from cryptocompare.com.")

    # Extract data from the dictionary.
    raw_data = raw_data["Data"]["BTC-USD"]

    # Extract values from the data dictionary.
    currency = raw_data.get("INSTRUMENT", None)
    price = raw_data.get("VALUE", None)
    volume = raw_data.get("CURRENT_HOUR_QUOTE_VOLUME_DIRECT", None)
    last_update = raw_data.get("VALUE_LAST_UPDATE_TS", None)

    # Convert the last update timestamp to a human-readable format.
    last_update = datetime.fromtimestamp(last_update).strftime("%Y-%m-%d %H:%M:%S")

    # Create a pandas DataFrame.
    df = pd.DataFrame(
        {
            "Currency": [currency],
            "Price (USD)": [price],
            "Volume": [volume],
            "Last Update": [last_update],
        }
    )

    # Log the DataFrame.
    dagster_logger.info(f"{df}")

    return df

