import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import urllib, json, csv
import time as tm

def geocode(addr):
    url = "http://maps.googleapis.com/maps/api/geocode/json?address=%s&sensor=false" %   (urllib.quote(addr.replace(' ', '+')))
    data = urllib.urlopen(url).read()
    info = json.loads(data).get("results")[0].get("geometry").get("location")  
    tm.sleep(0.2)
    #A little ugly I concede, but I am open to all advices :) '''
    return info

def start():
    df = pd.read_csv('res/EnergyMix.csv')
    
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
    
    ax = df2.plot(kind='bar', stacked=True, align='center')
    
    for container in ax.containers:
        plt.setp(container, width=1)
        
    x0, x1 = ax.get_xlim()
    ax.set_xlim(x0 -0.5, x1 + 0.25)
    
    lat = []
    lon = []
    
    for a in countries:
        r = geocode(a)
        print "%s %s %s" % (a, r['lat'], r['lng'])
        lat.append(r['lat'])
        lon.append(r['lng'])
        
    lat2 = np.array(lat)
    long2 = np.array(lon)
    
    df['Lat'] = lat2
    df['Long'] = long2
    
    df.to_csv('res/EnergyMixGeo.csv')
    
    plt.tight_layout()
    plt.show()


