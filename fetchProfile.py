from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError
import sqlite3 as lite
import sys


FILE = ''
DATABASE = ''

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

twitter = Twython(APP_KEY[0], APP_SECRET[0], oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()


twitter = Twython(APP_KEY[0], access_token=ACCESS_TOKEN)

ins = open( "ToFetch.txt", "r" )

for line in ins:
	line.rstrip('\n')
	line.rstrip()
	USER_NAME = line
	
	try:
		followers = twitter.get_followers_ids(screen_name = USER_NAME, count = 1000)
	except TwythonRateLimitError:
		print 'stopped at : ' + USER_NAME;
		sys.exit()

	try:
		user = twitter.show_user(screen_name = USER_NAME)
	except TwythonRateLimitError:
		print 'stopped at : ' + USER_NAME;
		sys.exit()
		
	con = lite.connect(DATABASE)

	for follower_id in followers['ids']:
		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO Profiles VALUES('" + user['id_str'] + "','" + str(follower_id) + "')")

con.close()