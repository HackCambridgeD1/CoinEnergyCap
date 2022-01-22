from enum import Enum


class CryptocurrencyType(str, Enum):
    PROOF_OF_WORK = "proof_of_work"
    PROOF_OF_STAKE = "proof_of_stake"
