from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError
import sqlite3 as lite
import sys
import loadConfig

FILE = ''
DATABASE = '/Users/cyriltrosset/Desktop/SPECIAL_PROJ_DB/database-50.sqlite'
APP_KEY = {}
APP_SECRET = {}
loadConfig.loadConfig(FILE,DATABASE,APP_KEY,APP_SECRET)


con = lite.connect(DATABASE)
    
con.row_factory = lite.Row


ins = open( "cie.txt", "r" )

profiles = []

		
for line in ins:
	line = line.rstrip('\n').lower()
	USER_NAME = line
	profiles.append(line)
	
i=0
file = open( "18-24.txt","r")
for line in file:
	line = line.strip('\n')
	cur = con.cursor()
	cur.execute("UPDATE ProfilesIds SET AgeOne='"+line+"' WHERE LOWER(screenName)='"+profiles[i]+"'")
	i+=1

i=0
file = open( "25-34.txt","r")
for line in file:
	line = line.strip('\n')
	cur = con.cursor()
	cur.execute("UPDATE ProfilesIds SET AgeTwo='"+line+"' WHERE LOWER(screenName)='"+profiles[i]+"'")
	i+=1

i=0
file = open( "35-44.txt","r")
for line in file:
	line = line.strip('\n')
	cur = con.cursor()
	cur.execute("UPDATE ProfilesIds SET AgeThree='"+line+"' WHERE LOWER(screenName)='"+profiles[i]+"'")
	i+=1

i=0
file = open( "45-54.txt","r")
for line in file:
	line = line.strip('\n')
	cur = con.cursor()
	cur.execute("UPDATE ProfilesIds SET AgeFour='"+line+"' WHERE LOWER(screenName)='"+profiles[i]+"'")
	i+=1

i=0
file = open( "55-64.txt","r")
for line in file:
	line = line.strip('\n')
	cur = con.cursor()
	cur.execute("UPDATE ProfilesIds SET AgeFive='"+line+"' WHERE LOWER(screenName)='"+profiles[i]+"'")
	i+=1

i=0
file = open( "65+.txt","r")
for line in file:
	line = line.strip('\n')
	cur = con.cursor()
	cur.execute("UPDATE ProfilesIds SET AgeSix='"+line+"' WHERE LOWER(screenName)='"+profiles[i]+"'")
	i+=1
	
con.commit()
con.close()