# Crypto API Ops
import os

import requests
from dagster import Backoff
from dagster import op
from dagster import Out
from dagster import RetryPolicy
from dotenv import load_dotenv

from logger import dagster_logger
from ops.op_config import CryptoConfig

# Get the API endpoint and credentials.
load_dotenv()
CRYPTO_ENDPOINT = os.getenv("CRYPTO_ENDPOINT")


# Define the op to get crypto data.
@op(
    name="get_crypto_data",
    description="Gets crypto data from CryptoCompare.com using API.",
    out=Out(dict),
    retry_policy=RetryPolicy(
        max_retries=3,
        delay=2.0,
        backoff=Backoff.EXPONENTIAL,
    ),
)
def get_crypto_data(context, config: CryptoConfig) -> dict:
    """Fetch data on cryptocurrencies."""
    dagster_logger.info("INFO: Collecting data from CryptoCompare.com")

    # Pull the crypto from the config.
    crypto_config = context.op_config["crypto"]
    crypto_instrument = context.op_config["instrument"]

    # Log the crypto_config.
    dagster_logger.info(f"INFO: Test pull from config - {crypto_config}.")

    # Set the parameters for the API call.
    params = {
        "market": crypto_instrument,
        "instruments": crypto_config,
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
