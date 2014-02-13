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


con = lite.connect(DATABASE)

con.row_factory = lite.Row
	
cur = con.cursor()
cur.execute("SELECT COUNT( * ) FROM Profiles LEFT OUTER JOIN Users ON Profiles.idFollower = Users.idUser WHERE Users.idUser IS NULL ")
numberOfRows = cur.fetchone()[0]
	
print str(numberOfRows);