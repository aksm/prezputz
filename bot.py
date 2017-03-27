import tweepy
from secrets import *
# import os
# consumer_key = os.environ.get('CONSUMER_KEY')
# consumer_secret = os.environ.get('CONSUMER_SECRET')
# access_token = os.environ.get('ACCESS_TOKEN')
# access_secret = os.environ.get('ACCESS_SECRET')
#OAuth Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)



#convert text
import requests
import re

def putzify(text, username, status_id):
  temp_text = re.compile(re.escape('trump'), re.IGNORECASE)
  putz_text = temp_text.sub('PUTZ', text)
  api.update_status(status='@{0}'.format(username)+' '+putz_text, in_reply_to_status_id=status_id)


#Twitter Streaming API
class BotStreamer(tweepy.StreamListener):

  def on_status(self, status):
    username = status.user.screen_name
    status_id = status.id

    if status.is_quote_status:
      quoted_text = status.quoted_status['text']
      putzify(quoted_text, username, status_id)

    else:
      status_text = status.text
      putzify(status_text, username, status_id)

myStreamListener = BotStreamer()

stream = tweepy.Stream(auth, myStreamListener)

stream.filter(track=['@presidentputz'])
