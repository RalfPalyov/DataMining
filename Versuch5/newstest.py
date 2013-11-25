import unittest
import newsfeatures

class JUnitTestCases(unittest.TestCase):

    ## Variables ##


    ## Setup- Function ##
    def setUp(self):
        pass


    ## Testfunctions ##

    def newsDictTest(self):
        newsDict = newsfeatures.getNewsDict()
        print newsDict.keys()
        print len(newsDict)
        self.assertTrue(True)
        #testfix

    def test2(self):
        # please rename function
        pass

    #...

suite = unittest.TestLoader().loadTestsFromTestCase(JUnitTestCases)
unittest.TextTestRunner(verbosity=2).run(suite)