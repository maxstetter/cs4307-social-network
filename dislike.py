#!/usr/bin/python3
import sqlite3
from datetime import datetime
connection = sqlite3.connect("social.db")
cursor = connection.cursor()

# dislike a post
def dislike_post():
    post_id = input("Post ID? ")
    original_likes = cursor.execute("SELECT dislikes FROM posts WHERE post_id = {}".format(post_id)).fetchone()[0]
    cursor.execute("UPDATE posts SET dislikes = {}".format(original_likes + 1))
    connection.commit()

dislike_post()




