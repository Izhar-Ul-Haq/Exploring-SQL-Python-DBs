# Inserting Multiples Values using Python
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Izhar",
    database = "izhardb"
)
# Creating Cursor Object
cur = mydb.cursor()
print(cur)

s = "INSERT INTO izhartable (title, Name, University, location) VALUES(%s, %s, %s, %s)"
recs = [("HouseWife", "Sumaira", "Peshawar Uni", "Peshawar"),
        ("Teacher", "Linda", "Texas", "USA"),
        ("Professor", "Suman", "Namal", "Mianwali")
        ]
cur.executemany(s, recs)
mydb.commit()

