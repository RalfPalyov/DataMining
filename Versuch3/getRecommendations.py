
import recommendations
import LastFMDic

lastFMDict = LastFMDic.lastFMdict
filmDict = recommendations.critics


dic_sum = {}
dic_ksum = {}

def getCleanedNames(prefs, searchedPerson):
    resultArray = []
    counter = 0
    for s in prefs.keys():
        if s != searchedPerson:
            resultArray.append(s)
            counter += 1
    return resultArray

def convertDict2List(dict):
    list = []
    for key in dict.keys():
        list.append([dict.get(key), key])
    return sorted(list, reverse=True)


def createSum(dict, person, distance):
    for item, v in dict[person].items():
        if v*distance > 0:
            if not dic_sum.__contains__(item):
                dic_sum.__setitem__(item, v*distance)
            else:
                dic_sum.__setitem__(item, dic_sum.__getitem__(item)+(v*distance))
    return dic_sum

def createKSum(dict, person, distance):
    for item, v in dict[person].items():
        if distance > 0:
            if not dic_ksum.__contains__(item):
                dic_ksum.__setitem__(item, distance)
            else:
                dic_ksum.__setitem__(item, dic_ksum.__getitem__(item)+(distance))
    return dic_ksum

def createRecomm():
    recom = {}
    for item in dic_ksum:
        if dic_sum.get(item) is not None:
            try:
                recom.__setitem__(item, dic_sum.get(item)/dic_ksum.get(item))
            except ZeroDivisionError:
                recom.__setitem__(item, 0)
    return recom

def getRecommendations(prefs, person_in, similarity='unknown', printOutput=False):
    '''
    This function returned a sorted list of recommendations.
    The first entry of the returned list is the recommendation-value (numeric, float), the second is
    the alphabetic name of the key.

    Parameter to pass:
    - prefs -> Dictionary of Values
    - person_in -> Person you want to get recommendations
    - similarity -> euclid or pearson
    - printOutput -> Boolean, True or False for output

    Returning parameters:
    - sorted List[] with pattern:
    [[0.6666666666666666, 'Radio Moscow'], [0.5588425208190283, 'Led Zeppelin'], [0.5563772968714236, 'Pink Floyd'], ...
    '''
    persons = getCleanedNames(prefs, person_in)
    if similarity == 'euclid':
        for person in persons:
            distance = recommendations.sim_euclid(prefs, person_in, person)
            dataDict_Sum = createSum(prefs, person, distance)
            dataDict_kSum = createKSum(prefs, person, distance)
        if printOutput:
            print ('Sumvalues: ' +str(dataDict_Sum))
            print ('Sumvalues of Korrelation: ' +str(dataDict_kSum))
            print ('Recommendationvalues: ' +str(createRecomm()))

    if similarity == 'pearson':
        for person in persons:
            distance = recommendations.sim_pearson(prefs, person_in, person)
            dataDict_Sum = createSum(prefs, person, distance)
            dataDict_kSum = createKSum(prefs, person, distance)
        if printOutput:
            print ('Sumvalues: ' +str(dataDict_Sum))
            print ('Sumvalues of Korrelation: ' +str(dataDict_kSum))
            print ('Recommendationvalues: ' +str(createRecomm()))

    return convertDict2List(createRecomm())

#print getRecommendations(lastFMDict, 'magicgoa', similarity='euclid', printOutput=True)
