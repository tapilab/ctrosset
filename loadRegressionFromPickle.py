import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle
import pylab as pl
import numpy as np
from sklearn import linear_model

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
# The mean square error
z = (regr.predict(X) - Y)
z = np.array(list(z.data))
print("Residual sum of squares: %.2f"
      % np.mean(z ** np.int(2)))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(X, Y))