class Block:
    """
    Block: A Unit Of Storage
    Store Transactions in a blockchain that supports cryptocurrency.
    """

    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return f'Block - Data : {self.data}'

def main():
    block = Block('luffy')
    print(block)
    print(f'block.py __name__: {__name__}')

if __name__ == "__main__":
    main()