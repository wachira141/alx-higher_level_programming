#!/usr/bin/python3
"""
 write a script that takes in arguments and displays all values in the states
 table of hbtn_0e_0_usa where name
 matches the argument
 """

 import sys
 import MySQLdb

 if __name__ == "__main__":
     #connect to db
     db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
     cursor = db.cursor()
     cursor.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC", (sys.argv[4],))
     data = cursor.fetchall()
     for state in data:
         print(state)
    cursor.close()
    db.close()
