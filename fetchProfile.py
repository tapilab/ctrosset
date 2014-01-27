from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError
import sqlite3 as lite
import sys


APP_KEY = 'ehStwg5ZzdSrYHR2m0bw'
APP_SECRET = 'iAXRVcfLvUiHTElQRE7iBlpp4sUvs9QhUPmleg6QIVU'


APP_KEY = 'ORjeiD5wdaUT30yo8r8WTg'
APP_SECRET = '1QVwIagGofI3r597nExmir61Y0wP9mbG8Z9ko6ILb0'

APP_KEY = '9frssTeB76DtFPRc4TdFw'
APP_SECRET = '4FMwg6P1s8oPKwYFjCu73bo212vIjHP8BOBxWzLbc'

APP_KEY = 'fY2pbaHjDvuTQCw907QuA'
APP_SECRET = '7dcB7yjGK76KVJOBAdCJJYRbk5ZdW2ufO4isgByw'


twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()


twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

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
		
	con = lite.connect('database.sqlite')

	for follower_id in followers['ids']:
		with con:
			cur = con.cursor()
			cur.execute("INSERT INTO Profiles VALUES('" + user['id_str'] + "','" + str(follower_id) + "')")

 
con.close()