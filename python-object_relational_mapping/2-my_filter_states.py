#!/usr/bin/python3
import MySQLdb
import sys
connect = MySQLdb.connect(
        host="localhost", user=sys.argv[1], password=sys.argv[2],
        database=sys.argv[3], port=3306
)
input_name = sys.argv[4]
cursor = connect.cursor()
query = """
    SELECT *
    FROM states
    WHERE name LIKE BINARY '{}%'
    ORDER BY id ASC;
    """.format(input_name)
cursor.execute(query)
for obj in cursor:
    print(obj)
cursor.close()
connect.close()
