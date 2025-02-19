from dagster import Config


class CryptoConfig(Config):
    instrument: str = "cadli"
    crypto: str = "BTC-USD"
