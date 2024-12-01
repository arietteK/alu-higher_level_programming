#!/usr/bin/python3
"""Lists the states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cu = conn.cursor()
    cu.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cu.fetchall()
    for row in query_rows:
        print(row)
    cu.close()
    conn.close()
