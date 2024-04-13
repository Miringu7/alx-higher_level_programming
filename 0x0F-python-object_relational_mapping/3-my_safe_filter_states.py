#!/usr/bin/python3

"""" Module that is safe from MySQL injection"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=dbname)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY states.id"
    cursor.execute(query, (name,))
    states = cursor.fetchall()

    [print(state) for state in states]

    cursor.close()
    db.close()
