import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle
import loadConfig

FILE = ''
DATABASE = ''
APP_KEY = {}
APP_SECRET = {}
loadConfig.loadConfig(FILE,DATABASE,APP_KEY,APP_SECRET)

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

def updateDB(i,delta):
	"function_docstring"
   
	j=0
   
	for val in range(i+1,2521967):
   		cur=con.cursor()
   		cur.execute("SELECT 1 FROM Friends WHERE id="+str(val))
   		result = cur.fetchone()
   		
   		if(val%10000==0):
   			con.commit()
   			print "SAVE"
	
   		if result==None:
   			j=val
   			cur.execute("UPDATE Friends SET id=id-"+str(delta)+" WHERE id>"+str(i)+" AND id<"+str(j))
   			print j
   			return j
    
   	return 2521968


i=0
for val in range(1,2521967):
	cur=con.cursor()
	cur.execute("SELECT 1 FROM Friends WHERE id="+str(val))
	result = cur.fetchone()
	
	if result==None:
		i=val
		break

delta=1
while(i<2521968):
	i = updateDB(i,delta)
	delta+=1
	
con.commit()