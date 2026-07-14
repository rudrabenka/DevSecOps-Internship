print("Hello from Jenkins Pipeline!")



unused_var = 42


def greet():
    print("Hello")

def greet_again():
    print("Hello")  

def a():
    pass


def risky_division(x, y):
    return x / y


db_password = "admin123"

import sqlite3
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE name = '" + username + "';")  
    return cursor.fetchall()


def buggy_division(x, y):
    return x / y  

def print_name(user):
    print(user["name"])  
