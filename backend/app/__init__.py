from flask import Flask, jsonify
from backend.blockchain.blockchain_mk7 import Blockchain

app = Flask(__name__)
# print(f'The NAME: {__name__}')
blockchain = Blockchain()

for i in range(3):
    blockchain.addBlock(i)

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

# app.run(port=5001)
app.run()

