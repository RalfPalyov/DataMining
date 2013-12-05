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
            print str('size of ' +str(list[i]) + ': '+ str(image.size[0]) + "x" + str(image.size[1]))
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
    for row in range(len(matrix)):
        for coulumn in range(length):
            imageAverage = np.average(matrix[row])
            #print str('Average of Line: ' + str(imageAverage))
            #print str('Row: ' + str(row) + ' Col: ' + str(coulumn))
            #print str('For Row: ' + str(matrix[row]))
            pixel = resultMatrix[row][coulumn]
            #print str('Current Pixelvalue: '+str(pixel))
            pixel -= imageAverage
            if pixel < 0:
                pixel = 0
            #print str('New value of Pixel (Difference): '+str(pixel))
            resultMatrix[row][coulumn] = pixel
            #print str('Modified Row: ' +str(matrix[row]))
            #print '---' *10
    print resultMatrix
    return resultMatrix


####################################################################################
#Start of main programm

#Choose Directory which contains all training images 
#TrainDir=tkFileDialog.askdirectory(title="Choose Directory of training images")
#Choose the file extension of the image files
#Extension='png'
#Choose the image which shall be recognized
#testImageDirAndFilename=tkFileDialog.askopenfilename(title="Choose Image to detect")

####################################################################################
# Implement required functionality of the main programm here


