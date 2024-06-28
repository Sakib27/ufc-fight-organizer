# This file is the user interface for the application

from prettytable import PrettyTable
import database
from database import connect_to_db, get_user, close_connection

def prompt_login():
    user = input('Username: ')
    password = input('Password: ')
    return user, password

def authenticate_user(conn, username, password):
    user = get_user(conn, username)
    if user and user[2] == password: # user[2] is the password
        return user
    return None

def attendee_menu():
    print('1. Buy Tickets')
    print('2. View Purchased Tickets')
    print('3. Buy More Ticekts')
    print('4. Sell Tickets')
    print('5. Logout')

def staff_menu():
    print('1. View Shifts')
    print('2. View Venue Assignments')
    print('3. Swap Shifts')
    print('4. Logout')

def admin_menu():
    print('1. Assign User Roles')
    print('2. Assign Shifts')
    print('3. Approve Shift Swaps')
    print('4. Logout')

def organizer_menu():
    print('1. Schedule Event')
    print('2. Manage Sponsors')
    print('3. Approve Fight Requests')

def fighter_menu():
    print('1. View Fight Schedule')
    print('2. View Upcoming Fights')
    print('3. Request Fight')
    print('4. Logout')

def run_ui():
    conn = connect_to_db()
    username, password = prompt_login()
    user = authenticate_user(conn, username, password)
    if user: 
        user_type = user[3] # user[3] is the user_type
        if user_type == 'attendee':
            attendee_menu()
        elif user_type == 'staff':
            staff_menu()
        elif user_type == 'admin':
            admin_menu()
        elif user_type == 'organizer':
            organizer_menu()
        elif user_type == 'fighter':
            fighter_menu()
        else:
            print('You are currently not a user')
    else:
        print('Invalid username or password')
    close_connection(conn)


