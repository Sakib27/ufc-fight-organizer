# This file handles the database connection and queries 

import psycopg2
from psycopg2 import connect
from getpass import getpass # getpass is a function that will hide the password when the user types it in


def connect_to_db():
    conn = psycopg2.connect(
        dbname= 'mma_system',
        user = 'postgres',
        password = 'panzer123', 
        host = 'localhost',
        port = '5432'
    )
    return conn

def create_user(conn, user_id, email, username, full_name, hashed_pw, dob, user_type='attendee'):
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users ("UserID", "Email", "Username", "Full_Name", "HashedPW", "dob", "UserType")
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (user_id, email, username, full_name, hashed_pw, dob, user_type))
    conn.commit()
    cur.close()

def get_user(conn, username):
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE username = %s",
        (username,)
    )
    return cur.fetchone() 

def get_user_by_login(username, password):
    conn = connect_to_db()
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE username = %s AND HashedPW = %s",
        (username, password)
    )
     

def set_user_type(conn, username, user_type):
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET usertype = %s WHERE username = %s",
        (user_type, username)
    )
    conn.commit()

def get_all_users(conn):
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users"
    )
    return cur.fetchall()

def close_connection(conn):
    conn.close() # close the connection