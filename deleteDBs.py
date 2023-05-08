import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Izhar",
    database="izhardb"
)
cur = mydb.cursor()
print(cur)
s = "DELETE from izhartable WHERE title='Professor'";
cur.execute(s)
mydb.commit()