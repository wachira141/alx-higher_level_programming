#!/usr/bin/python3
"""
script to list all cities from the db
"""

import sys
import MySQLdb

if __name__ == "__main__":
    #connect to db
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    #create cursor
    cursor = db.cursor()
    sql_query = "SELECT cities.id, cities.name, states.name FROM states \
            INNER JOIN cities ON states.id = cities.state_id \
            ORDER BY cities.id ASC"
            cursor.execute(sql_query)

            for city in cursor.fetchall():
                print(city)
            cursor.close()
            db.close()
