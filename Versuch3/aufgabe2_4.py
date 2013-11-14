'''
Created on 11.11.2013

@author: am095
'''

from recommendations import critics, sim_pearson, sim_euclid
from aufgabe2_2 import topMatches


def transformCriticsForICF(c):
    '''
    There are already functions to calculate distances for UCF.
    To reuse this functions for ICF, the critics dictionary must be transformed.
    
    
    Parameters:
    c: Dictionary with same format as 'critics' in recommendations.py
    
    
    Return
    transformed dictionary
    '''    
    
    result = {}
    
    for critic, criticism in c.iteritems():
        for filmName, value in criticism.iteritems():
            try:
                result[filmName][critic] = c[critic][filmName]
            except:
                result[filmName] = {critic: c[critic][filmName]}
    
    return result

def calculateSimilarItems(c, similarity, additional=None):
    '''
    Calculate distances for passed critic dictionary.
    
    
    Parameter:
    c: Dictionary returned by transformCriticsForICF()
    similarity: function pointer to a distance function (there are some in recommendations.py)
    additional: optional parameter, if set, the value will be passed through to the similarity function 
    
    
    Return:
    dictionary; keys like parameter c, values are results of function topMatches()
    '''
    
    result = {}
    for filmName, criticism in c.iteritems():        
        result[filmName] = topMatches(c, filmName, similarity, additional)
    return result
    
def getRecommendedItems(c, person, similarity, additional=None):
    '''
    Calculate recommendations for a specified person.
    
    Parameters:
    c: Dictionary specified in recommendations.py (critics)
    person: string name of the person, must be defined in c
    similarity: function pointer to a distance function (there are some in recommendations.py)
    additional: optional parameter, if set, the value will be passed through to the similarity function 
    
    Return:
    Dictionary; keys are film names; values are the correlated similarity to films, the person liked in the past.
    '''
    
    result = {}
    transCritics = transformCriticsForICF(c)
    similarItems = calculateSimilarItems(transCritics, similarity, additional)
    
    allRelevantFilmNames = set([filmName for filmName in similarItems[c[person].keys()[0]].iterkeys()])
    
    filmNamesNotSeen = allRelevantFilmNames - set(c[person].keys())
    
    # loop over films, the person has not seen yet
    for filmNameNotSeen in filmNamesNotSeen:
        
        weightedSumFilmSimilarity = 0
        sumFilmSimilarity = 0
        
        # compare this film to all films, person has already seen
        for filmNameSeen in c[person].keys():
            
            filmSimilarity = similarItems[filmNameNotSeen][filmNameSeen]
            
            # don't allow to continue with negative values from pearson correlation
            if filmSimilarity < 0:
                continue
            
            sumFilmSimilarity = sumFilmSimilarity + filmSimilarity
            weightedSumFilmSimilarity = weightedSumFilmSimilarity + filmSimilarity * c[person][filmNameSeen]
            
        
        # divide weighted film similarity by absolute similarity 
        try:
            result[filmNameNotSeen] = weightedSumFilmSimilarity / sumFilmSimilarity
        except ZeroDivisionError:
            result[filmNameNotSeen] = 0;
    
    return result


def init():
    
    print getRecommendedItems(critics, 'Toby', sim_euclid, True)
    
    
init()