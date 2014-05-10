1 - Install needed libraries
----
	twython
	sqlite3
	scikit-learn

2 - Fill foobar.config file
----

3 - Create the database schema 
----
(ignore next database commands if you do so)

	CREATE TABLE Profiles(idProfile NUMERIC, idFollower NUMERIC);
	CREATE INDEX indexProfiles on Profiles(idFollower ASC);
	CREATE TABLE Users(idUser NUMERIC, idFriend NUMERIC);
	CREATE INDEX IndexUser ON Users(idUser ASC);
	CREATE INDEX IndexFriends ON Users(idFriend ASC);
	CREATE TABLE Friends (id INTEGER PRIMARY KEY, idFriend NUMERIC, total NUMERIC);
	CREATE INDEX idFriendIndex ON Friends(idFriend ASC);
	CREATE TABLE Matrix(idProfile NUMERIC, idCriteria NUMERIC, coef NUMERIC);
	CREATE INDEX idCriteriaMatrix ON Matrix(idCriteria ASC);
	CREATE TABLE ProfilesIds(Male FLOAT, screenName TEXT, id INTEGER PRIMARY KEY, idProfile NUMERIC);
	CREATE INDEX IndexProfilesIds ON ProfilesIds(idProfile ASC)



4 - Fetch followers of twitter account.
---
**a - Database Table :**
	
	CREATE TABLE Profiles(idProfile NUMERIC, idFollower NUMERIC);
	CREATE INDEX indexProfiles on Profiles(idFollower ASC)

**b - Fill  ToFetch.txt with screen_name :**
	
Ex :

	Adobe
	TigerWoods
	hm

**c - Launch the script : fetchProfile.py**
		
Repeat the script until ToFetch.txt is empty
		

5 - Fetch followers's friends
---
**a - Database Table**
	
	CREATE TABLE Users(idUser NUMERIC, idFriend NUMERIC);
	CREATE INDEX IndexUser ON Users(idUser ASC);
	CREATE INDEX IndexFriends ON Users(idFriend ASC)

**b - Launch the script : fetchFollowersFriends.py**
	
Repeat the script until all followers have been treated. (Schedule a cron task every 16 minutes)
		
6 - Create the Friends dictionary table
---
**a - Database table**

	CREATE TABLE Friends (id INTEGER PRIMARY KEY, idFriend NUMERIC, total NUMERIC);
	CREATE INDEX idFriendIndex ON Friends(idFriend ASC)

**b - Launch the script : buildFriendsTable.py**

7 - Generate the Matrix table
---
**a - Database Table**

	CREATE TABLE Matrix(idProfile NUMERIC, idCriteria NUMERIC, coef NUMERIC);
	CREATE INDEX idCriteriaMatrix ON Matrix(idCriteria ASC)

**b - Launch the script : buildMatrixFromRawDatas.py**
	
8 - Create the Profiles dictionary table
---
**a - Database Table**
	
	CREATE TABLE ProfilesIds(Male FLOAT, screenName TEXT, id INTEGER PRIMARY KEY, idProfile NUMERIC);
	CREATE INDEX IndexProfilesIds ON ProfilesIds(idProfile ASC)

**b - Launch script : buildProfilesTable.py**
	
9 - Fill screenName in Profiles dictionary table
---
**a - Launch script : fillProfilesScreenName.py**
	

10 - Filter the datas
---	
**a - Remove profilesIDs from Friends and Matrix**
	
Launch the script : filterDatabaseBfromA.py
	
**b - Remove columns that appear less than n times**
	
Launch the script : filterMatrixDBMinAppear.py
		
11 - Shift dictionaries IDs
---

**a - Launch the script : shiftDatabaseFriends.py**
	
12 - Load gender demographics into DB
---
**a - Create a file cie.txt with twitter screen name**
	
Example : 

	Adobe
	Tiger
	Microsoft

**b - Create a file male.txt with male %**
	
Example : 

	57.2
	23.1
	81.32

**c - Launch the script : loadGenderDemographicsIntoDb.py**
	
13 - Generate Matrices pickle
---
**a - Launch the script : GenerateXFromDB.py**
	
**b - Launch the script : GenerateYGenderFromDb.py**

**c - Launch the script : GenerateFriendsDicFromDb.py**
	

14 - Compute cross-validation
---
**a - Launch the script : loadCrossValidationGenderFromPickle.py**
	
Output example
=============

Scatter plot :
---
![alt tag](http://imagizer.imageshack.us/v2/640x480q90/842/wu7i.png)

Script output :
---
	Column 0 Corr score : 
	(0.7589398643777906, 1.0938477299437908e-05)
	Column 1 Corr score : 
	(0.75893986437779093, 1.0938477299437772e-05)
	
	
	Column 0 TOP 10 twitter IDs : 
	[u'espn', u'SportsCenter', u'dannypudi', u'alisonbrie', u'ufc', u'danawhite', u'TheRock', u'nranews',,u'KingJames', u'GillianJacobs']
	[4.6639741242375905, 4.4249536094889059, 4.197788527746054, 4.1441647241449191, 3.939465340772681, 3.879895859102239, 3.8114338030340607, 3.588071212213586, 3.4063897185315017, 3.3494893308118283]
	Column 1 TOP 10 twitter IDs : 
	[u'VictoriasSecret', u'CHANEL', u'voguemagazine', u'KimKardashian', u'Burberry', u'TheEllenShow', u'ZooeyDeschanel', u'BritishVogue', u'WWF', u'MichaelKors']
	[8.8899854027565759, 7.6837236677788097, 6.9417159072819166, 6.1803594888925515, 4.7177453287301763, 4.5907904747778865, 4.3061436033869596, 4.1561446468227512, 3.7055174949998002, 3.6148485992880368]
	
	
	TOP 10 ERRORS CIE : 
	[u'hm', u'Greenpeace', u'TigerWoods', u'parksandrecnbc', u'nbccommunity', u'DuckDynastyAE', u'SamsungTVUSA', u'lordemusic', u'NRA', u'RealBenCarson']
	With Values : 
	[23.621380259528312, 21.333128355946968, 19.918321968660251, 19.529278676605927, 18.524504870396662, 15.714633085544676, 15.190264580750764, 14.948364690740899, 14.783643282409486, 13.728289787350832]
	
	
	Column 0 MSE : 
	157.565244494
	Column 1 MSE : 
	157.565244494
