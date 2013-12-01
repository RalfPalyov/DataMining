__author__ = 'janhorak'

import unittest

class JUnitTestCases(unittest.TestCase):

    def setup(self):
        pass



suite = unittest.TestLoader().loadTestsFromTestCase(JUnitTestCases)
unittest.TextTestRunner(verbosity=2).run(suite)