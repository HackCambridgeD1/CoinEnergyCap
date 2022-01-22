import dataclasses
import datetime

from cryptocurrency_metadata import CryptocurrencyMetadata


@dataclasses.dataclass
class CryptocurrencyTimestamp:
    timestamp: datetime.datetime
    metadata: CryptocurrencyMetadata
    market_cap: float
    hashes_per_second: float
