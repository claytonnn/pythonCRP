import mysql.connector
from mysql.connector import errorcode
try:
	db_connection = mysql.connector.connect(host='acw2033ndw0at1t7.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='wfxiy814wx954zpp', password='s8tg1ctsykwdqbkh', database='a8y2em80lfk86myb')
	print("Database connection made!")
except mysql.connector.Error as error:
	if error.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database doesn't exist")
	elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("User name or password is wrong")
	else:
		print(error)
else:
	db_connection.close()