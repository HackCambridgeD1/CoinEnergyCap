import dataclasses

from app.sources.cryptocurrency_data_schema.cryptocurrency_type import CryptocurrencyType


@dataclasses.dataclass
class CryptocurrencyMetadata:
    symbol: str
    name: str
    efficiency: float  # hashes per joule
    type: CryptocurrencyType
