import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle
import pylab as pl
import numpy as np
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import datasets
from sklearn import svm

FILE = ''
DATABASE = ''

APP_KEY = {}
APP_SECRET = {}

foobar = open( "foobar.config", "r" )

i=0
for line in foobar:
    line=line.rstrip('\n')
    if i==0:
        FILE = line
    elif i==1:
        DATABASE = line
    elif i==2:
        APP_KEY = line.split(',')
    elif i==3:
        APP_SECRET = line.split(',')
    i+=1
    
foobar.close()


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



f = open('regression.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
regr = cPickle.load(f) 
f.close()


print('Coefficients: \n', regr.coef_)

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X.todense(), Y.todense(), test_size=0.4, random_state=0)

clf = svm.SVC(kernel='linear', C=1).fit(X_train, y_train)
clf.score(X_test, y_test)