__author__ = 'janhorak'

import unittest

import facerecognitionTemplate as face

class JUnitTestCases(unittest.TestCase):

    def image(self):
        '''
        IMPORTANT
        =========
        BE CAREFULL: ITS A LONGTERM- TEST!!!
        ~ 3 - 5 Minutes with ~4GB Ram

        If you want to use this test, rename the def with a prefix "test_"
        '''
        list = face.generateListOfImgs(face.parseDirectory('res/training', 'png'))
        self.assertTrue(list is not None)
        # size of the pitcure is 41750 - so we need a length of 41750 for the matrix
        matrix = face.convertImgListToNumpyData(41750, list)
        self.assertIsNotNone(matrix)
        normedArrayOfFaces = face.calculateNormedArrayOfFaces(41750, matrix)
        self.assertIsNotNone(normedArrayOfFaces)


suite = unittest.TestLoader().loadTestsFromTestCase(JUnitTestCases)
unittest.TextTestRunner(verbosity=2).run(suite)