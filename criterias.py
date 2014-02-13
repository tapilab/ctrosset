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

def arrayForProfile(idProfile):
    "Build the array from a twitter profile"
    
    con = lite.connect(DATABASE)

    con.row_factory = lite.Row
    
    cur2 = con.cursor()
    cur2.execute("SELECT COUNT( * ) FROM Profiles P WHERE P.idProfile = "+str(idProfile))
    numberOfRows = cur2.fetchone()[0]
    
    print numberOfRows

    cur = con.cursor()
    cur.execute("SELECT idFriend, COUNT( * ) AS total FROM Profiles P JOIN Users U WHERE P.idProfile = "+str(idProfile)+" AND P.idFollower = U.idUser GROUP BY U.idFriend ORDER BY total DESC LIMIT 10")
    rows = cur.fetchall()
    
    myArray = []
    
    for criterias in rows:
        print str(criterias["idFriend"])
        myArray.append(float(criterias['total'])/float(numberOfRows))

    con.close()
    
    return myArray


for value in arrayForProfile(270533441):
    print str(value) + ", "

