#!/usr/bin/python3
import sqlite3
connection = sqlite3.connect("social.db")
cursor = connection.cursor()

# follow a user
def follow_user(current_id, wanted_id):
    cursor.execute("INSERT INTO follows (user_id, follow_id) VALUES ('{}', '{}')".format(current_id, wanted_id))

current = input("What's your user name? ")
wanted = input("What's the user name of the person you wish to follow? ")
follow_user(current, wanted)
