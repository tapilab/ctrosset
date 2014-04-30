from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError
import sqlite3 as lite
import sys

execfile('loadConfig.py')


con = lite.connect(DATABASE)
    
con.row_factory = lite.Row


ins = open( "cie.txt", "r" )

profiles = []

		
for line in ins:
	line = line.rstrip('\n').lower()
	USER_NAME = line
	profiles.append(line)
	
i=0

file = open( "male.txt","r")

for line in file:
	line = line.strip('\n')
	cur = con.cursor()
	print "UPDATE ProfilesIds SET Male='"+line+"' WHERE LOWER(screenName)='"+profiles[i]+"'"
	cur.execute("UPDATE ProfilesIds SET Male='"+line+"' WHERE LOWER(screenName)='"+profiles[i]+"'")
	i+=1
	
con.commit()
con.close()