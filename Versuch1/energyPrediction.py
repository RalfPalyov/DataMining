'''
Created on 26.10.2013

Aufgabe 2.3.2

@author: am095
'''


import numpy as np
import pandas as pd
import energyClustering
import sklearn.svm as sklsvm
import sklearn.cross_validation as sklcv
import sklearn.metrics as sklm
import matplotlib.pyplot as pyplot
import math


def bestCandEpsilon(rawData, rawDataSelectedMatrix):
    
    return r_bestC(rawData, rawDataSelectedMatrix, oldCalcResult = {'medScores' : 100}, direction='backwards', stepSize = 0.005, minStepSize = 0.00005, C=0.05, epsilon=0.125)
    
def r_bestC(rawData, rawDataSelectedMatrix, oldCalcResult, direction, stepSize, minStepSize, C, epsilon):
    
    print 'C: ' + str(C) + "\n" 
    
    if C <= 0:
        C = 0.00001
    
    calcResult = r_bestEpsilon(rawData, rawDataSelectedMatrix, oldCalcResult, direction = 'backwards', stepSize = 0.005, minStepSize = minStepSize, C = C, epsilon = epsilon)
    
    print "---------\n\n"
    
    # new score is worser than old one
    if calcResult['medScores'] >= oldCalcResult['medScores']:
        
        # change direction
        if direction == 'forward':
            direction = 'backwards'
        else:
            direction = 'forward'
            
        # reduce step size
        stepSize = stepSize / 2
    
    if direction == 'forward' :
        newC = C + stepSize
    else:
        newC = C - stepSize  
    
    # break recursion
    if stepSize < minStepSize:
        return oldCalcResult
    
    # recursion
    return r_bestC(rawData, rawDataSelectedMatrix, calcResult, direction, stepSize, minStepSize, newC, calcResult['epsilon'])
    
def r_bestEpsilon(rawData, rawDataSelectedMatrix, oldCalcResult, direction, stepSize, minStepSize, C, epsilon): 
    
    print 'epsilon: ' + str(epsilon)
    print 'stepSize = ' + str(stepSize)
    print 'minStepSize = ' + str(minStepSize)
    print 'direction = ' + direction
    
    if epsilon < 0:
        epsilon = 0 
    
    calcResult = bestCandEpsilonCalc(rawData, rawDataSelectedMatrix, oldCalcResult, C, epsilon)
    
    # new score is worser than old one
    if calcResult['medScores'] >= oldCalcResult['medScores']:
        
        # change direction
        if direction == 'forward':
            direction = 'backwards'
        else:
            direction = 'forward'
            
        # reduce step size
        stepSize = stepSize / 2
    
    if direction == 'forward' :
        newEpsilon = epsilon + stepSize
    else:
        newEpsilon = epsilon - stepSize  
    
    # break recursion
    if stepSize < minStepSize:
        print 'final epsilon = ' + str(newEpsilon)
        print 'returned score = ' + str(oldCalcResult['medScores'])
        return oldCalcResult
    
    # recursion
    return r_bestEpsilon(rawData, rawDataSelectedMatrix, calcResult, direction, stepSize, minStepSize, C, newEpsilon)
    
def bestCandEpsilonCalc(rawData, rawDataSelectedMatrix, oldCalcResult, C, epsilon):
    
    # svr object
    svr = sklsvm.SVR(kernel='linear', C=C, epsilon=epsilon)
    
    # validate: cross validation. create an iterator 
    kf = sklcv.KFold(n=len(rawData[:]['CO2Emm']), n_folds=10)
    
    # calculate cross validation score 
    crossScores = sklcv.cross_val_score(estimator=svr, X=rawDataSelectedMatrix, y=rawData[:]['CO2Emm'], cv=kf, scoring='mean_squared_error')
    
    medScores = 0
    for crossScore in crossScores:
        # median
        medScores = medScores + abs(crossScore)
    medScores = medScores / 10
    
    return {'svr': svr, 'medScores': medScores, 'crossScores': crossScores, 'C': C, 'epsilon': epsilon}
    


def init():

    # for auto completion
    rawData = pd.DataFrame()
    
    # load data from file (create file if it doesn't exist) 
    try:
        rawData = pd.read_csv("res/EnergyMixGeo.csv", index_col=0)
    except IOError:
        energyClustering.init()
        rawData = pd.read_csv("res/EnergyMixGeo.csv", index_col=0)
    
    rawDataSelectedMatrix = rawData.as_matrix(columns=('Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro'))
    
    # create optimal svr object
    bestSvr = bestCandEpsilon(rawData, rawDataSelectedMatrix)
    
    print 'SVR: best value for epsilon = ' + str(bestSvr['epsilon'])
    print 'SVR: best value for C       = ' + str(bestSvr['C']) + "\n\n"
    
    svr = bestSvr['svr']
    
    index = 1
    print 'cross validation scores:'
    for iteration in bestSvr['crossScores']:
        print 'Iteration ' + str(index) + ': ' + str(iteration)
        index = index + 1
    print "\n\n"
    
    # train with entire data
    svr.fit(rawDataSelectedMatrix, rawData[:]['CO2Emm'])
    
    # prediction for train data
    predictTrainData = svr.predict(rawDataSelectedMatrix)
    
    # absolute and median divergence between prediction result and target data
    absDiver = []
    medDiver = 0
    for index in range(len(rawData[:]['CO2Emm'])):
        
        diff = rawData[:]['CO2Emm'][index] - predictTrainData[index]
        
        # absolute
        absDiver.append(diff)
        
        # median
        medDiver = medDiver + abs(diff)
    medDiver = medDiver / len(rawData[:]['CO2Emm'])
    
    index = 1
    print 'cross validation divergence: absolute'
    for iteration in absDiver:
        print str(index) + ': ' + str(iteration)
        index = index + 1
    print ''
    print 'cross validation divergence: median'
    print medDiver
    print "\n\n"
    
    print "coefficients in svr object:\n" + str(svr.coef_)
    
    
    
    # show prediction result and target data in one diagram
    pyplot.title('cross validation')
    pyplot.barh(np.arange(0, len(rawData[:]['CO2Emm']), 1), rawData[:]['CO2Emm'], 0.3, label='real Data', color='r', log=True)
    pyplot.barh(np.arange(0.3, len(rawData[:]['CO2Emm']) + 0.3, 1), predictTrainData, 0.3, label='prediction', color='b', log=True)
    pyplot.yticks(np.arange(0, len(rawData[:]['CO2Emm']), 1), rawData[:]['Country'])
    pyplot.legend()
    pyplot.tight_layout()
    pyplot.show()

init()
