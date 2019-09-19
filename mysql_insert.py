#insert data into login table

import database_connection

cursor = database_connection.database.cursor();
sql = "INSERT INTO login (name, address) VALUES (%s, %s)"
val = [
    ("Nuhu", "Kibaoni"),
    ("Kakak","Kibaoni"),
    ("Mark","Mariakani")
]
cursor.executemany(sql, val)
database_connection.database.commit()