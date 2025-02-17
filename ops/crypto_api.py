### Crypto API Ops ###
import os
import requests
from dotenv import load_dotenv
from dagster import op, RetryPolicy, Backoff, Out
from logger import dagster_logger

# Get the api endpoint and credentials.
load_dotenv()
CRYPTO_ENDPOINT = os.getenv("CRYPTO_ENDPOINT")


# Define the op to get crypto data.
@op(
    name="get_crypto_data",
    description="Gets crypto data from cryptocompare.com using API.",
    out=Out(dict),
    retry_policy=RetryPolicy(
        max_retries=3,
        delay=2.0,
        backoff=Backoff.EXPONENTIAL,
    ),
)
def get_crypto_data() -> dict:
    """Fetch data on cryptocurrencies."""
    dagster_logger.info("INFO: Collecting data from cryptocompare.com")

    params = {
        "market": "cadli",
        "instruments": "BTC-USD",
    }

    try:
        # Call the API to get data.
        get_crypto_response = requests.get(
            url=CRYPTO_ENDPOINT + "/index/cc/v1/latest/tick", params=params
        )
        raw_data = get_crypto_response.json()

        # Log the data.
        dagster_logger.info(f"INFO: {raw_data}")
        dagster_logger.info(f"INFO: return type of API data {type(raw_data)}.")

        # Return the BTC-USD data.
        return raw_data

    # If error in API call, raise exception
    except Exception as e:
        raise e
