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

def create_user(conn, userid, email, username, name, hashedpw, dob, usertype ='attendee'):
    cur = conn.cursor() 
    cur.execute("""
        INSERT INTO users ("userid", "email", "username", "name", "hashedpw", "dob", "usertype")
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (userid, email, username, name, hashedpw, dob, usertype))
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

def set_shift(conn, userid, eventid, starttime, endtime):
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Shifts (userID, eventid, starttime, endtime) VALUES (%s, %s, %s, %s)",
        (userid, eventid, starttime, endtime)
    )
    conn.commit()

def close_connection(conn):
    conn.close() # close the connection