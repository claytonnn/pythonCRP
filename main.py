from datetime import date
import mysql.connector

db_connection = mysql.connector.connect(host='acw2033ndw0at1t7.cbetxkdyhwsb.us-east-1.rds.amazonaws.com', user='wfxiy814wx954zpp', password='s8tg1ctsykwdqbkh', database='a8y2em80lfk86myb')
cursor = db_connection.cursor()
sql = ("SELECT idTESTE, TESTEcol FROM teste")
cursor.execute(sql)

for (idTESTE, TESTEcol) in cursor:
    print(idTESTE, TESTEcol)
print("\n")

cursor.close()
db_connection.commit()
db_connection.close()