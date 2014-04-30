import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle

execfile('loadConfig.py')


con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

cur = con.cursor()
cur.execute("SELECT DISTINCT idProfile FROM Profiles")

rows = cur.fetchall()

for row in rows:
    cur.execute("DELETE FROM Users WHERE idFriend="+str(row['idProfile']))
    cur.execute("DELETE FROM Matrix WHERE idCriteria="+str(row['idProfile']))
    cur.execute("DELETE FROM Friends WHERE idFriend="+str(row['idProfile']))
    print row['idProfile']

con.commit()
con.close()