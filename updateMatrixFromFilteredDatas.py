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
cur.execute("SELECT save,id FROM Friends WHERE id!=save ORDER BY id ASC")

rows = cur.fetchall()

for row in rows:

	cur.execute("UPDATE Matrix SET idCriteria='"+str(row['id'])+"' WHERE idCriteria='"+str(row['save'])+"'")
	cur.execute("UPDATE Friends SET save='"+str(row['id'])+"' WHERE save='"+str(row['save'])+"'")
	print str(row['id'])
	if(row['id']%500==0):
		con.commit()
		
con.commit()