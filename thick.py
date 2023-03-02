#!/usr/bin/python3
import sqlite3
from datetime import datetime
connection = sqlite3.connect("social.db")
cursor = connection.cursor()

# create a post
def thick():
    not_thick = cursor.execute("SELECT name FROM users WHERE thickness = 'thicky'").fetchall()
    print(not_thick)
thick()
