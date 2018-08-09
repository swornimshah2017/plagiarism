
import requests,json
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin
import nltk
import os
from nltk.tokenize import sent_tokenize,word_tokenize
import difflib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.stem.porter import PorterStemmer
from flask import Flask# for web server request
from flask import Response
from flask import request

app = Flask(__name__)



@app.route("/",methods=['GET', 'POST'])
def hello():

    # if request.method=='POST':
    os.system("chcp 65001")
    class Palarism:
        def __init__(self, urlName,divPost):
            self.urlName=urlName #this holds the url of that web page
            self.divPost=divPost# this holds the entire div data as an array for that particular web page

        def setScore(self,score):
            self.score=score

        def setFilteredPosts(self,filteredPosts):
            self.filteredPosts=filteredPosts

        def setSimilarityScore(self,similarityScore):
            self.similarityScore=similarityScore

        def setOriginalSentence(self,originalSentence):
            self.originalSentence=originalSentence
    
    palarsimList=[]#this holds the palarism instances as a list
    innerUrls=[]
    urlContainer=[
        "http://www.ekantipur.com/eng",
        "https://thehimalayantimes.com/",
    # "http://www.fb.com/",
        "http://kathmandupost.ekantipur.com/",
        "http://annapurnapost.com/",
    "http://www.nepalipatra.com/"
    ]

    #switch to urlContainer if there is internet connection
    cacheUrlContainer=[
        "http://localhost/local-cache/ekantipur.html",
        "http://localhost/local-cache/himlayan.html",
        "http://localhost/local-cache/kathmandupost.html"

        ]
    #switch the urlcontainer


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
                # print(url.get('href'))
                # print('My urls ',url.text.encode('ascii', errors='replace').decode().replace("?", ""))
                urljoin(urlContainer[index],url.get('href'))
                innerUrls.append(urljoin(urlContainer[index],url.get('href')))
                # print('all the div ')


            
            divPost=[]#use and make it empty    
            for eachdiv in soup.find_all('div'):
                # print(eachdiv.text.encode('ascii', errors='replace').decode().replace("?", "null"))
                # print(eachdiv.text)
                divPost.append(eachdiv.text)
                # stores nepali encoded character divs as well
                #you can later check for the nepali palarism too if the users writes in nepali characters
            
            eachPalarismObject=Palarism(eachurl,divPost)
            palarsimList.append(eachPalarismObject)


    print('total inner urls are ',len(innerUrls))
    for url in innerUrls:
        print(url)


    print('total news ',len(innerUrls))
    divPost=sorted(list(set(divPost)))


    #for loop til palarsimList

    for index,eachPalarismObject in enumerate(palarsimList):
        divPost=eachPalarismObject.divPost
        filteredPosts=[]#use and make it empty
        for eachPost in divPost:
            if(len(eachPost)>=10):
                eachPost=eachPost.strip()
                eachPost=eachPost.strip('\r\n')
                # print(sorted(list(set(sent_tokenize(eachPost)))))
                # print((sent_tokenize(eachPost)))
                # print(sent_tokenize(eachPost))
                print("---------------------------------------------------------------------------------------------------------------------------------")
                if(len(sent_tokenize(eachPost))>0):
                    eachPost=sent_tokenize(eachPost)[0]
                    if(len(eachPost.split())>4):
                        #only take posts having more than 4 words
                        filteredPosts.append(eachPost)
        #now set filteredPosts
        palarsimList[index].filteredPosts=filteredPosts

    # filteredPosts.append('ahh ahh hola khai')
    textToCheck=input("Enter the text for palarism ")
    textToCheck = [textToCheck]

    #add the palarism sentence to each palarismObject in palarsimList
    for index,eachPalarsimObject in enumerate(palarsimList):
        filteredPosts=textToCheck+eachPalarsimObject.filteredPosts
        palarsimList[index].setFilteredPosts(filteredPosts)

    for index,eachPalarsimObject in enumerate(palarsimList): 
        filteredPosts=eachPalarsimObject.filteredPosts
        tfidf_vectorizer = TfidfVectorizer()
        tfidf_matrix = tfidf_vectorizer.fit_transform(filteredPosts)
        print (tfidf_matrix.shape)
        print(cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)) #[0:1] get the first row of the sparse matrix

        container=cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)#compare first with every body  (first,everybody)
        print(len(container[0]))

        similarityScore=[]
        for each in container[0]:
            similarityScore.append(each)

        # remove the first element from both the list(similartity score and filteredPosts)
        del similarityScore[0]
        del filteredPosts[0]
        palarsimList[index].setFilteredPosts(filteredPosts)
        palarsimList[index].setSimilarityScore(similarityScore)

        # find palarism by using t cosine algorithm 
        print("here is the palarsim sentence")
        filteredPosts=palarsimList[index].filteredPosts
        similarityScore=palarsimList[index].similarityScore

        print(filteredPosts[similarityScore.index(max(similarityScore))])
        palarsimList[index].originalSentence=filteredPosts[similarityScore.index(max(similarityScore))]
        # print(similarityScore.index(max(similarityScore)))
        # print('maximum percentage score is ',max(similarityScore))

        #set the new filteredPosts and similarityScore for that instance of palarismObject
        palarsimList[index].setScore(max(similarityScore))
        print('-------------------------------------------------------------------------------------------------------------------------------------------')
        print('url name ',palarsimList[index].urlName)
        print('score ',palarsimList[index].score)
        print('-------------------------------------------------------------------------------------------------------------------------------------------')


    # print(similarityScore.sort())
    # print(similarityScore)
    print('program ended success')


    #find palarism using diff algorithm which might perform not so well when large sentence are present
    #rather use algorithm which basically finds the substring (quite straight forward)
    # weighted_results=[]
    # for result in filteredPosts:
    #     ratio = difflib.SequenceMatcher(None, result, textToCheck[0]).ratio()
    #     weighted_results.append((result, ratio))

    # print(weighted_results)
    # print(sorted(weighted_results, key=lambda x: x[1]))
    # print(sorted(weighted_results))
    # print('last data is ',weighted_results[0])

    #filter data whose score is>=50%

    # for each in weighted_results:
    #     if((each[1]*100)>40):
    #         print(each)

    # print(weighted_results[similarityScore.index(max(similarityScore))])



    # for eachPalarismObject in palarsimList:
    #     score=eachPalarismObject.score
    #     urlName=eachPalarismObject.urlName
    #     # if score <1:
    #     #      print('url of the source is ',score)
    #     #      print('score of the url ',urlName)
    #     print('url of the source is ',score)
    #     print('score of the url ',urlName)

    #More and more students in Chitwan district have been found attracted


    #send the response to the web request as a JSON reposne


    #reset the lists divPosts and filteredPost to empty because it is no more needed for JSON RESPONSE
    for index,eachPalarismObject in enumerate(palarsimList):
        palarsimList[index].filteredPosts=[]
        palarsimList[index].divPost=[]
        palarsimList[index].similarityScore=[]

    jsonString=json.dumps([ob.__dict__ for ob in palarsimList])
    resp =Response(jsonString)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    palarsimList=[]#reset the data
    innerUrls=[]
    # print('server response data',jsonString)
    return resp




#main code to run the flask server 
if __name__ == "__main__":
    app.run()