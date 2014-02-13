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

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

MAX_CIE = 2
MAX_CRITERIAS = 2

def arrayForProfile(idProfile,matrix):
    "Build the array from a twitter profile"
    
    cur2 = con.cursor()
    cur2.execute("SELECT COUNT( * ) FROM Profiles P WHERE P.idProfile = "+str(idProfile))
    numberOfRows = cur2.fetchone()[0]

    cur = con.cursor()
    cur.execute("SELECT idFriend, COUNT( * ) AS total FROM Profiles P JOIN Users U WHERE P.idProfile = "+str(idProfile)+" AND P.idFollower = U.idUser GROUP BY U.idFriend ORDER BY total DESC LIMIT "+str(MAX_CRITERIAS))
    rows = cur.fetchall()
    
    array = []
    
    for criterias in rows:
        array.append(float(criterias['total'])/float(numberOfRows))
    
    matrix.append(array)
    
    return


cur = con.cursor()
cur.execute("SELECT idProfile FROM Profiles GROUP BY idProfile LIMIT "+str(MAX_CIE))
rows = cur.fetchall()

x = []

for profile in rows:
    arrayForProfile(profile["idProfile"],x)

print x

con.close()