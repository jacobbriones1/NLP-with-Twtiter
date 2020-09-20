# The getTweets.py function contains a single method which 
#   initializes a live stream of tweets which contain keywords
#   specified by the user. The tweets are stored into a json file
#   named tweets.json
#   Written by Jacob Briones: of tweets 
import datetime
import os
import json
#  For authenticating Twitter API
import credentials
# For streaming live tweets
from tweepy import Stream

# keywords_to_track: list of strings to watch for.
def getTweets(ketwords_to_track):
        #  Retrieve credentials
        consumer_key = credentials.CONSUMER_KEY
        consumer_secret = credentials.CONSUMER_SECRET
        access_token = credentials.ACCESS_TOKEN
        access_secret = credentials.ACCESS_SECRET
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        
        #  Authorization 
        auth.set_access_token(access_token, access_secret)
        
        # Instantiate Twitter API.
        # NOTE:Twitter limits the amount of data that a user may stream.
        #   if a user revcieves a rate_limit warning, then the user must 
        #   wait one hour before accessing data. The wait_on_rate_limit
        #   parameter ensures that our program will not terminate if this
        #   error occurs.
        api = tweepy.API(auth, wait_on_rate_limit=True,)
        
        # The file which we will be storing tweets in will be tweets.json
        save_file = open('tweets.json', 'a')
        
        # Overriding the Streamlistener class allows us to specify how we
        # want to handle our incoming twitter data.
        class CustomStreamListener(tweepy.StreamListener):
            def __init__(self, api):
                self.api = api
                super(tweepy.StreamListener, self).__init__()
                self.save_file = tweets
            
            # This method specifies that we want each tweet object to be
            # stored as a json object in our file in real time
            def on_data(self, tweet):
                self.save_file.append(json.loads(tweet))
                print(tweet)
                save_file.write(str(tweet))
                
        # Initiate the stream
        stream = Stream(auth, CustomStreamListener(api), tweet_mode='extended')
        stream.filter(track=keywords_to_track)
