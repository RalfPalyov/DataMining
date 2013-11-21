import aufgabe2_1_1

class Classifier:
    __cc = {'Good': 0, 'Bad': 0}
    __fc = {}


    def __init__(self, fc = {}, cc = {'Good': 0, 'Bad': 0}):
        '''Constructor for Classifier-class
       --------------------------------
       The Classifier needs two dictionaries for the input.

       Parameters to pass:
       -------------------
       fc ->
       cc -> The dictionary indicates the amount of occur
            of the Keys
            Per Default the Keyvalues are Good and Bad.
            Initialized with 0


       returns:
       --------
       -> Object
       '''
        self.__cc = cc
        self.__fc = fc


    def incf(self, word, category):
        '''
        Increase the count of the documents in category which contain the passed word.
        
        Paremters:
        word: String, the word that must be contained
        category: String, the category 
        '''
        try:
            self.__cc[category]
        except KeyError:
            return False
        try:
            self.__fc[word][category] = self.__fc[word][category] + 1
        except:
            self.__fc[word] = {category: 1}


    def incc(self, category):
        '''Increases the count of the passed category at 1

        Parameters to pass:
        -------------------
        category -> Keyvalue of the dictionary. Per Default "Good" or "Bad"

        returns:
        --------
        void'''
        try:
            self.__cc[category] = self.__cc[category] + 1
        except KeyError:
            return False



    def fcount(self, f, category):
        '''Returns the count of the passed word in the passed category
        Parameters to pass:
        -------------------
        f -> A Word we want to check (Type: String)
        category -> Keyvalue of the dictionary. Per Default "Good" or "Bad"

        returns:
        --------
        Value of the count (Integer)'''
        try:
            return self.__fc[f][category]
        except KeyError:
            return 0
         


    def catcounts(self, category):
        '''Returns the count of the passed category
        Parameters to pass:
        -------------------
        category -> Keyvalue of the dictionary. Per Default "Good" or "Bad"

        returns:
        --------
        Value of the count (Integer)'''
        try:
            return self.__cc[category]
        except KeyError:
            return 0


    def totalcount(self):
        '''Returns the total count of values Parameters to pass:
        Parameters to pass:
        -------------------
        None

        returns:
        --------
        Total count of both categories(Integer)'''
        result = 0
        for key in self.__cc.keys():
            result += self.__cc.get(key)
        return result



    def train(self, item, category):
        '''
        Train the object with a document/item.
        
        Parameters:
        item: String, document to train with
        category: String ('Bad'|'Good'), items category
        '''
        
        self.incc(category)
        
        for word in self.getFeatures(item).iterkeys():
            self.incf(word, category)        

    def fprob(self, f, category):
        try:
            return (self.fcount(f, category))/(self.catcounts(category))
        except StandardError:
            print 'Care, ZeroDivision or not on KeyList'
            return -1



    def getFeatures(self, text):
        '''
        Wrapper for aufgabe2_1_1.getwords(text). See the docu there
        '''
        return aufgabe2_1_1.getwords(text)
    
    
    
    def prob(self, item, cat):
        '''
        Calculates posterior probability (germ.: a-posteriori-Wahrscheinlichkeit) of category given a document.
        
        Parameters:
        item: String, document
        cat: String ('Bad'|'Good'), category
        
        Return:
        Float, probability
        '''
        
        probProduct = 1.0
        aPriori = self.catcounts(cat) / self.totalcount()
        
        for word in self.getFeatures(item):
            probProduct = probProduct * self.weightedprob(word, cat)
        
        return probProduct * aPriori
    

