# -*- coding: utf-8 -*-
"""
Created on Sat Nov 09 11:29:29 2013

@author: emBrio
"""
import pylast
import recommendations as rcmd

def init():
    
    API_KEY = "67660302ee23be8a69e4614b38df3d3f"
    API_SECRET = "25dca1ec537268160359a09e047c586e"
    
    username = "embr1o"
    password_hash = pylast.md5("DataMining")
    
    network = pylast.LastFMNetwork(api_key = API_KEY, api_secret = 
        API_SECRET, username = username, password_hash = password_hash)
    
    artist = network.get_artist("Radio Moscow")
    
    topfans = artist.get_top_fans(10)
    
    group = [a.item for a in topfans]
    
    userDict = rcmd.createLastfmUserDict(group)
    
    testband = "Pink Floyd"
    
    for testuser in group:
        print str(testuser) + " --> " + testband + " = " + str(userDict[testuser][testband])
        
        #user = ...topMatches(userDict, str(testuser), sim_euclid)
        #print user

        #recoms = ...getRecommendations(userDict, str(testuser), similarity='euklid')
        #print recoms

init()