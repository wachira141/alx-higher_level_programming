#!/usr/bin/python3
"""
script to list all states from hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ACC")
    [print(state) for state in cursor.fetchall()]
    cursor.close()
    db.close()
