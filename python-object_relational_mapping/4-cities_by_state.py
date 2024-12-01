#!/usr/bin/python3
"""Lists states in the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cu = conn.cursor()
    cu.execute("SELECT cities.id, cities.name, states.name FROM cities "
               "JOIN states ON cities.state_id = states.id "
               "ORDER BY cities.id ASC")
    query_rows = cu.fetchall()
    for row in query_rows:
        print(row)
    cu.close()
    conn.close()
