#create table in the database
import database_connection
cursor = database_connection.database.cursor()

cursor.execute("CREATE TABLE login (name VARCHAR(255), address VARCHAR(255))")