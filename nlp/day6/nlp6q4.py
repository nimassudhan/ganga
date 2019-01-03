import tweepy
from textblob import TextBlob
consumer_key="GwSN2UgAvnfOiLlFFWJwAA0Xx"
consumer_secret="y2JctkUCYNVHCBx2DsIr7UkWN1FBmShASb8dbpsxDNPcqY7LMr"
access_token="1070963226953711617-80rh8y0TAkYQroa5Ifh40BEQtTRDiT"
access_token_secret="v5VAXcNZKdNWNdhtfuG490bpfskLlebMbBni2pKztnbHk"

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
user=api.me()
print (user.name)
poscount=0
negcount=0
nuecount=0

public_tweets=api.user_timeline("@FIFAcom")
for tweet in public_tweets:
   t1=TextBlob(tweet.text)
   print("..........")
   print tweet.text
 #  print t1

if t1.sentiment.polarity>0:
   print("positive")
if t1.sentiment.polarity<0:
   print("negative")
if t1.sentiment.polarity==0:
   print("neutral")



