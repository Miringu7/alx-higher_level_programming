#!/usr/bin/python3

"""
2. Filter states by user input
"""
import sys
import MySQLdb


if __name__ == __main__:
    """
    script that takes in an argument and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM `states` ORDER BY states.id ASC")

    [print(state) for state in cursor.fetchall() if state[1] == sys.argv[4]]
