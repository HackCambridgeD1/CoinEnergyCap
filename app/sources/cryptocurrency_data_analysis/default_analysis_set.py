from typing import List

from app.sources.cryptocurrency_api_connections.minerstat_api_endpoint import MinerstatApiEndpoint
from app.sources.cryptocurrency_data_analysis.energy_consumption_calculations import get_annual_energy_consumption_in_j, \
    get_hourly_energy_consumption_in_j, get_power_consumption_in_w
from app.sources.cryptocurrency_data_schema.cryptocurrency_timestamp import CryptocurrencyTimestamp
from app.sources.cryptocurrency_data_schema.demo_cryptocurrency_metadata import demo_metadata


def get_default_analysis_set() -> List[CryptocurrencyTimestamp]:
    return list(filter(lambda meta_ts: meta_ts.hashes_per_second > 0,
                       MinerstatApiEndpoint.get_data_for_cryptocurrencies(demo_metadata)))


def get_annual_energy_consumption_in_j_from_timestamp(crypto_timestamp: CryptocurrencyTimestamp) -> float:
    return get_annual_energy_consumption_in_j(
        get_power_consumption_in_w_from_timestamp(crypto_timestamp)
    )


def get_hourly_energy_consumption_in_j_from_timestamp(crypto_timestamp: CryptocurrencyTimestamp) -> float:
    return get_hourly_energy_consumption_in_j(
        get_power_consumption_in_w_from_timestamp(crypto_timestamp)
    )


def get_power_consumption_in_w_from_timestamp(crypto_timestamp: CryptocurrencyTimestamp) -> float:
    return get_power_consumption_in_w(crypto_timestamp.hashes_per_second, crypto_timestamp.metadata.efficiency)
