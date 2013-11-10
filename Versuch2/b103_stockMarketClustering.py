"""
Created on 26.02.2012

@author: maucher
@author: am095

This version applies cleaned data provided by matplotlib.finance

In the cleaned data also the "open" value is adjusted w.r.t. splits and dividends

"""
from matplotlib.axis import Axis

print __doc__

import sys
sys.path.append("C:\Python27\lib\site-packages\sklearn\linear model")

import datetime
from matplotlib import finance
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import time as tm

from sklearn import cluster
from sklearn import metrics

# Choose a time period reasonnably calm (not too long ago so that we get
# high-tech firms, and before the 2008 crash)
d1 = datetime.datetime(2003, 01, 01)
d2 = datetime.datetime(2008, 01, 01)

symbol_dict = {
        'TOT'  : 'Total',
        'XOM'  : 'Exxon',
        'CVX'  : 'Chevron',
        'COP'  : 'ConocoPhillips',
        'VLO'  : 'Valero Energy',
        'MSFT' : 'Microsoft',
        'IBM'  : 'IBM',
        'TWX'  : 'Time Warner',
        'CMCSA': 'Comcast',
        'CVC'  : 'Cablevision',
        'YHOO' : 'Yahoo',
        'DELL' : 'Dell',
        'HPQ'  : 'Hewlett-Packard',
        'AMZN' : 'Amazon',
        'TM'   : 'Toyota',
        'CAJ'  : 'Canon',
        'MTU'  : 'Mitsubishi',
        'SNE'  : 'Sony',
        'F'    : 'Ford',
        'HMC'  : 'Honda',
        'NAV'  : 'Navistar',
        'NOC'  : 'Northrop Grumman',
        'BA'   : 'Boeing',
        'KO'   : 'Coca Cola',
        'MMM'  : '3M',
        
        'MCD'  : 'Mc Donalds',
        'PEP'  : 'Pepsi',
        'KFT'  : 'Kraft Foods',
        'K'    : 'Kellogg',
        'UN'   : 'Unilever',
        
        'MAR'  : 'Marriott',
        'PG'   : 'Procter Gamble',
        'CL'   : 'Colgate-Palmolive',
        
        #'NWS'  : 'News Corporation',
        
        'GE'   : 'General Electrics',
        'WFC'  : 'Wells Fargo',
        'JPM'  : 'JPMorgan Chase',
        'AIG'  : 'AIG',
        'AXP'  : 'American express',
        'BAC'  : 'Bank of America',
        'GS'   : 'Goldman Sachs',
        'AAPL' : 'Apple',
        'SAP'  : 'SAP',
        'CSCO' : 'Cisco',
        'TXN'  : 'Texas instruments',
        'XRX'  : 'Xerox',
        'LMT'  : 'Lookheed Martin',
        'WMT'  : 'Wal-Mart',
        'WAG'  : 'Walgreen',
        'HD'   : 'Home Depot',
        'GSK'  : 'GlaxoSmithKline',
        'PFE'  : 'Pfizer',
        'SNY'  : 'Sanofi-Aventis',
        'NVS'  : 'Novartis',
        'KMB'  : 'Kimberly-Clark',
        'R'    : 'Ryder',
        'GD'   : 'General Dynamics',
        'RTN'  : 'Raytheon',
        'CVS'  : 'CVS',
        'CAT'  : 'Caterpillar',
        'DD'   : 'DuPont de Nemours',
    }

symbols, names = np.array(symbol_dict.items()).T

print "----------------------------Symbols---------------------------------------"
print symbols

print "----------------------------Names---------------------------------------"
print names

quotes = []
for symbol in symbols:
    quotes.append(finance.quotes_historical_yahoo(symbol, d1, d2, asobject=True))
    tm.sleep(0.1)
    
'''
quotes = [finance.quotes_historical_yahoo(symbol, d1, d2, asobject=True)
                for symbol in symbols]
'''

print "----------------------------Quotes---------------------------------------"
print "Number of quotes:        ",len(quotes)


print "--------------------------open and close-----------------------------------"
#volumes = np.array([q.volume for q in quotes]).astype(np.float)
open    = np.array([q.open   for q in quotes]).astype(np.float)
close   = np.array([q.close  for q in quotes]).astype(np.float)

# difference between open and close
openCloseDiff = np.subtract(open, close)

# corellation matrix 
correlation = np.corrcoef(openCloseDiff)

affProp = cluster.AffinityPropagation()

# calculate clusters
affProp.fit(correlation)

# get cluster labels
clusters = affProp.labels_

# sort quotes and symbols by clusters
clusteredQuSy = []
for unused in range(1 + np.amax(np.array(clusters))):
    clusteredQuSy.append([]);
idx = 0
for clustersEntry in clusters:
    clusteredQuSy[clustersEntry].append({"quote":quotes[idx], "names":names[idx]})
    idx = idx + 1 


print "------------------------------clusters------------------------------------"

# print a plot for each cluster
clusterNo = 0
subplotNo = 1
for cluster in clusteredQuSy:
    axis = plt.subplot(410 + (subplotNo))
    plt.title('Cluster ' + str(clusterNo + 1))
    
    print "cluster no.: " + str(clusterNo)
    
    for quSy in cluster:
        
        print "quSy quote: " + str(quSy["names"])
        finance.candlestick2(axis, quSy["quote"]["open"], quSy["quote"]["close"], quSy["quote"]["high"], quSy["quote"]["low"], width=1, colorup=[0,1,0], colordown=[1,0,0], alpha=1)
    
    clusterNo = clusterNo + 1
    subplotNo = subplotNo + 1
    if subplotNo > 4:
        subplotNo = 1
        plt.show()
    print ""

plt.show()


