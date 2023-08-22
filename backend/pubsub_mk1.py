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

pubnub.subscribe().channels([TEST_CHANNEL]).execute()

class Listener(SubscribeCallback):
    def message(self, pubnub, message):
        print(f'\n -- Incoming Message_Object: {message}')

pubnub.add_listener(Listener())

def main():
    time.sleep(1)
    pubnub.publish().channel(TEST_CHANNEL).message({'eren':'tatakae'}).sync()

if __name__=='__main__':
    main()