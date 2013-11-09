__author__ = 'janhorak'


import pandas
import numpy
import matplotlib.pyplot as plt

def printSharePrice():
    dataFrame = pandas.read_csv('res/effectiveRates.csv')
    interestedData = numpy.array(['DELL', 'YHOO', 'CSCO', 'JPM', 'IBM'])
    realNames = numpy.array(['Dell', 'Yahoo!', 'Cisco', 'JP Morgan', 'IBM'])

    live = True
    position = 1
    dataPointer = 0
    plt.figure(1, figsize=(15, 10))
    plt.subplot2grid((3, 3), (0, 0), colspan=3)
    while live:
        firma = interestedData[dataPointer]
        plt.plot(dataFrame[firma], label=realNames[dataPointer])
        dataPointer += 1
        position += 1
        plt.legend()
        if dataPointer == interestedData.size:
            plt.ylabel("Share Price (in USD ($))")
            plt.xlabel("Time")
            live = False

    live = True
    dataPointer = 0
    positionPointer_row = 1
    positionPointer_col = 0


    while live:
        firma = interestedData[dataPointer]
        plt.subplot2grid((3, 3), (positionPointer_row, positionPointer_col))
        plt.plot(dataFrame[firma], label=realNames[dataPointer])
        plt.legend()
        plt.ylabel("Share Price (in USD ($))")
        plt.xlabel("Time")
        dataPointer += 1
        positionPointer_col += 1
        if positionPointer_col == 3:
            positionPointer_row += 1
            positionPointer_col = 0

        if dataPointer == interestedData.size:
            live = False

    plt.show()


printSharePrice()