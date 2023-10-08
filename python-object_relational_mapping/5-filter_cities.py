#!/usr/bin/python3
"""this script takes in the name of a state as
an argument and lists all cities of that state"""
import MySQLdb
import sys
connect = MySQLdb.connect(host="localhost", user=sys.argv[1],
                          password=sys.argv[2], port=3306, database=sys.argv[3]
                          )
cursor = connect.cursor()
cursor.execute("""
        SELECT cities.name
        FROM cities
        INNER JOIN states ON states.id=cities.state_id
        WHERE states.name=%s""", (sys.argv[4],))
rows = cursor.fetchall()
tmp = list(row[0] for row in rows)
print(*tmp, sep=", ")
cursor.close()
connect.close()
