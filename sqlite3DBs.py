import sqlite3
con = sqlite3.connect("izhardb.db")
print(con)
con.execute("CREATE TABLE student(title, year, score)")
