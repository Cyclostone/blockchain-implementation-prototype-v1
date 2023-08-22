from block_mk3 import Block, genesis, mine_block

class Blockchain:
    """
    Blockchain: A public Ledger for Transactions
    Implemented as a chain of blocks
    """

    def __init__(self):
        self.chain = [genesis()]

    def addBlock(self, data):
        self.chain.append(mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'The BlockChain: {self.chain}'

def main():
    blockchain = Blockchain()
    blockchain.addBlock(5)
    blockchain.addBlock(8)
    print(blockchain)
    print(f'blockchain_mk2.py __name__ : {__name__}')
        
if __name__ == "__main__":
    main()