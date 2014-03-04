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
cur.execute("SELECT idCriteria FROM Matrix GROUP BY idCriteria HAVING COUNT(*)<50")

rows = cur.fetchall()

i=0

for row in rows:
	cur.execute("DELETE FROM Matrix WHERE idCriteria='"+str(row['idCriteria'])+"'")
	cur.execute("DELETE FROM Friends WHERE save='"+str(row['idCriteria'])+"'")
	print i 
	i+=1
	
con.commit()
con.close()