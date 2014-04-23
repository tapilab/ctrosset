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


idDelete = input("Type the company's id you want to delete : ")

cur = con.cursor()
cur.execute("DELETE FROM ProfilesIds WHERE id="+str(idDelete))
cur.execute("DELETE FROM Matrix WHERE idProfile="+str(idDelete))
i=0
cur.execute("SELECT * FROM ProfilesIds ORDER BY id")

rows = cur.fetchall()

for row in rows:
    print i
    if(row['id']!=i):
        cur2 = con.cursor()
        cur2.execute("UPDATE ProfilesIds SET id="+str(i)+" WHERE id="+str(row['id']))
        cur2.execute("UPDATE Matrix SET idProfile="+str(i)+" WHERE idProfile="+str(row['id']))
    i = i+1

con.commit()