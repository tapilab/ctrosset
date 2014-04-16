import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle
import loadConfig

FILE = ''
DATABASE = '/Users/cyriltrosset/Desktop/SPECIAL_PROJ_DB/database-50.sqlite'
APP_KEY = {}
APP_SECRET = {}
loadConfig.loadConfig(FILE,DATABASE,APP_KEY,APP_SECRET)

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

cur = con.cursor()
cur.execute("UPDATE Matrix SET idProfile=idProfile-1");
cur.execute("UPDATE ProfilesIds SET id=id-1");
	
con.commit()
con.close()