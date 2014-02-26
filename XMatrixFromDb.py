import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle

APP_KEY = {}
APP_SECRET = {}

foobar = open( "foobar.config", "r" )

i=0
for line in foobar:
    line=line.rstrip('\n')
    if i==0:
        FILE = line
    elif i==1:
        DATABASE = line
    elif i==2:
        APP_KEY = line.split(',')
    elif i==3:
        APP_SECRET = line.split(',')
    i+=1
    
foobar.close()

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
	
f = open('matrixFiltered.pkl','wb')
cPickle.dump(matrix,f,-1)
f.close()