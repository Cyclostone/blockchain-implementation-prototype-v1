import time
from pubnub.pubnub import PubNub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback
from backend.blockchain.block_mk10 import Block
from backend.wallet.transaction import Transaction

# subscribe_key =
# publish_key =

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-cba2b90b-d799-40a1-8a2b-51b9f812e0a9"
pnconfig.publish_key = "pub-c-08345816-39f0-45f1-8f00-1c4f031be798"
pnconfig.user_id = "arpit.shrotriya5945@gmail.com"
pubnub = PubNub(pnconfig)

# TEST_CHANNEL = 'TEST_CHANNEL'

CHANNELS = {
    "TEST": "TEST",
    "BLOCK": "BLOCK",
    "TRANSACTION": "TRANSACTION",
}


class Listener(SubscribeCallback):
    def __init__(self, blockchain, transaction_pool):
        self.transaction_pool = transaction_pool
        self.blockchain = blockchain

    def message(self, pubnub, message):
        print(f"\n -- Channel: {message.channel} | Message: {message.message}")

        if message.channel == CHANNELS["BLOCK"]:
            block = Block.from_json(message.message)
            potential_chain = self.blockchain.chain[:]
            potential_chain.append(block)

            try:
                self.blockchain.replace_chain(potential_chain)
                print(f"\n -- Successfully replaced the local chain")
            except Exception as e:
                print(f"\n -- Did not replace Chain: {e}")

        elif message.channel == CHANNELS["TRANSACTION"]:
            transaction = Transaction.from_json(message.message)
            self.transaction_pool.set_transaction(transaction)
            print("\n -- Set the new transaction in the transaction pool")


class PubSub:
    """
    Handles the publish/subscribe layer of the application.
    Provides the communication between the nodes of the blockchain network.
    """

    def __init__(self, blockchain, transaction_pool):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels(CHANNELS).execute()
        self.pubnub.add_listener(Listener(blockchain, transaction_pool))

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.unsubscribe().channels([channel]).execute()
        self.pubnub.publish().channel(channel).message(message).sync()
        self.pubnub.subscribe().channels([channel]).execute()

    def broadcast_block(self, block):
        """
        Brodcast a block object to all nodes.
        """
        self.publish(CHANNELS["BLOCK"], block.to_json())

    def broadcast_transaction(self, transaction):
        """
        Broadcast a transaction to all nodes.
        """
        self.publish(CHANNELS["TRANSACTION"], transaction.to_json())


def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(CHANNELS["TEST"], {"eren": "tatakae"})


if __name__ == "__main__":
    main()
