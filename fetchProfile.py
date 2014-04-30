from twython import Twython, TwythonError, TwythonAuthError, TwythonRateLimitError
import sqlite3 as lite
import sys

execfile('loadConfig.py')

twitter = Twython(APP_KEY[0], APP_SECRET[0], oauth_version=2)
ACCESS_TOKEN = twitter.obtain_access_token()


twitter = Twython(APP_KEY[0], access_token=ACCESS_TOKEN)

ins = open("ToFetch.txt", "r" )

con = lite.connect(DATABASE)

for line in ins:
    line = line.rstrip('\n')
    line = line.rstrip()
    USER_NAME = line
    
    try:
        followers = twitter.get_followers_ids(screen_name = USER_NAME, count = 1000)
    except TwythonRateLimitError:
        print "API Limit reached"
        sys.exit()

    try:
        user = twitter.show_user(screen_name = USER_NAME)
    except TwythonRateLimitError:
        print "API Limit reached"
        sys.exit()

    for follower_id in followers['ids']:
        with con:
            cur = con.cursor()
            cur.execute("INSERT INTO Profiles VALUES('" + user['id_str'] + "','" + str(follower_id) + "')")

    with open('ToFetch.txt', 'r') as fin:
        data = fin.read().splitlines(True)
    with open('ToFetch.txt', 'w') as fout:
        fout.writelines(data[1:])
    print USER_NAME + " fetched"

con.close()