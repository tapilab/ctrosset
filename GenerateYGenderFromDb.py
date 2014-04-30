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

YMaleFemaleMatrix = lil_matrix((numberOfCriterias,2))

for row in rows:
	YMaleFemaleMatrix[row['id'],0] = row['Male']
	YMaleFemaleMatrix[row['id'],1] = 100-row['Male']
	
f = open('YMaleFemale.pkl','wb')
cPickle.dump(YMaleFemaleMatrix,f,-1)
f.close()