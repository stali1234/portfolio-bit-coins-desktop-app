# serverless database
import sqlite3

# create connection with database
con = sqlite3.connect("mycompany.db")
cobj = con.cursor()

# cobj.execute("CREATE TABLE employee(id INTEGER PRIMARY KEY, name TEXT , salary REAL, department TEXT, position TEXT)")
cobj.execute(
    "INSERT INTO employee VALUES(?,?,?,?,?)", (2, "stalin", 7500, "python", "developer")
)
con.commit()
cobj.close()
con.close()