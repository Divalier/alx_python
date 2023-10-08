#!/usr/bin/python3
"""this script connects to hbtn_0e_0_usa database, and
list  all states with a name starting with N (upper N)"""
import MySQLdb
import sys
connect = MySQLdb.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2],
        database=sys.argv[3]
)
cursor = connect.cursor()
query = "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
cursor.execute(query)
for row in cursor:
    print(row)
cursor.close()
connect.close()
