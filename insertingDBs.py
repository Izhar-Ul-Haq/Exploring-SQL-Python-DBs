import mysql.connector
# mydb or con: you can use whatever you want (For the sake of simplicity)
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Izhar",
    database = "izhardb"
)

cur = mydb.cursor()
print(cur)
s = ("INSERT INTO izhartable(title, Name, University, location) VALUES(%s,%s,%s,%s)")
rec1 = ("Traveler", "Izhar", "VU", "Islamabad")
rec2 = ("CS Student", "Izhar", "VU of Pakistan", "Lahore")
cur.execute(s, rec2)
mydb.commit()


