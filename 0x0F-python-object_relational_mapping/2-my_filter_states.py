#!/usr/bin/python3
"""
script that takes in an arg and displays all 
values in the state table
"""

import sys
import MySQLdb

if __name == "__main__":
    #connect to db
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    #create cursor()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY \
            id ASC".format(sys.argv[4]))
    for state = cursor.fetchall():
        if state[1] == sys.arg[4]:
            print(state)
        cursor.close()
        db.close()
