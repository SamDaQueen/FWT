import sqlite3
import mysql.connector

def opendb():

	con = mysql.connector.connect(
	  host="localhost",
	  user="sssm_admin",
	  passwd="Bt(c@245",
	  database="sssm",

	)

	#con = sqlite3.connect('sssm.db') #the database connector
	cur = con.cursor() #the database cursor

	return con,cur

def Query(query):

	con, cur = opendb()

	cur.execute("""CREATE TABLE IF NOT EXISTS QUERIES ( DateTime TEXT, Firstname TEXT, Lastname TEXT ,Email TEXT, Mobile TEXT, Query TEXT);""")
	con.commit()

	cur.execute("INSERT INTO QUERIES VALUES(%s,%s,%s,%s,%s,%s)",(query['date_time'],query['first_name'],
		query['last_name'],query['email'],query['mobile'],query['query']))
	con.commit()

	con.close()

def Member(member):

	con, cur = opendb()
	
	cur.execute("""CREATE TABLE IF NOT EXISTS MEMBERSD(DateTime TEXT, Firstname TEXT,
	Lastname TEXT ,Email TEXT, Birthdate TEXT, Address TEXT,Occupation TEXT,
	Mobile TEXT,Landline TEXT,Office TEXT,fm1_name TEXT, fm1_relation TEXT,
	fm1_birth_date TEXT, fm2_name TEXT, fm2_relation TEXT,fm2_birth_date TEXT,
	fm3_name TEXT, fm3_relation TEXT, fm3_birth_date TEXT, fm4_name TEXT,
	fm4_relation TEXT,fm4_birth_date TEXT, fm5_name TEXT,fm5_relation TEXT,
	fm5_birth_date TEXT);""")
	con.commit()

	cur.execute("INSERT INTO MEMBERS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
		(member['date_time'],member['first_name'],member['last_name'],member['email'],
		member['birth_date'],member['address'],member['occupation'],member['mobile'],
		member['landline'],member['office'],member['fm1_name'],member['fm1_relation'],
		member['fm1_birth_date'],member['fm2_name'],member['fm2_relation'],
		member['fm2_birth_date'],member['fm3_name'],member['fm3_relation'],
		member['fm3_birth_date'],member['fm4_name'],member['fm4_relation'],
		member['fm4_birth_date'],member['fm5_name'],member['fm5_relation'],
		member['fm5_birth_date']))
	con.commit()	

	con.close()

def Booking(booking):

	con, cur = opendb()

	cur.execute("""CREATE TABLE IF NOT EXISTS BOOKINGS(DateTime TEXT, Firstname TEXT,
	Lastname TEXT ,Email TEXT,Mobile TEXT, Address TEXT,CheckInDate TEXT,
	CheckInTimeHour TEXT, CheckInTimeMinute TEXT, CheckOutDate TEXT,ChechOutTimeHour TEXT,
	CheckOutTimeMinute TEXT,NumberOfPeople TEXT,RoomType TEXT);""")
	con.commit()

	print("INSERT INTO BOOKINGS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
		booking['date_time'],booking['first_name'],booking['last_name'],booking['email'],booking['mobile'],
		booking['address'],booking['check-in-date'],booking['check-in-time-hour'],
		booking['check-in-time-minute'],booking['check-out-date'],booking['check-out-time-hour'],
		booking['check-out-time-minute'],booking['no-of-people'],booking['room-type'])

	cur.execute("INSERT INTO BOOKINGS VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
		(booking['date_time'],booking['first_name'],booking['last_name'],booking['email'],booking['mobile'],
		booking['address'],booking['check-in-date'],booking['check-in-time-hour'],
		booking['check-in-time-minute'],booking['check-out-date'],booking['check-out-time-hour'],
		booking['check-out-time-minute'],booking['no-of-people'],booking['room-type']))
	con.commit()

	con.close()

def Admin(admin):
	pass


