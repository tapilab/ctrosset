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

cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM Friends")
numberOfCriterias = cur.fetchone()[0]

print numberOfCriterias

matrix = lil_matrix( (200,numberOfCriterias+1) )

cur = con.cursor()
cur.execute("SELECT idProfile FROM Profiles GROUP BY idProfile LIMIT 35,200")
rows = cur.fetchall()

iCie = -1

for profile in rows:
    print "SQL"
    iCie+=1
    cur2 = con.cursor()
    cur2.execute("SELECT COUNT( * ) FROM Profiles P WHERE P.idProfile = "+str(profile['idProfile']))
    numberOfRows = cur2.fetchone()[0]
    
    cur4 = con.cursor()
    cur4.execute("SELECT idFriend, COUNT( * ) AS total FROM Profiles P JOIN Users U WHERE P.idProfile = "+str(profile['idProfile'])+" AND P.idFollower = U.idUser GROUP BY U.idFriend ORDER BY total DESC")
    rows = cur4.fetchall()
    
    i=0
    print "RDY"
    
    for criterias in rows:
        value = (float(criterias['total'])/float(numberOfRows))
        cur3 = con.cursor()
        cur3.execute("SELECT id FROM Friends WHERE idFriend="+str(criterias['idFriend']))
        idFetched = cur3.fetchone()[0]
        print iCie
        print idFetched
        matrix[iCie,idFetched] = value
        i+=1
        print i
        cur5 = con.cursor()
        cur5.execute("INSERT INTO Matrix VALUES ('"+str(profile['idProfile'])+"','"+str(idFetched)+"','"+str(value)+"')")

con.commit()
con.close()