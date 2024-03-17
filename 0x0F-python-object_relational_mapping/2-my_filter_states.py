#!/usr/bin/python3
""" takes an argument and displays all values in the states table """
import MySQLdb
import sys


if __name__ == "__main__":
    db_username = sys.argv[1]
    db_password = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=db_username,
                           password=db_password, database=db_name,
                           charset="utf8")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY\
            '{}' ORDER BY id ASC".format(state_name))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
