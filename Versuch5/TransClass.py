import numpy

__author__ = 'janhorak'

class TransClass:
    __wordvec = []
    __articleWordMat = numpy.matrix

    def __init__(self, wordvector, articleWordMat):
        self.__wordvec = wordvector
        self.__articleWordMat = articleWordMat

    def setWordvector(self, wordvector):
        self.__wordvec = wordvector

    def setArticleWordMat(self, articleWordMat):
        self.__articleWordMat = articleWordMat

    def getWordVector(self):
        return self.__wordvec

    def getArticleWordMat(self):
        return self.__articleWordMat