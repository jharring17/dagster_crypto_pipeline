from dagster import job
from ops.crypto_api import get_crypto_data
from ops.process_data import process_data


@job(description="Get BTC data from cryptocompare.com")
def btc_data():
    # Setup the op interactions.
    raw_data = get_crypto_data()
    process_data(raw_data=raw_data)
