#!/usr/bin/python3

"""a script that takes in an argument and displays all values in the
    'states' table of hbtn_0e_0_usa where 'name' matches the argument.
    script take 4 arguments: mysql username, mysql password, database
    name and state name searched
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM states\
            WHERE name LIKE '{:s}'\
                ORDER BY states.id ASC".format(argv[4]))

    query_re = cur.fetchall()
    for row in query_re:
        print(row)

    cur.close()
    conn.close()
