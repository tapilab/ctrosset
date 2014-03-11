import sqlite3 as lite
import sys
import loadConfig

FILE = ''
DATABASE = ''
APP_KEY = {}
APP_SECRET = {}
loadConfig.loadConfig(FILE,DATABASE,APP_KEY,APP_SECRET)

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

cur = con.cursor()
con.row_factory = lite.Row

cur.execute("INSERT INTO Friends SELECT NULL,idFriend,COUNT(*) From Users GROUP BY idFriend")



con.commit()
con.close()