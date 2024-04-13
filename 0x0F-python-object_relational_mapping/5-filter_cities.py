#!/usr/bin/python3

"""" Module that is safe from MySQL injection"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=dbname)
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()

    print(", ".join([row[2] for row in rows if row[4] == state]))

    cursor.close()
    db.close()
