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
cur.execute("SELECT idCriteria FROM Matrix GROUP BY idCriteria HAVING COUNT(*)<50")

rows = cur.fetchall()

i=0

for row in rows:
	cur.execute("DELETE FROM Matrix WHERE idCriteria='"+str(row['idCriteria'])+"'")
	cur.execute("DELETE FROM Friends WHERE save='"+str(row['idCriteria'])+"'")
	print i 
	i+=1
	
con.commit()
con.close()