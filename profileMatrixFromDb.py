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
cur.execute("SELECT * FROM ProfilesIds")

rows = cur.fetchall()

profilesMatrix = lil_matrix((132,1))

for row in rows:
	profilesMatrix[row['id'],0] = row['idProfile']
	
f = open('profilesMatrix.pkl','wb')
cPickle.dump(profilesMatrix,f,-1)
f.close()