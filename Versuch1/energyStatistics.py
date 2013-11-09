import pandas
import matplotlib.pyplot as plt
import numpy

notInterestingData = numpy.array(['Country', 'Total2009', 'CO2Emm', 'Lat', 'Long', 'Cluster'])

def init_CSV(path):
    return pandas.read_csv(path)

def collectAndCleanData(pathToCSV, notInterestingData):
    cleanedDataFrame = init_CSV(pathToCSV)
    for x in notInterestingData:
        del cleanedDataFrame[x]
    return cleanedDataFrame

def createBoxPlot():
    live = True
    kindOfEnergy = 'unknown'
    kindOfEnergyPointer = 1
    plotPositionPointer = 1
    cleanedData = collectAndCleanData("res/EnergyMixGeo.csv", notInterestingData)
    kindOfEnergy = cleanedData.columns

    plt.figure(1, figsize=(15, 10))
    while live:
        kindOfEnergyTmp = kindOfEnergy[kindOfEnergyPointer]
        plt.subplot(2, 3, plotPositionPointer)
        plt.boxplot(cleanedData[kindOfEnergyTmp], 0)
        plt.xlabel(kindOfEnergyTmp)
        kindOfEnergyPointer += 1
        plotPositionPointer += 1
        if kindOfEnergyPointer == len(cleanedData.columns):
            live = False
    plt.show()

def createSingleBoxPlots():
    live = True
    kindOfEnergy = 'unknown'
    kindOfEnergyPointer = 1
    plotPositionPointer = 1
    cleanedData = collectAndCleanData("res/EnergyMixGeo.csv", notInterestingData)
    kindOfEnergy = cleanedData.columns

    while live:
        kindOfEnergyTmp = kindOfEnergy[kindOfEnergyPointer]
        plt.boxplot(cleanedData[kindOfEnergyTmp], 0)
        plt.xlabel(kindOfEnergyTmp)
        kindOfEnergyPointer += 1
        plotPositionPointer += 1
        plt.show()
        if kindOfEnergyPointer == len(cleanedData.columns):
            live = False


def printStatistic():
    dataFrame = init_CSV("res/EnergyMixGeo.csv")
    print dataFrame.describe()