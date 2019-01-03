from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


f=open("/home/ai15/Documents/nlp/DAY5/nlpd5q2.txt")
R=f.read()
print R
query="The day is bright and beautiful"
dataset=[query,R]


tfidf=TfidfVectorizer()
tfidf.fit(dataset)


matrix=tfidf.fit_transform(dataset)
print(matrix)

dict=(tfidf.vocabulary_)
for key in dict.keys():
 print(key+""+str(dict[key]))
