from dagster import repository

from jobs.btc_data import btc_data


@repository(
    name="crypto_data",
    description="Repository for pulling data from CryptoCompare.com",
)
def crypto_data():
    return [btc_data]
