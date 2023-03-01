#!/usr/bin/python3
import sqlite3
connection = sqlite3.connect("social.db")
cursor = connection.cursor()


# create the initial users table
def init_users_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS users( user_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, thickness TEXT NOT NULL, gender TEXT NOT NULL, age INTEGER NOT NULL )")
    print('initialized users DB')
    
# create the inital follows table    
def init_follows_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS follows( user_name TEXT NOT NULL, follow_name TEXT NOT NULL )")
    print("initialized follows DB")

# create the inital posts table
def init_posts_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS posts( post_id INTEGER PRIMARY KEY, author TEXT NOT NULL, content TEXT NOT NULL, time INTEGER NOT NULL, genre TEXT NOT NULL, likes INTEGER, dislikes INTEGER )")
    print("initialized posts DB")


# prints all users
def print_users():
    rows = cursor.execute("SELECT name, age, user_id FROM users").fetchall()
    print(rows)

# prints all follows    
def print_follows():
    rows = cursor.execute("SELECT * FROM follows").fetchall()
    print(rows)

# create a user

init_users_db()
init_follows_db()
init_posts_db()
print_follows()
print_users()

