class Block:
    """
    Block: A Unit Of Storage
    Store Transactions in a blockchain that supports cryptocurrency.
    """

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f'Block - Data : {self.data}'




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


blockchain = Blockchain()
blockchain.addBlock(5)
blockchain.addBlock(8)
print(blockchain)
        