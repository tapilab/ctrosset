import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle

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

cur = con.cursor()
cur.execute("SELECT * FROM Friends")

rows = cur.fetchall()

friendsMatrix = lil_matrix((numberOfCriterias+1,1))

for row in rows:
	friendsMatrix[row['id'],0] = row['idFriend']
	
f = open('friendsMatrix.pkl','wb')
cPickle.dump(friendsMatrix,f,-1)
f.close()