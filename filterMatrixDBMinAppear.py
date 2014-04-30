import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle

execfile('loadConfig.py')

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

maxCount = input('Enter the minimum appearance limit : ');

cur = con.cursor()
cur.execute("SELECT idCriteria FROM Matrix GROUP BY idCriteria HAVING COUNT(*)<"+str(maxCount))

rows = cur.fetchall()

i=0

for row in rows:
	cur.execute("DELETE FROM Matrix WHERE idCriteria='"+str(row['idCriteria'])+"'")
	cur.execute("DELETE FROM Friends WHERE idFriend='"+str(row['idCriteria'])+"'")
	print i 
	i+=1
	
con.commit()
con.close()