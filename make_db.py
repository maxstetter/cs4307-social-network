import sqlite3
connection = sqlite3.connect("social.db")
cursor = connection.cursor()




# create the initial users table
def init_users_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS users( user_id INTEGER PRIMARY KEY, name TEXT NOT NULL, thickness TEXT NOT NULL, gender TEXT NOT NULL, age INTEGER NOT NULL )")
    print('initialized users DB')


# create the inital posts table
def init_posts_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS posts ()")
    print('initialized posts DB')
    
# create the inital follows table    
def init_follows_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS follows( user_id INTEGER NOT NULL, follow_id INTEGER NOT NULL )")
    print("initialized follows DB")

# create the inital posts table
def init_posts_db():
    cursor.execute("CREATE TABLE IF NOT EXISTS posts( post_id INTEGER PRIMARY KEY, author TEXT NOT NULL, content TEXT NOT NULL, time INTEGER NOT NULL, genre TEXT NOT NULL, likes INTEGER, dislikes INTEGER )")
    print("initialized posts DB")

    
# follow a user
def follow_user(current_id, wanted_id):
    cursor.execute("INSERT INTO follows (user_id, follow_id) VALUES ('{}', '{}')".format(current_id, wanted_id))

# prints all users
def print_users():
    rows = cursor.execute("SELECT name, age, user_id FROM users").fetchall()
    print(rows)

# prints all follows    
def print_follows():
    rows = cursor.execute("SELECT * FROM follows").fetchall()
    print(rows)

# create a user
def create_user(name, thickness, gender, age):
    cursor.execute("INSERT INTO users (name, thickness, gender, age) VALUES('{}', '{}', '{}', '{}')".format(name, thickness, gender, age))
    print("user {} created".format(name))

init_users_db()
init_follows_db()
init_posts_db()
create_user('ben', 'thicky', 'm', 20)
create_user('max', 'not thick', 'm', 22)
follow_user(1, 2)
print_follows()
print_users()

