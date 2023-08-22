import time

class Block:
    """
    Block: A Unit Of Storage
    Store Transactions in a blockchain that supports cryptocurrency.
    """

    def __init__(self, timestamp, last_hash, hash, data):
        self.timestamp = timestamp
        self.last_hash = last_hash
        self.hash = hash
        self.data = data

    def __repr__(self) -> str:
        return (
            'Block ('
            f'Timestamp : {self.timestamp}, '
            f'Last hash : {self.last_hash}, '
            f'Hash : {self.hash},  '
            f'Data : {self.data})'
        )
    
    @staticmethod
    def mine_block(last_block, data):
        """
        Mines a block based on last_block, data
        """
        timestamp = time.time_ns()
        last_hash = last_block.hash
        hash = f'{timestamp}-{last_hash}'

        return Block(timestamp, last_hash, hash, data)
    
    @staticmethod
    def genesis():
        """
        Generate Genesis Block
        """

        return Block(1, '0000', 'genesis_block_hash', [])

def main():
    # block = Block('luffy')
    # print(block)
    # print(f'block.py __name__: {__name__}')

    genesis_block = Block.genesis()
    block = Block.mine_block(genesis_block, 'vinsmoke')
    print(block)

if __name__ == "__main__":
    main()