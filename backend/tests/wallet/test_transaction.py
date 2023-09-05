from backend.wallet.transaction import Transaction
from backend.wallet.wallet import Wallet
from backend.config import MINING_REWARD_INPUT, MINING_REWARD
import pytest


def test_transaction():
    sender_wallet = Wallet()
    recepient = "Cyclostone"
    amount = 50
    transaction = Transaction(sender_wallet, recepient, amount)

    assert transaction.output[recepient] == amount
    assert transaction.output[sender_wallet.address] == sender_wallet.balance - amount

    assert "timestamp" in transaction.input
    assert transaction.input["amount"] == sender_wallet.balance
    assert transaction.input["address"] == sender_wallet.address
    assert transaction.input["public_key"] == sender_wallet.public_key

    assert Wallet.verify(
        transaction.input["public_key"],
        transaction.output,
        transaction.input["signature"],
    )


def test_transaction_exceeds_balance():
    with pytest.raises(Exception, match="Amount Exceeds the balance"):
        Transaction(Wallet(), "ino", 1020)


def test_transaction_update_exceeds_balance():
    sender_wallet = Wallet()
    transaction = Transaction(sender_wallet, "pink trash", 50)

    with pytest.raises(Exception, match="Amount Exceeds the balance"):
        transaction.update(sender_wallet, "kazui", 5945)


def test_transaction_update():
    sender_wallet = Wallet()
    first_rep = "tony"
    first_amount = 250

    transaction = Transaction(sender_wallet, first_rep, first_amount)

    second_rep = "ezekiel"
    second_amount = 75
    transaction.update(sender_wallet, second_rep, second_amount)

    assert transaction.output[second_rep] == second_amount
    assert (
        transaction.output[sender_wallet.address]
        == sender_wallet.balance - first_amount - second_amount
    )

    assert Wallet.verify(
        transaction.input["public_key"],
        transaction.output,
        transaction.input["signature"],
    )

    again_first_amount = 250
    transaction.update(sender_wallet, first_rep, again_first_amount)

    assert transaction.output[first_rep] == first_amount + again_first_amount
    assert transaction.output[sender_wallet.address] == sender_wallet.balance - (
        first_amount + second_amount + again_first_amount
    )

    assert Wallet.verify(
        transaction.input["public_key"],
        transaction.output,
        transaction.input["signature"],
    )


def test_valid_transaction():
    Transaction.is_valid_transaction(Transaction(Wallet(), "choji", 70))


def test_valid_transaction_with_invalid_outputs():
    sender_wallet = Wallet()
    transaction = Transaction(sender_wallet, "yo", 590)
    transaction.output[sender_wallet.address] = 5900

    with pytest.raises(Exception, match="Invalid transaction output values"):
        Transaction.is_valid_transaction(transaction)


def test_valid_transaction_with_invalid_signature():
    transaction = Transaction(Wallet(), "ace", 60)
    transaction.input["signature"] = Wallet().sign(transaction.output)

    with pytest.raises(Exception, match="Invalid Signature"):
        Transaction.is_valid_transaction(transaction)


def test_reward_transaction():
    miner_wallet = Wallet()
    transaction = Transaction.reward_transaction(miner_wallet)

    assert transaction.input == MINING_REWARD_INPUT
    assert transaction.output[miner_wallet.address] == MINING_REWARD


def test_valid_reward_transaction():
    reward_transaction = Transaction.reward_transaction(Wallet())
    Transaction.is_valid_transaction(reward_transaction)


def test_invalid_reward_transaction_extra_recipient():
    reward_transaction = Transaction.reward_transaction(Wallet())
    reward_transaction.output["extra_recipient"] = 60

    with pytest.raises(Exception, match="Invalid mining reward"):
        Transaction.is_valid_transaction(reward_transaction)


def test_invalid_reward_transaction_invalid_amount():
    miner_wallet = Wallet()
    reward_transaction = Transaction.reward_transaction(miner_wallet)
    reward_transaction.output[miner_wallet.address] = 5000

    with pytest.raises(Exception, match="Invalid mining reward"):
        Transaction.is_valid_transaction(reward_transaction)
