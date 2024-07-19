import psycopg2
from psycopg2 import connect
from getpass import getpass

def connect_to_db():
    conn = psycopg2.connect(
        dbname= 'mma_system',
        user = 'postgres',
        password = 'panzer123',
        host = 'localhost',
        port = '5432'
    )
    return conn

def create_user(conn, user_id, email, username, full_name, hashed_pw, dob):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (user_id, email, username, full_name, password, dob, user_type) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (user_id, email, username, full_name, hashed_pw, dob, 'attendee')  # Default user_type as attendee
    )
    conn.commit()
    cursor.close()

def get_user(conn, username):
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM users WHERE username = %s",
        (username,)  # Single-element tuple
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
    conn.close()
