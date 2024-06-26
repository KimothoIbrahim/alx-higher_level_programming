#!/usr/bin/python3
"""a script that lists all states with
a name starting with N (upper N) from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
                ORDER BY states.id;""".format(sys.argv[4]))
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    conn.close()
