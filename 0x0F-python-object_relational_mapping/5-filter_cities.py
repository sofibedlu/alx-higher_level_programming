#!/usr/bin/python3

"""script that takes in the name of a state as an argument and lists
    all 'cities' of that state, using the database 'hbtn_0e_4_usa'
    -script take 4 arguments: mysql username, mysql password,
    database name and state name (SQL injection free!)
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset='utf8')
    cur = conn.cursor()

    cur.execute("SELECT cities.id, cities.name, states.name\
                FROM cities INNER JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC\
                ", (argv[4],))

    rows = cur.fetchall()

    i = 1
    for row in rows:
        print(row[1], end="")
        if len(rows) > i:
            print(", ", end="")
        i = i + 1
    print("")

    cur.close()
    conn.close()
