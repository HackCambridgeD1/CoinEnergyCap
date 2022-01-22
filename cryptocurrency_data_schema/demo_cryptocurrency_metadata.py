from cryptocurrency_data_schema.cryptocurrency_metadata import CryptocurrencyMetadata
from cryptocurrency_type import CryptocurrencyType

PROOF_OF_WORK = CryptocurrencyType.PROOF_OF_WORK

demo_metadata = [
    CryptocurrencyMetadata(symbol="BTC", name="Bitcoin", joules_per_hash=2.53E+10, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="ETH", name="Ethereum", joules_per_hash=1.64E+14, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="BSV", name="Bitcoin SV", joules_per_hash=3.88E+18, type=PROOF_OF_WORK),
]
