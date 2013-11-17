# -*- coding: utf-8 -*-
"""
Created on Sat Nov 09 11:29:29 2013

@author: emBrio
"""
import pylast
import recommendations
import getRecommendations
import aufgabe2_2
#import recommendations

def init():
    
    API_KEY = "67660302ee23be8a69e4614b38df3d3f"
    API_SECRET = "25dca1ec537268160359a09e047c586e"
    
    username = "embr1o"
    password_hash = pylast.md5("DataMining")
    
    network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
        API_SECRET, username = username, password_hash = password_hash)
    
    artistName = raw_input('Bitte geben Sie einen Kuenstlernamen ein: ')
    
    print "Bitte warten..."
    artist = network.get_artist(str(artistName))

    topfans = artist.get_top_fans(10)
    
    group = [a.item for a in topfans]
    
    userDict = recommendations.createLastfmUserDict(group)
     
    #testband="AFI"
    
    for testuser in group:
        
        #print str(testuser) + " --> " + testband + " = " + str(userDict[testuser][testband])
        
        similarUsers = aufgabe2_2.topMatches(userDict, str(testuser), recommendations.sim_euclid)
        
        #sort dictionary and save user with the highest distance
        for key, value in sorted(similarUsers.iteritems(), key=lambda (k,v): (v,k)):
            users = key
            distances = value
            
        print
        print "Aehnlichster Benutzer fuer " + str(testuser) + " = " + str(users) + " (" + str(round(distances, 3)) + ")" 
        
        #choose either euclidean or pearson distance
        recoms = getRecommendations.getRecommendations(userDict, str(testuser), similarity='euclid')

        print "Empfehlungen fuer Benutzer " + str(testuser) + ":"
       
        j = 0
        
        for i in range(0, 10):
            #skip artistName
            if  str(recoms[i][1]) == artistName:
                j += 1
                
            print recoms[j][1] + " (" + str(round(recoms[j][0],3)) + ")"
            
            j += 1
    
    print        
    exitApp = input("Druecken Sie eine beliebige Taste . . . ")
    
init()