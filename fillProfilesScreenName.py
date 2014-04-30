#!/usr/bin/env python

from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError
import sqlite3 as lite
import sys
from scipy.sparse import lil_matrix
import cPickle

execfile('loadConfig.py')

print "Connecting ..."
twitter = Twython(APP_KEY[0], APP_SECRET[0], oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()

twitter = Twython(APP_KEY[0], access_token=ACCESS_TOKEN)

con = lite.connect(DATABASE)
    
con.row_factory = lite.Row

currentAccount = 0

cur = con.cursor()
cur.execute("SELECT * FROM ProfilesIds WHERE screenName=''")
rows = cur.fetchall()
		
for row in rows:
	line.rstrip('\n')
	line.rstrip()
	USER_ID = row['idProfile']
	
	user = 0
	
	try:
		user = twitter.show_user(user_id = USER_ID)
	except TwythonRateLimitError:
		if currentAccount == len(APP_KEY):
			print 'Limit excedeed and all accounts have been used, quitting ...'
			con.commit()
			con.close()
			sys.exit()
		else:
			print 'Switching account ...'
			currentAccount+=1
			twitter = Twython(APP_KEY[currentAccount], APP_SECRET[currentAccount], oauth_version=2)
			ACCESS_TOKEN = twitter.obtain_access_token()
			twitter = Twython(APP_KEY[currentAccount], access_token=ACCESS_TOKEN)
			print 'OK'
			user = twitter.show_user(user_id = USER_ID)
			
	print "UPDATE ProfilesIds SET screenName='" + user['screen_name'] + "' WHERE idProfile='" + user['id_str'] + "'"
		
	cur = con.cursor()
	cur.execute("UPDATE ProfilesIds SET screenName='" + user['screen_name'] + "' WHERE idProfile='" + user['id_str'] + "'");

con.commit()
con.close()
	