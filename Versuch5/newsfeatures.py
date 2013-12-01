'''
Created on 25.11.2013

'''
import numpy

import feedparser
from nltk.corpus import stopwords
import re
import nltk
import TransClass
import math
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
              'http://rss.nytimes.com/services/xml/rss/nyt/Travel.xml',
              'http://rss.nytimes.com/services/xml/rss/nyt/InternationalDiningandWine.xml',
              'http://rss.nytimes.com/services/xml/rss/nyt/Weddings.xml',
              'http://rss.nytimes.com/services/xml/rss/nyt/PersonalTech.xml',
              'http://rss.nytimes.com/services/xml/rss/nyt/Obituaries.xml',
              'http://www.nytimes.com/services/xml/rss/nyt/pop_top.xml'
              ]
    
    newsDict = {}
    for feed in feedList:
        newsFeed = feedparser.parse(feed)
        newsLen = newsFeed['entries']
        for i in range(len(newsLen)):
            newsTitle = newsFeed['entries'][i]['title']
            newsDescription = newsFeed['entries'][i]['summary']
            tmpNewsDict = {newsTitle:newsDescription}
            print newsTitle
            print newsDescription
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


def makematrix(allw, articlew):
    '''
    This function filters the words of allw in dependency of their length,
    and in the percentage of their occurrence.


    Parameters:
    ===========
    allw -> Dictionary of all words in the feeds and their occurrence

    getartWords -> Dictionary of all words in the feeds and the feeds itself

    Return:
    =======

    Object with two attributes:
    * The cleaned list of words
    * The Matrix of these words
    '''
    wordVector_tmp = __getListOfWordsLongerAs(allw, 4)
    wordVector = __getListOfWordsWithPercentOccur(wordVector_tmp, articlew, 60)

    matrix = __createMatrix(wordVector, articlew)
    __writeMatrixToFile('matrix.txt', wordVector, matrix)

    transportObject = TransClass.TransClass(wordVector, matrix)
    return transportObject

def __getListOfWordsLongerAs(allw, amount):
    '''
    Private Function (Do not use it explicit)
    =========================================
    Returns only the words, that occur more often than the amount


    Parameters:
    ===========
    allw -> Dictionary of all Words in the feeds and their occurrence

    amount -> Integer, defines the upper interval for their occurrence

    Example:
    An amount of 4 returns all words, they've an occurrence of the amount or higher.
    Like the entries 'airlines': 5 or 'holiday': 6
    But not 'experimental': 3 or 'Datamining': 1

    Returns:
    ========
    List with words
    '''
    wordVector = []
    for item, v in allw.iteritems():
        if v >= amount:
            wordVector.append(item)
    return wordVector

def __getListOfWordsWithPercentOccur(cleanedWordList, articlew, percent):
    '''
    Private Function (Do not use it explicit)
    =========================================
    Only these words they are under a special likelihood have to be returned.
    So this function puts the word of the cleanedWordList in a dependency to
    his percentage of occurrence. If the passed percentage is bigger than the
    percentage of occurrence of the single word in all feeds it will be returned.

    Parameters:
    ===========
    cleanedWordList -> List of words (should be the result of
    __getListOfWordsLongerAs)

    articlew -> The List of words in the feeds

    percent -> Percentage (float)

    Returns:
    ========
    List with words
    '''
    resultList = []
    onePercent = float(float(len(articlew)) / 100)
    resultDict = {}
    limit = float(percent) / 100

    for word in cleanedWordList:
        resultDict.__setitem__(word, onePercent)
    counter = 1

    for feedList in articlew:
        for word in cleanedWordList:
            if word in feedList:
                newPerc = resultDict.__getitem__(word)
                newPerc += onePercent
                resultDict.__setitem__(word, newPerc)
        counter += 1

    for item, v in resultDict.iteritems():
        if v <= limit:
            resultList.append(item)
    return resultList

def __createMatrix(wordVector, articlew):
    '''
    Private Function (Do not use it explicit)
    =========================================
    This Function creates the matrix. The Matrix is
    2- Dimensional.

    Example:
    For two words in the wordvector and 4 Feeds
    in the articlew this function will create
    a Matrix like this:

    [ 2 0 ]
    [ 0 1 ]
    [ 2 1 ]
    [ 1 0 ]

    The Rows are the amount of the feeds. So we get 4 rows.
    The Columns are the words in the wordVector.
    A Query for the Value [0][0] returns the 2. The Word
    in the first column occurs twice in the first feed.

    Please Note:
    This is a cleaned matrix. All Feed where no of the words
    in the wordVector occurs are deleted.

    [ 2 0 ]
    [ 0 1 ]         [ 2 0 ]
    [ 2 1 ]   ->    [ 0 1 ]
    [ 0 0 ]         [ 2 1 ]
    [ 1 0 ]         [ 1 0 ]
    [ 0 0 ]

    Parameters:
    ===========
    wordVector -> is the final vector of words.
    articlew -> The List of words in the feeds

    Returns:
    ========
    Matrix (numpy.matrix)
    '''
    matrix = numpy.zeros(shape=(len(articlew), len(wordVector)))
    zeroTestArray = numpy.zeros(shape=(1, len(wordVector)))[0]
    rowCounter = 0
    columnCounter = 0
    for feed in articlew:
        columnCounter = 0
        for word in wordVector:
            if word in feed:
                matrix[rowCounter, columnCounter] = feed[word]
            columnCounter += 1
        rowCounter += 1

    dataBuffer = []
    for vector in matrix:
        if numpy.array_equal(vector, zeroTestArray) is False:
            dataBuffer.append(vector)
    matrix = numpy.matrix(dataBuffer)

    return matrix

def __writeMatrixToFile(path, wordVector, matrix):
    '''
    Private Function (Do not use it explicit)
    =========================================
    This function saved the matrix in a file.

    Firs Row is the Words of the wordVector,
    second row is the matrix

    Example/ pattern:

    holiday airlines
    [[ 5.  0.]], [[ 5.  0.]], [[ 5.  4.]]

    Parameters:
    ===========

    path -> Path to the save- location
    wordVector -> final vector of words
    matrix -> matrix

    Returns:
    ========
    Void
    '''
    resultString = ''
    for word in wordVector:
        resultString += str(word + ' ')
    resultString += str('\n')

    counter = 0
    for vector in matrix:
        if counter is not len(matrix)-1:
            resultString += str(vector) + str(', ')
        else:
            resultString += str(vector)
        counter += 1
    writer = open(path, "w")
    writer.write(resultString)



def showfeatures(w,h,titles,wordvec):
    '''
    The features are defined by words which are
    characteristic for each feature.
    Each article/feed can contain words that are
    part of different features, so each article/feed
    can be assigned to several features.
    
    Print the six most significant words of each feature.
    Print the three most significant features of each
    article/feed.
    
    
    Parameters:
    w:        feature matrix
    h:        weight matrix
    titles:   list of feed/article titles
    wordvec:  list of all words
    
    '''
    
    # most significant words of each feature
    # - - - - - - - - - - - - - - - - - - - -
    
    print "\nmost significant words of each feature"
    print "- - - - - - - - - - - - - - - - - - - -\n"
    
    # how many words?
    n = 6;
    
    mostSignificantWordsAllFeatures = __getMostSignificantColsForEachRow(h, wordvec)
    
    if mostSignificantWordsAllFeatures != None:
        __printMostSignificantColsForEachRow(mostSignificantWordsAllFeatures, n)        
        
    print "\n\n"        
    
    
    
    # most significant features of each feed
    # - - - - - - - - - - - - - - - - - - - -
    
    print "most significant features of each feed"
    print "- - - - - - - - - - - - - - - - - - - -\n"
    
    # how many features?
    m = 3
    
    mostSignificantFeatureAllArticles = __getMostSignificantColsForEachRow(w)
    
    if mostSignificantFeatureAllArticles != None:
        __printMostSignificantColsForEachRow(mostSignificantFeatureAllArticles, m, titles)
       
       
       
def cost(A,B):
    '''
    calculates the euclidean distance betreen two matrices
    
    Parameters:
    A:        Matrix A
    B:        Matrix B
    '''

    arrayA = numpy.array(A)
    arrayB = numpy.array(B)

    flatA = arrayA.flatten()
    flatB = arrayB.flatten()
    
    costs = 0
    
    for i in range(len(flatA)):
        costs = costs + math.pow(flatA[i]-flatB[i],2)
    
    return costs
    
    
    
def nnmf(A, m, it):
    
    matrShape = A.shape
    matrRows = matrShape[0]
    matrColumns = matrShape[1] 
    
    flatH = numpy.array([0 for x in xrange(m*matrColumns)])
    flatW = numpy.array([0 for x in xrange(matrRows*m)])
    
    for i in range(m*matrColumns):
        flatH[i] = random.randint(1,9)
    
    for i in range(matrRows*m):
        flatW[i] = random.randint(1,9)
        
    H = flatH.reshape(m,matrColumns)
    W = flatW.reshape(matrRows,m)
    
    for i in range(it):
    
        B = numpy.dot(W,H)
        
        costs = cost(A,B)
        
        if costs < 5:
            break
    
        Ht = H.transpose()
        Wt = W.transpose()
        
        counter = numpy.dot(Wt, A)
        denominator = numpy.dot((numpy.dot(Wt, W)), H)

        H = numpy.array(H) * (numpy.array(counter) / numpy.array(denominator))
        
        counter = numpy.dot(A, Ht)
        denominator = numpy.dot((numpy.dot(W, H)), Ht)

        W = numpy.array(W) * (numpy.array(counter) / numpy.array(denominator))
    
    return H, W  
    
    
    
def __getMostSignificantColsForEachRow(matrix, colIndices = None):
    '''
    Sort each row of the passed matrix in descending order.
    To preserve the original column indices, each item in the
    result matrix will be expanded by the original colIndex.
    
    
    Paremeters:
    matrix:     The matrix to sort (nested numpy array or nested list)
    colIndices: [optional] To preserve the old col indices, each item
                           will be extended by the old index. In default
                           case, the columns will be numbers. Set this
                           parameter to use your own column indices.
                           Note: The dimension of this parameter must
                                 match the count of columns in matrix.
    
    
    Return:
    List(List), a matrix with the same columns than the passed matrix.
    The columns are sorted, which means, that the row order has changed
    compared to the passed matrix. The old row index is stored in each
    item. Example:
    
    returnValue['columnIndex']['sortedRowIndex'][0]
      == passedMatrix['columnIndex']['originalRowIndex']
      
    returnValue['columnIndex']['rowIndex'][1] 
      == passedMatrix['columnIndex'].index(returnValue['columnIndex']['rowIndex'][0])
     
    
    '''
    
    result = []
    
    if colIndices == None:
        colIndices = range(len(matrix[0]))

    # iter over matrix rows
    for row in matrix:
        
        rowWithOldColIndeices = []
        
        rowIdx = 0
        
        for item in row:
            rowWithOldColIndeices.append([item, colIndices[rowIdx]])
            rowIdx = rowIdx + 1
        
        sortedRow = sorted(rowWithOldColIndeices, key=lambda el: el[0], reverse = True)
        
        result.append(sortedRow)

    return result


def __printMostSignificantColsForEachRow(matrix, count, name=None):
    '''
    Print the most significant column names for each row.
    
    Parameters:
    matrix: Return value of __getMostSignificantColsForEachRow().
    count:  Define how many cols will be printed for each row. 
    name:   Used as description of the rows
    '''

    rowIdx = 0
    
    if name == None:
        name = range(1, len(matrix) + 1)

    # iter over rows
    for mostSignificantCols in matrix:
                
        print str(name[rowIdx]) + ": "
        
        outputIndex = 0
        
        for itemCountAndOldIndex in mostSignificantCols:
            
            # don't print all
            if outputIndex == count:
                break
            
            # print            
            print str(itemCountAndOldIndex[1]) + " (" + str(itemCountAndOldIndex[0]) + ")"
            
            outputIndex = outputIndex + 1
        
        print "\n" 
        
        rowIdx = rowIdx + 1 


    
