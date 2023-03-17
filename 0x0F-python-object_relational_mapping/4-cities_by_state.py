#!/usr/bin/python3

"""scripts that lists all 'cities' from the database 'hbtn_0e_4_usa'
    -the script take 3 arguments: mysql username, mysql password
    and database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states\
                ON cities.state_id = states.id\
                ORDER BY cities.id ASC")

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()
