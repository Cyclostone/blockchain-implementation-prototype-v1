from backend.blockchain.block_mk10 import Block

class Blockchain:
    """
    Blockchain: A public Ledger for Transactions
    Implemented as a chain of blocks
    """

    def __init__(self):
        self.chain = [Block.genesis()]

    def addBlock(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'The BlockChain: {self.chain}'
    
    def replace_chain(self, chain):
        """
        Replace the local chain with the incoming one if the following applies:
         - The incoming chain is longer than the local one.
         - The incoming chain is formatted properly.
        """
        if len(chain) <= len(self.chain):
            raise Exception('Cannot replace the incoming chain must be longer.')
        
        try:
            Blockchain.is_valid_chain(chain)
        except:
            raise Exception(f'Cannot replace, the incoming chain is invalid')
        
        self.chain = chain

    def to_json(self):
        """
        serialize the blockchain into a list of blocks
        """
        serialized_chain = []

        for block in self.chain:
            serialized_chain.append(block.to_json())
        return serialized_chain

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain.
        Enforce the following rules of the blockchain:
         - the chain must start with the genesis block
         - blocks must be formatted correctly
        """
        if chain[0] != Block.genesis():
            raise Exception('The genesis block must be valid')

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i-1]
            Block.is_valid_block(last_block, block)

def main():
    blockchain = Blockchain()
    blockchain.addBlock(5)
    blockchain.addBlock(8)
    print(blockchain)
    print(f'blockchain_mk4.py __name__ : {__name__}')
        
if __name__ == "__main__":
    main()