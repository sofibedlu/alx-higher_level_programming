#!/usr/bin/python3

"""a script that lists all 'states' from the database 'hbtn_0e_0_usa'
"""
import MySQLdb
from sys import argv

conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                       passwd=argv[2], db=argv[3], charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC")
query_re = cur.fetchall()

for state in query_re:
    print(state)

cur.close()
conn.close()
