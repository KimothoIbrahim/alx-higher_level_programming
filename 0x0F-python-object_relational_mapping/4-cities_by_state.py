#!/usr/bin/python3
"""a script that lists all states with
a name starting with N (upper N) from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM states INNER JOIN cities ON states.id = cities.state_id
                ORDER BY cities.id;""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
