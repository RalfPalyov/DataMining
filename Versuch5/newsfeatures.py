import feedparser
import math
import numpy as np
import random

def getNewsDict():
    
    feedList=['http://feeds.reuters.com/reuters/topNews',
              'http://feeds.reuters.com/reuters/worldNews',
              'http://feeds2.feedburner.com/time/world',
              'http://feeds2.feedburner.com/time/business',
              'http://feeds2.feedburner.com/time/politics',
              'http://rss.cnn.com/rss/edition.rss',
              'http://rss.cnn.com/rss/edition_world.rss',
              'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/business/rss.xml',
              'http://newsrss.bbc.co.uk/rss/newsonline_world_edition/europe/rss.xml',
              'http://www.nytimes.com/services/xml/rss/nyt/World.xml',
              'http://www.nytimes.com/services/xml/rss/nyt/Economy.xml',
              'http://rss.nytimes.com/services/xml/rss/nyt/Sports.xml',
              'http://rss.nytimes.com/services/xml/rss/nyt/Science.xml',
              'http://rss.nytimes.com/services/xml/rss/nyt/Business.xml',
              'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml',
              'http://rss.nytimes.com/services/xml/rss/nyt/Travel.xml'
              ]
    
    newsDict = {}
    
    for feed in feedList:
        
        newsFeed = feedparser.parse(feed)
        
        for i in range(10):
            
            newsTitle = newsFeed['entries'][i]['title']
            newsDescription = newsFeed['entries'][i]['summary']
        
            print newsTitle
            print newsDescription
    
            tmpNewsDict = {newsTitle:newsDescription}
        
            newsDict.update(tmpNewsDict)
            
    return newsDict



def cost(A,B):

    if A.shape != B.shape:
        print "Error"
        
    matrColumns = len(A)
    matrRows = A.size / spalten

    costs = 0
    
    for i in range(matrColumns):
        for j in range(matrRows):
            costs = costs + math.pow(A[i][j] - B[i][j],2)
        
    return costs



def nnmf(A,m,it):
    
    matrColumns = len(A)
    matrRows = A.size / matrColumns
    

    
    H = [[0 for x in xrange(m)] for x in xrange(matrColumns)] 
    W = [[0 for x in xrange(matrRows)] for x in xrange(m)] 
    
    for i in range(m):
        for j in range(matrColumns):
            randomNr = random.randint(0, 10)
            H[i][j] = randomNr
    
    for i in range(matrRows):
        for j in range(m):
            randomNr = random.randint(0, 10)
            W[i][j] = randomNr
            
    print H
    print W
            
    if costs < 5:
        #Exit, return W and H
        print "test"
        
superdict = getNewsDict()      
    
    