from textblob import TextBlob;
from textblob import Word;
import math
s1= " The Game Of Thrones";
s2= " Winter is comming in thrones";
s3= " White walker are comming thrones to kill all";
d1= TextBlob(s1);
d2= TextBlob(s2);
d3= TextBlob(s3);


doclist=[d1,d2,d3];
def isWordPresent(doc,word):
    if doc.words.count(word)>0:
        return 1;

    else:
        return 0;
totdocs=len(doclist)
print("total docs" + str(totdocs));
doc=d1;
word=Word("thrones")
tot=0
for doc in doclist:
    tot=tot+isWordPresent(doc,word);
print(tot)
subexp=(float)(totdocs)/(float)(tot)
idf=1+math.log(subexp)
print(idf)













      
