#!/usr/bin/python3

"""
script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa:
"""

import sys
import MySQLdb


def list_states(username, password, database):
    """
    connects to MySQL server and prints the states starting with 'N'

    Args:
        username: mysql username
        password: mysql password
        name: database name
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    states = cursor.fetchall()

    for state in states:
        if state.startswith("N"):
            print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
