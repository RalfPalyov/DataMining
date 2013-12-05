from os.path import isdir,join,normpath
from os import listdir

import Image

import numpy as np

import tkFileDialog
from nltk.chunk.named_entity import shape


def parseDirectory(directoryName,extension):
    '''This method returns a list of all filenames in the Directory directoryName. 
    For each file the complete absolute path is given in a normalized manner (with 
    double backslashes). Moreover only files with the specified extension are returned in 
    the list.
    '''
    if not isdir(directoryName): return
    imagefilenameslist=sorted([
        normpath(join(directoryName, fname))
        for fname in listdir(directoryName)
        if fname.lower().endswith('.'+extension)            
        ])
    return imagefilenameslist

#####################################################################################
# Implement required functions here
#

def generateListOfImgs(list):
    '''
    This Function returns the list of images (Type Image) for the passed list of paths.

    Parameters:
    ===========

    list -> List of paths of Images (Type= String)

    Returns:
    ========
    resultList -> List of Images (Type = Image)
    '''
    resultList = []
    for i in range(len(list)):
        try:
            image = Image.open(list[i])
            #print str('size of ' +str(list[i]) + ': '+ str(image.size[0]) + "x" + str(image.size[1]))
            resultList.append(image)
        except StandardError:
            print 'Error: Can\'t read file: ' + image
    return resultList

def convertImgListToNumpyData(length, list):
    '''
    This Function returns a matrix (Type= numpy.asfarray) with the length of an Image
    (per Default 41750) and a depth of all images (per Default 21).

    A single value of Matrix[x][y] is the value of the Pixel y in the Image x.
    The Matrix has the values:
    x (0:20)
    y (0:41750)
    at 21 Pictures in the testdata and an imagesize of 167x250 pixels

    IMPORTANT
    =========
    If you want to set an other Image (with other size) you have to pass a new value for
    length

    Parameters:
    ===========

    length -> Size of the image (per Default 14750 | for an image with size: 167x250)

    list -> list of images

    Returns:
    ========
    resultMatrix -> Matrix (description in header)
    '''
    resultMatrix = np.asfarray(np.zeros(shape=(len(list), len(range(length)))), dtype='float')
    for k in range(len(list)):
        heighestValue = 0
        image = list[k]
        width = image.size[0]
        height = image.size[1]
        pixelData = []
        for i in range(height):
            for j in range(width):
                pixelValue = image.getpixel((j, i))[0]
                if pixelValue > heighestValue:
                    heighestValue = pixelValue
                pixelData.append(pixelValue)

        for i in range(len(pixelData)-1):
            newValue = float(float(pixelData[i]) / float(heighestValue))
            pixelData[i] = newValue

        counter = 0
        for x in pixelData:
            resultMatrix[k][counter] = x
            counter += 1
    return resultMatrix

def calculateNormedArrayOfFaces(length, matrix):
    '''
    This function returns the normed values of the matrix.

    Parameters:
    ===========

    length -> Size of the image (per Default 14750 | for an image with size: 167x250)

    matrix -> matrix for the images

    Returns:
    ========
    resultMatrix -> normed matrix of pixelvalues
    '''
    resultMatrix = matrix
    imageSum = matrix[0]
    for row in range(1, len(matrix)):
        imageSum = imageSum + row
    averageImage = imageSum / len(matrix)
    for row in range(len(matrix)):
        for coulumn in range(length):
            #print str('Average of Line: ' + str(imageAverage))
            #print str('Row: ' + str(row) + ' Col: ' + str(coulumn))
            #print str('For Row: ' + str(matrix[row]))
            pixel = resultMatrix[row][coulumn]
            #print str('Current Pixelvalue: '+str(pixel))
            pixel -= averageImage[row]
            if pixel < 0:
                pixel = 0
            #print str('New value of Pixel (Difference): '+str(pixel))
            resultMatrix[row][coulumn] = pixel
            #print str('Modified Row: ' +str(matrix[row]))
            #print '---' *10
    #print resultMatrix
    return resultMatrix



def calculateEigenfaces(adjfaces,width = None,height = None):
    '''
    Calculates all possible eigenfaces for a given matrix.
    The result will be ordered by eingenvalues in descending order.
    
    Parameter:
    adjfaces: numpy array, normed picture arrays (normed return value of convertImgListToNumpyData()) 
    width:    integer, width of each picture (all pictures must be the same size)
    height:   integer, height of each picture (all pictures must be the same size)
    
    Return:
    Numpy array, each row is a normed eigenface.
    '''
    
    transposedAdjfaces = np.transpose(adjfaces)
    
    xTmultiX = np.dot(adjfaces, transposedAdjfaces)
    
    eigenValues, eigenVectors = np.linalg.eigh(xTmultiX)
    
    sortedEigenValueIndices = np.argsort(eigenValues)[::-1]
    
    eigenfaces = np.zeros((eigenVectors.shape[0], adjfaces.shape[1]))
    
    eigenVectorIdx = 0
    
    for eigenVector in eigenVectors:
        
        dimensionIdx = 0
        
        for adjface in adjfaces:
            
            eigenfaces[eigenVectorIdx] = eigenfaces[eigenVectorIdx] + (eigenVector[dimensionIdx] * adjface)
            
            dimensionIdx = dimensionIdx + 1
        
        eigenVectorIdx = eigenVectorIdx + 1
    
    return eigenfaces[sortedEigenValueIndices]


def projectImageOnEigenspace(eigenVectors, image):
    '''
    Project the image (with the same dimension than its pixel count)
    to an eigenspace that is defined by the passed eigenVectors.
    
    Parameters:
    eigenVectors: 2 dimensional List/array, used to define eigenspace, each row represents a eigenvector
    image:        list/array, each value represents a pixel
    
    Return:
    Numpy array, point in eigenspace that represents the image.
    '''    
    
    eigenspacePoint = np.empty(eigenVectors.shape[0])
    
    idx = 0
    
    for eigenVector in eigenVectors:
        
        eigenspacePoint[idx] = np.dot(np.transpose(eigenVector), image)        
        idx = idx + 1
    
    return eigenspacePoint


def projectImagesOfSamePersonOnEigenspace(eigenVectors, images):
    '''
    It's recommended to train with more than one picture for
    one person. To calculate the distances to this person,
    that is represented by multiple pictures, it's required
    to calculate the average of all pictures of the person.
    The average should be used to compare with instead of each 
    single picture.
    
    Parameters:
    eigenVectors: 2 dimensional List/array, used to define eigenspace, each row represents a eigenvector
    images:       2 dimensional list/array, each value represents a image, each image is a array of pixels
    
    Return:
    Numpy array, point in eigenspace that represents the average image.    
    '''
    
    eigenspacePointSum = projectImageOnEigenspace(eigenVectors, images[0])
    
    for image in images[1:]:
        eigenspacePointSum = eigenspacePointSum + projectImageOnEigenspace(eigenVectors, image)
        
    return eigenspacePointSum / len(images) 
    
    


####################################################################################
#Start of main programm

# Don't execute this if this file is used as a module in another file. 
if __name__ == '__main__':

    #Choose Directory which contains all training images 
    TrainDir=tkFileDialog.askdirectory(title="Choose Directory of training images")
    #Choose the file extension of the image files
    Extension='png'
    #Choose the image which shall be recognized
    testImageDirAndFilename=tkFileDialog.askopenfilename(title="Choose Image to detect")

####################################################################################
# Implement required functionality of the main programm here

    faceList = generateListOfImgs(parseDirectory(TrainDir, Extension))
    
    # all images must be the same size
    imageSize = faceList[0].size[0] * faceList[0].size[1]
    
    # size of the pitcure is 41750 - so we need a length of 41750 for the matrix
    matrix = convertImgListToNumpyData(imageSize, faceList)
    
    normedArrayOfFaces = calculateNormedArrayOfFaces(imageSize, matrix)
    
    eigenfaces = calculateEigenfaces(normedArrayOfFaces)
    
    relevantEigenfaces = eigenfaces[:7]
    
    '''
    @todo calculate eigenspace average for all image of one person and compare them with eigenspace point of test image to find the person with minimum distance
    below there are two examples
    @todo remove examples :)
    '''
    # calculate eigenspace point for one picture
    print projectImageOnEigenspace(relevantEigenfaces, matrix[0])
    
    # calculate eigenspace point for multiple picture (they should be from the same person, maybe that's not true for this example, i didn't check that) 
    print projectImagesOfSamePersonOnEigenspace(relevantEigenfaces, matrix[3:6])
    

