

class Classifier:
    __cc = {'Good': 0, 'Bad': 0}
    __fc = {}


    def __init__(self, fc, cc):
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
        pass


    def incc(self, category):
        '''Increases the count of the passed category at 1

        Parameters to pass:
        -------------------
        category -> Keyvalue of the dictionary. Per Default "Good" or "Bad"

        returns:
        --------
        void'''
        newCount = self.__cc.get(category) +1
        self.__cc.update({category: newCount})



    def fcount(self, f, category):
        '''Returns the count of the passed word in the passed category
        Parameters to pass:
        -------------------
        f -> A Word we want to check (Type: String)
        category -> Keyvalue of the dictionary. Per Default "Good" or "Bad"

        returns:
        --------
        Value of the count (Integer)'''
        return self.__cc.get(category).get(f)


    def catcounts(self, category):
        '''Returns the count of the passed category
        Parameters to pass:
        -------------------
        category -> Keyvalue of the dictionary. Per Default "Good" or "Bad"

        returns:
        --------
        Value of the count (Integer)'''
        return self.__cc.get(category)


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
        pass



    def fprob(self, f, category):
        pass


