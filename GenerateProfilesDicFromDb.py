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
cur.execute("SELECT * FROM ProfilesIds")

rows = cur.fetchall()

profilesMatrix = lil_matrix((132,1))

for row in rows:
	profilesMatrix[row['id'],0] = row['idProfile']
	
f = open('profilesMatrix.pkl','wb')
cPickle.dump(profilesMatrix,f,-1)
f.close()