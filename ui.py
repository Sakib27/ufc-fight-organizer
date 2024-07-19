# This file is the user interface for the application

from prettytable import PrettyTable
import database, database2 
from database import connect_to_db, get_user, create_user, close_connection, set_user_type, close_connection, get_user_by_login
import hashlib

# def prompt_login(user, password):
#     user = input('Username: ')
#     password = input('Password: ')
#     hashed_pw = hashlib.sha256(password.encode()).hexdigest()  # saving the passwords as hashed values in the database
    # get_user_by_login(user, hashed_pw) 
    # if user:
    #     print(f"Welcome!")
    #     return user, hashed_pw
    # else:
    #     print("Invalid credentials, please try again.")
    #     return None
    # return user, hashed_pw
  
def account_create(conn, user_type='attendee'):
    user_id = input('UserID: ')
    email = input('Email: ')  # TODO: maybe add checks for email format
    username = input('Username: ')
    full_name = input('Full Name: ')
    password = input('Password: ')
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()  # saving the passwords as hashed values in the database
    dob = input('Date of Birth (YYYY-MM-DD): ')

    # Directly insert the new user into the users table
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users ("UserID", "Email", "Username", "Full_Name", "HashedPW", "dob", "UserType")
        VALUES (%s, %s, %s, %s, %s, %s, %s);
    """, (user_id, email, username, full_name, hashed_pw, dob, user_type))
    conn.commit()
    cur.close()
    
    print(f'{user_type.capitalize()} account created successfully')

# def authenticate_user(conn, username, password):
#     user = get_user(conn, username)
#     if user and user[2] == password: # user[2] is the password
#         return user
#     return None

# def assign_role(conn):
#     username = input('Enter username: ')
#     user_type = input('Enter new user type: (attendee, staff, admin, organizer, fighter) ')
#     set_user_type(conn, username, user_type)
#     print(f'assigned {username} as {user_type}')

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
    print('\n') # newline

def attendee_menu():
    while True:
        print('1. Buy Tickets')
        print('2. View Purchased Tickets')
        print('3. Buy More Ticekts')
        print('4. Sell Tickets')
        print('5. Logout')
        print('\n') # newline
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
        print('\n') # newline
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
        print('\n') # newline
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
        print('\n') # newline
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
    # while True:
    main_menu()
    choice = input('Enter choice: ')
    print('\n') # newline
    if choice == '1':
        username = input("Username: ")
        password = input("Password: ")
        print('\n') # newline
        user = get_user(conn, username)
        if user and hashlib.sha256(password.encode()).hexdigest() == user[4]: # user[4] is the password
            print(f'Welcome {user[3]}!')
            print('\n') # newline
            if user[6].lower() == 'attendee':
                while True:
                    attendee_menu()
                    attendee_choice = input('Select an option: ')
                    if attendee_choice == '4':
                        break
            elif user[6].lower() == 'staff':
                while True:
                    staff_menu()
                    staff_choice = input('Select an option: ')
                    if staff_choice == '4':
                        break
            elif user[6].lower() == 'admin':
                while True:
                    admin_menu()
                    admin_choice = input('Select an option: ')
                    if admin_choice == '5':
                        break
                    elif admin_choice == '4':
                        print("Create account for:")
                        print("1. Fighter")
                        print("2. Staff")
                        print("3. Organizer")
                        role_choice = input('Select an option: ')
                        if role_choice == '1':
                            account_create(conn, 'fighter')
                        elif role_choice == '2':
                            account_create(conn, 'staff')
                        elif role_choice == '3':
                            account_create(conn, 'organizer')
                        else:
                            print('Invalid choice')
                    elif admin_choice == '4':
                        break
            elif user[6].lower() == 'organizer':
                while True:
                    organizer_menu()
                    organizer_choice = input('Select an option: ')
                    if organizer_choice == '4':
                        break
            elif user[6].lower() == 'fighter':
                while True:
                    fighter_menu()
                    fighter_choice = input('Select an option: ')
                    if fighter_choice == '4':
                        break
        else:
            print('Invalid username or password')
    elif choice == '2':
        account_create(conn)
    elif choice == '3':
        return
    else:
        print('Invalid choice')
    close_connection(conn)

# if __name__ == '__main__':
#     run_ui()
