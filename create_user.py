#!/usr/bin/python3
import sqlite3
connection = sqlite3.connect("social.db")
cursor = connection.cursor()

class user:
    def __init__(self, name, thickness, gender, age):
        self.name = name
        self.thickness = thickness
        self.gender = gender 
        self.age = age

# get user input and return a user object.
def get_user_input():
    name = input("Name? ")
    thickness = input("Thickness? ")
    gender = input("Gender? ")
    age = input("Age? ")
    new_user = user(name, thickness, gender, age) 
    return new_user


# create a new user using user class
def create_user():
    new_user = get_user_input()
    cursor.execute("INSERT INTO users (name, thickness, gender, age) VALUES('{}', '{}', '{}', '{}')".format(new_user.name, new_user.thickness, new_user.gender, new_user.age))
    print("user {} created".format(new_user.name))


create_user()