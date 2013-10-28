# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:16:42 2013

@author: emBrio
"""

import pandas as pd
import matplotlib.pyplot as plt
import sklearn.manifold as skl
import math

def start():
    
    df = pd.read_csv('EnergyMix.csv')
    
    countries = df['Country']
    oil = df['Oil']
    gas = df['Gas']
    coal = df['Coal']
    nuclear = df['Nuclear']
    hydro = df['Hydro']
    
    df2 = pd.DataFrame(oil)
    
    df2['Gas'] = gas
    df2['Coal'] = coal
    df2['Nuclear'] = nuclear
    df2['Hydro'] = hydro

    df2.index = countries
    
    imap = skl.Isomap()

    X = imap.fit_transform(df2)
 
    plt.plot(X[:,0],X[:,1],'.')
    
    for z in range(len(df2)):
        plt.text(X[z,0], X[z,1], df2.index[z])
           
    plt.show()
    
start()

