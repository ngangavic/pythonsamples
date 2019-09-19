#display databases
import demo_mysql_connector
cursor = demo_mysql_connector.database.cursor()

cursor.execute("SHOW DATABASES")

for x in cursor:
  print(x)