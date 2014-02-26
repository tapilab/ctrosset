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


ins = open( "cie.txt", "r" )

profiles = []

		
for line in ins:
	line = line.rstrip('\n').lower()
	USER_NAME = line
	profiles.append(line)
	
i=0

file = open( "Male.txt","r")

for line in file:
	line = line.strip('\n')
	cur = con.cursor()
	print "UPDATE ProfilesIds SET Male='"+line+"' WHERE LOWER(screenName)='"+profiles[i]+"'"
	cur.execute("UPDATE ProfilesIds SET Male='"+line+"' WHERE LOWER(screenName)='"+profiles[i]+"'")
	i+=1
	
con.commit()
con.close()