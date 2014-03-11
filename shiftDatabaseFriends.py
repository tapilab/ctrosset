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
cur.execute("SELECT id FROM Friends");

rows = cur.fetchall()

i = 1

for row in rows:
	cur.execute("UPDATE Friends SET id="+str(i)+" WHERE id="+str(row['id']))
	i+=1
	
con.commit()
con.close()