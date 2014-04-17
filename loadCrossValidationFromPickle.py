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
clf = Ridge(alpha=0.1)
cv = cross_validation.KFold(len(Yd), n_folds=10, random_state=1234)
for train, test in cv:
	print 'train indices:', train
	print 'test indices:', test
	clf.fit(Xd[train], Yd[train])
	preds = clf.predict(Xd[test])
	

#PLOT PREDICTED VS "TRUE"
predict_table = clf.predict(X)
n_groups = predict_table.shape[0]

predicted_values = []
true_values = []
x = []

for i in range(0,n_groups):
    predicted_values.append(round(predict_table[i][0]))
    true_values.append(round(Y[i,0]))
    x.append(i)
    

plot(predicted_values,true_values,'.')
plot(x[0:100],x[0:100],'r',color='black')
xlabel('% of Male Predicted')
ylabel('% of Male True')
title('True vs Predicted')
legend()

show()
