'''
Created on 21.10.2013

Aufgabe 2.2.1

@author: am095
'''


import numpy as np
import pandas as pd
import sklearn.preprocessing as prepro
import scipy.spatial.distance as scispadist
import scipy.cluster.hierarchy as scicluhie
import matplotlib.pyplot as pyplot
import appendGeoCoordinates


def init():

    # for auto completion
    rawData = pd.DataFrame()
    
    # load data from file (create file if it doesn't exist) 
    try:
        rawData = pd.read_csv("res/EnergyMixGeo.csv", index_col=0)
    except IOError:
        appendGeoCoordinates.start()
        rawData = pd.read_csv("res/EnergyMixGeo.csv", index_col=0)
    
    rawDataSelectedMatrix = rawData.as_matrix(columns=('Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro'))
    
    # preprocess data: scale
    scaledData = np.array(prepro.scale((rawDataSelectedMatrix), with_mean=False))
    
    # correlation distance (difference between the countries)
    dist = scispadist.pdist(scaledData, 'correlation')
    
    # start clustering
    rawCluster = scicluhie.linkage(dist, method='average', metric='correlation')
    
    # print clustering image
    scicluhie.dendrogram(rawCluster, orientation="left", labels=rawData.as_matrix(['Country']), color_threshold=0.8)
    pyplot.show()
    
    # create 4 clusters
    clusters = scicluhie.fcluster(rawCluster, 4, "maxclust")
    
    # group data in clusters
    clusteredData = [[], [], [], []]
    idx = 0
    for cluster in clusters:
        clusteredData[cluster - 1].append(rawDataSelectedMatrix[:][idx])
        idx = idx + 1
 
    
    # draw a plot for each cluster
    idx = 0
    for clusteredDataEl in clusteredData:
        
        pyplot.subplot(410 + (idx+1))
        pyplot.title('Cluster ' + str(idx + 1))
        
        # draw each country in the cluster
        for singleClusterData in clusteredDataEl:
            pyplot.xticks(np.arange(0, 5, 1), ['Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro'])
            pyplot.plot(np.arange(0, 5, 1), singleClusterData)
        
        idx = idx + 1
        
    
    pyplot.show()
    
    # save cluster to file
    rawData['Cluster'] = clusters
    rawData.to_csv('res/EnergyMixGeo.csv')

