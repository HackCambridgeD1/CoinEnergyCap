from app.sources.cryptocurrency_data_schema.cryptocurrency_metadata import CryptocurrencyMetadata
from app.sources.cryptocurrency_data_schema.cryptocurrency_type import CryptocurrencyType

PROOF_OF_WORK = CryptocurrencyType.PROOF_OF_WORK

demo_metadata = [
    CryptocurrencyMetadata(symbol="BTC", name="Bitcoin", efficiency=2.53E+10, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="ETH", name="Ethereum", efficiency=2.28E+05, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="BSV", name="Bitcoin SV", efficiency=2.53E+10, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="BCH", name="Bitcoin Cash", efficiency=2.53E+10, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="LTC", name="Litecoin", efficiency=8.27E+05, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="XMR", name="Monero", efficiency=6.00E+00, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="DASH", name="Dash", efficiency=1.23E+08, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="ETC", name="Ethereum C", efficiency=2.28E+05, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="ZEC", name="Zcash", efficiency=9.00E+01, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="DOGE", name="DogeCoin", efficiency=8.27E+05, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="DCR", name="Decred", efficiency=1.89E+10, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="RVN", name="RavenCoin", efficiency=1.16E+05, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="MONA", name="MonaCoin", efficiency=1.17E+07, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="BTM", name="Bytom", efficiency=1.82E+02, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="SC", name="SiaCoin", efficiency=1.22E+09, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="DGB", name="DigiByte", efficiency=2.53E+10, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="ZEN", name="Horizen", efficiency=9.00E+01, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="KMD", name="Komodo", efficiency=9.00E+01, type=PROOF_OF_WORK),
    CryptocurrencyMetadata(symbol="BCN", name="Bytecoin", efficiency=5.00E+02, type=PROOF_OF_WORK)
]

demo_metadata_map = {metadata.symbol: metadata for metadata in demo_metadata}