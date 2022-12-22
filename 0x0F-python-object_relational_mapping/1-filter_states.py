#!/usr/bin/python3
"""
script that lists all states with a name 
starting with N from db hbt_0e_0_usa
"""

import sys
import MySQLdb

if __name__ == "__main__":
    #connect to db
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    [print(state) for state in cursor.fetchall() if state[1][0] == 'N']
