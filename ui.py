# This file is the user interface for the application

from prettytable import PrettyTable
import database
from database import connect_to_db, get_user, create_user, close_connection, get_user_by_login, set_user_type

def prompt_login():
    user = input('Username: ')
    password = input('Password: ')
    user = get_user_by_login(user, password) # TODO: Some error here
    return user, password

def prompt_signup():
    user_id = input('UserID: ')
    email = input('Email: ')
    username = input('Username: ')
    full_name = input('Full Name: ')
    hashed_pw = input('Password: ')  
    dob = input('Date of Birth (YYYY-MM-DD): ')
    return user_id, email, username, full_name, hashed_pw, dob

def authenticate_user(conn, username, password):
    user = get_user(conn, username)
    if user and user[2] == password: # user[2] is the password
        return user
    return None

def assign_role(conn):
    username = input('Enter username: ')
    user_type = input('Enter new user type: (attendee, staff, admin, organizer, fighter) ')
    set_user_type(conn, username, user_type)
    print(f'assigned {username} as {user_type}')

# def assign_shift(conn):

# def approve_shift_swap(conn):

# def create_event(conn):

# def manage_sponsors(conn):

# def approve_fight_requests(conn):

# def view_fight_schedule(conn):

# def view_upcoming_fights(conn):

# def request_fight(conn):

# def buy_tickets(conn):

# def view_purchased_tickets(conn):

# def buy_more_tickets(conn):

# def sell_tickets(conn):

# def view_shifts(conn):

# def view_venue_assignments(conn):

# def swap_shifts(conn):

# def logout(conn):

def main_menu():
    print('1. Login')
    print('2. Signup')
    print('3. Exit')

def attendee_menu():
    while True:
        print('1. Buy Tickets')
        print('2. View Purchased Tickets')
        print('3. Buy More Ticekts')
        print('4. Sell Tickets')
        print('5. Logout')
        choice = input('Enter choice: ')

        if choice == '1':
            buy_tickets(conn)
        elif choice == '2':
            view_purchased_tickets(conn)
        elif choice == '3':
            buy_more_tickets(conn)
        elif choice == '4':
            sell_tickets(conn)
        elif choice == '5':
            close_connection(conn)
        else:
            print('Invalid choice')


def staff_menu():
    while True:
        print('1. View Shifts')
        print('2. View Venue Assignments')
        print('3. Swap Shifts')
        print('4. Logout')
        # running the function corresponding to the choice
        choice = input('Enter choice: ')
        if choice == '1':
            view_shifts(conn)
        elif choice == '2':
            view_venue_assignments(conn)
        elif choice == '3':
            swap_shifts(conn)
        elif choice == '4':
            close_connection(conn)
        else:
            print('Invalid choice')

def admin_menu():
    while True:
        print('1. Assign User Roles')
        print('2. Assign Shifts')
        print('3. Approve Shift Swaps')
        print('4. Logout')
        # running the function corresponding to the choice
        choice = input('Enter choice: ')
        if choice == '1':
            assign_role(conn)
        elif choice == '2':
            assign_shift(conn)
        elif choice == '3':
            approve_shift_swap(conn)
        elif choice == '4':
            close_connection(conn)
        else:
            print('Invalid choice')

def organizer_menu():
    while True:
        print('1. Schedule Event')
        print('2. Manage Sponsors')
        print('3. Approve Fight Requests')
        print('4. Logout')
        # running the function corresponding to the choice
        choice = input('Enter choice: ')
        if choice == '1':
            create_event(conn)
        elif choice == '2':
            manage_sponsors(conn)
        elif choice == '3':
            approve_fight_requests(conn)
        elif choice == '4':
            close_connection(conn)
        else:
            print('Invalid choice')


def fighter_menu():
    while True:
        print('1. View Fight Schedule')
        print('2. View Upcoming Fights') 
        print('3. Request Fight') #  TODO: make this into a view that appears only if the fighter has more than 10 fights so far
        print('4. Logout')
        # running the function corresponding to the choice
        choice = input('Enter choice: ')
        if choice == '1':
            view_fight_schedule(conn)
        elif choice == '2':
            view_upcoming_fights(conn)
        elif choice == '3':
            request_fight(conn)
        elif choice == '4':
            close_connection(conn)
        else:
            print('Invalid choice')

def run_ui():
    conn = connect_to_db()
    while True:
        main_menu()
        choice = input('Enter choice: ')
        if choice == '1':
            username, password = prompt_login() # TODO: Some error here
            user = authenticate_user(conn, username, password)
            if user:
                user_type = user[3]  # user[3] is the user_type
                if user_type == 'attendee':
                    attendee_menu()
                elif user_type == 'staff':
                    staff_menu()
                elif user_type == 'admin':
                    admin_menu(conn)
                elif user_type == 'organizer':
                    organizer_menu()
                elif user_type == 'fighter':
                    fighter_menu()
                else:
                    print('You are currently not a user')
            else:
                print('Invalid username or password')
        elif choice == '2':
            user_id, email, username, full_name, hashed_pw, dob = prompt_signup()
            create_user(conn, user_id, email, username, full_name, hashed_pw, dob)
            print('User created successfully!')
        elif choice == '3':
            break
        else:
            print('Invalid choice')
    close_connection(conn)

# if __name__ == '__main__':
#     run_ui()
