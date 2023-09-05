from backend.wallet.wallet import Wallet
from backend.blockchain.blockchain_mk7 import Blockchain
from backend.wallet.transaction import Transaction
from backend.config import STARTING_BALANCE


def test_verify_valid_signature():
    data = {"foo": "test_data"}
    wallet = Wallet()
    signature = wallet.sign(data)

    assert Wallet.verify(wallet.public_key, data, signature)


def test_verify_invalid_signature():
    data = {"foo": "test_data"}
    wallet = Wallet()
    signature = wallet.sign(data)

    assert not Wallet.verify(Wallet().public_key, data, signature)


def test_calculate_balance():
    blockchain = Blockchain()
    wallet = Wallet()

    assert Wallet.calculate_balance(blockchain, wallet.address) == STARTING_BALANCE

    amount = 75
    transaction_1 = Transaction(wallet, "newgate", amount)
    blockchain.addBlock([transaction_1.to_json()])

    assert (
        Wallet.calculate_balance(blockchain, wallet.address)
        == STARTING_BALANCE - amount
    )

    recieved_amount_1 = 250
    transaction_2 = Transaction(Wallet(), wallet.address, recieved_amount_1)

    recieved_amount_2 = 25
    transaction_3 = Transaction(Wallet(), wallet.address, recieved_amount_2)

    blockchain.addBlock([transaction_2.to_json(), transaction_3.to_json()])

    assert (
        Wallet.calculate_balance(blockchain, wallet.address)
        == STARTING_BALANCE - amount + recieved_amount_1 + recieved_amount_2
    )
