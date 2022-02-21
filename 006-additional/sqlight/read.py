#https://docs.python.org/3/library/sqlite3.html

import sqlite3
import os
from tmp_db import tmp_db_path

con = sqlite3.connect(tmp_db_path())

cur = con.cursor()

#I inserted rowid - primary key
for row in cur.execute('SELECT * FROM stocks ORDER BY price'):
        print(row)

con.close()

