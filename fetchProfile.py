from twython import Twython
import sqlite3 as lite
import sys


APP_KEY = 'ORjeiD5wdaUT30yo8r8WTg'
APP_SECRET = '1QVwIagGofI3r597nExmir61Y0wP9mbG8Z9ko6ILb0'


twitter = Twython(APP_KEY, APP_SECRET, oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()


twitter = Twython(APP_KEY, access_token=ACCESS_TOKEN)

USER_ID = input("Veuillez entrer l'user ID : ")
followers = twitter.get_followers_ids(user_id = USER_ID, count = 1000)

con = lite.connect('database.sqlite')

for follower_id in followers['ids']:
	with con:
		cur = con.cursor()
		cur.execute("INSERT INTO Profiles VALUES('" + str(USER_ID) + "','" + str(follower_id) + "')")

 
con.close()