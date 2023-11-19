#!/usr/bin/python3
"""
    Script that lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cur = conn_db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)

    cur.close()
    conn_db.close()