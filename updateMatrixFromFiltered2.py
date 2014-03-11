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
cur.execute("SELECT save,id FROM Friends WHERE id!=save ORDER BY id DESC LIMIT 1000")

rows = cur.fetchall()

for row in rows:

	cur.execute("UPDATE Matrix SET idCriteria='"+str(row['id'])+"' WHERE idCriteria='"+str(row['save'])+"'")
	cur.execute("UPDATE Friends SET save='"+str(row['id'])+"' WHERE save='"+str(row['save'])+"'")
	print str(row['id'])
	if(row['id']%500==0):
		con.commit()
		
con.commit()