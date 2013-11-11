'''
Created on 11.11.2013

@author: am095
'''

from recommendations import sim_euclid, sim_pearson, critics

def topMatches(prefs, person, similarity):
    '''
    Calculates similarity between each critic in prefs and a single critic.
    
    
    Parameters
    prefs: critics list
    person: index in prefs; Defines the critic that will be compared with all others in prefs.
    similarity: function pointer; Function to calculate similarity (see import recommendations)
    
    
    Returns
    List with equal indices than parameter prefs. Stores distances for all prefs, prefs at index person is set to 0. 
    '''
    
    result = {}       
    
    for prefIdx, pref in prefs.iteritems():
        if prefIdx != person:
            result[prefIdx] = similarity(prefs, prefIdx, person)
        else:
            result[prefIdx] = 0
        
    return result

def init():
    
    # use euklidian distance
    resultEuclid = {}
    for criticIdx, critic in critics.iteritems():
        resultEuclid[criticIdx] = topMatches(critics, criticIdx, sim_euclid)
        
    # use pearson correlation
    resultPearson = {}
    for criticIdx, critic in critics.iteritems():
        resultPearson[criticIdx] = topMatches(critics, criticIdx, sim_pearson)
        
    # print results
    for criticIdx, critic in critics.iteritems():
        print "Input data (critic at index '" + criticIdx + "'): " + str(critic)
        print "\nResult (euclidian):"
        for resultIdx, result in resultEuclid[criticIdx].iteritems():
            print "Index '" + resultIdx + "': " + str(resultEuclid[criticIdx][resultIdx])  
        print "\nResult (pearson):" 
        for resultIdx, result in resultPearson[criticIdx].iteritems():
            print "Index '" + resultIdx + "': " + str(resultPearson[criticIdx][resultIdx])  
        print "_______________________________________________________________________________\n"
    
init()
    