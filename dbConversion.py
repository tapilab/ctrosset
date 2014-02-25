import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix

APP_KEY = {}
APP_SECRET = {}

foobar = open( "foobar.config", "r" )

i=0
for line in foobar:
    line=line.rstrip('\n')
    if i==0:
        FILE = line
    elif i==1:
        DATABASE = line
    elif i==2:
        APP_KEY = line.split(',')
    elif i==3:
        APP_SECRET = line.split(',')
    i+=1
    
foobar.close()

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

i=1


cur = con.cursor()
cur.execute("SELECT * FROM Profiles WHERE idProfile<140")
rows = cur.fetchall()

for row in rows:
	print i
	cur2 = con.cursor()
	cur2.execute("INSERT INTO ProfilesIds VALUES('"+str(row['idProfile'])+"','"+str(row['idFollower'])+"')")
	cur2.execute("DELETE FROM Profiles WHERE idProfile="+str(row['idProfile']))
	i+=1
	
	
con.commit()
con.close()