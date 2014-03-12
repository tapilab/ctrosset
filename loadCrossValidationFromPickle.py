import loadConfig
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

FILE = ''
DATABASE = ''

APP_KEY = {}
APP_SECRET = {}

loadConfig.loadConfig(FILE,DATABASE,APP_KEY,APP_SECRET)


print "Loading matrix X ..."

f = open('matrix.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
X = cPickle.load(f) 
f.close()

print "matrix X loaded"

print "Loading Y matrix ..."

f = open('yMaleFemale.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
Y = cPickle.load(f)
f.close()
	
print "Y matrix loaded"


'''
f = open('regression.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
regr = cPickle.load(f) 
f.close()


print('Coefficients: \n', regr.coef_)
'''


clf = Ridge(alpha=1.0)
clf.fit(X, Y.todense())
print clf.predict(X)

print np.mean(cv(clf, X, Y.todense(),scoring='mean_squared_error'))