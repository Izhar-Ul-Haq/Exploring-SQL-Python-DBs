import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Izhar",
    database = "izhardb"
)
cur = mydb.cursor()
print(cur)
s = "SELECT * from izhartable"
cur.execute(s)
result = cur.fetchall()
for rec in result:
    print(rec)
