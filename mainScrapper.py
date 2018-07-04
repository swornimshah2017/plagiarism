import requests,json
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import nltk
import os
from nltk.tokenize import sent_tokenize,word_tokenize
import difflib
from nltk.stem.porter import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer

os.system("chcp 65001")

innerUrls=[]
divPost=[]
filteredPosts=[]#this is the actual post that will be stored in the database
urlContainer=[
    "http://www.ekantipur.com/eng",
    "https://thehimalayantimes.com/",
# "http://www.fb.com/",
    "http://kathmandupost.ekantipur.com/",
    "http://annapurnapost.com/",
   "http://www.nepalipatra.com/"
]

for index,eachurl in enumerate(urlContainer):
    request=requests.get(eachurl,headers={'User-Agent': 'Mozilla/5.0'})
    # request=requests.get("https://kec.edu.np/",headers={'User-Agent': 'Mozilla/5.0'})
    if request.status_code==200:
        print('Request was successfull')
        # print(request.content)
        #print(request.text)
        soup=BeautifulSoup(request.content,"lxml",from_encoding='utf-8')
        for script in soup(["script", "style"]):
            script.extract()
            #remove all the scripts and styles

        print(soup.prettify().encode('utf-8'))
        print('title of page',soup.title.text.encode('ascii', errors='replace').decode().replace("?", ""))
        # print('p ',soup.find_all('p'))
        # #print(soup.get_text()) gets all the text including code js
        for eachParagraph in soup.find_all('p'):
            print(eachParagraph.text.encode('ascii', errors='replace').decode().replace("?", ""))
            
        for url in soup.find_all('a'):
            # print(url.text)
            # #get the tags but we need the actual link 
            print(url.get('href'))
            # print('My urls ',url.text.encode('ascii', errors='replace').decode().replace("?", ""))
            urljoin(urlContainer[index],url.get('href'))
            innerUrls.append(urljoin(urlContainer[index],url.get('href')))
            # print('all the div ')


        
            
        for eachdiv in soup.find_all('div'):
            # print(eachdiv.text.encode('ascii', errors='replace').decode().replace("?", "null"))
            print(eachdiv.text)
            divPost.append(eachdiv.text)
            # stores nepali encoded character divs as well
            #you can later check for the nepali palarism too if the users writes in nepali characters

print('total inner urls are ',len(innerUrls))
for url in innerUrls:
    print(url)


print('total news ',len(innerUrls))
divPost=sorted(list(set(divPost)))
for eachPost in divPost:
    if(len(eachPost)>=10):
        eachPost=eachPost.strip()
        eachPost=eachPost.strip('\r\n')
        print(sorted(list(set(sent_tokenize(eachPost)))))#remove whitespaces
        if(len(eachPost.split())>4):
            #only take posts having more than 4 words
            filteredPosts.append(eachPost)

filteredPosts.append('ahh ahh hola khai')
textToCheck=input("Enter the text for palarism ")
textToCheck = [textToCheck]
# filteredPosts=textToCheck+filteredPosts
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(filteredPosts)
# print (tfidf_matrix.shape)
# print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)) #[0:1] get the first row of the sparse matrix

container=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)#compare first with every body  (first,everybody)
print(len(container[0]))

similarityScore=[]
for each in container[0]:
    similarityScore.append(each)

# print(similarityScore.sort())
# print(similarityScore)
print('program ended success')

weighted_results=[]
for result in filteredPosts:
    ratio = difflib.SequenceMatcher(None, result, textToCheck[0]).ratio()
    weighted_results.append((result, ratio))

# print(weighted_results)
# print(sorted(weighted_results, key=lambda x: x[1]))
# print(sorted(weighted_results))
# print('last data is ',weighted_results[0])

#filter data whose score is>=50%

for each in weighted_results:
    if((each[1]*100)>40):
        print(each)

