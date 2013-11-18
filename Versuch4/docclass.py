

class Classifier:
    __cc = {'Good': 0, 'Bad': 0}
    __fc = {}

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
    def __init__(self, fc, cc):
        self.__cc = cc
        self.__fc = fc

    ''''''
    def incf(self, word, category):
        pass

    '''Increases the count of the passed category at 1

        Parameters to pass:
       -------------------
       category -> Keyvalue of the dictionary. Per Default "Good" or "Bad"

       returns:
       --------
       void
    '''
    def incc(self, category):
        newCount = self.__cc.get(category) +1
        self.__cc.update({category: newCount})

    '''Returns the count of the passed word in the passed category
        Parameters to pass:
       -------------------
       f -> A Word we want to check (Type: String)
       category -> Keyvalue of the dictionary. Per Default "Good" or "Bad"

       returns:
       --------
       Value of the count
       (Integer)
    '''
    def fcount(self, f, category):
        return self.__cc.get(category).get(f)

    '''Returns the count of the passed category
        Parameters to pass:
       -------------------
       category -> Keyvalue of the dictionary. Per Default "Good" or "Bad"

       returns:
       --------
       Value of the count
       (Integer)
    '''
    def catcounts(self, category):
        return self.__cc.get(category)

    '''Returns the total count of values Parameters to pass:
        Parameters to pass:
       -------------------
       None

       returns:
       --------
       Total count of both categories
       (Integer)
    '''
    def totalcount(self):
        result = 0
        for item, v in self.__cc:
            result += v
        return result

    def train(self, item, category):
        pass

    def fprob(self, f, category):
        pass

