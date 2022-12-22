#!/usr/bin/python3
"""
script that takes in the name of a state as an arg
and lists all cities of that state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    #connect to db
    db = MySQL.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    sql_query ="""SELECT * FROM cities \
            INNER JOIN states ON states.id == cities.states_id \
            WHERE states.name LIKE %s ORDER BY cities.id ASC"""
    cursor.execute(sql_query, (sys.argv[4], ))
    print(", ".join(["{:s}".format(city[0]) for city in cursor.fetchall()]))
    cursor.close()
    db.close()
