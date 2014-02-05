#!/usr/bin/env python

from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError
import sqlite3 as lite
import sys

FILE = ''
DATABASE = ''

APP_KEY = {}
APP_SECRET = {}

foobar = open( "foobar.config", "r" )

i=0
for line in foobar
    line.rstrip('\n')
    line.rstrip()
    elif i==0:
        FILE = line
    elif i==1
        DATABASE = line
    elif i==2:
        APP_KEY = line.split(',')
    elif i==3
        APP_SECRET = line.split(',')
    i++

print "Connecting ..."
twitter = Twython(APP_KEY[0], APP_SECRET[0], oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()


twitter = Twython(APP_KEY[0], access_token=ACCESS_TOKEN)
print "OK"
print "Looking for the first row not treated ..."

con = lite.connect(DATABASE)
with con:
	con.row_factory = lite.Row
	
	file = open(FILE, 'r')
	treatedInFile = file.read()
	file.close()
	
	cur = con.cursor()
#	cur.execute("SELECT * FROM Profiles LIMIT "+treatedInFile+",200")
 	cur.execute("SELECT * FROM Profiles")
	rows = cur.fetchall()
	
	currentAccount = 0
	
	iRow = 1
	treated = int(treatedInFile)
	treatedSave = 0
	
	for row in rows:
		cur2 = con.cursor()
		cur2.execute("SELECT Count(*) FROM Users WHERE idUser=" + str(row["idFollower"]))
		
		if(treated>=0):
			treated+=1
		
		numberOfRows = cur2.fetchone()[0]
		if(numberOfRows==0):
			if(iRow==1 and treated>=0):
				print 'OK, ' + str(treated) + ' rows already treated'
				treatedSave = treated
				treated = -1
			try:
				error = False
				friends = twitter.get_friends_ids(user_id = row["idFollower"])
			except TwythonAuthError:
				error = True
				cur4 = con.cursor()
				cur4.execute("DELETE FROM Users WHERE idUser="+str(row["idFollower"]))
				cur4.execute("DELETE FROM Profiles WHERE idFollower="+str(row["idFollower"]))
			except TwythonRateLimitError:
				error = True
				currentAccount+=1
				if currentAccount == len(APP_KEY):
					print 'Limit excedeed and all accounts have been used, quitting ...'			
					
					file = open(FILE,'w')
					print str(treatedSave+iRow)
					file.write(str(treatedSave+iRow-5))
					file.close()
					sys.exit()
				else:
					print 'Switching account ...'
					twitter = Twython(APP_KEY[currentAccount], APP_SECRET[currentAccount], oauth_version=2)
					ACCESS_TOKEN = twitter.obtain_access_token()
					twitter = Twython(APP_KEY[currentAccount], access_token=ACCESS_TOKEN)
					print 'OK'
			except TwythonError as (e):
				error = True
				cur4 = con.cursor()
				cur4.execute("DELETE FROM Users WHERE idUser="+str(row["idFollower"]))
				cur4.execute("DELETE FROM Profiles WHERE idFollower="+str(row["idFollower"]))

			if 'friends' in locals():
				for friends_id in friends['ids']:
					with con:
						cur3 = con.cursor()
						cur3.execute("INSERT INTO Users VALUES('" + str(row["idFollower"]) + "','" + str(friends_id) + "')")
		
			if(error==False):				
				iRow+=1
				print "Row " + str(iRow) + " treated"
				
con.close()
