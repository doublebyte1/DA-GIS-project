import tweepy

consumer_key = 'sOFJBb6SlaGaQAm0lYzKjoRWP'
consumer_secret = 'E8HCTfkFkXxHzVJB5z9zV0VXjXlk6XbfiEv0IQOKBqTDrA7YXI'
access_token = '19970339-N6TJUc2hSFdTWmXa790BZ0xphhZeOjK1tiC0IbbjH'
access_secret = '36EriZwc8u3yUjXluUMD3xAgrG8f0QQL7Eb4J5mTcP14q'

key = tweepy.OAuthHandler(consumer_key, consumer_secret)
key.set_access_token(access_token, access_secret)
 
# here come the tweepy part:
class stream2lib(tweepy.StreamListener):
    output = {}
    def __init__(self, api=None):
        api = tweepy.API(key)
        self.api = api or API()
        self.n = 0 #we will start with zero tweets
        self.m = 10 #let's stop with 10 tweets
        def on_status(self, status):
        #we will parse the interesting information into a nice format
            self.output[status.id] = {
                'tweet':status.text.encode('utf8'), #text could have non utf8 characters, so change this!
                'user':status.user.screen_name.encode('utf8'), #user name should be utf8 conform as well
                'geo':status.geo, #this is the point location of the device
                'localization':status.user.location, #user location as part of the user profile (normally set fixed per user)
                'time_zone':status.user.time_zone, #quite
                'time':status.timestamp_ms} #the timestamp given in ms since 01.01.1970
            #we will only care about tweets with geo
            if self.output[status.id]['geo']!=None:
                self.n = self.n+1 #we found a geotweet. but that's always true when calling the command with "locations=[-x,-y,x,y]" as below
                if self.n < self.m:
                    return True
                else:
                    return False
        stream = tweepy.streaming.Stream(key, stream2lib()) #initiate the stream
        stream.filter(locations=[-180,-90,180,90]) #filter the stream for tweets in this "box"
        tweetdic = stream2lib().output #copy it in a variable
        print (tweetdic) #just to be sure ;-) 
