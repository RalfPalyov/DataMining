__author__ = 'janhorak'

import unittest

import numpy as np
import facerecognitionTemplate as face
import tkFileDialog

class JUnitTestCases(unittest.TestCase):

    def est_image(self):
        list = face.generateListOfImgs(face.parseDirectory('res/training', 'png'))
        self.assertTrue(list is not None)
        # size of the pitcure is 41750 - so we need a length of 41750 for the matrix
        matrix = face.convertImgListToNumpyData(41750, list)
        self.assertIsNotNone(matrix)
        normedArrayOfFaces = face.calculateNormedArrayOfFaces(41750, matrix)
        self.assertIsNotNone(normedArrayOfFaces)
        
    def est_eigenfaces(self):
        eigenfaces = face.calculateEigenfaces(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]), 3, 1)
        self.assertIsNotNone(eigenfaces)
        
    def est_projectImage(self):
        image1 = [1, 2, 3, 4]
        image2 = [9, 8, 7, 6] 
        eigenfaces = face.calculateEigenfaces(np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]), 2, 2)
        self.assert_(np.all(np.equal(face.projectImageOnEigenspace(eigenfaces, image1), face.projectImagesOfSamePersonOnEigenspace(eigenfaces, [image1, image1]))), "Projection results must be equal.")
        self.assertIsNotNone(face.projectImagesOfSamePersonOnEigenspace(eigenfaces, [image1, image2]))
         
    def est_saveEigenvectors(self):
        images = face.generateListOfImgs(face.parseDirectory('res/test', 'png'))
        matrix = face.convertImgListToNumpyData(41750, images)
        normedArrayOfFaces = face.calculateNormedArrayOfFaces(41750, matrix)
        face.saveEigenvektorsAsImage(matrix, normedArrayOfFaces)
        
    def test_maintest(self):
        #Choose Directory which contains all training images 
        TrainDir=tkFileDialog.askdirectory(title="Choose Directory of training images")
        #Choose the file extension of the image files
        Extension='png'
        #Choose the image which shall be recognized
        testImageDirAndFilename[0]=tkFileDialog.askopenfilename(title="Choose Image to detect")

        faceList = generateListOfImgs(parseDirectory(TrainDir, Extension))
    
        # all images must be the same size
        imageSize = faceList[0].size[0] * faceList[0].size[1]
        
        # size of the pitcure is 41750 - so we need a length of 41750 for the matrix
        matrix = convertImgListToNumpyData(imageSize, faceList)
        
        normedArrayOfFaces = calculateNormedArrayOfFaces(imageSize, matrix)
        
        eigenfaces = calculateEigenfaces(normedArrayOfFaces)
        
        relevantEigenfaces = eigenfaces[:7]
        
        #saveEigenvektorsAsImage(matrix, relevantEigenfaces)
        matrix2 = face.convertImgListToNumpyData(imageSize, testImageDirAndFilename[0])
        normedArrayOfFaces2 = calculateNormedArrayOfFaces(imageSize, matrix2)
        imageAverage = face.calculateAverageArrayOfFaces(matrix)
        print imageAverage
        
    def est_recognize(self):
        imagelist = face.parseDirectory('res/test', 'png')
        imagelist2 = face.parseDirectory('res/training', 'png')
        list = face.generateListOfImgs(imagelist)
        list2 = face.generateListOfImgs(imagelist2)
        matrix = face.convertImgListToNumpyData(41750, list)
        matrix2 = face.convertImgListToNumpyData(41750, list2)
        normedArrayOfFaces = face.calculateNormedArrayOfFaces(41750, matrix)
        normedArrayOfFaces2 = face.calculateNormedArrayOfFaces(41750, matrix2)
        
        #eigenfaces = face.calculateEigenfaces(normedArrayOfFaces)
        #eigenfaces2 = face.calculateEigenfaces(normedArrayOfFaces2)
        
        for i in range(len(matrix)):
            testcosts = face.calculateEuclideanDistance(matrix[i], normedArrayOfFaces[i])
            print str(imagelist[i]) + " --> " + str(testcosts)
            
        for i in range(len(matrix)):
            
            maxCosts = 0
            minCosts = 99999
            
            for j in range(len(matrix2)):
                
                tmpCosts = face.calculateEuclideanDistance(matrix[i], matrix2[j])
                
                if tmpCosts > maxCosts:
                    maxCosts = tmpCosts
                    maxJ = j
                
                if tmpCosts < minCosts:
                    minCosts = tmpCosts
                    minJ = j
                    
                # print str(imagelist[i]) + " --> " + str(imagelist2[j]) + ": " + str(costs)
                
            print "Min: " + str(imagelist[i]) + " --> " + str(imagelist2[minJ]) + ": " + str(minCosts)
            print "Max: " + str(imagelist[i]) + " --> " + str(imagelist2[maxJ]) + ": " + str(maxCosts)
            
suite = unittest.TestLoader().loadTestsFromTestCase(JUnitTestCases)
unittest.TextTestRunner(verbosity=2).run(suite)
