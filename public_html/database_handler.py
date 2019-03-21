import sqlite3

def opendb():

	con = sqlite3.connect('sssm.db') #the database connector
	cur = con.cursor() #the database cursor

	return con,cur

def Query(query):

	con, cur = opendb()

	cur.execute("CREATE TABLE IF NOT EXISTS QUERYS('DateTime' TEXT, 'Firstname' TEXT, 'Lastname' TEXT ,'Email' TEXT, 'Mobile' TEXT, 'Query' TEXT);")
	con.commit()

	cur.execute("INSERT INTO QUERYS VALUES(?,?,?,?,?,?)",(query['date_time'],query['first_name'],query['last_name'],query['email'],query['mobile'],query['query']))
	con.commit()

def Member(member):

	con, cur = opendb()
	
	cur.execute("""CREATE TABLE IF NOT EXISTS MEMBERS('DateTime' TEXT, 'Firstname' TEXT,
	'Lastname' TEXT ,'Email' TEXT, 'Birthdate' TEXT, 'Address' TEXT,'Occupation' TEXT,
	'Mobile' TEXT,'Landline' TEXT,'Office' TEXT, 'fm1-name' TEXT, 'fm1-relation' TEXT,
	'fm1-birth-date' TEXT, 'fm2-name' TEXT, 'fm2-relation' TEXT,'fm2-birth-date' TEXT,
	'fm3-name' TEXT, 'fm3-relation' TEXT,'fm3-birth-date' TEXT, 'fm4-name' TEXT,
	'fm4-relation' TEXT,'fm4-birth-date' TEXT, 'fm5-name' TEXT,'fm5-relation' TEXT,
	'fm5-birth-date' TEXT);""")
	con.commit()

	cur.execute("INSERT INTO MEMBERS VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
		(member['date_time'],member['first_name'],member['last_name'],member['email'],
		member['birth_date'],member['address'],member['occupation'],member['mobile'],
		member['landline'],member['office'],member['fm1-name'],member['fm1-relation'],
		member['fm1-birth-date'],member['fm2-name'],member['fm2-relation'],
		member['fm2-birth-date'],member['fm3-name'],member['fm3-relation'],
		member['fm3-birth-date'],member['fm4-name'],member['fm4-relation'],
		member['fm4-birth-date'],member['fm5-name'],member['fm5-relation'],
		member['fm5-birth-date']))
	con.commit()	 

