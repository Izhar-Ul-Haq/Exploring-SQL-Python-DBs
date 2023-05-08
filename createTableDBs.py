import mysql.connector
# mydb or con is just variable you can use whatever you want
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Izhar",
    database = "izhardb"
    )
cur = mydb.cursor()
print(cur)
tab = ("CREATE TABLE izharTable(title VARCHAR(10), Name varchar(10), University varchar(20), location varchar(15))")
cur.execute(tab)
