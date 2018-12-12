from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

# From the twitter developer's account
#consumer key, consumer secret, access token, access secret.

# I've regenerated these tokens, so do not copy them xDxD
ckey='YI3WOidCTeeYCVDBjLcgXzvpW'
csecret='mtUBQJsFZ1Tg7h3sFbix6Pb81kcow1eVId6OX44FL8DBbWpqaI'
atoken = '793442207508287491-6FQokeVwbrjX7iIdOT0E0uXCLEi784q'
asecret = 'iSbK56Fdt9JgdysyoFWpvahhsQFjQqlPQpVspyjaxTJrq'

class listener(StreamListener):
    def on_data(self, data):
        try:
            print(data)
            file = open('database.csv', 'a')
            file.write(data)
            file.write('\n')
            file.write('\n')
            file.close()
        except BaseException as error:
            print("Couldn't write because of: "+ str(error))
            time.sleep(5)
    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])    
