from dataclasses import dataclass

from flax.types.blockchain_format.coin import Coin
from flax.types.blockchain_format.sized_bytes import bytes32
from flax.util.ints import uint32, uint64
from flax.util.streamable import Streamable, streamable


@dataclass(frozen=True)
@streamable
class CoinRecord(Streamable):
    """
    These are values that correspond to a CoinName that are used
    in keeping track of the unspent database.
    """

    coin: Coin
    confirmed_block_index: uint32
    spent_block_index: uint32
    spent: bool
    coinbase: bool
    timestamp: uint64  # Timestamp of the block at height confirmed_block_index

    @property
    def name(self) -> bytes32:
        return self.coin.name()
