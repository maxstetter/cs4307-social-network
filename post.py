#!/usr/bin/python3
import sqlite3
from datetime import datetime
connection = sqlite3.connect("social.db")
cursor = connection.cursor()

# create a post
def create_post(a, c, t, l, d):
    cursor.execute("INSERT INTO posts (author, content, time, likes, dislikes ) VALUES ('{}', '{}', '{}', '{}', '{}')".format(a, c , t, l, d))


a = input("Input user name: ")
c = input("Post: ")
t = datetime.now()
l = 0
d = 0
create_post(a,c,t,l,d)
connection.commit()


