#!/usr/bin/env python
# coding: utf-8
import tweepy
import time
import random
import pymongo
import json
import sys

# Functions
def get_creds(line):  
  keys = []    
  for l in line:
    keys.append(l.split("=")[1].splitlines(False)[0])
  return keys

tw_creds = open("creds.txt", "r")
lines = tw_creds.readlines()


# Twitter API Credentials
CONSUMER_KEY = get_creds(lines)[0]
CONSUMER_SECRET = get_creds(lines)[1]
ACCESS_TOKEN = get_creds(lines)[2]
ACCESS_TOKEN_SECRET = get_creds(lines)[3]

# Hashtags
HASHTAG = ['#AI']

# Datas of CosmoDB - clusterName, db, collection
uri = "mongodb://<ENDPOINT>"
client = pymongo.MongoClient(uri)

db = client.TwitterDB_AI
collection = db.hashtag

# Main functions
class StreamListener(tweepy.StreamListener):
    #This is a class provided by tweepy to access the Twitter Streaming API. 

    def on_connect(self):
        # Called initially to connect to the Streaming API
        print("You are now connected to the streaming API.")

    def on_error(self, status_code):
        # On error - if an error occurs, display the error / status code
        print('An Error has occured: ' + repr(status_code))
        return False

    def on_data(self, data):
        #This is the meat of the script...it connects to your mongoDB and stores the tweet
        try:
            # client = MongoClient(MONGO_HOST)
            # Use twitterdb database. If it doesn't exist, it will be created.
            # db = client.twitterdb
            # Decode the JSON from Twitter
            datajson = json.loads(data)

            #grab the 'created_at' data from the Tweet to use for display
            created_at = datajson['created_at']

            #print out a message to the screen that we have collected a tweet
            print("Tweet collected at " + str(created_at))

            #insert the data into the mongoDB into a collection called twitter_search
            #if twitter_search doesn't exist, it will be created.
            db.twitter_search.insert(datajson)
        except Exception as e:
            print(e)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
#Set up the listener. The 'wait_on_rate_limit=True' is needed to help with Twitter API rate limiting.
listener = StreamListener(api=tweepy.API(wait_on_rate_limit=True))
streamer = tweepy.Stream(auth=auth, listener=listener)
print("Tracking: " + str(HASHTAG))
streamer.filter(track=HASHTAG)