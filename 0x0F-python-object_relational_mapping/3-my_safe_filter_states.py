#!/usr/bin/python3

"""" Module that is safe from MySQL injection"""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    name = sys.argv[4]

    db = MySQLdb.connect(user=username, passwd=password, db=dbname)
    query = "SELECT * FROM `states` WHERE BINARY `name` = %s"
    cursor = db.cursor()
    cursor.execute(query, (name,))

    [print(state) for state in cursor.fetchall()]
