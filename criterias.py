import sqlite3 as lite
import sys

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

idProfile = 205671915

con = lite.connect(DATABASE)

con.row_factory = lite.Row
	
cur = con.cursor()
cur.execute("SELECT idFriend, COUNT( * ) AS total FROM Profiles P JOIN Users U WHERE P.idProfile = "+str(idProfile)+" AND P.idFollower = U.idUser GROUP BY U.idFriend ORDER BY total DESC LIMIT 0,10")
rows = cur.fetchall()
	
i = 0;
	
for criterias in rows:
	print str(criterias['idFriend']) + " appears : " + str(criterias['total'])
	
con.close()