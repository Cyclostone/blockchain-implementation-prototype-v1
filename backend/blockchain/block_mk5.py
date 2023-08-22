import time
from backend.util.crypto_hash_mk3 import crypto_hash

GENESIS_DATA = {
    'timestamp': 1,
    'last_hash': 'genesis_last_hash',
    'hash': 'genesis_hash',
    'data': [],
    'difficulty': 3,
    'nonce': 'genesis_nonce'
}

class Block:
    """
    Block: A Unit Of Storage
    Store Transactions in a blockchain that supports cryptocurrency.
    """

    def __init__(self, timestamp, last_hash, hash, data, difficulty, nonce):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data
        self.difficulty = difficulty
        self.nonce = nonce

    def __repr__(self) -> str:
        return (
            'Block ('
            f'Timestamp : {self.timestamp}, '
            f'Last hash : {self.last_hash}, '
            f'Hash : {self.hash},  '
            f'Data : {self.data}, '
            f'Difficulty : {self.difficulty}, '
            f'Nonce : {self.nonce})'
        )
    
    @staticmethod
    def mine_block(last_block, data):
        """
        Mines a block based on last_block, data, until a block hash
        is found that meets the leading 0's proof of work requirement.
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        #hash = f'{timestamp}-{last_hash}'
        difficulty = last_block.difficulty
        nonce = 0
        hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)
        
        while hash[0:difficulty] != '0' * difficulty:
            nonce += 1
            timestamp = time.time_ns()
            hash = crypto_hash(timestamp, last_hash, data, difficulty, nonce)

        return Block(timestamp, last_hash, hash, data, difficulty, nonce)
    
    @staticmethod
    def genesis():
        """
        Generate Genesis Block
        """

        # return Block(
        #     GENESIS_DATA['timestamp'],
        #     GENESIS_DATA['last_hash'],
        #     GENESIS_DATA['hash'],
        #     GENESIS_DATA['data']
        # )
        return Block(**GENESIS_DATA)

def main():
    # block = Block('luffy')
    # print(block)
    # print(f'block.py __name__: {__name__}')

    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'vinsmoke')
    print(block)

if __name__ == "__main__":
    main()