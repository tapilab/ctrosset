import sys

foobar = open("/Users/cyriltrosset/Dropbox/IIT/Special project/ctrosset/foobar.config", "r")
i=0
for line in foobar:
    line=line.rstrip('\n')
    if i==0:
        DATABASE = line
    elif i==1:
        APP_KEY = line.split(',')
    elif i==2:
        APP_SECRET = line.split(',')
    i+=1

foobar.close()
