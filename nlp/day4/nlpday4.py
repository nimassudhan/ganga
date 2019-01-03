from textblob import TextBlob;
from textblob import Word;
s1= " The Game Of Thrones";
s2= " Winter is comming in thrones";
s3= " White walker are comming to kill all";
d1= TextBlob(s1);
d2= TextBlob(s2);
d3= TextBlob(s3);

word=Word("thrones");
doclist=[d1,d2,d3];
for doc in doclist:
 wordlist=doc.words;
 #noofwords=len(wordlist);

 for word in wordlist:

  tf=doc.words.count(word);
  
  print(tf)
  print(word+"occur"+str(tf)+"times")

#ntf=tf/noofwords;
#print(ntf)      
