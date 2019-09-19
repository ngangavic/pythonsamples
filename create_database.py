import demo_mysql_connector
#create database
cursor = demo_mysql_connector.database.cursor()

cursor.execute("CREATE DATABASE pythondb")