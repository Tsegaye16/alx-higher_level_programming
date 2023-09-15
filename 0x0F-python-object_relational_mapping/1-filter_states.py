#!/usr/bin/python3
import MySQLdb
from sys import argv

if __name__ == '__main__':
	db = MySQL.connect(host = "localhost", user = argv[1],
	port = 3306, passwd = argv[2], db = argv[3])
	cur = db.cursore()
	cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
	row = cur.fetchall()
	for rows in row:
		print(rows)
