#!/usr/bin/python3

"""" Module that is safe from MySQL injection"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=dbname)
    cursor = db.cursor()
    query = "SELECT cities.id, cities.name, states.name FROM cities \
            INNER JOIN states \
            ON states.id = cities.state_id"
    cursor.execute(query)
    cities = cursor.fetchall()

    [print(city) for city in cities]

    cursor.close()
    db.close()
