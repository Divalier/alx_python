#!/usr/bin/python3
import sys
import MySQLdb

# take in arguments: mysql username, mysql password, database name, state name searched
mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]
state_name = sys.argv[4]

# connect to MySQL server running on localhost at port 3306
db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=mysql_username,
    passwd=mysql_password,
    db=database_name,
    charset="utf8"
)

# execute SQL query safely using parameterized queries
cur = db.cursor()
sql_query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
params = (state_name,)
cur.execute(sql_query, params)

# fetch all the rows in a list of lists.
rows = cur.fetchall()

# display results
for row in rows:
    print(row)

# close all cursors and databases
cur.close()
db.close()
