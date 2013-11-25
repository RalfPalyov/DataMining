'''
Created on 25.11.2013

'''

import feedparser
from nltk.corpus import stopwords
import re
import nltk

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
              'http://www.nytimes.com/services/xml/rss/nyt/Economy.xml'
              ]
    
    newsDict = {}
    
    for feed in feedList:
        
        newsFeed = feedparser.parse(feed)

        newsTitle = newsFeed['entries'][1]['title']
        newsDescription = newsFeed['entries'][1]['summary']
    
        tmpNewsDict = {newsTitle:newsDescription}
        
        newsDict.update(tmpNewsDict)
        
    return newsDict

def stripHTML(h):
    p=''
    s=0
    for c in h:
        if c=='<': s=1
        elif c=='>':
            s=0
            p+=' '
        elif s==0:
            p+=c
    return p

def separatewords(text):
    try:
        sw = stopwords.words('english')
    except:
        print "Seems like you haven't installed the stopword collection yet."
        nltk.download()
        sw = stopwords.words('english')
    splitter = re.compile('\\W*')
    return [s.lower() for s in splitter.split(text) if len(s) > 4 and s not in sw]

def countwords(words):
    result = {}
    for word in words:
        try:
            result[word] = result[word] + 1
        except:
            result[word] = 1
    return result

def getarticlewords():
    '''
    Collect feeds and extract all words, count them and get feed titles.
    
    Returns:
    Dictionary, collection of three return values:
    The dict keys are: 
    'allwords', 'articlewords' and 'articletitles'
    =================================
    Detailed description of the return values:
    'allwords':
    Dictionary, contains each word of all feeds. 
    The words are the dict keys and the values are
    the count, how many times the word absolutely
    exists in all feeds.
    ------------------------
    'articlewords':
    List, contains an entry for each feed. 
    For each feed there is a dictionary stored.
    This Dictionary contains all words that are
    contained in this feed. The dict keys are 
    the word and the values are the count, 
    how many times the word is contained in the feed.
    ------------------------
    'articletitles':
    List, contains an entry for each feed. 
    For each feed the feed title is stored.
    '''
    
    result = {'allwords': {}, 'articlewords': [], 'articletitles': []}
    
    feeds = getNewsDict()
    
    for feedTitle, feedContent in feeds.iteritems():
        
        # process the feed text: strip html and tokenize it to words
        wordsInFeed = separatewords(stripHTML(feedContent))
        
        # count the words in the feed
        wordCounts = countwords(wordsInFeed)
        
        # actualize the total word counts
        result['allwords'] = dict(result['allwords'].items() + wordCounts.items())
        
        # set the feed word counts
        result['articlewords'].append(wordCounts)
        
        # set the title
        result['articletitles'].append(feedTitle)        
    
    return result

