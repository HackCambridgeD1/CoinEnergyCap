import math


def get_power_consumption_in_mw(hashrate_in_hash_per_s, power_efficiency_in_j_per_hash):
    power_in_j_per_s = hashrate_in_hash_per_s * power_efficiency_in_j_per_hash
    return power_in_j_per_s * math.pow(10, -6)
    # constants from formula ( 2.78*3600*10^(-10) ) only multiply up to 10^(-6) --> use that instead


def get_hourly_energy_consumption_in_mj(power_in_mw):
    return power_in_mw * 3600
