1 - Fill foobar.config file
----

2 - Create the database schema 
----
(ignore next database commands if you do so)

```CREATE TABLE Profiles(idProfile NUMERIC, idFollower NUMERIC);
CREATE INDEX indexProfiles on Profiles(idFollower ASC);
CREATE TABLE Users(idUser NUMERIC, idFriend NUMERIC);
CREATE INDEX IndexUser ON Users(idUser ASC);
CREATE INDEX IndexFriends ON Users(idFriend ASC);
CREATE TABLE Friends (id INTEGER PRIMARY KEY, idFriend NUMERIC, total NUMERIC);
CREATE INDEX idFriendIndex ON Friends(idFriend ASC);
CREATE TABLE Matrix(idProfile NUMERIC, idCriteria NUMERIC, coef NUMERIC);
CREATE INDEX idCriteriaMatrix ON Matrix(idCriteria ASC);
CREATE TABLE ProfilesIds(Male FLOAT, screenName TEXT, id INTEGER PRIMARY KEY, idProfile NUMERIC);
CREATE INDEX IndexProfilesIds ON ProfilesIds(idProfile ASC)```



3 - Fetch followers of twitter account.
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
		

4 - Fetch followers's friends
---
**a - Database Table**
	
CREATE TABLE Users(idUser NUMERIC, idFriend NUMERIC);
CREATE INDEX IndexUser ON Users(idUser ASC);
CREATE INDEX IndexFriends ON Users(idFriend ASC)

**b - Launch the script : fetchFollowersFriends.py**
	
		Repeat the script until all followers have been treated
		
5 - Create the Friends dictionary table
---
**a - Database table**

CREATE TABLE Friends (id INTEGER PRIMARY KEY, idFriend NUMERIC, total NUMERIC);
CREATE INDEX idFriendIndex ON Friends(idFriend ASC)

**b - Launch the script : buildFriendsTable.py**

6 - Generate the Matrix table
---
**a - Database Table**

CREATE TABLE Matrix(idProfile NUMERIC, idCriteria NUMERIC, coef NUMERIC);
CREATE INDEX idCriteriaMatrix ON Matrix(idCriteria ASC)

**b - Launch the script : buildMatrixFromRawDatas.py**
	
7 - Create the Profiles dictionary table
---
**a - Database Table**
	
CREATE TABLE ProfilesIds(Male FLOAT, screenName TEXT, id INTEGER PRIMARY KEY, idProfile NUMERIC);
CREATE INDEX IndexProfilesIds ON ProfilesIds(idProfile ASC)

**b - Launch script : buildProfilesTable.py**
	
8 - Fill screenName in Profiles dictionary table
---
**a - Launch script : fillProfilesScreenName.py**
	

9 - Filter the datas
---	
**a - Remove profilesIDs from Friends and Matrix**
	
		a_1 - Launch the script : filterDatabaseBfromA.py
	
**b - Remove columns that appear less than n times**
	
		b_1 - Launch the script : filterMatrixDBMinAppear.py
		
10 - Shift dictionaries IDs
---

**a - Launch the script : shiftDatabaseFriends.py**
	
11 - Load gender demographics into DB
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
	
12 - Generate Matrices pickle
---
**a - Launch the script : GenerateXFromDB.py**
	
**b - Launch the script : GenerateYGenderFromDb.py**

**c - Launch the script : GenerateFriendsDicFromDb.py**
	

13 - Compute cross-validation
---
**a - Launch the script : loadCrossValidationGenderFromPickle.py**
	
