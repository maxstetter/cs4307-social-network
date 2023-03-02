#!/usr/bin/python3
import sqlite3
connection = sqlite3.connect("social.db")
cursor = connection.cursor()

# like a post
def like_post():
    post_id = input("Post ID? ")
    original_likes = cursor.execute("SELECT likes FROM posts WHERE post_id = {}".format(post_id)).fetchone()[0]
    print(original_likes + 1)
    cursor.execute("UPDATE posts SET likes = {}".format(original_likes + 1))
    connection.commit()

like_post()