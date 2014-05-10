import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle

FILE = ''
DATABASE = '/Users/cyriltrosset/Desktop/SPECIAL_PROJ_DB/database-50.sqlite'
APP_KEY = {}
APP_SECRET = {}

con = lite.connect(DATABASE)

con.row_factory = lite.Row

cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM Friends")
numberOfCriterias = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM ProfilesIds")
numberOfCie = cur.fetchone()[0]

cur.execute("SELECT * FROM Matrix")

rows = cur.fetchall()

matrix = lil_matrix((numberOfCie,numberOfCriterias+1))

i=0

for row in rows:
	cur.execute("SELECT id FROM Friends WHERE save='"+str(row['idCriteria'])+"'")
	id = cur.fetchone()[0]
	matrix[row['idProfile'],id] = row['coef']
	if(row['idProfile']!=i):
		i=row['idProfile']
		print i

f = open('X.pkl','wb')
cPickle.dump(matrix,f,-1)
f.close()