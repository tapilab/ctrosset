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
import matplotlib.pyplot as plt
from pylab import *

FILE = ''
DATABASE = ''

APP_KEY = {}
APP_SECRET = {}

loadConfig.loadConfig(FILE,DATABASE,APP_KEY,APP_SECRET)

"""
print "Loading matrix X ..."

f = open('X.pkl','rb') # open the file in read binary mode
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


Xd = X.todense()
Yd = Y[:,0].todense()
"""

clf = Ridge(alpha=1)
cv = cross_validation.KFold(len(Yd), n_folds=10, random_state=1234)

predicted_values = []
true_values = []

for train, test in cv:
	print 'train indices:', train
	print 'test indices:', test
	clf.fit(Xd[train], Yd[train])
	preds = clf.predict(Xd[test])	
	predicted_values.extend(preds[:,0])
	true_values.extend(np.squeeze(np.asarray(Yd[test]))) 
	

#PLOT PREDICTED VS "TRUE"

plot(predicted_values,true_values,'.')
plot(range(0,100),range(0,100),'r',color='black')
xlabel('% of Male Predicted')
ylabel('% of Male True')
title('True vs Predicted')
legend()

show()
