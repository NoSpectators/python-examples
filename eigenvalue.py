# -*- coding: utf-8 -*-
"""
Created on Mon Dec 05 14:48:05 2016

@author: John
"""

#complete the matrix
import numpy as np

A = np.array([ [1,    4, 3,    6   ],
               [1/4., 1, 1/2., 1/3.],
               [1/3., 2, 1,    3   ],
               [1/6., 3, 1/3., 1   ]  ])
#A = A.astype(float)
print A
_lambda =  max(np.linalg.eigvals(A))#4.316
print "lambda = ",  _lambda

#normalize the matrix
#get sum of columns
colsums = A.sum(0)
print "colsums = ", colsums

normalizedMatrix = A/colsums
print "normalized matrix = "
print normalizedMatrix

#calculate CI and CR
consistency_index = (_lambda-4)/(4-1)
print "CI = ", consistency_index
consistency_ratio = consistency_index / .89
print "CR = ", consistency_ratio 
"""this CI is > .1, so I would have to try to throw out some comparisons
"""

#calculate geometric means
prod = np.prod(normalizedMatrix,axis=1)
#print prod
from scipy.special import cbrt
geom = cbrt(prod)
print "geometric means = ", geom

#normalize the geometric weights
normGeomSum = np.sum(geom)
print "sum of geom weights = ", normGeomSum
normGeom = geom/normGeomSum
print normGeom





               