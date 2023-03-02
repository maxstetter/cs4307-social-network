#!/usr/bin/python3
import sqlite3
from datetime import datetime
connection = sqlite3.connect("social.db")
cursor = connection.cursor()

# create a post
def active(size):
    recent = cursor.execute("SELECT author FROM posts ORDER BY time DESC ").fetchmany(size)
    print(recent)

the_size = int(input("How many recent users would you like to see? "))
active(the_size)

