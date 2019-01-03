from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

s1="The sky is blue"
s2="The sun is bright"
s3="The flowers are beautiful"
s4="cersei is beautiful"
s5="jon snow is bright"

query="The day is bright and beautiful"
#dataset=[s1,s2,s3]
dataset=[query,s1,s2,s3,s4,s5]


tfidf=TfidfVectorizer()
tfidf.fit(dataset)

#dataset=[query,s1,s2,s3,s4,s5]
matrix=tfidf.fit_transform(dataset)
print(matrix)

dict=(tfidf.vocabulary_)
for key in dict.keys():
 print(key+""+str(dict[key]))
