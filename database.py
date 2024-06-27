# This file handles the database connection and queries 

import psycopg2
from psycopg2 import sql

def connect_to_db():
    conn = psycopg2.connect(
        dbname='deds', #TODO: change this to the name of the database
        user = 'postgres',
        password = 'password', #TODO: change this to the password of the database
        host = 'localhost',
        port = '5432'
    )
    return conn

def view_fighters(conn):
    cur = conn.cursor() # create a cursor object using the connection
    cur.execute("SELECT * FROM fighters") # execute the query
    rows = cur.fetchall() # fetch all the rows
    return rows

def close_db(conn):
    conn.close() # close the connection



