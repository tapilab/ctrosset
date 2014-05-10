import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle

execfile('loadConfig.py')

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM ProfilesIds")
numberOfCriterias = cur.fetchone()[0]

cur = con.cursor()
cur.execute("SELECT * FROM ProfilesIds")

rows = cur.fetchall()

YAge = lil_matrix((numberOfCriterias,6))

for row in rows:
    YAge[row['id'],0] = row['AgeOne']
    YAge[row['id'],1] = row['AgeTwo']
    YAge[row['id'],2] = row['AgeThree']
    YAge[row['id'],3] = row['AgeFour']
    YAge[row['id'],4] = row['AgeFive']
    YAge[row['id'],5] = row['AgeSix']
	
f = open('YAge.pkl','wb')
cPickle.dump(YAge,f,-1)
f.close()