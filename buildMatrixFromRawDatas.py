import sqlite3 as lite
import sys

execfile('loadConfig.py')

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

cur = con.cursor()
cur.execute("SELECT COUNT(*) FROM Friends")
numberOfCriterias = cur.fetchone()[0]

print numberOfCriterias

cur = con.cursor()
cur.execute("SELECT idProfile FROM Profiles GROUP BY idProfile")
rows = cur.fetchall()

iCie = -1

for profile in rows:
    iCie+=1
    print iCie;
    cur2 = con.cursor()
    cur2.execute("SELECT COUNT( * ) FROM Profiles P WHERE P.idProfile = "+str(profile['idProfile']))
    numberOfRows = cur2.fetchone()[0]
    
    cur4 = con.cursor()
    cur4.execute("SELECT idFriend, COUNT( * ) AS total FROM Profiles P JOIN Users U WHERE P.idProfile = "+str(profile['idProfile'])+" AND P.idFollower = U.idUser GROUP BY U.idFriend ORDER BY total DESC")
    rows = cur4.fetchall()
    
    for criterias in rows:
        value = (float(criterias['total'])/float(numberOfRows))
        cur5 = con.cursor()
        cur5.execute("INSERT INTO Matrix VALUES ('"+str(profile['idProfile'])+"','"+str(criterias['idFriend'])+"','"+str(value)+"')")

con.commit()
con.close()