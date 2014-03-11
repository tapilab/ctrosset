#!/usr/bin/env python

from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError
import sqlite3 as lite
import sys
import loadConfig

FILE = ''
DATABASE = ''
APP_KEY = {}
APP_SECRET = {}
loadConfig.loadConfig(FILE,DATABASE,APP_KEY,APP_SECRET)

print "Connecting ..."
twitter = Twython(APP_KEY[0], APP_SECRET[0], oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()


twitter = Twython(APP_KEY[0], access_token=ACCESS_TOKEN)
print "OK"
print "Looking for the first row not treated ..."

con = lite.connect(DATABASE)

con.row_factory = lite.Row
	
cur = con.cursor()
cur.execute("SELECT Profiles.idFollower FROM Profiles LEFT OUTER JOIN Users on Profiles.idFollower = Users.idUser WHERE Users.idUser is null GROUP BY Profiles.idFollower LIMIT 0,100")
rows = cur.fetchall()
	
currentAccount = 0
	
iRow = 1
	
for row in rows:
    cur2 = con.cursor()
    cur2.execute("SELECT Count(*) FROM Users WHERE idUser=" + str(row["idFollower"]))
		
    numberOfRows = cur2.fetchone()[0]
    if(numberOfRows==0):
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
                
                con.commit()
                con.close()
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
                    cur3 = con.cursor()
                    cur3.execute("INSERT INTO Users VALUES('" + str(row["idFollower"]) + "','" + str(friends_id) + "')")
		
        if(error==False):
            iRow+=1
            print "Row " + str(iRow) + " treated"

con.commit()
con.close()
