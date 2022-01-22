from datetime import datetime
from typing import List, TypedDict
import requests

from sources.cryptocurrency_data_schema.cryptocurrency_metadata import CryptocurrencyMetadata
from sources.cryptocurrency_data_schema.cryptocurrency_timestamp import CryptocurrencyTimestamp, \
    estimate_transactions_from_volume_and_price


class MinerstatResponse(TypedDict):
    id: str
    coin: str
    name: str
    type: str
    algorithm: str
    network_hashrate: float
    difficulty: float
    reward: float
    reward_unit: str
    reward_block: float
    price: float
    volume: float
    updated: int


def map_minerstat_response_to_crypto_timestamp(cryptocurrency_metadata: CryptocurrencyMetadata,
                                               minerstat_response: MinerstatResponse):
    return CryptocurrencyTimestamp(
        timestamp=datetime.fromtimestamp(minerstat_response["updated"]),
        metadata=cryptocurrency_metadata,
        hashes_per_second=minerstat_response["network_hashrate"],
        volume=minerstat_response["volume"],
        price=minerstat_response["price"],
    )


class MinerstatApiEndpoint:

    @staticmethod
    def get_data_for_cryptocurrencies(
            cryptocurrency_metadata: List[CryptocurrencyMetadata]
    ) -> List[CryptocurrencyTimestamp]:
        symbol_metadata_map = {metadata.symbol: metadata for metadata in cryptocurrency_metadata}
        cryptocurrency_identifiers = list(map(lambda metadata: metadata.symbol, cryptocurrency_metadata))
        response = requests.get(f"https://api.minerstat.com/v2/coins?list={','.join(cryptocurrency_identifiers)}")

        return [map_minerstat_response_to_crypto_timestamp(
            symbol_metadata_map[minerstat_response["coin"]], minerstat_response
        )
            for minerstat_response in response.json()]
