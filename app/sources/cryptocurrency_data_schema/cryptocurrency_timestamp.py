import dataclasses
import datetime

from app.sources.cryptocurrency_data_schema.cryptocurrency_metadata import CryptocurrencyMetadata


@dataclasses.dataclass
class CryptocurrencyTimestamp:
    timestamp: datetime.datetime
    metadata: CryptocurrencyMetadata
    hashes_per_second: float
    volume: float
    price: float
