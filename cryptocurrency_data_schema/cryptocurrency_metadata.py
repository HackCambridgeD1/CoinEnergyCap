import dataclasses

from cryptocurrency_type import CryptocurrencyType


@dataclasses.dataclass
class CryptocurrencyMetadata:
    symbol: str
    name: str
    joules_per_hash: float
    type: CryptocurrencyType
