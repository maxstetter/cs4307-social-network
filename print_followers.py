#!/usr/bin/python3
import sqlite3
connection = sqlite3.connect("social.db")
cursor = connection.cursor()


# prints all follows    
def print_follows():
    rows = cursor.execute("SELECT * FROM follows").fetchall()
    print(rows)

print_follows()
