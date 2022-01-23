from datetime import datetime
from typing import List, TypedDict
import requests

from app.sources.cryptocurrency_data_schema.cryptocurrency_metadata import CryptocurrencyMetadata
from app.sources.cryptocurrency_data_schema.cryptocurrency_timestamp import CryptocurrencyTimestamp
from app.sources.cryptocurrency_data_schema.cryptocurrency_type import CryptocurrencyType
from app.sources.cryptocurrency_data_schema.demo_cryptocurrency_metadata import demo_metadata_efficiency_map, \
    AVG_EFFICIENCY


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
        price=minerstat_response["price"]
    )


# Cause Problems with Coinmarketcap API
API_INCOMPATIBILITIES = ["ADOT", "ARMS", "BTCV2", "BTMC", "C0BAN", "CRUZ", "DBIX", "DNGR", "ERE", "HVQ", "INES", "IXI",
                         "MZC", "PESP", "PGC", "REA", "SIPC", "TLO", "TNA", "URX", "VCASH", "ZELS"]
UNREALISTIC_DATA = ["ELA", "NMC", "SYS"]
INCOMPATIBLE_SYMBOLS = API_INCOMPATIBILITIES + UNREALISTIC_DATA


class MinerstatApiEndpoint:

    @staticmethod
    def get_data_for_cryptocurrencies(
            cryptocurrency_metadata: List[CryptocurrencyMetadata]
    ) -> List[CryptocurrencyTimestamp]:
        symbol_metadata_map = {metadata.symbol: metadata for metadata in cryptocurrency_metadata}
        cryptocurrency_identifiers = list(map(lambda metadata: metadata.symbol, cryptocurrency_metadata))
        response = requests.get(f"https://api.minerstat.com/v2/coins?list={','.join(cryptocurrency_identifiers)}")

        dedup_responses = {minerstat_response["coin"]: minerstat_response for minerstat_response in response.json()}

        return [map_minerstat_response_to_crypto_timestamp(
            symbol_metadata_map[minerstat_response["coin"]], minerstat_response
        )
            for minerstat_response in dedup_responses.values()]

    @staticmethod
    def get_complete_cryptocurrency_set(

    ):
        response = requests.get(f"https://api.minerstat.com/v2/coins")
        dedup_responses = {minerstat_response["coin"]: minerstat_response for minerstat_response in response.json()
                           if minerstat_response["coin"] not in INCOMPATIBLE_SYMBOLS}
        positive_hashrate_responses = [minerstat_response for minerstat_response in dedup_responses.values()
                                       if minerstat_response["network_hashrate"] > 0]
        positive_price_responses = [minerstat_response for minerstat_response in positive_hashrate_responses
                                    if minerstat_response["price"] > 0]

        return [map_minerstat_response_to_crypto_timestamp(
            CryptocurrencyMetadata(
                symbol=minerstat_response["coin"],
                name=minerstat_response["name"],
                efficiency=demo_metadata_efficiency_map.get(minerstat_response["coin"], AVG_EFFICIENCY),
                type=CryptocurrencyType.PROOF_OF_WORK
            ), minerstat_response
        ) for minerstat_response in positive_price_responses]
