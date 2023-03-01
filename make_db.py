import sqlite3
connection = sqlite3.connect("social.db")
cursor = connection.cursor()




# create the initial db tables
def init_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS users( user_id INTEGER PRIMARY KEY, name TEXT NOT NULL, thickness TEXT NOT NULL, gender TEXT NOT NULL, age INTEGER NOT NULL )")
    print('initialized DB')


def print_users():
    rows = cursor.execute("SELECT name, age, user_id FROM users").fetchall()
    print(rows)
    

def create_user(name, thickness, gender, age):
    cursor.execute("INSERT INTO users (name, thickness, gender, age) VALUES('{}', '{}', '{}', '{}')".format(name, thickness, gender, age))
    print("user {} created".format(name))

init_db()
create_user('ben', 'thicky', 'm', 20)
create_user('max', 'not thick', 'm', 22)
print_users()

