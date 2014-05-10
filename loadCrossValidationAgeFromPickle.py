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
from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError

execfile('loadConfig.py')


print "Loading matrix X ..."

f = open('X.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
X = cPickle.load(f) 
f.close()

print "matrix X loaded"

print "Loading Y matrix ..."

f = open('yAge.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
Y = cPickle.load(f)
f.close()
	
print "Y matrix loaded\n"


Xd = X.todense()
Yd = Y.todense()

clf = Ridge(alpha=0.001)
cv = cross_validation.KFold(len(Yd), n_folds=10, random_state=1234)

predicted_values = []
true_values = []
indices = []

for train, test in cv:
    print 'train indices:', train
    print 'test indices:', test
    clf.fit(Xd[train], Yd[train])
    preds = clf.predict(Xd[test])
    predicted_values.extend(preds)
    true_values.extend(np.squeeze(np.asarray(Yd[test])))
    indices.extend(test)
	

#PLOT PREDICTED VS "TRUE"

mpl.axes.set_default_color_cycle(['r', 'g', 'b', 'c','m','y','k','#ff3ed8','#ffd83e'])
p1 = plot(predicted_values,true_values,'.')
p2 = plot(range(0,100),range(0,100),'r',color='black')
xlabel('% Predicted')
ylabel('% True')
title('True vs Predicted')
legend(p1,['0-16','17-19','20-24','25-29','30-34','35-39','40-49','50-59','60+'])

#Columns corr

for i in range(0,len(predicted_values[0])):
    Cpred = []
    Ctrue = []
    for j in range(0,len(predicted_values)):
        Cpred.append(predicted_values[j][i])
        Ctrue.append(true_values[j][i])
    
    corr = scistat.pearsonr(Cpred, Ctrue)
    print "Column " + str(i) + " Corr score : "
    print corr

#PRINT TOP 10 WEIGHTS

f = open('friendsMatrix.pkl','rb') # open the file in read binary mode
# load the data in the .pkl file into a new variable spmat
friends = cPickle.load(f)
f.close()

twitter = Twython(APP_KEY[2], APP_SECRET[2], oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()


twitter = Twython(APP_KEY[2], access_token=ACCESS_TOKEN)

print "\n"

for k in range(0,clf.coef_.shape[0]):
    Weights = []
    Values = []
    Strings = []
    sup = 99999999
    for i in range(0,10):
        max = 0
        index = 0
        for j in range(0,clf.coef_.shape[1]):
            if(clf.coef_[k][j]>max and clf.coef_[k][j]<sup):
                max = clf.coef_[k][j]
                index = j
        Weights.append(friends[index,0])
        Values.append(max)
        try:
            user = twitter.show_user(user_id = int(friends[index,0]))
        except TwythonRateLimitError:
            print "API Limit reached"
        Strings.append(user['screen_name'])
        sup = max
        print("@" + user['screen_name'] + "\t" + str(max))
    print "Column " + str(k) + " TOP 10 twitter IDs : "
    print Strings
    print Values

#PRINT TOP 10 ERRORS

print "\n"

con = lite.connect(DATABASE)

con.row_factory = lite.Row

cur = con.cursor()

CieId = []
CieString = []
ErrorValue = []
sup = 99999999
for i in range(0,10):
    max = 0
    index = 0
    for j in range(0,len(true_values)):
        if(abs(true_values[j][0]-predicted_values[j][0])>max and abs(true_values[j][0]-predicted_values[j][0])<sup):
            max = abs(true_values[j][0]-predicted_values[j][0])
            index = j
    CieId.append(index)
    cur.execute("SELECT screenName FROM ProfilesIds WHERE id='"+str(index)+"'")
    ScreenName = cur.fetchone()[0]
    CieString.append(ScreenName)
    ErrorValue.append(max)
    sup=max

print "TOP 10 ERRORS CIE : "
print CieString
print "With Values : "
print ErrorValue

#Compute MSE For each columns

print "\n"

for k in range(0,len(predicted_values[0])):
    sum = 0
    for i in range(0,len(predicted_values)):
        sum += (predicted_values[i][k]-true_values[i][k])*(predicted_values[i][k]-true_values[i][k])
    result = (1/float(len(predicted_values)))*sum
    print "Column " +str(k)+" MSE : "
    print result

show()