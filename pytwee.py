from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

# From the twitter developer's account
#consumer key, consumer secret, access token, access secret.


api_key = input('Enter the API Key: \n')
secret_api_key = input('Enter the API secret key: \n')
access_token = input('Enter Access token: \n')
access_token_secret = input('Access token secret: \n')

class listener(StreamListener):
    def on_data(self, data):
        try:
            # Trimming out tweets from the data 
            tweet = data.split(',"text":"')[1].split('","source"')[0]

 	    # Appending
            file = open('database.csv', 'a')
            file.write(tweet)
            file.write('\n')
            file.write('\n')
            file.close()
        except BaseException as error:
            print("Couldn't write because of: "+ str(error))
            time.sleep(5)
    def on_error(self, status):
        print (status)

auth = OAuthHandler(api_key, secret_api_key)
auth.set_access_token(access_token, access_token_secret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])    
