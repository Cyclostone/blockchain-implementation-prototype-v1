import time
from pubnub.pubnub import PubNub 
from pubnub.pnconfiguration import PNConfiguration
from pubnub.callbacks import SubscribeCallback

# subscribe_key = 
# publish_key = 

pnconfig = PNConfiguration()
pnconfig.subscribe_key = 'sub-c-cba2b90b-d799-40a1-8a2b-51b9f812e0a9'
pnconfig.publish_key = 'pub-c-08345816-39f0-45f1-8f00-1c4f031be798'
pnconfig.user_id = 'arpit.shrotriya5945@gmail.com'
pubnub = PubNub(pnconfig)

TEST_CHANNEL = 'TEST_CHANNEL'



class Listener(SubscribeCallback):
    def message(self, pubnub, message):
        print(f'\n -- Channel: {message.channel} | Message: {message.message}')



class PubSub():
    """
    Handles the publish/subscribe layer of the application.
    Provides the communication between the nodes of the blockchain network.
    """
    def __init__(self):
        self.pubnub = PubNub(pnconfig)
        self.pubnub.subscribe().channels([TEST_CHANNEL]).execute()
        self.pubnub.add_listener(Listener())

    def publish(self, channel, message):
        """
        Publish the message object to the channel.
        """
        self.pubnub.publish().channel(channel).message(message).sync()

def main():
    pubsub = PubSub()
    time.sleep(1)
    pubsub.publish(TEST_CHANNEL, {'eren':'tatakae'})
    
    

if __name__=='__main__':
    main()