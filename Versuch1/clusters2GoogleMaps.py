# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 16:58:13 2013

@author: emBrio
"""

import pymaps as pm
import pandas as pd
   
def start():
    
    df = pd.read_csv('EnergyMixGeo.csv')
    
    g = pm.PyMap()
    
    icon1 = pm.Icon('icon1')
    icon1.image = "http://labs.google.com/ridefinder/images/mm_20_blue.png"
    icon1.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png"
    g.addicon(icon1)
       
    icon2 = pm.Icon('icon2')
    icon2.image = "http://labs.google.com/ridefinder/images/mm_20_red.png"
    icon2.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png"
    g.addicon(icon2)    
    
    icon3 = pm.Icon('icon3')
    icon3.image = "http://labs.google.com/ridefinder/images/mm_20_green.png"
    icon3.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png"
    g.addicon(icon3)    
    
    icon4 = pm.Icon('icon4')
    icon4.image = "http://labs.google.com/ridefinder/images/mm_20_yellow.png"
    icon4.shadow = "http://labs.google.com/ridefinder/images/mm_20_shadow.png"
    g.addicon(icon4)
    
    #g.key = "ABQIAAAAQQRAsOk3uqvy3Hwwo4CclBTrVPfEE8Ms0qPwyRfPn-DOTlpaLBTvTHRCdf2V6KbzW7PZFYLT8wFD0A"
    
    for c in df.index:
        
        countryX = df['lat'][c] #alternative: df.loc[c,'Lat']
        countryY = df['long'][c]
        countryName = df['Country'][c]
        countryOil = df.loc[c,'Oil']
        countryGas = df.loc[c,'Gas']
        countryCoal = df.loc[c,'Coal']
        countryNuclear = df.loc[c,'Nuclear']
        countryHydro = df.loc[c,'Hydro']
        countryCluster = df['cluster'][c]
        countryTotal = countryOil+countryGas+countryCoal+countryNuclear+countryHydro
        
        countryText = countryName + ": Oil=" + str(countryOil) + " Gas= " +str(countryGas) + " Coal= " + str(countryCoal) + " Nuclear= " + str(countryNuclear) + " Hydro= " + str(countryHydro) + " Total= " + str(countryTotal)
        
        s = [countryX,countryY,countryName + str(countryText), 'icon' + str(countryCluster)]
        g.maps[0].setpoint(s)
        
    print g.showhtml()
    open('test.htm','wb').write(g.showhtml())

start()