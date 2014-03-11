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

idProfile = 19039286;

con = lite.connect(DATABASE)

con.row_factory = lite.Row
	
cur = con.cursor()
cur.execute("SELECT * FROM Profiles WHERE idProfile="+str(idProfile))
rows = cur.fetchall()
	
i = 0;
	
for profile in rows:
	cur2 = con.cursor()
	cur2.execute("SELECT * FROM Users WHERE idUser="+str(profile['idFollower']))
	rows2 = cur2.fetchall()
		
	for user in rows2:
		i+=1
		print i
		cur3 = con.cursor()
		cur3.execute("SELECT total FROM Arrays WHERE idProfile="+str(idProfile)+" AND idCriteria="+str(user['idFriend']))
		
		total = cur3.fetchone()
			
		if(total is None):
			cur4 = con.cursor()
			cur4.execute("INSERT INTO Arrays VALUES('"+str(idProfile)+"','"+str(user['idFriend'])+"','1')")
		elif(total['total']>0):
			cur4 = con.cursor()
			cur4.execute("UPDATE Arrays SET total = "+str(total['total']+1)+" WHERE idProfile="+str(idProfile)+" AND idCriteria="+str(user['idFriend']))
		else:
			cur4 = con.cursor()
			cur4.execute("INSERT INTO Arrays VALUES('"+str(idProfile)+"','"+str(user['idFriend'])+"','1'")

con.commit()
con.close()