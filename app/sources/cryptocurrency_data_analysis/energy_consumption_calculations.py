import math


def get_power_consumption_in_w(hashrate_in_hash_per_s, power_efficiency_in_hash_per_j):
    power_in_j_per_s = hashrate_in_hash_per_s / power_efficiency_in_hash_per_j
    return power_in_j_per_s
    # constants from formula ( 2.78*3600*10^(-10) ) only multiply up to 10^(-6) --> use that instead


def get_annual_energy_consumption_in_j(power_consumption_in_w):
    return power_consumption_in_w * 3600 * 24 * 365


def get_hourly_energy_consumption_in_j(power_consumption_in_w):
    return power_consumption_in_w * 3600


def to_scientific_notation(num: float, digits=3):
    return format(num, f".{digits}e")


def to_twh_from_j(num: float, digits=3):
    twh = num / 3.6 / 10 ** 15
    return twh


# https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1021836/Energy_Consumption_in_the_UK_2021.pdf
ENERGY_TONNE_OF_OIL_J = 41.868E+9


def j_to_tonnes_of_oil(energy_j: float):
    return energy_j / ENERGY_TONNE_OF_OIL_J


# https://www.gov.uk/government/publications/greenhouse-gas-reporting-conversion-factors-2021
KG_CO2_PER_KWH_UK = 0.2123
KG_CO2_PER_J_UK = KG_CO2_PER_KWH_UK / 3.6E+6


def j_to_co2_kg_UK(energy_j: float):
    return KG_CO2_PER_J_UK * energy_j

#https://pdf.sciencedirectassets.com/277910/1-s2.0-S1876610217X00398/1-s2.0-S1876610217361714/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjECYaCXVzLWVhc3QtMSJGMEQCIGx8%2B4mP3%2FwTLc1Y29Ucao6WoUTipasozBtlRvLFzLo8AiA5WdvFA5QS5AKxlfz9FMKbFtzbPe9B7Ta4pqQHF3W5CSr6AwhPEAQaDDA1OTAwMzU0Njg2NSIMmoUq%2FwjtgPpA96d5KtcDivtaUze4NmwAp47pqs518eqvJK6ZOW8kUu6Q24TJhO88Nk29EGwSqRHHQWnvcgp9NwVqBUoetCa2D5Bis4%2F4jbC1tLGmWO5b%2Fmha400o%2F1ComDIknEviu9ZqGToRcHGuuKMOjhWfTFfUwBOS37b9WDohsoeo7O7VjGF5UmMEK%2BDgzkLXQQR3V0zlZekJGx4ldP8RBXDK%2FlQwpXz7icyipgIpMpMJP7NlDhRP9TSdjXbbREnDtzLJrSQdZykNcPXgh26x1%2Fgq6%2F8SCiEmrfSBqZ4gc0mIvYJDN1tFiGJ0Y4y%2B%2FwK3gSCsTFU5TnBQQkOiZpxscqX6TlClCWIUQuHnlY3wE2skTASzLP96Jtblo1bDZJi0YykZ0T0CXwodGEGvvsSpDeeEy2xjb%2FR7c6thePo7haVboXd3LjTsmHK%2Fp242hgqSw24OdUhmOBZJ%2B7CzeTzpEv%2Bw77fwusswlhJDW8BQBf0ywoKVi%2Fq0eusjyIMMbBmpOJqOsm3ZRnVvi0G%2FLBI3nv0YQ1bK2FrNDqBAGRD2E0lz%2BIvd4XmXoUB6ORaSFreyqXJqk2eDhlDC2jlT4GBiOgylGTkydAHxf7ywDPnuzroz8a8wYyfCYL1Y29gnQf91xHIHMP71sY8GOqYBKbJTHWTBN4Rf9ofq2s9uDbpCimKLBRlGZBWEZSrYLtfKVLK6zHPXzXkuwtAHGbBwdjZC1pMr7qE1a0xZ3HXOJtpz72iVMTAyPsShX3B%2BqYPGV6ijSnakEMsAS%2Fr6hEXPPbIqfepylod5jiA16WXtf%2F3YLJSb9fSf%2Bx7oO9M8jXJWnkng59qagBK%2Bf1ISErYyBuVNDsFOpODDSoLSWb1jUtOkz3n2Ng%3D%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220122T220244Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTY3BQVZXH4%2F20220122%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=607973e1fc8a11cb9f0b311a85200ef08004af43fd272a44ee6d81a687e79673&hash=70eaa09746f68a37c249167aa80f1d001e316001964bdbb410e42e6ae0b2080b&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S1876610217361714&tid=spdf-d0fdc771-987a-4d07-b0bc-5778679cd91a&sid=b6c68e7454e3024f1b4949310a6f7527c45bgxrqb&type=client
KG_CO2_PER_KWH_AVG = 0.6
KG_CO2_PER_J_AVG = KG_CO2_PER_KWH_AVG / 3.6E+6


def j_to_co2_kg_AVG(energy_j: float):
    return KG_CO2_PER_J_AVG * energy_j
