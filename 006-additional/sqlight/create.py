#https://docs.python.org/3/library/sqlite3.html
#https://www.sqlitetutorial.net/

#AR: autoincremental primary key is added to example

import sqlite3
import os
from tmp_db import tmp_db_path

db_path = tmp_db_path()
if(os.path.isfile(db_path)):
    os.remove(db_path)

con = sqlite3.connect(db_path)

cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE stocks
               ( id INTEGER PRIMARY KEY AUTOINCREMENT, date text, trans text, symbol text, qty real, price real)''')

# Insert a row of data
cur.execute("INSERT INTO stocks (date, trans, symbol, qty, price) VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

print("DB with one table and ('2006-01-05','BUY','RHAT',100,35.14) row is created.")