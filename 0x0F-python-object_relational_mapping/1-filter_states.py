#!/usr/bin/python3

"""script that lists all 'states' with a 'name' starting with 'N' (upper N)
    from the database 'hbtn_0e_0_usa'
    script take 3 arguments: mysql username, mysql password
    and database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_re = cur.fetchall()
    for row in query_re:
        if row[1][0] == 'N':
            print(row)

    cur.close()
    conn.close()
