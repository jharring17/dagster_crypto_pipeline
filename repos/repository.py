from dagster import repository
from jobs.btc_data import btc_data


@repository
def my_repo():
    return [btc_data]
