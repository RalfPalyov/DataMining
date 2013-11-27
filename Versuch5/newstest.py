import unittest
import newsfeatures

class JUnitTestCases(unittest.TestCase):

    ## Variables ##
    __allwords = {u'sticking': 1, u'remarkable': 1, u'finalized': 1, u'global': 1, u'alternatives': 1, u'years': 2, u'unrest': 1, u'london': 1, u'talks': 1, u'still': 1, u'police': 1, u'intercontinental': 1, u'delays': 3, u'actually': 1, u'flights': 2, u'forbes': 2, u'candidates': 1, u'shinawatra': 1, u'holiday': 5, u'thousands': 1, u'scheduled': 1, u'prime': 1, u'worse': 1, u'government': 1, u'regional': 1, u'overall': 1, u'protesters': 1, u'coast': 2, u'primesense': 1, u'worst': 2, u'schedules': 1, u'trade': 1, u'presidential': 1, u'landings': 1, u'denounced': 1, u'busiest': 1, u'arrivals': 3, u'morning': 1, u'night': 1, u'popular': 1, u'become': 1, u'europe': 1, u'right': 1, u'often': 1, u'demonstrations': 1, u'extremist': 1, u'captive': 1, u'traveling': 1, u'takeoff': 1, u'event': 1, u'banska': 1, u'abandon': 1, u'israeli': 1, u'broad': 1, u'decision': 1, u'since': 1, u'research': 1, u'suspect': 1, u'closed': 1, u'capital': 1, u'shared': 1, u'christmas': 2, u'arrival': 2, u'annan': 1, u'stance': 1, u'schedule': 1, u'shankar': 1, u'bangkok': 1, u'reported': 1, u'ranked': 2, u'focused': 1, u'found': 2, u'based': 1, u'change': 1, u'shazia': 1, u'climate': 2, u'improved': 1, u'hampers': 1, u'region': 1, u'according': 1, u'ideology': 1, u'carrier': 1, u'place': 1, u'airline': 2, u'syria': 1, u'origin': 1, u'major': 1, u'already': 1, u'apple': 1, u'purchases': 1, u'northeastern': 1, u'angrily': 1, u'litmus': 1, u'three': 1, u'homosexuality': 1, u'slovak': 1, u'another': 1, u'prasad': 1, u'conference': 1, u'given': 1, u'political': 1, u'airlines': 4, u'reuters': 1, u'agreements': 1, u'biggest': 1, u'bystrica': 1, u'marchers': 1, u'today': 1, u'comair': 1, u'flight': 2, u'geneva': 2, u'season': 3, u'hotel': 1, u'airplanes': 1, u'delayed': 2, u'yingluck': 1, u'minister': 1, u'delta': 1, u'women': 1, u'detection': 1, u'pakistani': 1, u'politician': 1, u'elected': 1, u'signed': 1, u'abortion': 1, u'governor': 1, u'nations': 1, u'specialises': 1, u'believed': 1, u'making': 1, u'something': 1, u'program': 1, u'almost': 1, u'turned': 1, u'departure': 1, u'periods': 1, u'schoolgirl': 1, u'story': 1, u'technology': 1, u'jetblue': 3, u'motion': 1, u'compared': 1, u'hawaiian': 1, u'efficient': 1, u'deadly': 1, u'began': 1, u'administration': 1, u'shuttered': 1, u'saturday': 1, u'majority': 1, u'sunday': 1, u'resignation': 1, u'pathway': 1, u'obama': 1, u'experienced': 1, u'monday': 1, u'though': 1, u'demanding': 1, u'marched': 1, u'united': 1, u'winter': 1, u'tracking': 1, u'analyzing': 1, u'lines': 1, u'thanksgiving': 2, u'treaty': 1, u'looked': 1, u'rather': 1, u'nuclear': 1, u'flightaware': 2, u'ramzan': 1, u'travel': 3}
    __articleWords = [{u'sticking': 1, u'annan': 1, u'alternatives': 1, u'holiday': 5, u'administration': 1, u'syria': 1, u'worse': 1, u'obama': 1}, {u'police': 1, u'political': 1, u'three': 1, u'holiday': 5, u'years': 1, u'ideology': 1, u'captive': 1, u'london': 1, u'shared': 1, u'believed': 1, u'suspect': 1, u'women': 1}, {u'origin': 1, u'stance': 1, u'almost': 1, u'abortion': 1, u'political': 1, u'litmus': 1, u'homosexuality': 1, u'candidates': 1, u'something': 1, u'become': 1, u'presidential': 1}, {u'major': 1, u'since': 1, u'began': 1, u'often': 1, u'northeastern': 1, u'three': 1, u'comair': 1, u'analyzing': 1, u'traveling': 1, u'takeoff': 1, u'actually': 1, u'still': 1, u'jetblue': 3, u'compared': 1, u'based': 1, u'focused': 1, u'efficient': 1, u'shuttered': 1, u'travel': 3, u'thanksgiving': 2, u'airlines': 4, u'research': 1, u'majority': 1, u'flights': 2, u'forbes': 2, u'departure': 1, u'closed': 1, u'holiday': 5, u'christmas': 2, u'arrival': 2, u'experienced': 1, u'flight': 2, u'hawaiian': 1, u'though': 1, u'season': 3, u'regional': 2, u'airplanes': 1, u'delayed': 2, u'coast': 2, u'overall': 1, u'reported': 1, u'ranked': 2, u'worst': 2, u'schedules': 1, u'years': 2, u'winter': 1, u'landings': 1, u'tracking': 1, u'improved': 1, u'hampers': 1, u'busiest': 1, u'lines': 1, u'according': 1, u'arrivals': 3, u'looked': 1, u'rather': 1, u'delta': 1, u'carrier': 1, u'place': 1, u'airline': 2, u'popular': 1, u'found': 2, u'flightaware': 2, u'delays': 3, u'periods': 1}, {u'europe': 1, u'scheduled': 1, u'denounced': 1, u'government': 1, u'broad': 1, u'decision': 1, u'political': 1, u'angrily': 1, u'signed': 1, u'trade': 1, u'agreements': 1, u'abandon': 1, u'marchers': 1}, {u'prime': 1, u'yingluck': 1, u'unrest': 1, u'monday': 1, u'government': 1, u'resignation': 1, u'since': 1, u'political': 1, u'protesters': 1, u'demanding': 1, u'bangkok': 1, u'marched': 1, u'reuters': 1, u'minister': 1, u'capital': 1, u'biggest': 1, u'shinawatra': 1, u'thousands': 1, u'demonstrations': 1, u'deadly': 1}, {u'event': 1, u'program': 1, u'given': 1, u'already': 1, u'geneva': 2, u'schedule': 1, u'nuclear': 1, u'hotel': 1, u'turned': 1, u'morning': 1, u'intercontinental': 1, u'sunday': 1, u'reuters': 1, u'another': 1, u'night': 1, u'talks': 1, u'saturday': 1}, {u'banska': 1, u'right': 1, u'politician': 1, u'region': 1, u'regional': 1, u'governor': 1, u'extremist': 1, u'elected': 1, u'slovak': 1, u'bystrica': 1}, {u'conference': 1, u'climate': 2, u'united': 1, u'treaty': 1, u'finalized': 1, u'global': 1, u'shankar': 1, u'nations': 1, u'prasad': 1, u'pathway': 1, u'change': 1}, {u'shazia': 1, u'story': 1, u'remarkable': 1, u'schoolgirl': 1, u'pakistani': 1, u'ramzan': 1, u'today': 1}, {u'purchases': 1, u'israeli': 1, u'primesense': 1, u'apple': 1, u'detection': 1, u'motion': 1, u'specialises': 1, u'making': 1, u'technology': 1}]
    ## Setup- Function ##
    def setUp(self):
        pass


    ## Testfunctions ##

    def newsDict(self):
        newsDict = newsfeatures.getNewsDict()
        self.assertTrue(True)

    def test_makeMatrix_offline(self):
        allwords = self.__allwords
        articleWords = self.__articleWords
        returnedObject = newsfeatures.makematrix(allwords, articleWords)

        self.assertTrue(len(returnedObject.getWordVector()) > 0)


    def test_makeMatrix_online(self):
        inDict = newsfeatures.getarticlewords()
        allwords = inDict['allwords']
        articleWords = inDict['articlewords']
        returnedObject = newsfeatures.makematrix(allwords, articleWords)

        self.assertTrue(len(returnedObject.getWordVector()) > 0)




suite = unittest.TestLoader().loadTestsFromTestCase(JUnitTestCases)
unittest.TextTestRunner(verbosity=2).run(suite)