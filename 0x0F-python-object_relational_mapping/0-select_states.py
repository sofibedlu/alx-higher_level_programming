#!/usr/bin/python3

"""a script that lists all 'states' from the database 'hbtn_0e_0_usa'
   script take 3 arguments: mysql username, mysql password and
   database name
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_re = cur.fetchall()

    for state in query_re:
        print(state)

    cur.close()
    conn.close()
