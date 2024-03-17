#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa"""
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
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY %s"
                   "ORDER BY id ASC", [sys.argv[4]])

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()
