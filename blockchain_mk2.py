from block_mk2 import Block

class Blockchain:
    """
    Blockchain: A public Ledger for Transactions
    Implemented as a chain of blocks
    """

    def __init__(self):
        self.chain = []

    def addBlock(self, data):
        self.chain.append(Block(data))

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