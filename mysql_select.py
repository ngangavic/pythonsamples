#select data from database

import database_connection;

cursor = database_connection.database.cursor()
cursor.execute("SELECT * FROM login")
result = cursor.fetchall()
for x in result:
  print(x)