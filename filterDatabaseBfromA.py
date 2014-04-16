import loadConfig
import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle

FILE = ''
DATABASE = '/Users/cyriltrosset/Desktop/SPECIAL_PROJ_DB/database-50.sqlite'

APP_KEY = {}
APP_SECRET = {}

loadConfig.loadConfig(FILE,DATABASE,APP_KEY,APP_SECRET)

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

cur = con.cursor()
cur.execute("SELECT DISTINCT idProfile FROM Profiles")

rows = cur.fetchall()

for row in rows:
	cur.execute("DELETE FROM Users WHERE idFriend="+str(row['idProfile']))
	cur2 = con.cursor()
	cur2.execute("SELECT save FROM Friends WHERE idFriend="+str(row['idProfile']))
	save = cur2.fetchone()
	
	if save is None:
		print 'Nothing'
	else:
		save = save[0]
		cur.execute("DELETE FROM Matrix WHERE idCriteria="+str(save))
		
	cur.execute("DELETE FROM Friends WHERE idFriend="+str(row['idProfile']))
	print row['idProfile']

con.commit()