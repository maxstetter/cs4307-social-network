#!/usr/bin/python3
import sqlite3
connection = sqlite3.connect("social.db")
cursor = connection.cursor()

# checks n most recent posts of people that you follow
def check_feed():
    who = input("Who are you? ")
    many = int(input("How many posts do you want to see? "))

    rows = cursor.execute("SELECT posts.author, posts.content FROM posts, follows WHERE follows.user_name = ? AND follows.follow_name = posts.author ORDER BY posts.time DESC",(who,),).fetchmany(many)
    print(rows)




check_feed()