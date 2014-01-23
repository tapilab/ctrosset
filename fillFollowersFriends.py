from twython import Twython
import sqlite3 as lite
import sys


APP_KEY = 'ORjeiD5wdaUT30yo8r8WTg'
APP_SECRET = '1QVwIagGofI3r597nExmir61Y0wP9mbG8Z9ko6ILb0'


twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()


twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

con = lite.connect('database.sqlite')
with con:
	con.row_factory = lite.Row
	cur = con.cursor()
	
	cur.execute("SELECT * FROM Profiles")
	rows = cur.fetchall()
	
	for row in rows:
		cur2 = con.cursor()
		cur2.execute("SELECT Count(*) FROM Users WHERE idUser=" + str(row["idFollower"]))
		
		numberOfRows = cur2.fetchone()[0]
		if(numberOfRows==0):
			print row["idFollower"]
			friends = twitter.get_friends_ids(user_id = row["idFollower"])
			for friends_id in friends['ids']:
				with con:
					cur3 = con.cursor()
					cur3.execute("INSERT INTO Users VALUES('" + str(row["idFollower"]) + "','" + str(friends_id) + "')")
					
	
con.close()