import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle

execfile('loadConfig.py')

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM Friends")
numberOfCriterias = cur.fetchone()[0]

cur.execute("SELECT COUNT(*) FROM ProfilesIds")
numberOfCie = cur.fetchone()[0]

cur.execute("SELECT * FROM Matrix")

rows = cur.fetchall()

matrix = lil_matrix((numberOfCie,numberOfCriterias))

i=0

for row in rows:
    cur.execute("SELECT id FROM Friends WHERE idFriend='"+str(row['idCriteria'])+"'")
    idCol = cur.fetchone()[0]
    cur.execute("SELECT id FROM ProfilesIds WHERE idProfile='"+str(row['idProfile'])+"'")
    idRow = cur.fetchone()[0]
    matrix[idRow,idCol] = row['coef']
    if(row['idProfile']!=i):
        i=row['idProfile']
        print i
f = open('X.pkl','wb')
cPickle.dump(matrix,f,-1)
f.close()