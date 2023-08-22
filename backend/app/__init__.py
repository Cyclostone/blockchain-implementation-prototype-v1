import os
import random
from flask import Flask, jsonify
from backend.blockchain.blockchain_mk7 import Blockchain
from backend.pubsub_mk3 import PubSub

app = Flask(__name__)
# print(f'The NAME: {__name__}')
blockchain = Blockchain()
pubsub = PubSub()

# for i in range(3):
#     blockchain.addBlock(i)

@app.route('/test')
def test():
    return 'test'

@app.route('/')
def route_default():
    return 'Welcome to Blockchain'

@app.route('/blockchain')
def route_blockchain():
    # return blockchain.chain
    # return blockchain.__repr__()
    return jsonify(blockchain.to_json())

@app.route('/blockchain/mine')
def route_blockchain_mine():
    transaction_data = 'stubbed_transacton_data'
    blockchain.addBlock(transaction_data)
    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)
    return jsonify(block.to_json())

PORT = 5000

if os.environ.get('PEER') == 'True':
    PORT = random.randint(5001, 6000)

# app.run(port=5001)
app.run(port=PORT)

