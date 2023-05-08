import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Izhar"
)
print(mydb)
cur = mydb.cursor()
print(cur)
# Code to Create DataBase in Python
cur.execute("CREATE DATABASE IzharDB")


