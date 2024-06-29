# This file handles the database connection and queries 

import psycopg2
from psycopg2 import connect
from getpass import getpass # getpass is a function that will hide the password when the user types it in


def connect_to_db():
    conn = psycopg2.connect(
        dbname= 'SQL_code', #TODO: change this to the name of the database
        user = 'postgres',
        password = 'panzer123', #TODO: change this to the password of the database
        host = 'localhost',
        port = '5432'
    )
    return conn



def create_user(conn, username, password, user_type = 'attendee'): #TODO: figure out what we want the default user type to be
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (username, password, user_type) VALUES (%s, %s, %s)", 
        (username, password, user_type)
        )
    conn.commit() 
    

def get_user(conn, username):
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE username = %s",
        (username,)
    )
    return cur.fetchone()

def set_user_type(conn, username, user_type):
    cur = conn.cursor()
    cur.execute(
        "UPDATE users SET user_type = %s WHERE username = %s",
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



