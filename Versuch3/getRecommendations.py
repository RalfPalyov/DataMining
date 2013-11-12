import recommendations

def getCleanedNames(prefs, searchedPerson):
    resultArray = []
    counter = 0
    for s in prefs.keys():
        if s != searchedPerson:
            resultArray.append(s)
            counter += 1
    return resultArray

def getFilmratings_Night(prefs, person):
    if 'The Night Listener' in prefs[person]:
        return prefs[person]['The Night Listener']
    return 0
def getFilmratings_Lady(prefs, person):
    if 'Lady in the Water' in prefs[person]:
        return prefs[person]['Lady in the Water']
    return 0
def getFilmratings_Luck(prefs, person):
    if 'Just My Luck' in prefs[person]:
        return prefs[person]['Just My Luck']
    return 0

def getPersons_getFilm(prefs, searchedPerson, filmTitle):
    resultArray = []
    for person in prefs.keys():
        print prefs.keys()
        if person != searchedPerson:
            resultArray.append(person)
    print resultArray
    return resultArray

def getRecommendations(prefs, person_in, similarity='unknown', printOutput=False):

    persons = getCleanedNames(prefs, person_in)
    night_sum = 0
    lady_sum = 0
    luck_sum = 0
    night_Ksum = 0
    lady_Ksum = 0
    luck_Ksum = 0
    if similarity == 'euklid':
        for person in persons:
            distance = recommendations.sim_euclid(prefs, person_in, person)
            if printOutput:
                print ('Distance between: '+ person+ ' and '+ person_in)
                print distance
            if distance > 0:
                if printOutput:
                    print ('Rating of '+person+' for Film: The Night Listener: ' + str(getFilmratings_Night(prefs, person)))
                    print ('Rating of '+person+' for Film: Lady in the Water: ' + str(getFilmratings_Lady(prefs, person)))
                    print ('Rating of '+person+' for Film: Just My Luck: ' + str(getFilmratings_Luck(prefs, person)))
                    print ('Korrelation * Film (Night):')
                    print (recommendations.sim_euclid(prefs, person_in, person)*getFilmratings_Night(prefs, person))
                night_sum += (recommendations.sim_euclid(prefs, person_in, person)*getFilmratings_Night(prefs, person))
                if recommendations.sim_euclid(prefs, person_in, person)*getFilmratings_Night(prefs, person) > 0:
                    night_Ksum += distance
                if printOutput:
                    print ('Korrelation * Film (Luck):')
                luck_sum += (recommendations.sim_euclid(prefs, person_in, person)*getFilmratings_Luck(prefs, person))
                if recommendations.sim_euclid(prefs, person_in, person)*getFilmratings_Luck(prefs, person) > 0:
                    luck_Ksum += distance
                if printOutput:
                    print (recommendations.sim_euclid(prefs, person_in, person)*getFilmratings_Luck(prefs, person))
                    print ('Korrelation * Film (Lady):')
                lady_sum += (recommendations.sim_euclid(prefs, person_in, person)*getFilmratings_Lady(prefs, person))
                if recommendations.sim_euclid(prefs, person_in, person)*getFilmratings_Lady(prefs, person) > 0:
                    lady_Ksum += distance
                if printOutput:
                    print (recommendations.sim_euclid(prefs, person_in, person)*getFilmratings_Lady(prefs, person))
                    print ('---' *10)

    if similarity == 'pearson':
        for person in persons:
            distance = recommendations.sim_pearson(prefs, person_in, person)
            if printOutput:
                print ('Distance between: '+ person+ ' and '+ person_in)
                print distance
            if distance > 0:
                if printOutput:
                    print ('Rating of '+person+' for Film: The Night Listener: ' + str(getFilmratings_Night(prefs, person)))
                    print ('Rating of '+person+' for Film: Lady in the Water: ' + str(getFilmratings_Lady(prefs, person)))
                    print ('Rating of '+person+' for Film: Just My Luck: ' + str(getFilmratings_Luck(prefs, person)))
                    print ('Korrelation * Film (Night):')
                    print (recommendations.sim_pearson(prefs, person_in, person)*getFilmratings_Night(prefs, person))
                night_sum += (recommendations.sim_pearson(prefs, person_in, person)*getFilmratings_Night(prefs, person))
                if recommendations.sim_pearson(prefs, person_in, person)*getFilmratings_Night(prefs, person) > 0:
                    night_Ksum += distance
                if printOutput:
                    print ('Korrelation * Film (Luck):')
                luck_sum += (recommendations.sim_pearson(prefs, person_in, person)*getFilmratings_Luck(prefs, person))
                if recommendations.sim_pearson(prefs, person_in, person)*getFilmratings_Luck(prefs, person) > 0:
                    luck_Ksum += distance
                if printOutput:
                    print (recommendations.sim_pearson(prefs, person_in, person)*getFilmratings_Luck(prefs, person))
                    print ('Korrelation * Film (Lady):')
                lady_sum += (recommendations.sim_pearson(prefs, person_in, person)*getFilmratings_Lady(prefs, person))
                if recommendations.sim_pearson(prefs, person_in, person)*getFilmratings_Lady(prefs, person) > 0:
                    lady_Ksum += distance
                if printOutput:
                    print (recommendations.sim_pearson(prefs, person_in, person)*getFilmratings_Lady(prefs, person))
                    print ('---' *10)


    empfehlungsWert_Lady = lady_sum / lady_Ksum
    empfehlungsWert_Night = night_sum / night_Ksum
    empfehlungsWert_Luck = luck_sum / luck_Ksum

    resultArray = []
    resultArray.append(['Lady in the Water', empfehlungsWert_Lady])
    resultArray.append(['The Night Listener', empfehlungsWert_Night])
    resultArray.append(['Just My Luck', empfehlungsWert_Luck])

    return sorted(resultArray, reverse=True)



