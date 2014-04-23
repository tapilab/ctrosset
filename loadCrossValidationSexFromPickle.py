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
import scipy.stats as scistat

FILE = ''
DATABASE = '/Users/cyriltrosset/Desktop/SPECIAL_PROJ_DB/database-50.sqlite'

APP_KEY = {}
APP_SECRET = {}

loadConfig.loadConfig(FILE,DATABASE,APP_KEY,APP_SECRET)


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
Yd = Y.todense()
YdMale = Y[:,0].todense()

clf = Ridge(alpha=1)
cv = cross_validation.KFold(len(Yd), n_folds=10, random_state=1234)

predicted_values = []
true_values = []

for train, test in cv:
	print 'train indices:', train
	print 'test indices:', test
	clf.fit(Xd[train], Yd[train])
	preds = clf.predict(Xd[test])	
	predicted_values.extend(preds)
	true_values.extend(np.squeeze(np.asarray(Yd[test])))
	

#PLOT PREDICTED VS "TRUE"

plot(predicted_values,true_values,'.')
plot(range(0,100),range(0,100),'r',color='black')
xlabel('% Predicted')
ylabel('% True')
title('True vs Predicted')
legend()

show()

'''
corr = scistat.pearsonr(predicted_values, true_values)
print "Corr score : "
print corr
'''

#PRINT TOP 10 WEIGHTS

f = open('friendsMatrix.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
friends = cPickle.load(f)
f.close()

maleWeights = []
maleString = []
maleValues = []
sup = 99999999
for i in range(0,10):
    max = 0
    index = 0
    for j in range(0,clf.coef_.shape[1]):
        if(clf.coef_[0][j]>max and clf.coef_[0][j]<sup):
            max = clf.coef_[0][j]
            index = j
    maleWeights.append(friends[index,0])
    maleValues.append(max)
    sup = max

print "Male TOP 10 twitter IDs : "
print maleWeights

femaleWeights = []
femaleString = []
femaleValues = []
sup = 99999999
for i in range(0,10):
    max = 0
    index = 0
    for j in range(0,clf.coef_.shape[1]):
        if(clf.coef_[1][j]>max and clf.coef_[1][j]<sup):
            max = clf.coef_[1][j]
            index = j
    femaleWeights.append(friends[index,0])
    femaleValues.append(max)
    sup = max

print "Female TOP 10 twitter IDs : "
print femaleWeights




