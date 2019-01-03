from textblob import TextBlob
s1="jon snow is a good killer"
t1=TextBlob(s1)
print(t1.sentiment)
#if t1.sentiment.polarity>0:
#   print("positive")
#if t1.sentiment.polarity<0:
#  print("negative")
#if t1.sentiment.polarity==0;
#  print("neutral")
