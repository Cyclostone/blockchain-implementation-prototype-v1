from backend.blockchain.blockchain_mk4 import Blockchain
from backend.blockchain.block_mk7 import GENESIS_DATA

def test_blockchain_instance():
    blockchain = Blockchain()

    assert blockchain.chain[0].hash == GENESIS_DATA['hash']

def test_add_block():
    blockchain = Blockchain()
    data = 'test-data'
    blockchain.addBlock(data)

    assert blockchain.chain[-1].data == data