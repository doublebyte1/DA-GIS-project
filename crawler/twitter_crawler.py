import tweepy
from tweepy import Stream
#from tweepy.stream import StreamListener 
from tweepy import OAuthHandler
import json

consumer_key = 'sOFJBb6SlaGaQAm0lYzKjoRWP'
consumer_secret = 'E8HCTfkFkXxHzVJB5z9zV0VXjXlk6XbfiEv0IQOKBqTDrA7YXI'
access_token = '19970339-N6TJUc2hSFdTWmXa790BZ0xphhZeOjK1tiC0IbbjH'
access_secret = '36EriZwc8u3yUjXluUMD3xAgrG8f0QQL7Eb4J5mTcP14q'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
@classmethod
def parse(cls, api, raw):
    status = cls.first_parse(api, raw)
    setattr(status, 'json', json.dumps(raw))
    return status
 
# Status() is the data model for a tweet
tweepy.models.Status.first_parse = tweepy.models.Status.parse
tweepy.models.Status.parse = parse
class MyListener(tweepy.StreamListener):
 
    def on_data(self, data):
        try:
            with open('FILENAME.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s" % str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
#Set the hashtag to be searched
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#COVID'])