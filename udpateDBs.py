import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Izhar",
    database = "izhardb"
)

cur = mydb.cursor()
print(cur)

s = "UPDATE izhartable SET Name = 'OOSama' WHERE Name = 'Sanam'"

# s = "UPDATE izhartable SET Name = Sanam WHERE Name = Suman"
cur.execute(s)
mydb.commit()
# c = "SELECT * from izhartable"
# cur.execute(c)
# cur.fetchall()