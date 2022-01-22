import dataclasses
import datetime

from sources.cryptocurrency_data_schema.cryptocurrency_metadata import CryptocurrencyMetadata


@dataclasses.dataclass
class CryptocurrencyTimestamp:
    timestamp: datetime.datetime
    metadata: CryptocurrencyMetadata
    hashes_per_second: float
    volume: float
    price: float
    estimated_transaction: float


def estimate_transactions_from_volume_and_price(volume: float, price: float):
    return volume / price
