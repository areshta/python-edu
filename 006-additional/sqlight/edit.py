import sqlite3
import os
from tmp_db import tmp_db_path

con = sqlite3.connect(tmp_db_path())

cur = con.cursor()

#delete row that was created with db
cur.execute("DELETE FROM stocks WHERE symbol = 'RHAT'")

# Insert a row of data
cur.execute("INSERT INTO stocks (date, trans, symbol, qty, price) VALUES ('2006-03-28', 'BUY', 'IBM', 1000, 45.0)")
cur.execute("INSERT INTO stocks (date, trans, symbol, qty, price) VALUES ('2006-04-06', 'SELL', 'IBM', 500, 53.0)")
cur.execute("INSERT INTO stocks (date, trans, symbol, qty, price) VALUES ('2006-04-05', 'BUY', 'MSFT', 1000, 72.0)")
# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()

print("DB is edited.")