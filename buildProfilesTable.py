import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix

execfile('loadConfig.py')

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

i=0


cur = con.cursor()
cur.execute("SELECT * FROM Profiles GROUP BY idProfile")
rows = cur.fetchall()

for row in rows:
	print i
	cur2 = con.cursor()
	cur2.execute("INSERT INTO ProfilesIds VALUES('','','"+str(i)+"','"+str(row['idProfile'])+"')")
	i+=1
	
	
con.commit()
con.close()