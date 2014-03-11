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


con = lite.connect(DATABASE)

con.row_factory = lite.Row
	
cur = con.cursor()
cur.execute("SELECT COUNT( * ) FROM Profiles LEFT OUTER JOIN Users ON Profiles.idFollower = Users.idUser WHERE Users.idUser IS NULL ")
numberOfRows = cur.fetchone()[0]
	
print str(numberOfRows);