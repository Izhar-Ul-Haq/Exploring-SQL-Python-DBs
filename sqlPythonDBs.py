import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Izhar",
  database="Izhar_Khan_Khattak_DB"
)

print(mydb)
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE Izhar_Khan_Khattak_DB")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Izhar Khan Khattak", "Highway 20")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
