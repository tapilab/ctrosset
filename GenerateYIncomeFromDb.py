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

YInc = lil_matrix((numberOfCriterias,8))

for row in rows:
    YInc[row['id'],0] = row['IncOne']
    YInc[row['id'],1] = row['IncTwo']
    YInc[row['id'],2] = row['IncThree']
    YInc[row['id'],3] = row['IncFour']
    YInc[row['id'],4] = row['IncFive']
    YInc[row['id'],5] = row['IncSix']
    YInc[row['id'],6] = row['IncSeven']
    YInc[row['id'],7] = row['IncEight']
	
f = open('YInc.pkl','wb')
cPickle.dump(YInc,f,-1)
f.close()