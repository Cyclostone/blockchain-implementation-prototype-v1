from backend.blockchain.block_mk10 import Block
from backend.wallet.transaction import Transaction
from backend.wallet.wallet import Wallet
from backend.config import MINING_REWARD_INPUT


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
        return f"The BlockChain: {self.chain}"

    def replace_chain(self, chain):
        """
        Replace the local chain with the incoming one if the following applies:
        - The incoming chain is longer than the local one.
        - The incoming chain is formatted properly.
        """
        if len(chain) <= len(self.chain):
            raise Exception("Cannot replace the incoming chain must be longer.")

        try:
            Blockchain.is_valid_chain(chain)
        except:
            raise Exception(f"Cannot replace, the incoming chain is invalid")

        self.chain = chain

    def to_json(self):
        """
        serialize the blockchain into a list of blocks
        """
        # serialized_chain = []

        # for block in self.chain:
        #     serialized_chain.append(block.to_json())
        # return serialized_chain
        return list(map(lambda block: block.to_json(), self.chain))

    @staticmethod
    def from_json(chain_json):
        """
        Deserialize a list of serialized blocks into a blockchain instance.
        The result will contain a chain list of Block instances.
        """
        blockchain = Blockchain()
        blockchain.chain = list(
            map(lambda block_json: Block.from_json(block_json), chain_json)
        )
        return blockchain

    @staticmethod
    def is_valid_chain(chain):
        """
        Validate the incoming chain.
        Enforce the following rules of the blockchain:
        - the chain must start with the genesis block
        - blocks must be formatted correctly
        """
        if chain[0] != Block.genesis():
            raise Exception("The genesis block must be valid")

        for i in range(1, len(chain)):
            block = chain[i]
            last_block = chain[i - 1]
            Block.is_valid_block(last_block, block)

        Blockchain.is_valid_transaction_chain(chain)

    @staticmethod
    def is_valid_transaction_chain(chain):
        """
        Enforce the rules of a chain composed of blocks of transactions.
        - Each transaction must only appear once in the chain.
        - There can only be one mining reward per block
        - Each transaction must be valid.
        """
        transaction_ids = set()

        for i in range(len(chain)):
            block = chain[i]
            has_mining_reward = False
            for transaction_json in block.data:
                transaction = Transaction.from_json(transaction_json)

                if transaction.id in transaction_ids:
                    raise Exception(f"Transaction {transaction_ids} is not unique")

                transaction_ids.add(transaction.id)

                if transaction.input == MINING_REWARD_INPUT:
                    if has_mining_reward:
                        raise Exception(
                            f"There can only be one mining reward per block\n Check block with hash: {block.hash}"
                        )
                    has_mining_reward = True
                else:
                    historic_blockchain = Blockchain()
                    historic_blockchain.chain = chain[0:i]
                    historic_balance = Wallet.calculate_balance(
                        historic_blockchain, transaction.input["address"]
                    )

                    if historic_balance != transaction.input["amount"]:
                        raise Exception(
                            f"Transaction {transaction.id} has an invalid input amount"
                        )

                Transaction.is_valid_transaction(transaction)


def main():
    blockchain = Blockchain()
    blockchain.addBlock(5)
    blockchain.addBlock(8)
    print(blockchain)
    print(f"blockchain_mk4.py __name__ : {__name__}")


if __name__ == "__main__":
    main()
