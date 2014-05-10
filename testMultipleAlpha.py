import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn import cross_validation
from sklearn.linear_model import Ridge
from sklearn.cross_validation import cross_val_score as cv
from sklearn.cross_validation import KFold
import matplotlib.pyplot as plt
from pylab import *
import scipy.stats as scistat

execfile('loadConfig.py')


print "Loading matrix X ..."

f = open('X.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
X = cPickle.load(f) 
f.close()

print "matrix X loaded"

print "Loading Y matrix ..."

f = open('yInc.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
Y = cPickle.load(f)
f.close()
	
print "Y matrix loaded"


Xd = X.todense()
Yd = Y.todense()

max = -9999999
maxAlpha = 0

alphas = [0.001,0.01,0.1,1,5,10,30,50,80,100,1000]

for alpha in alphas:

    clf = Ridge(alpha=alpha)
    cv = cross_validation.KFold(len(Yd), n_folds=10, random_state=1234)

    predicted_values = []
    true_values = []
    indices = []

    for train, test in cv:
        clf.fit(Xd[train], Yd[train])
        preds = clf.predict(Xd[test])
        predicted_values.extend(preds)
        true_values.extend(np.squeeze(np.asarray(Yd[test])))
        indices.extend(test)


#Columns corr
    print "ALPHA  : " + str(alpha)

    corrAverage = 0
    nValues = 0

    for i in range(0,len(predicted_values[0])):
        Cpred = []
        Ctrue = []
        for j in range(0,len(predicted_values)):
            Cpred.append(predicted_values[j][i])
            Ctrue.append(true_values[j][i])

        corr = scistat.pearsonr(Cpred, Ctrue)
        print "Column " + str(i) + " Corr score : "
        print corr
        corrAverage = (corrAverage*nValues + corr[0]) / (nValues+1)
        nValues += 1

    if corrAverage>max:
        max = corrAverage
        maxAlpha = alpha

print "maxAlpha : " + str(maxAlpha) + " , value : " + str(max)
