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


'''
f = open('regression.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
regr = cPickle.load(f) 
f.close()


print('Coefficients: \n', regr.coef_)
'''

print 'Computing cross validation'

clf = Ridge(alpha=0.1)
clf.fit(X, Y.todense())
print clf.predict(X)

print np.mean(cv(clf, X, Y.todense(),scoring='mean_squared_error'))


#PLOT PREDICTED VS "TRUE"
predict_table = clf.predict(X)
n_groups = predict_table.shape[0]

predicted_values = []
true_values = []

for i in range(0,n_groups):
    predicted_values.append(round(predict_table[i][0]))
    true_values.append(round(Y[i,0]))

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4
error_config = {'ecolor': '0.3'}

rects1 = plt.bar(index, true_values, bar_width,
                 alpha=opacity,
                 color='b',
                 error_kw=error_config,
                 label='TRUE')

rects2 = plt.bar(index, predicted_values, bar_width,
                 alpha=opacity,
                 color='r',
                 error_kw=error_config,
                 label='Predicted')

plt.xlabel('Cie ID')
plt.ylabel('% of Male')
plt.title('True vs Predicted')
plt.legend()

plt.tight_layout()
plt.show()