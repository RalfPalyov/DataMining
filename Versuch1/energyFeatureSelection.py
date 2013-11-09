import warnings

from pandas.util.testing import Series
from sklearn.feature_selection import SelectKBest, chi2
import energyStatistics
import pandas
import numpy

warnings.filterwarnings("ignore", category=DeprecationWarning)
notInterestingData_In = numpy.array(['Country', 'Total2009', 'Lat', 'CO2Emm', 'Long', 'Cluster'])
notInterestingData_Out = numpy.array(['Country', 'Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro', 'Total2009', 'Lat', 'Long', 'Cluster'])


def learning():
    dataFrame_In = energyStatistics.collectAndCleanData("res/EnergyMixGeo_mod.csv", notInterestingData_In)
    arrayIn = numpy.array(dataFrame_In)

    dataFrame_target = energyStatistics.collectAndCleanData("res/EnergyMixGeo_mod.csv", notInterestingData_Out)
    arrayOut = numpy.array(dataFrame_target)

    trans = SelectKBest(score_func=chi2)

    trans.fit(arrayIn, range(len(arrayOut)))

    dataFrame_result = pandas.DataFrame({ 'Co2-Emissions' : Series(trans.scores_, index=['Oil', 'Gas', 'Coal', 'Nuclear', 'Hydro']) })

    print dataFrame_result.sort('Co2-Emissions')
