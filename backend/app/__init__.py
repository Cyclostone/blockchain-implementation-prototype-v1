import os
import random
import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
from backend.blockchain.blockchain_mk7 import Blockchain
from backend.pubsub_mk3 import PubSub
from backend.wallet.wallet import Wallet
from backend.wallet.transaction import Transaction
from backend.wallet.transaction_pool import TransactionPool

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
blockchain = Blockchain()
transaction_pool = TransactionPool()
pubsub = PubSub(blockchain, transaction_pool)
wallet = Wallet(blockchain)

# for i in range(3):
#     blockchain.addBlock(i)


@app.route("/test")
def test():
    return "test"


@app.route("/")
def route_default():
    return "Welcome to Blockchain"


@app.route("/blockchain")
def route_blockchain():
    # return blockchain.chain
    # return blockchain.__repr__()
    return jsonify(blockchain.to_json())


@app.route("/blockchain/mine")
def route_blockchain_mine():
    transaction_data = transaction_pool.transaction_data()
    transaction_data.append(Transaction.reward_transaction(wallet).to_json())
    blockchain.addBlock(transaction_data)
    block = blockchain.chain[-1]
    pubsub.broadcast_block(block)
    transaction_pool.clear_blockchain_transactions(blockchain)
    return jsonify(block.to_json())


@app.route("/wallet/transact", methods=["POST"])
def route_wallet_transact():
    # api input: {'recipient':'foo', 'amount':15}
    transaction_data = request.get_json()
    transaction = transaction_pool.existing_transaction(wallet.address)

    if transaction:
        transaction.update(
            wallet, transaction_data["recipient"], transaction_data["amount"]
        )
    else:
        transaction = Transaction(
            wallet, transaction_data["recipient"], transaction_data["amount"]
        )

    # print(f"transaction.to_json(): {transaction.to_json()}")
    pubsub.broadcast_transaction(transaction)

    return jsonify(transaction.to_json())


@app.route("/wallet/info")
def route_wallet_info():
    return jsonify({"address": wallet.address, "balance": wallet.balance})


ROOT_PORT = 5000
PORT = 5000

if os.environ.get("PEER") == "True":
    PORT = random.randint(5001, 6000)

    result = requests.get(f"http://localhost:{ROOT_PORT}/blockchain")
    print(f"result.json() : {result.json()}")

    result_blockchain = Blockchain.from_json(result.json())
    try:
        blockchain.replace_chain(result_blockchain.chain)
        print("\n -- Successfully synchronized the local chain")
    except Exception as e:
        print(f"\n -- Error Synchronizing: {e}")

# app.run(port=5001)
app.run(port=PORT)
