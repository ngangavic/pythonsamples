import mysql.connector

#connect to mysql db
database = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythondb"
)
if database.is_connected():
    print("connected")
else:
    print("connection failed")