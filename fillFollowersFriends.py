from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError
import sqlite3 as lite
import sys

APP_KEY = {}
APP_SECRET = {}

APP_KEY[0] = '9frssTeB76DtFPRc4TdFw'
APP_SECRET[0] = '4FMwg6P1s8oPKwYFjCu73bo212vIjHP8BOBxWzLbc'

APP_KEY[1] = 'ORjeiD5wdaUT30yo8r8WTg'
APP_SECRET[1] = '1QVwIagGofI3r597nExmir61Y0wP9mbG8Z9ko6ILb0'

APP_KEY[2] = 'fY2pbaHjDvuTQCw907QuA'
APP_SECRET[2] = '7dcB7yjGK76KVJOBAdCJJYRbk5ZdW2ufO4isgByw'

print "Connection ..."
twitter = Twython(APP_KEY[0], APP_SECRET[0], oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()


twitter = Twython(APP_KEY[0], access_token=ACCESS_TOKEN)
print "OK"
print "Looking for the first row not treated ..."

con = lite.connect('database.sqlite')
with con:
	con.row_factory = lite.Row
	cur = con.cursor()
	
	cur.execute("SELECT * FROM Profiles")
	rows = cur.fetchall()
	
	currentAccount = 0
	
	iRow = 1;
	
	for row in rows:
		cur2 = con.cursor()
		cur2.execute("SELECT Count(*) FROM Users WHERE idUser=" + str(row["idFollower"]))
		
		numberOfRows = cur2.fetchone()[0]
		if(numberOfRows==0):
			if(iRow==1):
				print 'OK'
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
					sys.exit()
				else:
					print 'Switching account ...'
					twitter = Twython(APP_KEY[currentAccount], APP_SECRET[currentAccount], oauth_version=2)
					ACCESS_TOKEN = twitter.obtain_access_token()
					twitter = Twython(APP_KEY[currentAccount], access_token=ACCESS_TOKEN)
					print 'OK'

			if 'friends' in locals():
				for friends_id in friends['ids']:
					with con:
						cur3 = con.cursor()
						cur3.execute("INSERT INTO Users VALUES('" + str(row["idFollower"]) + "','" + str(friends_id) + "')")
		
			if(error==False):				
				iRow+=1
				print "Row " + str(iRow) + " treated"
	
con.close()