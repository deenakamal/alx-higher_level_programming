#!/usr/bin/python3
""" takes in the name of a state as an argument and lists all cities"""
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
    cursor.execute("SELECT cities.name FROM cities "
                   "INNER JOIN states ON states.id=cities.state_id "
                   "WHERE states.name=%s", [sys.argv[4]])

    rows = cursor.fetchall()

    val = list(row[0] for row in rows)
    print(*val, sep=", ")

    cursor.close()
    conn.close()
