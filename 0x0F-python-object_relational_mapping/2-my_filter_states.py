#!/usr/bin/python3

"""
Module that lists all states from the hbtn_0e_0_usa database.
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    script that takes in an argument and displays all values in states table
    of hbtn_0e_0_usa where name matches the argument.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` WHERE BINARY `name` == {}"
                   .format(sys.argv[4]))

    [print(state) for state in cursor.fetchall()]
