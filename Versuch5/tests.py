

import numpy as np
import math
import random

A = np.array([[1,2,3,4],[4,5,6,7],[7,8,9,10]])
B = np.array([[11,12,13,14],[14,15,16,17],[17,18,19,20]])

print len(A)
print A.size

spalten = len(A)
zeilen = A.size / spalten

print zeilen
print spalten

kosten = 0

for i in range(spalten):
    for j in range(zeilen):
        print A[i][j]
        print B[i][j]
        kosten = kosten + math.pow(A[i][j] - B[i][j],2)
        
print kosten

matrColumns = len(A)
matrRows = A.size / matrColumns
m = 2
H = [[0 for x in xrange(m)] for x in xrange(matrColumns)] 
W = [[0 for x in xrange(matrRows)] for x in xrange(m)] 
    
for i in range(m):
    for j in range(matrColumns):
        randomNr = random.randint(0, 10)
        H[j][i] = randomNr
    
for i in range(matrRows):
    for j in range(m):
        randomNr = random.randint(0, 10)
        W[j][i] = randomNr

print W
print H

B = np.dot(W,H)

print A
print B  

        
    