import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle
import loadConfig

FILE = ''
DATABASE = ''
APP_KEY = {}
APP_SECRET = {}
loadConfig.loadConfig(FILE,DATABASE,APP_KEY,APP_SECRET)

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM Friends")
numberOfCriterias = cur.fetchone()[0]

cur.execute("SELECT * FROM Matrix")

rows = cur.fetchall()

matrix = lil_matrix((132,numberOfCriterias+1))

i=0

for row in rows:
	cur.execute("SELECT id FROM Friends WHERE save='"+str(row['idCriteria'])+"'")
	id = cur.fetchone()[0]
	matrix[row['idProfile'],id] = row['coef']
	if(row['idProfile']!=i):
		i=row['idProfile']
		print i
	
f = open('matrix','wb')
cPickle.dump(matrix,f,-1)
f.close()