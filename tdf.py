
import nltk
import string
import os
from nltk.stem.porter import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

# token_dict = {'doc2':"Todays match is against the might germans"}
# stemmer = PorterStemmer()

# def stem_tokens(tokens, stemmer):
#     stemmed = []
#     for item in tokens:
#         stemmed.append(stemmer.stem(item))
#     return stemmed

# def tokenize(text):
#     tokens = nltk.word_tokenize(text)

#     for each in tokens:
#         print(each)
#     return tokens

# #this can take some time
# tfidf = TfidfVectorizer(tokenizer=tokenize, stop_words='english')
# tfs = tfidf.fit_transform(token_dict.values())
# print(type(tfs))
# print(tfs)


# str = 'this sentence has unseen text such as computer but also king lord juliet'
# response = tfidf.transform([str])
# print (response)

documents = ["The sky is bright","The sky is bright"]

tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
print (tfidf_matrix.shape)
print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)) #[0:1] get the first row of the sparse matrix

container=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)
print(len(container[0]))

for each in container[0]:
    print(each)