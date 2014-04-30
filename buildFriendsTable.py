import sqlite3 as lite
import sys

execfile('loadConfig.py')

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

cur = con.cursor()

cur.execute("INSERT INTO Friends SELECT NULL,idFriend,COUNT(*) From Users GROUP BY idFriend")


con.commit()
con.close()