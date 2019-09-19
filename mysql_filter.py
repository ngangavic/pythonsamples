#select with filter

import database_connection;

cursor = database_connection.database.cursor()
sql = "SELECT * FROM login WHERE address = %s"
adr = ("Kibaoni", )

cursor.execute(sql, adr)

result = cursor.fetchall()

for x in result:
  print(x)