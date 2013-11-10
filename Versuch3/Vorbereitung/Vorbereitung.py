import numpy
import scipy.spatial.distance as scDist
import scipy.stats.stats as scipyStats
import scipy as scipy
from Versuch3.CosinusSimilarity import cosinusSim


vector1 = numpy.array([1, 2, 3, 4, 5, 6])
vector2 = numpy.array([3, 3, 5, 6, 7, 8])

vector2D = numpy.array([[1, 2, 3, 4, 5, 6], [3, 3, 5, 6, 7, 8]])

print numpy.var(vector1) #Varianz
print numpy.mean(vector1) #Mittelwert

print scDist.pdist(vector2D, metric='euclidean')
print scipyStats.pearsonr(vector1, vector2)

print scipy.cos(vector2D)

print cosinusSim(vector1, vector2)